# Milestone Task Lists

[← Master Plan](../../MASTER_PLAN.md) · Prev: [UI Specification](ui-specification.md) · Milestones: [Build Roadmap](roadmap.md)

Each roadmap milestone (MA, then M0 to M14) broken into ordered tasks. A task is finished when its acceptance test exists and passes, along with the rest of the [definition of done](repo-and-conventions.md#7-version-control-and-review). Task ids are used as branch and commit prefixes. Tasks within a milestone are done in the order listed unless marked "parallel", with the one exception stated next.

**Order of the build-out: the dwarf starting zone first** (decided by the owner, 2026-11-24). Embercrag Hollow, the dwarf starting zone, is the priority of the build-out. After T-M2-16 the build does T-M3-01 (the dwarf race and its start) and T-M3-02 (Embercrag Hollow) ahead of T-M2-17, and then brings the dwarf starting zone to a finished, polished state: final models, textures, animations, icons and interface, with no placeholder left in the zone. Inside that work the art is ranked: **the player bodies (human and dwarf) and their animations come first**, ahead of all other art; then what the zone itself shows. Only when Embercrag Hollow is finished does the build return to the remaining M2 work (T-M2-17) and to the rest of M3 (T-M3-03 onward). No task id changes; the tables below keep their numbering.

"Bot test" means a scripted headless client in `Game.Bots.Tests`; the bot brains, the questing bot, the load-test mix and the scripted-client plays are specified in [Bots and Testing](bots-and-testing.md). "Sim test" means a combat simulator run in `Game.Sim.Tests`. "Manual" means a scripted run of the real client with state checks and a picture review, **performed by the builder itself** and saved as evidence ([Build Procedure §6](build-procedure.md#6-how-the-builder-sees-the-game)). No game-code task waits for a person: tests written for human testers are run with the substitutes in [Build Procedure §7](build-procedure.md#7-tests-written-for-people). Art is the exception: assets are generated in number only after the owner has approved the style bible and the pipeline's first results ([Build Procedure §5](build-procedure.md#the-owners-approval-of-art)); until then an art task uses placeholders and the game build goes on. How the builder tracks progress, resumes, and handles a test it cannot pass is in [Build Procedure](build-procedure.md).

**Applies to every zone, capital and instance task below (M2, M3, M6, M7, M8, M9, M10):** the place is built by the world generator from its layout tables and must pass the checks in [World Construction §10](../13-world/10-world-construction.md#10-checks) (rule V27); its items are written by [Item Rules](../12-data/item-rules.md) (V28); every quest objective must resolve (V30); and its models, effects, icons and sounds are assigned by [Presentation Rules](../12-data/presentation-rules.md) (V31). Each such task ends with the Quester or Party bots playing the place and the [visual walk](build-procedure.md#the-visual-walk) of it.

Specifications each task builds from: [Repository](repo-and-conventions.md) · [Content Schemas](content-schemas.md) · [Database](database-schema.md) · [Protocol](network-protocol.md) · [UI](ui-specification.md) · the design documents linked in the [Master Plan](../../MASTER_PLAN.md).

## MA — Asset Forge (done first)

The asset generation system on the dedicated GMKtec EVO-X3, specified in [Asset Forge](../14-asset-pipeline/00-asset-forge.md). It is built before any game code so that assets are generated in the background for the whole build. From MA-08 onward the forge runs unattended; the builder moves on to M0 and returns to the forge only when a pipeline reports failures. What the forge may make in number is set by the owner's approvals ([Build Procedure §5](build-procedure.md#the-owners-approval-of-art)): until a pipeline's style guidelines and its first results are approved, only the guidelines themselves and the calibration set (the manifest's first row of each kind) are generated.

| Task | Work | Acceptance test |
|---|---|---|
| T-MA-01 | Audit, then provision, the asset machines over SSH, following [Preparing the machines](../14-asset-pipeline/00-asset-forge.md#preparing-the-machines-is-the-builders-job): record what each machine has, reuse software and model weights already present, install and download only what is missing. **Forge C (the RTX 3060 laptop, optional helper):** a CUDA PyTorch environment, Blender and the Forge worker, limited to the work listed in [Asset Forge §1](../14-asset-pipeline/00-asset-forge.md#forge-c-the-laptop-optional-helper). **Forge A (EVO-X3):** Ubuntu packages, ROCm and a PyTorch build for the Radeon 8060S, Vulkan, containers, Blender, audio and mesh tools. **Forge B (the RTX 5070 Ti desktop):** a CUDA PyTorch environment (in WSL2 if the desktop runs Windows), containers, Blender, and the Forge worker. Either may be absent | A GPU tensor test passes on each machine present (ROCm and Vulkan on A, CUDA on B and C); the audit, versions, graphics memory, models reused and downloaded, and which machines are present written to `forge/bringup-report.md`; running the provisioning scripts a second time changes nothing |
| T-MA-02 | The Forge service: job API, SQLite queue, scheduler (one GPU job per machine, strict manifest order, CPU jobs in parallel; each machine runs its own service and queue, and the supervisor on the build machine shares the work out and hands over what waited for a machine that was away), resumable steps, and the transfer of files through the Forge service itself: step files between workers and finished assets to the build machine, one way, changed files only, written beside the target and renamed | API tests for every call in [Asset Forge §4](../14-asset-pipeline/00-asset-forge.md#4-the-forge-service); a job interrupted by a restart resumes from its last step; work assigned to a machine that is then stopped is taken up from its last finished step when the machine returns, or is shared out again on request |
| T-MA-03 | Convert the [Asset Manifest](../15-asset-manifest/00-manifest-index.md) (`asset-manifest.csv`, one row per asset in order of first appearance) into `asset-manifest.yaml`, adding file names, dependencies and contracts; set the queue's priority to the manifest order | Entry count equals the CSV's row count; every entry has an order, pipeline, subject, targets and file name; the queue hands out rows in manifest order per machine |
| T-MA-04 | **Contracts and placeholders** ([Placeholders and Swapping](../14-asset-pipeline/04-placeholders-and-swap.md)): write the 67 rig contracts (bones, sockets, height, clip list: the 65 rigs of the manifest, and the ship and the mine-cart, whose animated parts need bones) and the per-asset contracts; generate a placeholder for every manifest entry from its contract, including a block-out figure per rig and a procedural placeholder clip for every animation; write `asset-status.json` | The count of placeholder files equals the manifest count; every rigged placeholder contains exactly its contract's bones and sockets; every placeholder clip has its contract's length and contact frame; no two rigs share a skeleton file |
| T-MA-05 | Shared validators: technical, structural, visual (local vision model) and audio (similarity, speech detection, speech recognition), plus the **measured style gates** in [Art Direction §7](../10-art/10-art-direction.md#7-measured-style-gates) and the shared **shape pass** and **repaint pass** | Each validator rejects a deliberately bad sample and accepts a good one; the repaint pass applied to two differently lit source textures yields results whose palette and painted-light measures agree within tolerance |
| T-MA-06 | **Bring-up**: a smoke job through each of the 21 pipelines on the machine it prefers, trying the primary model, then alternates, then the other machine, then the fallback; record what runs, what fits in memory, measured seconds per asset, and each model's licence | `forge/bringup-report.md` lists, for P01–P21, the method and machine in use, its speed and its licence; every pipeline produces one valid asset |
| T-MA-07 | The fallback libraries: procedural painting, parametric Blender generators for every asset family, the audio synthesis library, constructed fonts | Every pipeline produces a valid asset with all models disabled |
| T-MA-08 | P01 style bible, generated to match [Art Direction](../10-art/10-art-direction.md): palette, anchors, proportion sheets, swatches, prompt fragments, the material library, and the style adapter if training runs on this hardware. Then calibrate the style gate thresholds on block A and freeze them | The style bible's checks pass; thresholds are recorded; everything is frozen and committed |
| T-MA-09 | Image pipelines P02–P09 | Block A's image assets pass all gates |
| T-MA-10 | 3D pipelines P10–P15 and the hair pipeline P21, including the template meshes for every rig family (built on the skeletons from the rig contracts of T-MA-04) and the kit generators | Block A's model, rig and clip pass all gates and the contract check; each kit's assembly test passes |
| T-MA-11 | Audio and font pipelines P16–P20, including the voice definitions and the pronunciation list | Block A's audio passes all gates; every proper name in the string tables is in the pronunciation list |
| T-MA-12 | Queue every remaining block in priority order. Build the delivery path: synchronisation every 2 minutes, the acceptance step with its contract checks, atomic replacement, state file update. Build the client's `AssetService` (loose run-time loading by asset id, cache by hash) and the in-place swap for every asset kind | `GET /queue` shows the full manifest queued. A test client shows a block-out wolf walking; when the generated wolf is delivered it replaces the block-out within 10 seconds, mid-stride, with no restart and no change in position. A model delivered with a missing bone is rejected and the block-out stays. The same test passes for a weapon in a hand, a skin, a clip, an icon, a sound and a music track |

**Exit:** the forge is running the whole manifest unattended, block A is complete and passes every gate, and the game build can start with placeholders for everything else.

## M0 — Foundations

| Task | Work | Acceptance test |
|---|---|---|
| T-M0-01 | Create the solution, projects, `Directory.Build.props`, the `ci fast` / `ci milestone` / `ci soak` commands ([Bots and Testing §8](bots-and-testing.md#8-where-and-when-tests-run)) and a CI workflow file; confirm the `build/` ledger files from [Build Procedure §1](build-procedure.md#1-the-ledger) exist and are current | `dotnet build` and `dotnet test` succeed on a clean clone; `ci fast` runs both and finishes inside 10 minutes |
| T-M0-02 | `Game.Shared`: `ContentId`, `EntityId`, time, yards, money types, `BitWriter` / `BitReader` | Unit tests: round-trip of every primitive; money formats "1g 20s 5c" |
| T-M0-03 | `Game.Content`: YAML loader, record base types, id handle table, `constants.yaml` | Loads a sample folder; the handle table hash is stable across runs |
| T-M0-04 | Validator framework with rules V01–V04 | A fixture folder with one broken reference fails with the file and line |
| T-M0-05 | Pack compiler and `Game.Tools content validate / build` | `build/content` is produced; the server refuses to start on a hash mismatch |
| T-M0-06 | Database: migrations 0001–0003 (account, session, character), `db migrate`, `db reset` | A test creates an account and a character against a container database |
| T-M0-07 | Login server: `LoginRequest` through `EnterWorldTicket`, Argon2id, character list, create, delete, name rules | Protocol tests for each message; bot logs in, creates "Testa", fails to create a duplicate |
| T-M0-08 | Game connection: LiteNetLib host, ticket check, `Ping`, disconnect rules | Bot connects with a ticket; a reused ticket is refused |
| T-M0-09 | Zone host skeleton: 20 Hz loop, entity registry, grid interest, `EntityCreate` / `EntityDestroy` / `EntityMove` | Two bots in the same cell see each other; a third 200 yards away sees neither |
| T-M0-10 | Server-side movement validation and `MoveCorrection` | A bot sending a 50-yard jump is corrected and logged; legal movement is not |
| T-M0-11 | Godot client: project, login and character screens (greybox), network layer, flat test map, third-person controller and camera; **the scripted client (`--play-script`) and the debug automation port** from [Build Procedure §6](build-procedure.md#6-how-the-builder-sees-the-game) | Manual: two scripted clients run around the test map; each reports the other's position through the automation port within 0.5 m of the server's, and a screenshot from each shows the other |
| T-M0-12 | Character save and load (position), logout timer | Bot logs out and back in at the same position |
| T-M0-13 | Structured logging, metrics (tick time, players), `ops/docker-compose.yml` | Tick time is reported; server runs 1 hour with 20 idle bots at < 5 ms average tick |

**Exit:** two players run around a flat test map.

## M1 — Combat core

| Task | Work | Acceptance test |
|---|---|---|
| T-M1-01 | `Game.Rules`: attributes, derived stats, armor formula, crit and dodge tables | Unit tests quoting every example value in [Combat §1–2](../02-systems/combat-and-stats.md) |
| T-M1-02 | Resources: health, rage (gain, decay), mana (regeneration, five-second rule) | Unit tests for the rage formula at levels 1, 10, 30 and for regeneration timing |
| T-M1-03 | Melee: swing timers, the single-roll attack table, glancing, dual wield | Sim test: 100,000 swings match the table within 0.3% |
| T-M1-04 | Spell engine core: cast, channel, instant, GCD, cooldowns, range, facing, line of sight, cost | Unit tests per failure reason in the protocol's spell error list |
| T-M1-05 | Effects: damage, weaponDamage, heal, applyAura, energize, interrupt, taunt, threat | One unit test per effect type |
| T-M1-06 | Auras: periodic, stat mods, stun, root, slow, absorb, stacks, exclusivity, dispel types | One unit test per aura type implemented; buff and debuff caps |
| T-M1-07 | Threat table, target switching at 110% and 130%, taunt | Sim test with scripted threat values |
| T-M1-08 | Creature records, stat templates, spawn, basic AI state machine (idle, aggro, chase, melee, flee, evade, return), leash | Bot pulls a wolf 70 yards; it evades and heals |
| T-M1-09 | Creature ability use by priority; the ability kinds in [Data Index §2](../12-data/00-data-index.md#2-creature-rules) | Sim test: each kind fires with the documented numbers at level 10 |
| T-M1-10 | Death, corpse, release, ghost run, graveyard, spirit healer, durability loss on death | Bot dies, runs back, resurrects at 50% health |
| T-M1-11 | Combat protocol messages (§5.1) end to end | Protocol tests; bot casts, is interrupted, and receives the right `CastFailed` codes |
| T-M1-12 | Client: target frame, player frame, action bar, cast bar, swing timer, buffs, floating combat text, combat log, nameplates | Manual: checklist of HUD elements in [UI §2](ui-specification.md#2-hud-layout-default-positions) present and updating |
| T-M1-13 | Level 1–10 kits for the three classes entered as content (hand-written effects) | Validator passes; each ability has a unit test for its rank 1 numbers |
| T-M1-14 | Combat simulator (`sim duel`) | Prints time to kill for each class against the level 5 template within the 12–18 s target ± 30% |

**Exit:** a Fighter, Cleric and Druid can each kill a wolf and die to three.

## M2 — Vertical slice: Brightmead Vale

| Task | Work | Acceptance test |
|---|---|---|
| T-M2-01 | Zone format: terrain chunks, streaming, collision; **the hole mask and cutouts** ([Terrain and Cutouts](terrain-and-cutouts.md)); zone editor plugin (sculpt, paint, place props, **Cutout tool**); **the world generator `tools/worldgen`**, which builds a zone from its layout tables by the rules in [World Construction](../13-world/10-world-construction.md), and is used for every later zone, capital and instance | Brightmead Vale is generated from its layout and passes every check in [World Construction §10](../13-world/10-world-construction.md#10-checks); generating it twice gives identical files. Manual: Brightmead loads; walking the whole zone never shows a hitch over 50 ms. A cutout placed in the editor removes the terrain's mesh, collision and navigation there at every detail level; a bot walks from the surface through the Hartwell Mine cutout onto the interior floor and back; deleting the cutout restores the ground; validator rule V26 rejects a cutout with no frame |
| T-M2-02 | The walk grid (`terrain/nav.bin`, [Terrain and Cutouts §1.1](terrain-and-cutouts.md#11-the-walk-grid)) baked by the world generator, and server pathfinding over it (A*) | Creatures path around the mill and fences; unreachable target evades |
| T-M2-03 | Spawns, pools, respawn timers, dynamic respawn, patrol and wander | Bot test: kill 8 pups; all respawn within 2.5 minutes ± 10% |
| T-M2-04 | Items, inventory, bags, equipment, stat application, durability; **the item generator `tools/itemgen`**, which writes every item record by [Item Rules](../12-data/item-rules.md) | Unit tests; bot equips a reward and its stats change by the item's values; the two worked examples in Item Rules §3 come out exactly; rule V28 passes for every Brightmead item |
| T-M2-05 | Loot tables, loot window, coin, corpse rules, tapping | Sim test: 10,000 kills match loot table percentages within 1% |
| T-M2-06 | Vendors, buyback, repair; stock lists; vendor values and repair costs by [Item Rules §7–§8](../12-data/item-rules.md#7-vendor-value-and-vendor-price) | Bot buys bread, sells junk, repairs; the repair bill equals the formula |
| T-M2-07 | Trainers and ability purchase; first ability free flag | Bot at level 1 knows only its class's level-1 abilities, is not offered the trainer's summons and finds every rank at its trainer unavailable (the first trainer rank of every class is learned at level 2); at level 2 it is refused without coin, trains with it, and still knows the rank after logging in again |
| T-M2-08 | Quest engine: objective types kill, collect, interact, talk, deliver, explore; prerequisites; rewards; quest log limit | Unit tests per objective type; validator rules V05–V11; the objective locator and rule V30 ([Bots and Testing §3](bots-and-testing.md#3-how-the-quester-plays)) |
| T-M2-09 | Gossip and quest dialog, quest log, tracker, quest giver markers, minimap icons; the string table with every error and system message in [Game Text](../12-data/game-text.md), and rule V29 | Manual: accept, progress and complete BM-02 with correct text; each error code shows its message |
| T-M2-10 | XP, levelling, level-up stats, rested XP, exploration XP, the group XP rule | Unit tests against [Progression](../02-systems/progression.md) tables; two-bot test of the 5-level rule |
| T-M2-11 | Inn, hearthstone, bind, rest areas, sitting, food and drink; the movement, interaction and timer values in the [Rules Reference](../02-systems/rules-reference.md) | Bot binds, hearths, eats to full; unit tests for fall damage, walk and backwards speed, interaction ranges and the idle timers |
| T-M2-12 | Import and place Brightmead content: 12 creatures, 22 NPCs, 18 quests, objects. Positions come from the world generator; models, outfits, effects, icons and sounds are assigned by [Presentation Rules](../12-data/presentation-rules.md) | `content validate` passes including V31; every spawn and NPC has a position |
| T-M2-13 | Per-player world objects and world state (grain sacks, cider barrels, the Burned Mill trigger) | Bot test for BM-07, BM-11 and BM-13 |
| T-M2-14 | Elite and mini-boss creatures; summon-at-health ability (Hale Morrow) | Two-bot test kills Morrow; he summons at 50% |
| T-M2-15 | Minimap, zone map with fog, zone banner, tutorial tips 1–10 | Manual checklist |
| T-M2-16 | **Zone bot run:** the Quester brain ([Bots and Testing §3](bots-and-testing.md#3-how-the-quester-plays)) plays BM-01 to BM-18 from the content data alone | The run completes all 18 quests; the bot is level 5 or more (the measured run leaves at level 7); the quest XP it earned is within 5% of the zone document's quest XP total; its total XP, kills, deaths, time and final level are recorded in the evidence, to be read beside the zone document's expectation of about 200–280 kills in all and leaving at about level 7 (measured: about 281 kills) |
| T-M2-17 | Art block C integrated (Brightmead kit, creatures, effects, icons) | No placeholder assets remain in the zone; 60 fps on the reference machine in Millbrook |

T-M2-17 is done after T-M3-01, T-M3-02 and the finishing of Embercrag Hollow (the order of the build-out, above). Until it is done Brightmead is played with whatever of its assets the forge has delivered and placeholders for the rest.

**Exit:** a new human plays Brightmead 1→5 start to finish with all 18 quests.

## M3 — Second start and travel

T-M3-01 and T-M3-02 are done first, ahead of T-M2-17, and Embercrag Hollow is then finished before any later task of M3 is begun (the order of the build-out, above). Finished means: every model, texture, animation, icon, sound and interface element a dwarf sees from character creation to the end of EC-18 is final and approved, none a placeholder; the visual walk of the zone passes; and the zone holds its frame-rate target. The player bodies and their animations are made first, then the zone's creatures and NPCs, its buildings, props and ground, its icons, and the interface.

| Task | Work | Acceptance test |
|---|---|---|
| T-M3-01 | Dwarf race, character creation complete | Manual: create each race, sex and class |
| T-M3-02 | Embercrag Hollow content and zone; snow terrain | Zone bot run EC-01 to EC-18 completes, held to the same checks as T-M2-16, with a dwarf (the measured run: 211 kills in 96 minutes, leaving at level 7) |
| T-M3-03 | Solhaven and Hammerdeep as zones with all service NPCs placed (no quests yet) | Every roster NPC is present and its service window opens |
| T-M3-04 | Transports: the ship on its path and schedule; lifts; boarding and riding as a passenger | Bot rides Solhaven → Seagate and arrives standing on the quay |
| T-M3-05 | Eyries: discovery, taxi map, routes and fares | Bot test: fares and times match [Reference Tables §1](../12-data/reference-tables.md#1-eyrie-routes-and-fares) |
| T-M3-06 | World map with continents; exploration saved | Manual |
| T-M3-07 | Bank and bag slots | Bot deposits, buys a slot, withdraws |
| T-M3-08 | Chat: say, yell, whisper, channels, emotes, throttling, ignore | Protocol and bot tests |
| T-M3-09 | Friends, who, AFK and DND, inspect | Bot tests |
| T-M3-10 | Groups: invite, roster, party frames, shared kill credit, shared quest credit, quest sharing | Two-bot test completes BM-16 together |
| T-M3-11 | Mail with attachments, postage, COD, delivery delay, expiry | Bot tests including a returned mail |
| T-M3-12 | Zone hand-over between adjacent zones without loading | Bot walks Brightmead → Solhaven with no disconnect and continuous position |
| T-M3-13 | Guards and the directions menu | Manual |

**Exit:** a dwarf and a human level to 5 in each other's zones and meet in Solhaven.

## M4 — Classes to 30 and talents

| Task | Work | Acceptance test |
|---|---|---|
| T-M4-01 | Remaining effect and aura types from [Content Schemas §2.4](content-schemas.md#24-spell-effect-and-aura) | One unit test per type |
| T-M4-02 | Fighter: all 27 abilities and ranks, three stances, next-swing queue | Each row of the Fighter section of [spells.md](../12-data/spells.md) has a test of its numbers |
| T-M4-03 | Cleric: all 27 abilities; Oaths, Verdict, Litanies, Benedictions, Forbearance | Same, for the Cleric section |
| T-M4-04 | Druid: all 19 abilities; Reawaken with its reagent, channelled spells | Same, for the Druid section |
| T-M4-05 | Spell power coefficients and the low-level penalty | Unit tests against the coefficient column |
| T-M4-06 | Talent system, the nine trees, prerequisites, preview and commit, respec with price decay | Unit tests; all 138 talents load and each changes the stat or ability it names |
| T-M4-07 | Talent, spellbook and character windows | Manual checklist against [UI §3](ui-specification.md#3-windows) |
| T-M4-08 | Class quests | Bot runs each of the 10 class quests on one continent |
| T-M4-09 | Crowd control diminishing returns, dispels, resistances, immunities | Unit tests |
| T-M4-10 | Weapon skills, defense skill, weapon master | Unit tests |
| T-M4-11 | Simulator rotations for the nine specs | Sim test: every spec meets its target in [Combat §11](../02-systems/combat-and-stats.md#11-role-balance-targets-at-level-30-v0); failures are fixed in data, not code |
| T-M4-12 | Enter the verified XP table and lock it | Unit test: the table sums to 499,000 at level 30 and 4,084,700 at level 60 |

**Exit:** the simulator hits the role targets.

## M5 — Professions and economy

| Task | Work | Acceptance test |
|---|---|---|
| T-M5-01 | Skill lines, ranks, skill-up chance by recipe colour | Unit tests |
| T-M5-02 | Gathering nodes (mining, herbalism), skinning, tracking | Bot gathers copper; node respawns; skill rises |
| T-M5-03 | Crafting engine and UI; tools and stations | Bot crafts Copper Chain Belt at an anvil |
| T-M5-04 | All recipes entered (about 220) | Validator V18; every recipe is craftable in a scripted test with granted reagents |
| T-M5-05 | Enchanting and disenchanting; temporary weapon enchants | Unit tests |
| T-M5-06 | Cooking, fishing (pools, tables), first aid | Sim test: 10,000 casts match the fishing tables within 1% |
| T-M5-07 | Consumables: potions with shared cooldown, elixir slots, scrolls, food buffs | Unit tests |
| T-M5-08 | Random-suffix items and world drops | Sim test: suffix stat budgets within 5% |
| T-M5-09 | Trade window | Two-bot test including a cancel after a change |
| T-M5-10 | Auction house: search, bid, buyout, expiry, mail delivery, the cut; linked capitals | Bot tests for each path; coin is conserved except for cut and deposit |
| T-M5-11 | Economy log and the coin-flow report | Report shows coin in and out per level for a bot run 1–10 |
| T-M5-12 | Recipe vendors and limited stock | Bot buys a limited recipe; restock after the timer |

**Exit:** craft a blue from gathered materials and sell it on the auction house.

## M6 — Level 5–20 zones and Main Chain 1

| Task | Work | Acceptance test |
|---|---|---|
| T-M6-01 | Objective types escort, defend, useItem, subdue, castOn, event; quest timers and failure | Unit tests per type |
| T-M6-02 | Exclusive groups and any-of prerequisites | Bot enters Thornwick from Harrowfield and, on a second character, from Russetwood |
| T-M6-03 | Reputation: gains, standings, discounts, quartermasters | Unit tests against [Reference Tables §2](../12-data/reference-tables.md#2-reputation) |
| T-M6-04 | Interior zone support: no heightmap, ceiling-aware camera, layered minimap, a walk grid of interior layers only, mine-carts | Manual in Stoneheart Deeps; bot rides the carts |
| T-M6-05 | Day and night, night-only spawns and objects, weather | Bot test for TM-27 and IR-20 time rules |
| T-M6-06 to T-M6-11 (parallel) | One task per zone: Harrowfield, Russetwood, Stonewake Dale, Stoneheart Deeps, Thornwick Marches, Ironroot Highlands. Import, place, script | Zone bot run completes every quest in the zone in an order that respects prerequisites |
| T-M6-12 | Named, rare and elite creatures with their timers; wanted boards | Sim test of rare timers; bot test of one wanted quest per zone |
| T-M6-13 | Neutral NPC camps that change reaction by quest (Pact Watch, Mugga's camp) | Bot test of TM-23 and IR-22 |
| T-M6-14 | The Brandspire siege: phased camp, the two-route TM-35, the finale and its scripted scene | Three-bot test kills Ashgrave on each route |
| T-M6-15 | Validator reports: XP available per zone against the curve | Report matches the zone documents' totals within 3% |

**Exit:** play Chain 1 to the Branded Lord on both routes.

## M7 — Instances and Dungeon 1

| Task | Work | Acceptance test |
|---|---|---|
| T-M7-01 | Instance allocation, entry, reset, the 5-per-hour cap, transfer of group members | Bot soak: 50 instances created and destroyed with no leaked entities |
| T-M7-02 | Group loot: round-robin, need and greed rolls, threshold, master looter, bind-on-pickup prompts | Five-bot tests per method |
| T-M7-03 | Meeting stones and the group-finder board | Bot tests |
| T-M7-04 | Encounter engine: phases, timelines, adds, objects, enrage, boss frames, the encounter debugger | Unit tests driving a sample timeline |
| T-M7-05 | Gallowmere Crypts: map, 21 packs, 4 bosses with the numbers in [encounters.md](../12-data/encounters.md) | Each boss has a scripted five-bot test that wins when mechanics are followed and loses when they are ignored |
| T-M7-06 | Dungeon quests TM-15, TM-16, TM-17 and the IR-15 route | Bot test |
| T-M7-07 | Dungeon elite XP and the tuning targets | Five bots in level-appropriate greens clear in 35–45 minutes |

**Exit:** a five-player group clears the Crypts; bots soak-test instance creation.

## M8 — Level 20–30 zones, Dungeons 2–3, Main Chain 2

| Task | Work | Acceptance test |
|---|---|---|
| T-M8-01 to T-M8-03 (parallel) | Cinderfall Barrens, the Riftlands, Veilmoor: import, place, script | Zone bot runs |
| T-M8-04 | Kite's Rest: sanctuary rules, neutral auction house, shared bank, envoys and the RL-14 flags | Bot tests; flags are saved |
| T-M8-05 | Environmental hazards (lava, slag) and defend events (CF-35, RL-33, VM-21) | Bot tests |
| T-M8-06 | Ride-along and scripted travel (CF-13) | Bot test |
| T-M8-07 | The Slagworks | Per-boss five-bot tests, including Lull Beast on Cinderpaw |
| T-M8-08 | Hollowspire Keep, the ward quest gate (VM-28), the VM-29 ending scene and shard removal | Per-boss tests; the two shards leave the bags of every player on the quest |
| T-M8-09 | The attunement quest RL-35 | Bot holding the three parts receives the Vault Key |
| T-M8-10 | Level 30 cap behaviour: quest XP to coin | Unit test at 6 copper per XP |

**Exit:** play Chain 2 to the raid attunement.

## M9 — PvP

| Task | Work | Acceptance test |
|---|---|---|
| T-M9-01 | The hostility function and duels | Unit tests for every case in [PvP §1–2](../02-systems/pvp.md) |
| T-M9-02 | Free-for-all areas; the Dustpit, its chest, tokens, graveyard and guards | Bot tests |
| T-M9-03 | Battleground framework with N teams: queue, brackets, assignment, backfill, deserter | Unit tests with 2, 3 and 4 teams |
| T-M9-04 | Crownfall: hill, crown, shrines, scoring, scoreboard | 24-bot match ends with a winner and correct marks |
| T-M9-05 | Marks of Valor and the Valor quartermasters | Bot buys a Contender's piece |
| T-M9-06 | Diminishing returns against players; PvP-only consumables | Unit tests |

**Exit:** twelve scripted clients, four per team, play a full three-team match to a win.

## M10 — Endgame

| Task | Work | Acceptance test |
|---|---|---|
| T-M10-01 | Raid groups: 10 and 20, subgroups, raid frames, ready check, raid targets, raid lockouts and saves | Bot tests |
| T-M10-02 | Raid loot: tier tokens and their exchange, the two-hour trade window | Bot tests |
| T-M10-03 | The Hollow Throne: map, trash, Ward Strain, six bosses | Per-boss ten-bot tests; Ilyra's Recitation needs three interrupts |
| T-M10-04 | RL-36 and the ending, skybox change, epilogue scene | Bot test |
| T-M10-05 | World bosses: spawn timers, tagging, loot lock, the three encounters and their quests | 40-bot load test holds the tick under 25 ms |
| T-M10-06 | Riding, mounts, mount vendors and the reputation rule | Bot tests |
| T-M10-07 | Epic mount feed system, dormant | Unit tests with the cap raised in a test configuration |

**Exit:** raid cleared internally; the 40-bot world-boss load test passes.

## M11 — Social and polish

| Task | Work | Acceptance test |
|---|---|---|
| T-M11-01 | Guilds: charter, ranks, permissions, roster, notes, MOTD, events | Bot tests |
| T-M11-02 | Guild bank: tabs, slots, money, per-rank limits, logs, guild repair | Bot tests of every limit; logs record each action |
| T-M11-03 | Tabards, barber, titles | Manual |
| T-M11-04 | Macros and the slash commands in [UI §5](ui-specification.md#5-slash-commands) | Unit test per command |
| T-M11-05 | Options, key bindings, accessibility, movable frames | Manual checklist |
| T-M11-06 | GM commands, audit log, tickets; player reports, automatic mute, penalties and appeals, the ignore rules and chat limits in [Accounts and Live Service §3–§4](accounts-and-live-service.md#3-conduct-and-moderation) | Bot tests per command; five bots reporting a sixth for spam mute it for 30 minutes; a muted bot cannot speak in public channels |
| T-M11-07 | Audio pass (list 9 of the art lists): every event triggers the sound chosen by [Presentation Rules §5–§6](../12-data/presentation-rules.md#5-hits-steps-and-voices); every line in [Spoken Lines](../12-data/spoken-lines.md) plays at its moment with its subtitle | State checks through the automation port: each listed event reports the expected sound asset; each boss line fires once at its moment |
| T-M11-08 | Remaining tutorial tips and the 40 loading tips from [Game Text](../12-data/game-text.md), loading screens, credits (the third-party notices and the AI-generated content statement) | Manual: each tip fires on its trigger with its text |
| T-M11-09 | Critters, ambient citizens and street chatter, and the 12 Athenaeum books, from [Spoken Lines §6–§7](../12-data/spoken-lines.md#6-the-athenaeum-books) | Manual: chatter appears at the stated rate in each capital; each book opens with its text |

**Exit:** the full-game bot run, the visual walk of the whole world and the state check of every window all pass ([Build Procedure §7](build-procedure.md#7-tests-written-for-people)).

## M12 — Hardening

| Task | Work | Acceptance test |
|---|---|---|
| T-M12-01 | Single-process load test | 300 bots for 4 hours, tick under 25 ms, no restart |
| T-M12-02 | Bandwidth checks against the protocol budget | Measured values within the targets in [Protocol §8](network-protocol.md#8-bandwidth-budget) |
| T-M12-03 | Anti-cheat and anti-botting as in [Accounts and Live Service §5](accounts-and-live-service.md#5-anti-cheat-and-anti-botting): movement strikes, timing checks, economy anomaly report, bot signals, the nightly coin balance check | Every cheater bot in [Bots and Testing §5](bots-and-testing.md#5-cheater-bots) is refused and logged; a bot that runs one route for three hours is scored and queued for review, not banned |
| T-M12-04 | Backup and restore drill | A restored database passes the login and inventory tests |
| T-M12-05 | Full-game bot run: one bot per class plays 1–30 on each continent | All six finish; the played time is within 25% of the target in [Progression §6](../02-systems/progression.md) |
| T-M12-06 | Bug burn-down | No open bug of the two highest severities |

**Exit:** 300 concurrent bots for 4 hours without a restart.

## M13 — Scale-out to 5,000

The launch target is 5,000 concurrent players on one realm ([Architecture §9](architecture.md#9-performance-targets)). Everything before this milestone runs in one process; this milestone splits it into processes that run **either all on one server or across a cluster**, chosen only by `deploy/topology.yaml` ([Architecture: One server to a cluster](architecture.md#one-server-to-a-cluster)). Game servers are given to the builder as the environment variable `GAME_SERVER_HOSTS` (a list of SSH hosts). If it is absent or names one machine, every test here runs in the single-server shape, the cluster shape is exercised with containers on that one machine standing in for separate machines, and the full-size figures (5,000 bots, 1,500 in a zone) are run at the largest size the machine holds, with the measured size recorded in `deploy/capacity.md`.

| Task | Work | Acceptance test |
|---|---|---|
| T-M13-01 | Redis-backed `IBus` beside the in-process one; every cross-module message serialisable | The whole test suite passes with either bus selected by configuration |
| T-M13-02 | Split the gateway into its own process tier; clients connect only to gateways | Killing a zone host disconnects nobody on other zone hosts |
| T-M13-03 | World service and social service as separate processes; realm state survives a zone-host restart | Bot test: groups, guild chat and auctions keep working while a zone host restarts |
| T-M13-04 | Zone hosts and instance hosts as a managed pool; a supervisor reads `deploy/topology.yaml` and starts, places and stops them on one machine or across several; processes find each other through its registry | 60 zone-host processes and 400 instance copies start and stop cleanly in a soak test; the whole test suite passes with the single-server topology and with a three-machine topology |
| T-M13-05 | Seamless hand-over between zone hosts on different machines | Bot walks every zone border 1,000 times with no disconnect and no duplicated or lost item |
| T-M13-06 | **One world at full density** (there are no layers): crowd update-rate tiers on the server, low-detail crowd rendering on the client, dynamic respawn down to 15%, per-player quest objects | Bot tests for each rule in [Architecture: One world, no layers](architecture.md#one-world-no-layers); 1,500 bots in Brightmead Vale in one copy of the zone, all visible to each other, tick within budget |
| T-M13-07 | Capitals at 2,000 players; border strips between zone hosts so players see across zone edges | 2,000 bots in Solhaven within the bandwidth and tick budgets; a bot standing at a border sees bots on the other side |
| T-M13-08 | Login queue with position and estimated wait; reconnect grace so a dropped player keeps their place | 6,000 bots log in: 5,000 play, 1,000 queue and enter in order as others leave |
| T-M13-09 | Database: connection pooling, a read replica for auction search and who-lists, save batching, slow-query log | At 5,000 bots, 95% of saves complete within 200 ms and no auction search exceeds 500 ms |
| T-M13-10 | Chat, who, auction and mail at realm scale: fan-out limits, paging, rate limits re-checked | Trade channel at 20 messages a second reaches 3,000 capital players within the bandwidth budget |
| T-M13-11 | Deployment: container images per process type, configuration per environment, rolling restart of zone hosts, weekly full restart | A full deploy from one command to a clean single server, and to a clean cluster; **a running single-server realm is grown to two machines by editing the topology file and redeploying, then folded back to one, with no character data lost**; `realm.maxPlayers` is honoured by the login queue; a zone host is replaced under load with no player-visible error beyond a 5-second pause for its players |
| T-M13-12 | Monitoring and alerting: per-host tick time, players per zone, queue length, database latency, error rates; dashboards | An induced slow host raises an alert within 60 seconds |
| T-M13-13 | Staged load tests: 1,000, 2,500, then 5,000 bots playing a realistic mix (questing 60%, capitals 20%, dungeons 12%, battleground 5%, raid and world boss 3%) | On a single server: the bot count is raised until the tick budget is reached, and that count is written to `deploy/capacity.md` as the server's `realm.maxPlayers`; it then holds that count for 8 hours. On a cluster, where one is provided: 5,000 bots for 8 hours. In both: every host under its tick budget; bandwidth within the protocol budget; no data loss |
| T-M13-14 | Failure drills: kill a gateway, the world service, a zone host, Redis and the database primary in turn | Each recovers by the documented runbook; at worst players on the failed part reconnect within 2 minutes with nothing lost beyond 60 seconds of position |

**Exit:** the game runs complete on a single server at its measured capacity for 8 hours, grows onto a second machine and back by configuration alone, and (where a cluster is provided) holds 5,000 bots for 8 hours with every host under its tick budget.

## M14 — Launch readiness

| Task | Work | Acceptance test |
|---|---|---|
| T-M14-01 | Account services as specified in [Accounts and Live Service](accounts-and-live-service.md): registration, e-mail verification, password reset, account security log, account deletion | Bot and scripted-client tests of each flow against a local mail catcher |
| T-M14-02 | Patcher and installer: content and client updates by manifest, resume, integrity check | A client two versions behind updates and logs in; a corrupted file is repaired |
| T-M14-03 | Client crash reporting and server error aggregation | A forced crash appears in the report tool with its build and log |
| T-M14-04 | Support tools: web admin for accounts, characters, tickets, item restoration from the economy log | A deleted item is restored from the log by a GM account, with an audit entry |
| T-M14-05 | Name reservation and reserved-name list; profanity filter for names and chat (optional per player for chat) | Reserved and filtered names are refused at creation |
| T-M14-06 | Launch-day plan for one shared world: staggered queue release, starting-zone respawn at its 15% floor, extra guards on the roads out | Dry run with 5,000 bots all created at level 1 within 10 minutes |
| T-M14-07 | Beta readiness: a 72-hour soak at the deployment's measured capacity with bots playing the realistic mix, including two rolling restarts, a backup-and-restore and a content hotfix. Betas with real players are the owner's, listed in `build/for-the-owner.md` | No data loss; the two highest bug severities at zero at the end |
| T-M14-08 | Live-operations runbook: restart, rollback, hotfix of content without a client patch, incident roles | A content-only hotfix reaches a running realm with a rolling zone-host restart |
| T-M14-09 | Legal and policy pages: terms, privacy, code of conduct, AI-generated content statement | Drafted from [Accounts and Live Service §8](accounts-and-live-service.md#8-legal-and-policy-pages), marked DRAFT, and linked from the login screen and the installer; legal review is the owner's |

**Exit:** the 72-hour soak passes with no data loss, and the files in [Build Procedure §9](build-procedure.md#9-what-the-builder-leaves-at-the-end) are written. The game is then ready for the owner to play and to open to real players.

## Counts

16 milestones (MA, then M0 to M14) · 169 tasks (MA 12 · M0 13 · M1 14 · M2 17 · M3 13 · M4 12 · M5 12 · M6 10 · M7 7 · M8 8 · M9 6 · M10 7 · M11 9 · M12 6 · M13 14 · M14 9). Assets arrive in the order of the [Asset Manifest](../15-asset-manifest/00-manifest-index.md), which follows first appearance in the game, so each zone and dungeon task finds its assets generated before those of later zones; anything not yet generated is a placeholder.
