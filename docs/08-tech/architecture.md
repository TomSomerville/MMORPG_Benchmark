# Technical Architecture

[← Master Plan](../../MASTER_PLAN.md) · Prev: [World Bosses](../07-instances/world-bosses.md) · Next: [Data Model](data-model.md) · [Roadmap](roadmap.md)

How the game is built. This is a plan, not code. The engine choice in §1 was **decided on 2026-11-10: Godot 4 with C# for both client and server** (see [decisions](../../MASTER_PLAN.md#8-decisions)).

## 1. Technology choice

| Option | Client | Server | Why / why not |
|---|---|---|---|
| **A — chosen** | **Godot 4 (.NET / C#)**, desktop (Windows first, Linux/macOS later) | **.NET (C#)** authoritative server | One language end to end; a shared C# rules library runs identically on client and server (prediction, tooltips, formulas). Godot is free, has terrain, animation, navigation and UI tooling, and its scenes are text files that version cleanly. Cost: Godot's C# build has no web export; 3D MMO-scale streaming needs custom work |
| B | Browser client (TypeScript + Babylon.js/WebGPU) | Node.js or .NET | Zero-install, easy playtests, and the client can be driven and screenshotted automatically. Cost: weaker tooling for terrain/animation, heavier asset constraints, harder to reach a WoW-like look |
| C | Unreal or Unity | Custom | Best visuals/tooling; licence terms, binary scenes and build complexity make it the slowest path for a small, code-first team |

**Decision: Option A.** Options B and C are kept above for the record. The rest of this document uses Godot and .NET vocabulary; its core still rests on an authoritative server, a shared rules library, and data-driven content.

**Build-level specifications:** [Repository Layout](repo-and-conventions.md) · [Content Schemas](content-schemas.md) · [Database Schema](database-schema.md) · [Network Protocol](network-protocol.md) · [UI Specification](ui-specification.md) · [Milestone Task Lists](milestone-tasks.md). Where those pages are more specific than this one, they are the rule.

**Supporting stack:** PostgreSQL (persistent data) · Redis (sessions, presence, cross-process messaging; introduced at milestone M13 when the server is split into several processes; until then one process uses an in-process bus behind the same interface) · content authored as YAML/JSON files in the repository and compiled to a binary pack · a walk grid per zone, baked by the world generator, in place of a navigation mesh library ([Terrain and Cutouts §1.1](terrain-and-cutouts.md#11-the-walk-grid)) · reliable-UDP transport (LiteNetLib) · Docker for server deployment · GitHub Actions for build/test.

## 2. Guiding principles

1. **Server-authoritative.** The client sends *intent* (move input, "cast spell 123 on target 456"); the server decides everything that matters.
2. **Data-driven.** Classes, races, allegiances, spells, items, creatures, quests, zones and loot are data. Adding a faction, race or class must not require engine changes (see [Data Model](data-model.md)).
3. **One rules library.** Combat formulas, spell effects, stat calculation and XP tables live in a single library referenced by server, client and tools.
4. **Monolith first, split later.** Start as one server process with clear module boundaries; split into services only when load requires.
5. **Testable without a client.** Headless bots can log in, quest, fight and group; combat and quests are covered by automated simulation tests.

## 3. Server architecture

```
                 +-----------------+
 Client <-TLS--> |  Login / Auth   |--> accounts DB
                 +-----------------+
                          | session ticket
                 +-----------------+        +-------------+
 Client <-UDP--> |     Gateway     |<------>|    Redis    |
                 +-----------------+        +-------------+
                    |           |
          +----------------+  +------------------+
          |  World Service |  |   Social/Chat    |
          | (realm state:  |  | (chat, guilds,   |
          |  who is where, |  |  friends, mail,  |
          |  groups, AH,   |  |  LFG board)      |
          |  instance mgr) |  +------------------+
          +----------------+
            |     |      |
     +--------+ +--------+ +-----------------+
     | Zone   | | Zone   | | Instance hosts  |
     | host A | | host B | | (dungeons, raid,|
     | (maps) | | (maps) | |  battlegrounds) |
     +--------+ +--------+ +-----------------+
            \      |       /
             +-------------+
             | PostgreSQL  |
             +-------------+
```

| Component | Responsibility |
|---|---|
| Login/Auth | Accounts, passwords (Argon2), session tickets, realm list, character list/create/delete |
| Gateway | Holds client connections, encryption, rate limiting, routes packets to the zone host that owns the player |
| World Service | Realm-wide state: online players, groups/raids, instance allocation and lockouts, auction house, battleground queues, world-boss timers, ship schedules |
| Zone host | Runs the simulation for one or more maps: movement, AI, combat, loot, quests, gathering. Fixed tick |
| Instance host | Same code as a zone host, spun up per dungeon/raid/battleground copy |
| Social/Chat | Channels, whispers, guilds, friends, mail delivery |
| Persistence | Write-behind saves: character state every 60 s and on key events (level-up, loot of quality ≥ green, trade, logout); inventory and currency changes are transactional |

During development (milestones M0–M12) all of these are modules inside **one process**, which is enough for a few hundred players and keeps debugging simple. The boundaries above are interfaces from the first day, and **milestone M13 splits them into separate processes**: one gateway tier, one world service, one social service, and a pool of zone-host and instance-host processes. Those processes can all run on one server or be spread over many.

### One server to a cluster

Decided 2026-11-14: **the game is designed for a server cluster, and the same build must also run complete on a single server.** A realm starts on one machine and machines are added as the player count grows. Nothing is rebuilt or redesigned to grow; only a configuration file changes.

| Rule | Detail |
|---|---|
| One build | There is one set of server programs. Whether they run on one machine or twenty is decided only by the topology file |
| Topology file | `deploy/topology.yaml` lists the machines and, for each, which process types it may run and how many cores and how much memory they may use. The single-server topology is one entry |
| Three shapes | **Single process** (development: every module in one process, in-process bus). **Single server** (every process type on one machine, as separate processes so that all cores are used; the database and Redis on the same machine). **Cluster** (the same processes spread over machines) |
| Supervisor | One supervisor reads the topology and starts, places and restarts processes. On a single server it places everything locally. It never assumes a second machine exists |
| No fixed addresses | Processes find each other through the supervisor's registry, never through addresses written in code or content, so a process can move to another machine |
| Realm cap follows capacity | The realm's player cap is the setting `realm.maxPlayers`, not a constant. The design maximum is 5,000. Each deployment sets it to what its hardware has been measured to hold, and the login queue takes anyone beyond it |
| Growing | To add a machine: add it to the topology file and run the deploy command. The supervisor moves processes onto it at the next rolling restart of zone hosts; nobody's character data moves, because it is all in the database |
| Order of moving out | As load grows, move off the first server in this order: the database, then instance hosts, then the busiest zone hosts, then a second gateway. Each step is one edit to the topology file |
| Shrinking | The same in reverse. A cluster can be folded back onto one server by editing the topology and lowering `realm.maxPlayers` |
| Per-zone limit | A zone is one process and its simulation runs on one core, so the 1,500 players per zone limit depends on the speed of one core, not on the number of machines |

The topology file, for a single server and then for the same realm grown onto three machines:

```yaml
# deploy/topology.yaml — single server
realm: { name: Halcyra, maxPlayers: 1200 }
machines:
  - host: game1
    runs: [database, redis, login, gateway, world, social, zoneHosts, instanceHosts]
```

```yaml
# deploy/topology.yaml — the same realm on three machines
realm: { name: Halcyra, maxPlayers: 3500 }
machines:
  - host: game1
    runs: [login, gateway, world, social, zoneHosts]
    zones: [solhaven, hammerdeep, brightmead, stonewake, harrowfield, russetwood]
  - host: game2
    runs: [zoneHosts, instanceHosts]
    zones: [embercrag, stoneheart, thornwick, ironroot, cinderfall, riftlands, veilmoor]
    instanceCopies: 200
  - host: db1
    runs: [database, redis]
```

Zones are named by their content ids (shortened here). A machine that lists no `zones` takes whatever the supervisor assigns. Every zone must be assigned to exactly one machine, and the validator checks the file before a deploy.

How many players one server holds is unmeasured. As a planning guess only: about 1,000 to 1,500 concurrent on a 16-core, 64 GB server, and 2,500 to 3,000 on a 32-core, 128 GB server, with the full 5,000 needing a cluster or a very large machine. The load tests in milestone M13 replace these guesses with a measured table of players per machine size, written to `deploy/capacity.md`.

### One world, no layers

Decided 2026-11-12: **there are no layers, shards or phases of the open world.** Each zone exists once per realm. Every player in a zone is in the same copy of it and can see every other player there, as in the 2004 genre standard. Only dungeons, the raid and the battleground are instanced.

| Rule | Detail |
|---|---|
| One copy | One zone host process runs each zone and each capital: thirteen zone hosts in all, plus instance hosts |
| Everyone is visible | A client receives every player and creature within its interest range. Nobody is hidden or culled by a population limit |
| Crowds, server side | When more than 100 players are within one client's interest range, the server lowers the movement update rate for the more distant ones: the nearest 60 at 10 Hz, the next 140 at 5 Hz, the rest at 2 Hz. State changes (casts, health, death, chat) are never dropped |
| Crowds, client side | Beyond the nearest 60 characters the client uses the low-detail model and skips cloth, weapon trails and footstep sounds. Names and health bars always show. An option sets the threshold |
| Zone capacity | Each zone host must hold **1,500 players** within the tick budget, and a capital 2,000. This covers launch day, when most of the realm is in the two starting zones |
| Dynamic respawn | Respawn time in a sub-area scales with the players in it: 100% up to 15 players, falling in a straight line to **15%** at 150 or more, so a 2.5-minute spawn becomes about 22 seconds. Gathering nodes scale to 30% |
| Quest objects | Clickable quest objects are per-player wherever the quest text or layout says so; all others respawn in 30 seconds scaled by the same rule, so a crowd cannot starve a collect quest |
| Tagging | Classic rule kept: the first player or party to damage a creature owns its XP, loot and quest credit |
| Realm cap and queue | The realm holds up to 5,000 concurrent players; the cap in force is the setting `realm.maxPlayers`, set from the deployment's measured capacity ([One server to a cluster](#one-server-to-a-cluster)). Beyond that, new logins wait in a queue showing their position and an estimated wait |
| World bosses, rares, the Pitmaster's Chest | One of each in the one world; whoever is there contests it |
| Zone hand-over | Crossing a zone border moves the player between zone hosts with no loading screen. Players near a border see across it through a 60-metre strip that both hosts replicate |

## 4. Simulation

| Topic | Design |
|---|---|
| Tick rate | 20 Hz world tick (50 ms). Spell/aura timers in milliseconds; periodic effects scheduled, not polled |
| Entities | Component-based: Transform, Movement, Stats, Health/Resource, Auras, Threat, AI, Inventory, QuestLog, Loot, Interactable |
| Interest management | Uniform grid (cells ≈ 50 m). A client receives updates for entities in its cell and neighbours (≈ 100–150 m view); far objects of interest (group members, world boss) by subscription |
| Movement | Client-predicted with server validation; the server sends corrections. Speed is held by an allowance that builds with time (allowed speed × elapsed × tolerance, at most one second's worth) and is spent by each move, so packets bunched by the network are not corrected. A claimed position must have a floor on the zone's walk grid within 2 yards of its height unless the character is jumping or falling; a jump of more than 12 yards in one packet is a strike. Server and client stand on the same walk grid through the same code. Other players interpolated ~100 ms behind |
| Combat | Fully server-side. Client shows cast bars and GCD optimistically and rolls back on server refusal |
| Spell engine | Spells = data: a list of **effects** (damage, heal, apply aura, dispel, summon, teleport, threat, resource…) and **auras** (periodic, stat modifiers, control, proc triggers, absorbs). ~40 effect types and ~60 aura types cover every ability in the class docs |
| AI | State machine + ability priority lists; boss encounters as data timelines with script hooks |
| Pathfinding | One walk grid per zone: one-metre cells holding floor heights, layer 0 the open ground and a layer for each interior, shared by server, client and the generator's checks. A mover heads straight for its goal when the way can be walked; otherwise the zone finds a path by A* over the grid, with corners cut wherever a body 0.7 m wide can walk straight. The zone keeps one route per creature, found again when the goal has moved 3 yards or after 2 seconds. With no way at all the creature's unreachable timer runs and it evades. Distance between units adds what their heights differ by beyond 2.5 yards |
| Instances | World Service allocates an instance host slot; group members are transferred with their state; idle instances are frozen then destroyed |
| Time | Server-authoritative game clock (day/night, respawns, lockouts) |

## 5. Networking

- **Transport:** reliable-ordered channel for state changes (spells, loot, chat); unreliable-sequenced channel for movement.
- **Protocol:** compact binary messages generated from a schema shared by client and server; versioned.
- **Update model:** entity create / delta-update / destroy per interest set; aura and stat changes as events.
- **Bandwidth target:** ≤ 6 KB/s per client in a busy town; ≤ 15 KB/s in a 40-player world boss fight.
- **Security:** TLS for login; session keys for gameplay; all input validated; per-opcode rate limits; movement and cooldown sanity checks; server never trusts client timers.
- **Latency tolerance:** playable to 250 ms; spell queueing window 400 ms; interrupt/GCD checks use server time.

## 6. Client architecture

| Layer | Contents |
|---|---|
| Network | Connection, message codec, entity replication |
| World | Terrain streaming (chunked heightmap + splat textures, chunks at four detail levels joined by skirts, with a **hole mask** so caves and dungeon entrances can be cut into the ground: see [Terrain and Cutouts](terrain-and-cutouts.md)), static props, sky/weather, day-night, water. The ground a character stands on is the zone's walk grid, the same one the server uses; no physics collision is built per chunk |
| Entities | Character controller, animation state machines (locomotion, cast, attack, hit, death, emotes), nameplates, spell visual effects |
| Gameplay UI | All windows in [UI & Controls](../02-systems/ui-and-controls.md), built from data-described frames |
| Audio | Music by sub-area, ambience, combat and UI sounds |
| Rules | The shared rules library (tooltips, predicted cooldowns, range checks) |

**Character rendering:** one skeleton per race/sex; all player bodies share one texture layout, and armor is region textures layered over the body's skin texture in a fixed order, with geometry swaps built into the body mesh for shapes a texture cannot make; helms, shoulders, weapons and shields are models attached to bones ([Characters, Armor & Weapons §4](../10-art/01-characters-armor-weapons.md#4-how-armor-is-built-the-permutation-rules)). Because armor is made for the shared layout and the skeletons, a new *class* needs no new character art.

## 7. Content pipeline and tools

| Content | Authored as | Tool |
|---|---|---|
| Spells, items, creatures, quests, loot, recipes, talents, factions, races, classes | YAML files in `content/` | Text editor + a **validator** that checks references, level ranges, budgets and broken chains |
| Zones | Layout tables (`layout.yaml`), from which the world generator builds the heightmap, splat maps, hole mask, walk grid, prop placements, sub-areas and spawns | The world generator (`worldgen`), and the Godot editor with a custom zone plugin for fixes: sculpt, paint, props and cutouts, saved as `overrides.yaml` and `cutouts.yaml` and replayed by the generator at every rebuild |
| Walk grid | Baked by the world generator from heights, holes, interiors and what it places | Part of `worldgen` |
| Encounters | YAML timeline + optional script | Text + in-game encounter debugger |
| Balance | Spreadsheet-like views generated from YAML (stat budgets, XP per zone, gold flow) | Reports from the validator |
| Localisation | String tables keyed by id | Export/import |

The design documents in this repository are the **source of truth for the first data pass**: each table (quests, creatures, recipes, talents) is laid out so it can be transcribed nearly one-to-one into content files.

**Art sourcing (major risk):** stylised low-poly, hand-painted look, **entirely AI-generated, audio included; no licensed or bought assets are used** (decided 2026-11-12). The pipeline, review gates and record-keeping are in [Art Master To-Do §8](../10-art/00-art-master-todo.md#8-how-the-art-is-made). The risk is no longer cost but consistency and technical quality: generated models need clean-up, rigging and a single shared palette and shader to look like one game.

## 8. Persistence model (overview)

Accounts · characters (identity, position, stats, XP, money) · inventory items (instances with durability, enchant, random suffix) · spells/talents/skills · quest states · reputations · action bars and settings · social (friends, ignore, guild, mail, auctions) · instance lockouts · world state (boss timers, AH). Static content is **not** in the database — it is the compiled content pack. Detail in [Data Model](data-model.md).

## 9. Performance targets

| Target | Development build (single process, M0–M12) | Launch realm (after M13) |
|---|---|---|
| Concurrent players per realm | 300 | **5,000** |
| Players in one zone (one copy of each zone; no layers) | 300 | 1,500 per zone, 2,000 per capital |
| Players in one sub-area without degradation | 60 | 150 |
| World-boss fight | 40 players + boss + adds at 20 Hz | 80 |
| Active creatures per zone | 1,500 | 1,500 |
| Zone and instance host processes | 1 | 13 zone hosts (one per zone and capital) and up to 400 instance copies, on one server or spread over a cluster (see [One server to a cluster](#one-server-to-a-cluster)) |
| Server tick budget | < 25 ms average at target load | same, per host |
| Login | No queue | Queue above 5,000, with position and estimated wait |
| Database | One PostgreSQL instance | One primary with a read replica for auction search and who-lists; connection pooling |
| Client | 60 fps on a mid-range 2020 GPU at 1080p | same |

The launch-realm column is the design maximum, reached on a cluster. A single server runs the same game with a lower `realm.maxPlayers`, set from the M13 load tests. "5,000" is read as concurrent players on one realm; a second realm is a deployment of the same build.

## 10. Operations

- **Environments:** local (single process + containers for DB), single-server realm, cluster realm. The last two differ only in `deploy/topology.yaml`.
- **Deploy:** container images; zero-downtime restarts are not a goal — scheduled restart window weekly with the raid reset.
- **Observability:** structured logs, metrics (tick time, players, DB latency), crash reports from client and server.
- **GM tools:** in-game commands (teleport, spawn, kick, mute, item/quest fix-ups), an audit log, a web admin page for accounts and tickets.
- **Anti-cheat:** server authority first; movement anomaly detection; economy anomaly reports (gold/time, AH patterns).
- **Backups:** nightly database snapshots, point-in-time recovery.

## 11. Testing strategy

- Unit tests for the rules library (every formula in [Combat & Stats](../02-systems/combat-and-stats.md) and [Progression](../02-systems/progression.md)).
- **Combat simulator:** scripted fights between class builds and stat templates to check time-to-kill and role targets.
- **Bot players:** headless clients that run quest chains end to end — every quest in the zone docs gets a "can be completed" test.
- Content validator in continuous integration: no dangling ids, no unreachable quests, budgets within tolerance.
- Load tests with bots for the performance targets.
