# Build Roadmap

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Data Model](data-model.md) · Next: [WoW Feature Inventory](../09-reference/wow-feature-inventory.md)

Order of construction once coding begins. Each milestone ends in something playable and testable. No dates — sizes are relative (S / M / L / XL).

## Launch scope

This is a full game, not a proof of concept, built for 5,000 concurrent players on one realm. **Version 1.0** is everything in these documents: 1 allegiance, 2 races, 3 classes, 11 zones, 2 capitals, 296 zone quests + class quests, 3 dungeons, 1 ten-player raid, 3 world bosses, 9 gathering/crafting + 3 secondary professions, guilds and guild banks, duels, the Dustpit arena and the Crownfall battleground, levels 1–30.

## Milestones

Milestones are built in the order of the table, with one exception decided by the owner on 2026-11-24: **the dwarf starting zone, Embercrag Hollow, is the priority of the build-out.** Once Brightmead Vale is playable from start to finish by the bots (M2 up to its zone bot run), the dwarf race and Embercrag Hollow (the first two tasks of M3) are built next, and Embercrag Hollow is brought to a finished, polished state (final models, textures, animations, icons and interface) before the build returns to what remains of M2 (Brightmead's art integration) and to the rest of M3. Inside that work the player bodies and their animations come before all other art. The task-level statement is in [Milestone Task Lists](milestone-tasks.md).

| # | Milestone | Size | Contents | Exit test |
|---|---|---|---|---|
| MA | **Asset Forge** (first) | L | The asset generation system on the dedicated EVO-X3 and the RTX 5070 Ti desktop: provisioning, the Forge service and queue, the asset manifest, placeholders, automatic quality gates, the owner's approval of the style guidelines and of each pipeline's first results before anything is generated in number, the style bible, and twenty-one pipelines (images, 3D, hair, rigs, animation, audio, fonts) each with a model-free fallback | The forge is generating the whole manifest unattended and block A passes every gate |
| M0 | **Foundations** | M | Repository, build, content format + validator, shared rules library skeleton, database schema, login → character create → enter empty world; two clients see each other move | Two players run around a flat test map |
| M1 | **Combat core** | L | Stats, auto-attack, spell engine (effects + auras), GCD/cast/cooldowns, health/rage/mana, threat, basic creature AI, death and respawn, target/HUD frames, action bar, combat log | A Fighter, Cleric and Druid (level 1–10 kits) can each kill a wolf and die to three |
| M2 | **Vertical slice: Brightmead Vale** | XL | Terrain streaming, zone tools, spawns, loot, inventory/equipment, vendors, trainers, quest system + log + tracker, XP/leveling, NPC dialog, minimap, graveyard/corpse run, inn/hearthstone/rest | A new human plays [Brightmead](../05-zones/t1-brightmead-vale.md) 1→5 start to finish with all 18 quests |
| M3 | **Second start + travel** | L | Dwarf race, Embercrag Hollow, both capitals (services only), the capital ship (Solhaven ↔ the Seagate inside Hammerdeep), eyries, world map, exploration, bank, mail, chat channels, friends, groups | A dwarf and a human level to 5 in each other's zones and meet in Solhaven |
| M4 | **Classes to 30 + talents** | L | All abilities and ranks, stances/Oaths/Litanies, talent UI and all nine trees, class quests, respec, buffs/debuffs UI, combat simulator and balance pass | Simulator hits the role targets in [Combat §11](../02-systems/combat-and-stats.md#11-role-balance-targets-at-level-30-v0) |
| M5 | **Professions + economy** | L | Gathering nodes, all recipes, crafting UI, enchanting, auction house, trade, repair, durability, random-suffix items, consumables | Craft a blue from gathered materials and sell it on the auction house |
| M6 | **T2 + T3 zones, Main Chain 1** | XL | Harrowfield, Russetwood, Stonewake Dale, Stoneheart Deeps (the first interior zone: cavern kit, a walk grid of interior layers, layered minimap), Thornwick, Ironroot; elites and rares; escort/defend/object quest types; exclusive-group chains; reputation | Play Chain 1 to the Branded Lord on both routes |
| M7 | **Instances + Dungeon 1** | L | Instance hosting, group loot rules, meeting stones, encounter scripting, Gallowmere Crypts, group-finder board | A 5-player group clears the Crypts; bots soak-test instance creation |
| M8 | **T4 zones, Dungeons 2–3, Main Chain 2** | XL | Cinderfall, Riftlands (incl. Kite's Rest, neutral AH), Veilmoor; The Slagworks; Hollowspire Keep | Play Chain 2 to the raid attunement |
| M9 | **PvP** | M | Duels, Free-for-all area + Dustpit chest, battleground framework (N teams), Crownfall, Marks of Valor vendor | 12 scripted clients play a full three-team match |
| M10 | **Endgame** | L | Raid framework (10- and 20-player sizes, lockouts, master loot), The Hollow Throne, tier sets, world bosses, riding/mounts and the epic-mount feed system (dormant at cap 30) | Raid cleared internally; 40-bot world-boss load test passes |
| M11 | **Social + polish** | M | Guilds, guild bank (tabs, per-rank permissions and limits, logs), tabards, inspect, emotes, barber, macros, options/accessibility, GM tools, weather/day-night, audio pass, tutorial tips | Full-game bot run, visual walk of the world and window checks all pass |
| M12 | **Hardening** | M | Single-process load tests, anti-cheat checks, backup/restore drill, economy audit, bug burn-down | 300 concurrent bots for 4 hours without a restart |
| M13 | **Scale-out to 5,000** | XL | Split into gateway, world, social, zone-host and instance-host processes that run on one server or across a cluster, chosen by a topology file; Redis bus; one copy of every zone at 1,500 players (no layers); login queue; database replica and pooling; deployment and monitoring; staged load tests | Runs complete on one server at its measured capacity; grows onto more machines by configuration alone; 5,000 bots for 8 hours where a cluster is provided |
| M14 | **Launch readiness** | L | Beta readiness, account services (registration, password reset, support tools), patcher and installer, crash reporting, live-operations runbook, launch-day plan | A 72-hour soak at measured capacity with no data loss; betas with real players are the owner's |

## Dependency notes

- M1 before everything: the spell engine is the foundation for classes, items, creatures, professions and encounters.
- The **content validator** (M0) is what lets the 296 quests, 151 creature types, about 220 recipes and 138 talents in these documents be entered quickly and safely.
- Zones can be built in parallel with systems after M2 because zone content is data + art.
- The dwarf start (the first two tasks of M3) depends on nothing in M2's last task, art integration, which is why it can come first: both starting zones are generated by the same world generator and imported by the same zone importer.
- PvP (M9) is independent of M6–M8 and can move earlier if desired for fun-testing combat.

## Biggest risks

| Risk | Mitigation |
|---|---|
| **Art volume** — 11 zones (one fully interior), 2 cities, ~60 creature skeletons, armor sets | Stylised low-poly; all art AI-generated by the [Asset Forge](../14-asset-pipeline/00-asset-forge.md) to one [art direction](../10-art/10-art-direction.md), checked by automatic gates and, per pipeline, approved by the owner before anything is generated in number; reuse skeletons with re-textures (the zone docs already share families across zones); grey-box everything first |
| **AI-generated art and audio quality** — inconsistent style between assets, poor mesh topology, rigs and animation that generation tools do poorly | Lock the style guide first (art block A); generate against fixed reference sheets; retopologise and rig by a fixed procedure; reject and regenerate rather than hand-repair; keep the rig count low (62) so animation is produced once per rig |
| **Population density at 5,000** — starting zones are 1 km² | There are no layers: every zone is one shared copy. Each zone host is built to hold 1,500 players; dynamic respawn falls to 15% in crowds; quest objects are per-player; a login queue caps the realm at 5,000 (see [Architecture](architecture.md#one-world-no-layers)). Launch-day crowding in the two starting zones is accepted, as it was in 2004 |
| **Scope** — this is a very large game | Milestones are each shippable; M2 alone proves the core loop. Cut order if needed: Engineering → world bosses → third T4 zone's side quests → weapon skills |
| **Server performance at world bosses** | Interest management and load tests from M7; cap visible effects |
| **Balance of nine specs** | Simulator from M4; tuning as data |
| **The builder losing its place in a run that lasts weeks** | The ledger, resume steps and failure rules in [Build Procedure](build-procedure.md); automated tests and the validator; documentation as the source of truth |

## After version 1.0 (not scheduled)

1. Level cap 40: five new zones (2 Meridia, 2 Khazrun, 1 Sundrel), plate armor, Artisan professions, dungeon 4.
2. Second allegiance (Wildpact: Elf, Ogre) with start zones; world PvP flagging; Crownfall by allegiance.
3. Class 4 and 5 (Warlock, Rogue), then Archer.
4. Third allegiance (Ashen Covenant: Undead).
5. Sundrel continent 40–60; second raid; three-way control zone.
