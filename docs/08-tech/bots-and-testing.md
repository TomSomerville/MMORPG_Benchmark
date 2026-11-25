# Bots and Testing

[← Master Plan](../../MASTER_PLAN.md) · Related: [Build Procedure](build-procedure.md) · [Milestone Task Lists](milestone-tasks.md) · [Repository & Conventions](repo-and-conventions.md) · [Architecture §11](architecture.md#11-testing-strategy)

No person plays the game during the build, so bots are both the test harness and the only players the game has until the owner logs in. The task lists say "bot test" in over a hundred places; this page says what the bots are, how a bot knows where to go, what the load-test mix means, and which scripted-client plays exist.

## 1. Three kinds of automated player

| Kind | What it is | Lives in |
|---|---|---|
| **Bot** | A headless program using the real network protocol through the `Game.Bots` library. It has no graphics. Hundreds run in one process | `src/Game.Bots` |
| **Scripted client** | The real Godot client following a play script, observed through the automation port ([Build Procedure §6](build-procedure.md#6-how-the-builder-sees-the-game)) | `tests/plays/` |
| **Simulator** | The rules library run with no server or client, for balance | `src/Game.Sim` |

Bots are honest clients: they send only what a real client could send, receive only what a real client would receive, and are subject to every server check. The exception is the cheater bots in §5, which exist to be caught.

## 2. Bot brains

A brain is the logic that decides what a bot does next. Each is built when its feature is built.

| Brain | Does | First needed |
|---|---|---|
| Idle | Logs in, stands, answers a ping | M0 |
| Wander | Walks random reachable paths in a zone; used for stuck-spot and seam checks | M2 |
| Fighter | Finds the nearest creature of a named type, fights it with its class priority list, loots, rests | M1 |
| **Quester** | Plays a zone from the content data alone: accepts, does and hands in quests (§3) | M2 |
| Trader | Uses vendors, bank, mail, trade and the auction house on a script of buys and sells | M3, M5 |
| Crafter | Gathers nodes, trains recipes, crafts to a target skill | M5 |
| Party | Five bots with roles (tank, healer, three damage) clear an instance along its room order, using the boss notes in [Encounter Data](../12-data/encounters.md) for positioning rules | M7 |
| Raid | Ten bots, the same with raid roles | M10 |
| Battler | Queues for Crownfall and plays the objectives: hold the hill, carry the crown, attack the nearest enemy | M9 |
| Townsfolk | Stands or walks in a capital, speaks in channels at a set rate, browses the auction house | M12 |

Class priority lists (which ability to press when) are data files beside the bots, one per class and role, taken from the "Role playstyles" section of each class document. The same lists drive the simulator.

## 3. How the Quester plays

The Quester needs no hand-written script per quest. It reads the same content pack the server does.

### Finding where to go

| Objective type | The bot goes to |
|---|---|
| `kill`, `subdue`, `castOn` | The nearest spawn record of that creature that is not already crowded by other bots |
| `collect` | The source of the item: the spawns of a creature that drops it, the world object that holds it, or the vendor that sells it |
| `interact`, `useItem` on an object | The nearest world object of that kind |
| `useItem` on an area, `explore` | The centre of the sub-area or trigger volume |
| `talk`, `deliver` | The NPC's position |
| `escort`, `defend`, `event` | The NPC or object that starts it, then follows the escort or stays within 15 yd of the defended target |

This lookup is a shared library, the **objective locator**. Validation rule V30 requires that every objective of every quest resolves to at least one reachable position; a quest that fails cannot be completed by anyone, bot or player. The locator is a testing and validation tool only. **The game client never shows objective positions to players**: quest map markers and arrows are a cut feature ([Feature Inventory §4](../09-reference/wow-feature-inventory.md#4-questing)), and players find things by reading the quest text.

### What it does, in order of priority

1. Dead: release, run to the corpse, resurrect. If the corpse cannot be reached in 5 minutes, use the spirit healer.
2. In combat: fight by the class priority list. With two or more enemies and health under 25%, run toward the nearest hub.
3. Health under 50% or mana under 30%, out of combat: eat or drink. With no food, wait.
4. Bags full, or any equipped item under 20% durability, or no food: go to the nearest vendor; sell everything grey and every item it cannot use or that scores lower than what it wears; repair; buy 20 food and drink of its level.
5. A new level with unlearned abilities and enough coin: go to the class trainer and learn them, most used first.
6. A quest ready to hand in: hand it in. Choose the reward that scores highest for its class by the profiles in [Item Rules §4](../12-data/item-rules.md#4-stat-profiles), and equip it if it beats what is worn.
7. Quests available at the current hub at its level + 2 or below: accept them, up to the log limit. It skips quests marked group or elite, and dungeon quests, unless it is running as a party.
8. Otherwise: do the nearest objective of an accepted quest.
9. Nothing left at this hub: move to the next hub on the [Leveling Path](../05-zones/00-leveling-path.md) for its level and race. If it is under the next hub's level, kill creatures of its own level near the current hub until it is not.
10. At levels 10, 20 and 30: do the class quest. At 10 and after: spend talent points down one tree, named in the bot's configuration.

Pulling: one creature at a time, never a creature more than 2 levels above itself, never a pack unless in a party. A bot that makes no progress on an objective for 10 minutes abandons it, records why, and moves on; those records are the list of quests that need fixing.

## 4. The load-test mix

"A realistic mix" in the task lists means this, by share of bots:

| Share | Brain | Where |
|---|---|---|
| 60% | Quester | Spread over zones by the level profile below |
| 20% | Townsfolk and Trader | Solhaven and Hammerdeep, split evenly |
| 12% | Party | Dungeons, in groups of five, by level |
| 5% | Battler | Crownfall, queued continuously |
| 3% | Raid, and a world-boss crowd | The Hollow Throne; one world boss kept under attack by 40 bots |

| Level profile | Levels | Used for |
|---|---|---|
| Launch day | Everyone created at level 1 within 10 minutes, half human and half dwarf | The launch-day dry run and the 1,500-in-one-zone test |
| Settled realm | 1–9: 20% · 10–19: 30% · 20–29: 30% · 30: 20% | Soak tests and capacity measurement |

Bots for a load test are created beforehand at the levels needed, with gear of their level made by the item rules, by a tool command, so a test does not wait for them to level.

## 5. Cheater bots

Each breaks one rule and the test passes when the server refuses and logs it: moving at twice run speed · teleporting 50 yd · walking through a wall · using an ability on cooldown · casting without the mana · looting a corpse it did not tag · selling an item it does not own · sending the same trade acceptance twice · sending malformed and oversized packets · flooding chat.

## 6. Scripted-client plays

Kept in `tests/plays/`, each with its state checks and picture checklist. Run at the milestone named and at every milestone after.

| Play | Covers | From |
|---|---|---|
| `login-create` | Login, realm list, create each race, sex and class, enter the world | M0, M3 |
| `two-clients` | Two clients see each other move, emote and chat | M0 |
| `combat-hud` | Every HUD element present and updating in a fight | M1 |
| `first-quests` | The first five quests of each starting zone, with text checked against the quest files | M2 |
| `death-run` | Die, release, run back, resurrect; then the spirit healer | M2 |
| `town-services` | Vendor, repair, trainer, innkeeper and bind, mailbox, bank | M2, M3 |
| `travel` | Eyrie flight, the ship between capitals, zone crossing with no loading screen | M3 |
| `every-window` | Opens every window in the [UI Specification](ui-specification.md), checks its controls exist and are labelled | M4, then every milestone |
| `professions` | Gather a node, craft an item, list it on the auction house, buy it on a second client | M5 |
| `dungeon` | A party enters each dungeon through its cutout, kills the first boss, rolls for loot | M7, M8 |
| `battleground` | Twelve clients play a Crownfall match to a win | M9 |
| `raid` | Ten clients enter the raid and kill the first boss | M10 |
| `social` | Guild create, invite, bank deposit and withdraw, tabard, inspect, duel | M11 |
| `options` | Every option changes what it says it changes; key rebinding; accessibility settings | M11 |
| `visual-walk` | The walk in [Build Procedure §6](build-procedure.md#the-visual-walk) | M2 on |
| `crowd` | One client stands among 300 bots (1,500 where the hardware allows) and holds its frame-rate target with crowd detail rules on | M13 |

## 7. Time in tests

| Need | Rule |
|---|---|
| Timers | The server takes its clock from one interface. Unit and bot tests may run it faster or jump it forward, so that a one-hour mail delay, a weekly raid reset or a respawn timer is tested in seconds |
| Soak and load tests | Always real time |
| Randomness | Every bot and every test has a fixed seed, recorded in its evidence, so a failure can be replayed |

## 8. Where and when tests run

| Suite | Contents | When | Limit |
|---|---|---|---|
| Fast | Unit tests, the validator, protocol tests, short bot tests | Every commit | 10 minutes |
| Milestone | All bot tests, simulator targets, every scripted-client play built so far, the visual walk | End of every milestone | 3 hours |
| Soak and load | The tests in M12 and M13 and the 72-hour run in M14 | Where the task lists place them | As stated |

All suites start from one command, `ci fast`, `ci milestone` or `ci soak`, run on the build machine with the database in a container. A workflow file for a hosted build service is written too, but the build does not depend on one: the builder has no hosted service.

The game client is built for Windows first ([Architecture §1](architecture.md#1-technology-choice)) and also for the build machine's own operating system if that differs, because the scripted client must run where the builder is. The server runs in Linux containers everywhere.
