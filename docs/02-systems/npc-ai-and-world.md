# NPC AI & World Simulation

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Economy & Social](economy-and-social.md) · Next: [PvP](pvp.md)

## 1. Creature definition

Every creature is a data record: name, level range, **family** (wolf, boar, humanoid-bandit, undead, elemental…), **type** (Beast, Humanoid, Undead, Elemental, Construct, Dragonkin, Giant, Plant, Aberration), **rank** (Normal, Elite, Rare, Rare-Elite, Boss, World Boss), allegiance/reaction, stat template, ability list, loot table, skinning/mining/herb table, AI script id, movement type, model, sounds.

### Stat templates (v0)

| Level | Normal HP | Normal melee DPS | Armor |
|---|---|---|---|
| 1 | 42 | 2.0 | 20 |
| 5 | 102 | 5.5 | 130 |
| 10 | 198 | 11 | 400 |
| 15 | 328 | 17 | 760 |
| 20 | 484 | 24 | 1,000 |
| 25 | 664 | 31 | 1,260 |
| 30 | 896 | 40 | 1,500 |

Interpolate between rows. Casters: 80% HP, 40% melee DPS, spells make up the rest. **Elite:** ×3.0 HP, ×1.8 damage (dungeon trash ×2.4 HP). **Rare:** ×1.5 HP, ×1.2 damage. **Dungeon boss:** health is set by fight length (expected group DPS × target duration); see [Encounter Data](../12-data/encounters.md#1-rules-used-to-set-the-numbers). **Raid boss:** hand-tuned (see raid doc).

## 2. AI state machine

`Idle → (Wander | Patrol | Scripted pose) → Aggro → Combat → (Flee) → Evade → Return → Idle`, plus `Dead → Corpse → Despawn → Respawn`.

| Behaviour | Rule |
|---|---|
| Idle movement | Stationary, random wander within radius, or waypoint patrol (data) |
| Aggro | Proximity (radius by level difference), damage, assist call, or script |
| Target selection | Highest threat (see [Combat](combat-and-stats.md#7-threat)) |
| Ability use | Each ability has cooldown, range, conditions (health %, target casting, number of enemies) and a priority; the AI fires the highest-priority ready ability |
| Movement in combat | Melee chase with pathfinding; casters hold at range and close when silenced/out of mana; ranged kiters optional |
| Call for help | Social families assist within 10 yd; fleeing humanoids alert within 30 yd |
| Flee | Humanoids at 15% HP run for 8 s |
| Evade | Leash 60 yd, or target unreachable for 6 s → run home, immune, full heal |
| Corpse | Lootable 2 min (owner only), then free-for-all 1 min, then despawn |
| Scripted encounters | Boss scripts are data-driven timelines + phase triggers (health %, timers, add deaths) with hooks for custom logic |

## 3. Spawning

- **Spawn points** are placed by the world generator from the camp tables in the [World Layout](../13-world/00-world-layout.md), under the rules in [World Construction §6](../13-world/10-world-construction.md#6-spawn-points-patrols-and-nodes); each references a creature (or a weighted pool) and a respawn timer.
- Respawn timers: normal outdoor 4–6 min (T1: 2–3 min); named quest targets 3–5 min; rares 2–8 h random; chests 5–15 min; world bosses 3–5 days random; dungeon mobs do not respawn until instance reset.
- **Dynamic respawn:** the open world has no layers, so crowds are absorbed by faster respawns. Timers are 100% with up to 15 players in a sub-area and fall in a straight line to 15% at 150 or more; gathering nodes fall to 30%.
- **Pools:** "one of these 4 points has the rare", "70% wolf / 30% bear".
- **Gathering nodes** use the same system (see [Gathering](../04-professions/gathering.md)).
- **Day/night** flags on spawn points.

## 4. Pathfinding and movement

- Navmesh per zone (generated from terrain and collision), server-side path queries for mobs.
- Mobs cannot be exploited by standing on unreachable ledges: unreachable target → evade.
- Swimming mobs, flying mobs (ignore navmesh, hover height) and rooted/stationary turrets supported as movement types.
- Player movement: client-predicted, server-validated (speed, teleport and fall checks). Detail in [Architecture](../08-tech/architecture.md).

## 5. Friendly NPCs

| Type | Function |
|---|---|
| Quest giver / ender | "!" and "?" indicators; gossip text; quest dialog |
| Vendor, repairer | Shop UI |
| Trainer (class, profession, weapon, riding) | Trainer UI |
| Innkeeper | Bind hearthstone, sells food, rested area |
| Flight master | Eyrie map |
| Banker, auctioneer, mailbox | Service UIs |
| Guard | Attacks hostiles; gives directions via gossip menu in capitals |
| Battlemaster | Battleground queue |
| Stable/mount vendor, barber, guild master, tabard designer | Service UIs |
| Spirit healer | Graveyard resurrection |
| Ambient citizens, critters | Patrols, scripted chatter; critters are level 1 killables |

## 6. Quest system (engine view)

Objective types supported: kill N of creature (or any of a set) · collect N items (drop, object, or purchased) · interact with world object · use item at location/on target · explore area · escort NPC · defend/survive timer · deliver item · speak to NPC (gossip option) · cast spell on target · reach reputation/skill · complete inside instance · kill player in battleground (PvP dailies later).

Quest fields: id, title, level, minimum level, type tag (normal/elite/dungeon/raid/class/profession/PvP), giver, ender, prerequisite quests (all/any), exclusive group (for the A/B variants of Main Chain 1), allegiance (default any), class (default any — only class quests set it), objectives, description/progress/completion text, XP difficulty tag, coin, reward items (fixed + choice), reputation, follow-up quest, shareable flag, timer.

Chain features: breadcrumbs (optional lead-ins that never block the chain), **exclusive groups** ("finish either A or B to unlock C"), repeatables, and item-started quests (drop begins a quest).

## 7. World objects

Chests · gathering nodes · doors and levers · quest objects (sparkle when relevant) · campfires (cooking; Spirit buff) · mailboxes · anvils and forges (profession requirements) · meeting stones · ships and their schedules · signposts · books (readable lore) · fishing pools · PvP objectives (flags, capture points).

## 8. Environment systems

- **Day/night:** 4 h real-time cycle, lighting and ambient sound change; flagged spawns.
- **Weather:** per-zone weighted states with smooth transitions; cosmetic.
- **Ambient audio:** per sub-area music and ambience tracks.
- **Zone/sub-area triggers:** name banner, exploration credit, rest state, PvP tag, graveyard assignment.

## 9. Instances

- An **instance** is a private copy of a map for one group. Entering the portal creates or joins the group's copy.
- Dungeons: 5 players, soft reset when empty for 30 min or by leader; max 5 new instances per hour per player.
- Raid: 10 players, **weekly lockout** (resets Tuesday 09:00 server time); boss kills are saved to an instance id.
- Instance difficulty is fixed (no heroic modes at launch).
- Server allocates instance processes on demand; see [Architecture](../08-tech/architecture.md).
