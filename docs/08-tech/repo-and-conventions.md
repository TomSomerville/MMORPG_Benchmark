# Repository Layout and Coding Conventions

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Technical Architecture](architecture.md) · Next: [Content Schemas](content-schemas.md)

How the code is organised and the rules every file follows. This page is a specification; nothing here has been built yet. Where it fixes a choice that [Architecture](architecture.md) left open, the choice is listed in §1.

## 1. Choices fixed here

| Topic | Choice | Reason |
|---|---|---|
| Engine | Godot 4, .NET build, pinned to one exact version in `client/.godot-version` | Reproducible builds; upgrade is a deliberate task |
| .NET target | The framework the pinned Godot build supports (`net8.0` at the time of writing); every project uses the same one, set once in `Directory.Build.props` | One runtime for client, server and tools |
| Transport | **LiteNetLib** (pure C#, reliable UDP) | Runs unchanged in the Godot client, the server and headless bots; no native library to ship |
| Message encoding | Hand-written `Write` / `Read` on each message type, using one shared `BitWriter` / `BitReader` | No reflection, no generator to maintain; every message has a round-trip test |
| Database access | **Npgsql + Dapper**, plain SQL, numbered migration files | The schema is the specification ([Database Schema](database-schema.md)); no ORM to drift from it |
| Content format | YAML in `content/`, read with YamlDotNet, compiled to one pack per record type | Human-editable, diffs cleanly, matches the design documents |
| Redis | **Not used until milestone M13.** Until then presence and cross-module messages go through an in-process `IBus`; M13 adds a Redis-backed `IBus` and splits the modules into processes for the 5,000-player target | One process is simplest to build and debug; the interface is the seam, and the split is a planned milestone, not an afterthought |
| Tests | xUnit | Standard |
| Logging | `Microsoft.Extensions.Logging` with structured JSON output | Standard |
| Server shape | One executable, `Game.Server`, hosting every module in [Architecture §3](architecture.md#3-server-architecture) | Monolith first |

## 2. Folder layout

```
MMORPG/
  MASTER_PLAN.md
  docs/                      planning documents (the source of truth)
  tools/doc-generators/      scripts that rebuild generated planning documents
  content/                   game data as YAML  (see Content Schemas)
    constants.yaml
    allegiances/ races/ classes/ resources/
    spells/<class>/  spells/creature/  spells/item/
    talents/<class>/
    items/<source>/           quest/ dungeon/ raid/ world/ crafted/ vendor/ pvp/
    itemsets/ suffixes/
    creatures/<zone>/  loot/<zone>/
    npcs/<zone>/  vendors/  trainers/
    quests/<zone>/
    zones/<zone>/             zone.yaml, subareas.yaml, spawns.yaml, objects.yaml, nodes.yaml
    instances/  encounters/  battlegrounds/
    professions/  recipes/<profession>/
    travel/                   eyries.yaml, routes.yaml, ship.yaml
    reputations/
    strings/en/               display text keyed by id
  src/
    Game.Shared/              ids, fixed-point math, time, BitWriter/BitReader, protocol messages
    Game.Rules/               every formula and the spell engine; no I/O, no engine types
    Game.Content/             YAML loader, record types, validator, pack compiler
    Game.Server/              the server executable
      Auth/ Gateway/ World/ Zone/ Social/ Persistence/ Gm/ Hosting/
    Game.Bots/                headless client library and bot scripts
    Game.Tools/               command-line tool: content, db, sim, import
  tools/
    worldgen/                 builds zones from layout tables (docs/13-world/10-world-construction)
    itemgen/                  writes item records by the item rules (docs/12-data/item-rules)
  client/                     the Godot project
    project.godot
    Game.Client.csproj        references Game.Shared, Game.Rules, Game.Content
    scenes/ ui/ world/ entities/ audio/ net/
    assets/                   imported art and audio (glTF, PNG, OGG)
  tests/
    Game.Rules.Tests/ Game.Content.Tests/ Game.Protocol.Tests/
    Game.Server.Tests/ Game.Sim.Tests/ Game.Bots.Tests/
    plays/                    scripted-client play scripts and their checklists (docs/08-tech/bots-and-testing)
  build/                      the builder's ledger, decisions, deferred list, evidence and report
                              (docs/08-tech/build-procedure)
  deploy/                     topology.yaml (which processes run on which machines), capacity.md,
                              container images and the deploy command
  db/migrations/              0001_accounts.sql, 0002_characters.sql, ...
  forge/                      the Asset Forge: provisioning, service, pipelines, style bible, manifest
                              (see docs/14-asset-pipeline; runs on the separate asset machines)
  assets-src/                 intermediate files synchronised back from the forge (not imported by Godot)
  ops/                        docker-compose.yml (PostgreSQL), Dockerfile, CI workflow
  Directory.Build.props       target framework, nullable, warnings as errors
  MMORPG.sln
```

## 3. Project dependencies

```
Game.Shared   <-  Game.Rules   <-  Game.Content  <-  Game.Server
                                                 <-  Game.Client (Godot)
                                                 <-  Game.Bots   <-  Game.Tools
```

Rules that keep the layers honest, each enforced by a test in `Game.Server.Tests/ArchitectureTests`:

1. `Game.Shared` and `Game.Rules` reference nothing but the base class library. No Godot types, no database, no clock, no random number source of their own.
2. `Game.Rules` is pure: every function takes its inputs, including the time and a random source, as parameters. The same call gives the same result on client and server.
3. `Game.Client` never references `Game.Server`. The client knows only the protocol and the rules.
4. Server modules talk to each other only through the interfaces in `Game.Server/Hosting/Contracts`. A module never reads another module's fields.
5. Only `Persistence` holds a database connection.

## 4. Coding conventions

| Topic | Rule |
|---|---|
| Language | C# with nullable reference types on and warnings treated as errors |
| Naming | Types and methods `PascalCase`; locals and parameters `camelCase`; private fields `_camelCase`; constants `PascalCase`; one public type per file, file named after it |
| Ids | Content ids are strings in YAML and `ContentId` (an interned 32-bit handle) in code. Entity ids are `EntityId` (64-bit: 8 bits kind, 56 bits counter). Never compare raw strings in the simulation |
| Time | Milliseconds as `long` server time. No `DateTime.Now` outside `Hosting/Clock`. Durations in the rules library are `int` milliseconds |
| Distance | Yards as `float`, matching the design documents (1 yard = 0.9144 metres; Godot units are metres, converted once at the scene boundary) |
| Money | Copper as `long` |
| Randomness | Through `IRandom`, seeded per simulation; loot and combat rolls are reproducible in tests |
| Numbers that are rules | Live in `content/constants.yaml`, never as literals in code. A literal number in `Game.Rules` other than 0, 1, 2 or 100 fails review |
| Allocation | No per-tick heap allocation in the zone loop: pooled lists, struct components |
| Errors | Bad client input is rejected with a protocol error code and logged at `Debug`; it never throws. Exceptions are for programmer errors only |
| Threading | Each zone or instance simulation is single-threaded. Cross-zone work goes through the bus as messages |
| Text | No user-visible text in code. Everything comes from `content/strings` by id |
| Comments | Explain why, not what. Each public type in `Game.Rules` names the design document section it implements |
| Tests | Every formula in [Combat & Stats](../02-systems/combat-and-stats.md) and [Progression](../02-systems/progression.md) has a test that quotes the document's own example values |

## 5. Commands

All run from the repository root.

```bash
dotnet build MMORPG.sln
```

```bash
dotnet test MMORPG.sln
```

```bash
docker compose -f ops/docker-compose.yml up -d
```

```bash
dotnet run --project src/Game.Tools -- db migrate
```

```bash
dotnet run --project src/Game.Tools -- content validate
```

```bash
dotnet run --project src/Game.Tools -- content build
```

```bash
dotnet run --project src/Game.Server
```

```bash
dotnet run --project src/Game.Tools -- bots run --script quest-zone --zone bm --count 5
```

```bash
dotnet run --project src/Game.Tools -- sim duel --a fighter.greatarms.30 --b creature.template.30
```

The client is run from the Godot editor, or exported with `godot --headless --export-release`.

| `Game.Tools` command | Does |
|---|---|
| `content validate` | Loads every YAML file and runs every validation rule in [Content Schemas §4](content-schemas.md#4-validation-rules) |
| `content build` | Validates, then writes the packs to `build/content/` with a manifest hash |
| `content import <kind>` | Transcribes a generated planning document into YAML: `creatures`, `spells`, `quests`, `npcs`, `items`. Used once per milestone to seed content |
| `db migrate` / `db reset` | Applies migrations; drops and recreates a local database |
| `sim duel` / `sim rotation` | Runs the combat simulator and prints time to kill, damage per second, resource use |
| `bots run` | Starts headless bots against a running server |
| `gm` | Sends a GM command to a running server |

## 6. Configuration

One file, `ops/server.json`, overridden by environment variables with the prefix `GAME_`.

| Key | Default | Meaning |
|---|---|---|
| `Db.ConnectionString` | local PostgreSQL | Database |
| `Net.Port` | 7777 (UDP) | Game port |
| `Auth.Port` | 7778 (TCP, TLS) | Login port |
| `Realm.Name` | "Dev" | Shown in the realm list |
| `Sim.TickMs` | 50 | Zone tick |
| `Content.Path` | `build/content` | Compiled packs |
| `Save.IntervalSeconds` | 60 | Write-behind interval |
| `Gm.Accounts` | empty | Account names with GM rights |
| `Dev.SkipPasswordCheck` | false | Local testing only; refuses to start with this set when `Realm.Name` is not "Dev" |

## 7. Version control and review

During the unattended build the rules in [Build Procedure §3](build-procedure.md#3-order-and-commits) apply: work on `main`, one commit per task, no pull requests and no human review. What follows describes the conventions for people working on the repository afterwards.

| Rule | Detail |
|---|---|
| Branches | `main` always builds and passes tests. Work happens on `m<N>/<task-id>-short-name` branches named after the [milestone task](milestone-tasks.md) |
| Commits | One logical change each; the message starts with the task id, for example `T-M1-07 threat table` |
| Definition of done | The task's acceptance test exists and passes · `dotnet test` passes · `content validate` passes · no new warnings · the design document is updated in the same change if behaviour differs from it |
| Documents first | If code and a design document disagree, the document is changed first, in its own commit, with the reason in the master plan change log |
| Binary assets | Git LFS for everything under `client/assets` and `assets-src` |
| Secrets | None in the repository. `ops/server.json` holds only local defaults |
