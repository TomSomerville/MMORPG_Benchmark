# MMORPG — Master Plan

**Project:** `MMORPG` (working title: Halcyra) · **World:** Halcyra · **Document version:** 0.17 (specification only — no game code) · **Date:** 2026-11-25

**What this repository is for.** It is a complete design specification for an MMORPG, written to be handed to an AI model with a single prompt, to see whether the model can build a full, playable game from it in one run. The prompt is in **[Build Prompt](BUILD_PROMPT.md)**. There is no scoring: the result is judged by playing it.

This is the single starting point. Read it top to bottom, then follow the links in [§3 Reading order](#3-reading-order) to walk the whole game from level 1 to the raid. What changed in each version is listed in [§10](#10-change-log).

---

## 1. What we are building

A classic-style, tab-target, open-world MMORPG modelled on the 2004-era genre standard — the same breadth of systems, the same leveling pace — with these deliberate differences:

| Area | Launch (version 1.0, a full game) | Designed to grow into |
|---|---|---|
| Factions | **1** — the Concord of Dawn | **3** in a power triangle: Concord, Wildpact, Ashen Covenant |
| Races | **2** — Human, Dwarf (dwarves in two cultures: mountain and hill) | Gnome, Elf, Ogre, Undead, more |
| Classes | **3** — Fighter, Cleric, Druid (9 specs covering tank, healer, melee and ranged damage) | Warlock, Rogue, Archer, more |
| Level cap | **30**, with a full endgame at 30 | 60 (all curves already defined) |
| Continents | Meridia (human), Khazrun (dwarf) | Sundrel (30–60) |
| Zones | **11**: 2 × 1–5, 4 × 5–10, 2 × 10–20, 3 × 20–30. No water zones | 22 by level 60, filling only **half** of each continent |
| Story | Two main chains: 1–20 and 15–30 | Faction war |
| Group content | 3 dungeons (13–16, 20–23, 27–30), 1 ten-player raid, 3 world bosses | Raids of 10 and 20 players (never 40) |
| PvP | Duels, one FFA arena, one **three-team** battleground | World PvP between three allegiances |
| Guilds | Guilds and guild banks | Calendar |

## 2. Design pillars

1. **Classic pace.** ~48 hours played solo to reach 30. Levels matter; the world is the content. ([Progression](docs/02-systems/progression.md))
2. **Everything extensible is data.** Allegiances, races, classes, spells, items, quests are records, never hard-coded. Nothing assumes "two sides". ([Data Model](docs/08-tech/data-model.md))
3. **No race-locked questing, and redundancy.** Two starting zones and four 5–10 zones; any character can level in any of them.
4. **Three classes, nine real roles.** Every 5-player and 10-player composition is buildable. ([Class Framework](docs/03-classes/class-framework.md))
5. **A triangle, not a line.** Three factions that each prey on one and fear the other, so no side can ever "win". ([Lore](docs/01-world/lore.md#4-the-three-factions--the-power-triangle))
6. **Room to grow.** Planned zones use half of each continent; the rest is reserved for future zones, capitals and starting areas. ([World](docs/01-world/world-and-travel.md))
7. **Gold keeps leaving.** Sinks that scale with time played, so the economy holds at the level cap. ([Economy](docs/02-systems/economy-and-social.md#4-the-level-60-gold-sink-plan))
8. **Read your way through it.** Every zone, quest, creature, talent and recipe is written down before a line of code.

## 3. Reading order

### Part 1 — The world
| # | Document | What it covers |
|---|---|---|
| 1 | [Lore of Halcyra](docs/01-world/lore.md) | Cosmology, history, the three-faction triangle, villains, story summary |
| 2 | [Factions & Races](docs/01-world/factions-and-races.md) | Allegiance system built for N factions, reputation, Human and Dwarf racials, mountain and hill dwarves, future races |
| 3 | [World, Zones & Travel](docs/01-world/world-and-travel.md) | Continents, the zone plan to 60 and the half rule, both capitals, the capital ship, flight |

### Part 2 — Core systems
| # | Document | What it covers |
|---|---|---|
| 4 | [Progression](docs/02-systems/progression.md) | XP table 1–60, kill and quest XP formulas, group XP rules, rested XP, unlocks by level, death |
| 5 | [Combat & Stats](docs/02-systems/combat-and-stats.md) | Attributes, attack table, spells, rage and mana, threat, crowd control |
| 6 | [Items & Loot](docs/02-systems/items-and-loot.md) | Qualities, slots, stat budgets, random suffixes, loot tables, bags, consumables |
| 7 | [Economy & Social](docs/02-systems/economy-and-social.md) | Money flow, the level-60 gold sink plan, auction house, mail, chat, groups, guilds, guild bank |
| 8 | [NPC AI & World Simulation](docs/02-systems/npc-ai-and-world.md) | Creature stats, AI, spawning, quest engine, world objects, instances |
| 9 | [PvP](docs/02-systems/pvp.md) | Duels, the Dustpit FFA arena, Crownfall three-team battleground, future faction war |
| 10 | [UI & Controls](docs/02-systems/ui-and-controls.md) | Controls, HUD, every window |

### Part 3 — Classes
| # | Document | What it covers |
|---|---|---|
| 11 | [Class Framework](docs/03-classes/class-framework.md) | Roles, base stats, talents rules, class quests, how new classes are added |
| 12 | [Fighter](docs/03-classes/fighter.md) | Rage, stances, every ability 1–30; Bulwark / Reaver / Greatarms talents |
| 13 | [Cleric](docs/03-classes/cleric.md) | Oaths, Verdict, Litanies, Benedictions; Aegis / Grace / Reckoning talents |
| 14 | [Druid](docs/03-classes/druid.md) | Every spell 1–30; Verdance / Stormcall / Starweave talents |

### Part 4 — Professions
| # | Document | What it covers |
|---|---|---|
| 15 | [Framework & Gathering](docs/04-professions/gathering.md) | Rules, material tiers, every ore, herb and hide and where it is found |
| 16 | [Crafting](docs/04-professions/crafting.md) | Every recipe: Blacksmithing, Leatherworking, Tailoring, Alchemy, Enchanting, Engineering |
| 17 | [Secondary](docs/04-professions/secondary.md) | Cooking, Fishing, First Aid |

### Part 5 — The journey, level 1 to 30
| # | Document | Levels |
|---|---|---|
| 18 | [The Leveling Path](docs/05-zones/00-leveling-path.md) | Overview and level-by-level expectations |
| 19 | [Brightmead Vale](docs/05-zones/t1-brightmead-vale.md) · [Stonewake Dale](docs/05-zones/t1-stonewake-dale.md) | 1–5 |
| 20 | [Harrowfield](docs/05-zones/t2-harrowfield.md) · [Russetwood](docs/05-zones/t2-russetwood.md) · [Embercrag Hollow](docs/05-zones/t2-embercrag-hollow.md) · [Stoneheart Deeps](docs/05-zones/t2-stoneheart-deeps.md) | 5–10 |
| 21 | [Thornwick Marches](docs/05-zones/t3-thornwick-marches.md) · [Ironroot Highlands](docs/05-zones/t3-ironroot-highlands.md) | 10–20 |
| 22 | [Cinderfall Barrens](docs/05-zones/t4-cinderfall-barrens.md) · [The Riftlands](docs/05-zones/t4-riftlands.md) · [Veilmoor](docs/05-zones/t4-veilmoor.md) | 20–30 |
| 23 | [Main Chain 1 — Embers of the Brand](docs/06-quests/main-chain-1-embers-of-the-brand.md) | 1–20 |
| 24 | [Main Chain 2 — The Hollow Crown](docs/06-quests/main-chain-2-the-hollow-crown.md) | 15–30 |
| 24a | [Quest Text — all 296 quests written out](docs/06-quests/text/00-quest-text-index.md) (offer, tracker, progress and completion text, prerequisites, exact rewards, drop sources) | 1–30 |

### Part 6 — Group content
| # | Document | What it covers |
|---|---|---|
| 25 | [Dungeons](docs/07-instances/dungeons.md) | Gallowmere Crypts, The Slagworks, Hollowspire Keep — bosses, mechanics, loot |
| 26 | [Raid — The Hollow Throne](docs/07-instances/raid-the-hollow-throne.md) | 10 players, 6 bosses, tier sets |
| 27 | [World Bosses](docs/07-instances/world-bosses.md) | Grimroot, Pyrraxis, Gorrath |

### Part 7 — How it gets built
| # | Document | What it covers |
|---|---|---|
| 28 | [Technical Architecture](docs/08-tech/architecture.md) | Godot 4 + C#, server and client design, networking, tools, testing |
| 29 | [Data Model & Extensibility](docs/08-tech/data-model.md) | Every content record; how factions, races and classes are added later |
| 30 | [Build Roadmap](docs/08-tech/roadmap.md) | Milestones MA and M0–M14, risks, post-launch order |
| 30a | [Repository Layout and Conventions](docs/08-tech/repo-and-conventions.md) | Folder and project layout, fixed technical choices, coding rules, commands |
| 30b | [Content Schemas](docs/08-tech/content-schemas.md) | Exact YAML fields for every record type, worked examples, 31 validation rules |
| 30a2 | [Build Procedure](docs/08-tech/build-procedure.md) | How the builder works through an unattended run: the progress ledger, resuming, what to do when a test fails or the documents are silent, how it sees and checks the game itself, and what replaces tests written for human testers |
| 30a4 | [Bots and Testing](docs/08-tech/bots-and-testing.md) | The automated players that test the game: bot brains, how a questing bot plays a zone from the content data, the load-test mix, cheater bots, the scripted-client plays |
| 30a3 | [Accounts and Live Service](docs/08-tech/accounts-and-live-service.md) | Accounts, names, conduct and moderation, support, anti-cheat and anti-botting, updates and restarts, telemetry, policy pages |
| 30b2 | [Terrain and Cutouts](docs/08-tech/terrain-and-cutouts.md) | The terrain format and how holes are cut in the map for caves and dungeon entrances; how to insert a dungeon later |
| 30c | [Database Schema](docs/08-tech/database-schema.md) | Every table as SQL, limits, atomic transactions |
| 30d | [Network Protocol](docs/08-tech/network-protocol.md) | Connection sequence, wire format, full message catalogue, error codes, GM commands |
| 30e | [UI Specification](docs/08-tech/ui-specification.md) | Layout and behaviour of every HUD element and window, keybindings, slash commands |
| 30f | [Milestone Task Lists](docs/08-tech/milestone-tasks.md) | 169 ordered tasks across 16 milestones (the Asset Forge first), each with an acceptance test |
| 31 | [Feature Inventory vs. Classic WoW](docs/09-reference/wow-feature-inventory.md) | Every capability of the model game: in, later, changed or cut |

### Part 8 — Art to produce before coding
| # | Document | What it covers |
|---|---|---|
| 32 | [Art Master To-Do](docs/10-art/00-art-master-todo.md) | Totals, permutation rules, technical targets, order of work |
| 33 | [Characters, Armor & Weapons](docs/10-art/01-characters-armor-weapons.md) | Bodies, customisation, animations, 23 armor sets, 145 weapons, mounts |
| 34 | [Creatures & NPCs](docs/10-art/02-creatures-npcs.md) | Every creature by rig, bosses, NPC outfits |
| 35 | [Environments & Props](docs/10-art/03-environments-props.md) | Building kits, nature, every zone, city and instance |
| 36 | [Spell, Particle & World Effects](docs/10-art/04-vfx.md) | Every ability, item, creature, boss and weather effect |
| 37 | [User Interface](docs/10-art/05-ui.md) | HUD, windows, screens, maps, crests |
| 38 | [Icons](docs/10-art/06-icons.md) | Every icon |
| 39 | [Named Item Index](docs/10-art/07-named-item-index.md) · [Quest Art Index](docs/10-art/08-quest-art-index.md) | 765 named items and 296 quests, one row each |
| 40 | [Audio](docs/10-art/09-audio.md) | Music, ambience, sound effects, voice |
| 40b | [Asset Manifest](docs/15-asset-manifest/00-manifest-index.md) and its level-band files | **Every asset, one row each (8,994)**: what it is, a description to generate it from, what it is for, its zone and first-seen level, **in order of first appearance**, which is the order the forge generates in. Also as `asset-manifest.csv` |
| 40a | [Art Direction](docs/10-art/10-art-direction.md) | What the game looks like (shapes, surfaces, the 32-colour palette, one shader) and the ten mechanisms that keep every generated asset in one style, including the repaint pass and measured style gates |

### Part 9 — Build data (what the code loads)
| # | Document | What it covers |
|---|---|---|
| 41 | [NPCs — index, vendor stock, trainer lists](docs/11-npcs/00-npc-index.md) and nine rosters | All 356 named NPCs: role, location, what they sell or teach, the quests they give and end, greeting line |
| 42 | [Data index and rules](docs/12-data/00-data-index.md) | The rules every generated number follows |
| 43 | [Creature Data](docs/12-data/creatures.md) | Stat block, ability numbers and loot table for 151 creature types and 76 named creatures |
| 44 | [Spell Data](docs/12-data/spells.md) | All 73 abilities as 152 rank rows |
| 45 | [Encounter Data](docs/12-data/encounters.md) | Trash packs by room, boss timers and damage, drop chances for dungeons, raid and world bosses |
| 46 | [Reference Tables](docs/12-data/reference-tables.md) | Flight routes and fares, reputation rewards, Valor prices, fishing tables, world drops, recipe sources |
| 46a | [Item Rules](docs/12-data/item-rules.md) | The rules that give every one of the 765 named items, and every random drop, its stats, armor, damage, vendor value, durability and repair cost |
| 46b | [Game Text](docs/12-data/game-text.md) | Every error and system message, tutorial and loading tips, emote text, tooltip wording, NPC stock phrases |
| 46e | [Presentation Rules](docs/12-data/presentation-rules.md) | Which model, skin, animation, effect, icon and sound each creature, NPC, ability and item uses; how music and ambience play |
| 46d | [Spoken Lines](docs/12-data/spoken-lines.md) | The voice script: NPC barks, story lines, announcers, lines for every boss, the Athenaeum books, street chatter |
| 46c | [Rules Reference](docs/02-systems/rules-reference.md) | Small rules not stated elsewhere: movement speeds, interaction ranges, timers, skill gains, food values, camera |
| 47 | [Class Quests](docs/06-quests/text/cq-class-quests.md) | The 10 class quests at levels 10, 20 and 30, in full |
| 48a | [World Construction](docs/13-world/10-world-construction.md) | How the layout tables become terrain, ground textures, scattered nature, buildings, spawn points, caves and dungeon interiors, by rule, with the checks each zone must pass |
| 48 | [World Layout](docs/13-world/00-world-layout.md) and nine layout files | Continent maps, and for every zone, capital and instance: grid map, sub-areas, hub buildings, quest locations, spawn camps with counts, nodes, graveyards, roads |
| 49 | [Asset Forge](docs/14-asset-pipeline/00-asset-forge.md) and its three pipeline files | The asset generation system on up to three machines, each with its own queue and a supervisor on the build machine, built first: service, manifest, quality gates, the owner's approval of the style and of each pipeline, and twenty-one pipelines for [images and textures](docs/14-asset-pipeline/01-image-pipelines.md), [3D models, hair, rigs and animation](docs/14-asset-pipeline/02-3d-pipelines.md), [audio and fonts](docs/14-asset-pipeline/03-audio-pipelines.md), and [placeholders and swapping](docs/14-asset-pipeline/04-placeholders-and-swap.md): how stand-in assets work and how finished ones replace them |

## 4. The game at a glance

### World
```
MERIDIA (human)                                     KHAZRUN (dwarf)
        Veilmoor 20-30                              Embercrag Hollow 5-10  (mountain dwarves, snow)
           |         \                                  |
 Thornwick Marches -- The Riftlands 20-30           HAMMERDEEP  (inside Mount Khaz, on the coast)
      10-20            (Kite's Rest, Dustpit, raid)    |              \
      /       \                                 Stoneheart Deeps -- Stonewake Dale
 Russetwood -- Harrowfield  5-10                 5-10 (interior)     1-5 (hill dwarves, spring; dwarf start)
      \       /                                         \              /
      SOLHAVEN  ~~~~ ship sails into the mountain ~~~>  Ironroot Highlands 10-20
          |                                             |
   Brightmead Vale 1-5                              Cinderfall Barrens 20-30

                         SUNDREL (30-60, not built)
```

### Classes
| Class | Resource | Tank | Healer | Damage |
|---|---|---|---|---|
| Fighter | Rage | Bulwark | — | Reaver (dual wield), Greatarms (two-hander) |
| Cleric | Mana | Aegis | Grace | Reckoning (two-hander, Holy) |
| Druid | Mana | — | Verdance (heal-over-time) | Stormcall (Nature, ranged), Starweave (Arcane, ranged) |

### Factions (the triangle)
**Concord of Dawn** (order; steel; humans and dwarves — playable) beats the **Ashen Covenant** (undeath; aether), which beats the **Wildpact** (the living wild; lifebloom), which beats the Concord. Each needs the resource its prey controls.

### Story
- **1–20, Embers of the Brand:** a branding cult behind arson, sabotage and grave-robbing leads to a hollow puppet-master in a tower.
- **15–30, The Hollow Crown:** five shards of an emperor's crown are being gathered; the heroes fail to stop it and follow it down into a city the earth swallowed.

### Endgame at 30
Hollowspire Keep and pre-raid crafting → raid attunement (the Vault Key) → **The Hollow Throne** (10 players, 6 bosses, Vaultforged tier sets) · three world bosses · Crownfall battleground and the Dustpit · reputation with the Athenaeum · guild banks.

## 5. Content totals

| Content | Count |
|---|---|
| Zones / capitals | 11 / 2 (+1 neutral town) |
| Zone quests | 296, all with full text (+ 10 class quests) |
| Named NPCs | 356, plus about 240 guards and other generic NPCs |
| Named items | 765 |
| Main-chain quests | 26 (Chain 1, any route) + 25 (Chain 2) |
| Creature types | 151 outdoor types and 76 named, rare and elite creatures, plus 25 instance trash types and 22 bosses |
| Class abilities | 27 Fighter · 27 Cleric · 19 Druid (before ranks) |
| Talents | 9 trees, 14–16 talents each, 138 in total |
| Professions | 3 gathering, 6 crafting, 3 secondary; ~220 recipes |
| Dungeons / raid / world bosses | 3 (13 bosses) / 1 (6 bosses) / 3 |
| PvP | Duels, 1 FFA arena, 1 three-team battleground |

## 6. Scope boundaries

**In the launch game (version 1.0):** everything linked above, including guilds and guild banks. This is a full game built for a live population of **5,000 concurrent players on one realm**, not a proof of concept (decided 2026-11-12).

**Designed for but not built:** allegiances 2 and 3 and their races; classes 4–6; levels 31–60 and their 11 zones; Sundrel; 20-player raids; epic mounts and mount feed (system built, dormant at cap 30); world PvP; add-ons; seasonal events; Artisan professions; plate armor.

**Not planned:** water zones, 40-player raids, flying, automatic dungeon finder, achievements, transmog, heroic difficulties, rated arenas, cash shop.

## 7. Status of the numbers

All statistics (damage, costs, stat budgets, loot values, gold-sink prices) are **balance v0**: internally consistent first-pass values meant for a simulator and playtests. The XP-per-level curve was checked against published classic-era figures on 2026-11-12 and matches at every checkpoint tested (see [Progression](docs/02-systems/progression.md)). The kill-XP and quest-XP rules are still reproduced from memory.

## 8. Decisions

Every decision is now settled. Items marked "by default" were accepted without a specific choice when you asked for planning to continue; any of them can still be changed, and the affected documents are listed.

### Decided
| Decision | Outcome | Affects |
|---|---|---|
| Engine and language | **Godot 4 + C# client, C# server** (2026-11-10) | [Architecture](docs/08-tech/architecture.md) |
| Riding level | **30**; epic riding at 60, which needs feed | [Economy](docs/02-systems/economy-and-social.md) |
| Raid sizes | **10 and 20**, never 40 | [Raid](docs/07-instances/raid-the-hollow-throne.md) |
| Group XP | **No split, no bonus**; 0 XP for the whole party if its level spread exceeds 5 | [Progression](docs/02-systems/progression.md#group-xp-rules) |
| Water zones | **None** | [World & Travel](docs/01-world/world-and-travel.md) |
| Replacement for the removed sea zone | **The Riftlands** (2026-11-10) | [The Riftlands](docs/05-zones/t4-riftlands.md) |
| Stonewake | **Stays Stonewake Dale**, the hill-dwarf farm valley (2026-11-12) | [Stonewake Dale](docs/05-zones/t1-stonewake-dale.md) |
| Dwarf starting zone | **Stonewake Dale, in spring**: the hill dwarves' farming valley, warm and welcoming, levels 1–5, with the valley farmed below and the mountainsides worked above (2026-11-25); **Embercrag Hollow moves to 5–10**, sister to Stoneheart Deeps. The owner: winter is a cold and harsh start, and "snowy areas can come later" | [Stonewake Dale](docs/05-zones/t1-stonewake-dale.md), [Embercrag Hollow](docs/05-zones/t2-embercrag-hollow.md), [Leveling Path](docs/05-zones/00-leveling-path.md) |
| Dwarf cultures | **One dwarf race, one starting zone, no culture choice for players.** Hallborn and Dalefolk exist only as NPC cultures (2026-11-12). Players are still one dwarf race; since 2026-11-25 they start among the hill dwarves, in Stonewake Dale, and are no more Dalefolk for it than they were Hallborn before | [Factions & Races](docs/01-world/factions-and-races.md#52-mountain-dwarves-and-hill-dwarves) |
| Level 30 to 40 zones | **Five**: 2 Meridia, 2 Khazrun, 1 Sundrel (2026-11-12) | [World & Travel](docs/01-world/world-and-travel.md#2-full-zone-plan-160) |
| XP in raid groups | **No kill XP in a raid group** (2026-11-12) | [Progression](docs/02-systems/progression.md#group-xp-rules) |
| Mount feed | **6g per 10 hours played**; unfed mounts drop to level-30 speed (2026-11-12) | [Economy](docs/02-systems/economy-and-social.md#4-the-level-60-gold-sink-plan) |
| Druid shapeshifting | **None.** Stag Form removed; the Druid is always in humanoid form (2026-11-12) | [Druid](docs/03-classes/druid.md) |
| Cleric conveniences | **Kept**: taunt, Dawnstrike, area threat from Hallowed Ground (2026-11-12) | [Cleric](docs/03-classes/cleric.md) |
| Weapon skills | **Kept** (2026-11-12) | [Combat](docs/02-systems/combat-and-stats.md) |
| Engineering at launch | **In**, by default; still the first thing to cut if scope must shrink | [Crafting](docs/04-professions/crafting.md) |
| Battleground mode | **King-of-the-hill with a carried Crown**, by default | [PvP](docs/02-systems/pvp.md) |
| Future races by faction | Gnome to the Concord; Elf and Ogre to the Wildpact; Undead to the Covenant, by default | [Factions & Races](docs/01-world/factions-and-races.md) |
| Server deployment | **Designed for a cluster; the same build runs complete on one server.** Machines are added by editing a topology file as players grow; the realm cap is a setting, at most 5,000 (2026-11-14) | [Architecture](docs/08-tech/architecture.md#one-server-to-a-cluster) |
| Who prepares the machines | **The builder.** Given SSH and `sudo`, it checks each machine and installs and downloads what is missing (2026-11-14) | [Asset Forge](docs/14-asset-pipeline/00-asset-forge.md#preparing-the-machines-is-the-builders-job) |
| Who tests and reviews during the build | **The builder itself** for the game's code, rules and content, with bots, a scripted client and screenshot checks; no such task waits for a person (2026-11-14). **Art is the exception: the owner approves it** (next row) | [Build Procedure](docs/08-tech/build-procedure.md) |
| Who approves the art | **The owner.** Approval is given pipeline by pipeline: nothing is generated in number until the owner has approved the style guidelines that govern that pipeline (the style bible for pictures and models, the icon style bible for icons, the audio style guide for music, sound and voice) and its first results. Music and voice wait as the rest do. Only the guidelines themselves and the calibration set are made unapproved; the game is built on placeholders meanwhile and the build does not wait (2026-11-23) | [Asset Forge](docs/14-asset-pipeline/00-asset-forge.md), [Build Procedure](docs/08-tech/build-procedure.md) |
| Build order of the two starting zones | **The dwarf starting zone is the priority of the build-out, and since 2026-11-25 that zone is Stonewake Dale.** The dwarf race and Stonewake Dale (T-M3-01, T-M3-02) are built ahead of the rest of M2, and Stonewake Dale is the zone finished first (final models, textures, animations, icons, interface) before the build returns to the remaining M2 work and the rest of M3 (2026-11-24; the zone changed 2026-11-25). Embercrag Hollow, which was built first under the earlier arrangement, is rebuilt as a level 5–10 zone with the other T2 zones | [Milestone Task Lists](docs/08-tech/milestone-tasks.md), [Roadmap](docs/08-tech/roadmap.md) |
| Most important art | **The player bodies (human and dwarf, man and woman) and their animations**: a player looks at them for the whole of every session. They are made first, then what the dwarf starting zone needs (2026-11-23) | [Art Master To-Do](docs/10-art/00-art-master-todo.md), [Characters, Armor & Weapons](docs/10-art/01-characters-armor-weapons.md) |
| How bodies and creatures are modelled | **Generated, then fitted to the rig.** A painted picture of the figure is turned into a 3D model by an image-to-3D model, and the model is fitted to the game's rig contract, keeping its own shape and texture. An NPC is one dressed body for its outfit (2026-11-23) | [3D Pipelines](docs/14-asset-pipeline/02-3d-pipelines.md), [Art Direction](docs/10-art/10-art-direction.md) |
| Character customisation | **Separate hair and faces on bald fitted bodies; skin and hair colour as tints.** The four player bodies are generated bald and clean-shaven; hair, facial hair and features are separate pieces that follow the head, faces are variants of the body's head, and every option goes with every other. The bald bodies and a first set of pieces are shown to the owner before the full set is made. Armor on these bodies is the next row (2026-11-24) | [Characters, Armor & Weapons](docs/10-art/01-characters-armor-weapons.md), [3D Pipelines](docs/14-asset-pipeline/02-3d-pipelines.md), [Placeholders and Swapping §2a](docs/14-asset-pipeline/04-placeholders-and-swap.md), [Presentation Rules](docs/12-data/presentation-rules.md) |
| Armor on player bodies | **Region textures on one shared texture layout.** All player bodies share one layout: each generated, rig-fitted body is re-wrapped onto the shared region layout of the constructed template bodies, keeping its own painted look. The layout has fixed rectangles for each body region (upper arm, lower arm, hand, upper torso, lower torso, upper leg, lower leg, foot; head and face for customisation). Armor is textures painted for those rectangles, layered over the skin texture in a fixed order, so one armor texture fits every race and both sexes. Geometry swaps built into the body mesh give the shapes a texture cannot make (flared sleeves, boot tops, robe skirt, glove cuffs, tabard, cloak) and may come after the textures. Helms, shoulders, weapons and shields are models attached to bones; a helm hides hair and, as needed, ears or beard; "hide helm" option. The textures are made by pipeline P06, and a first batch (the starting cloth set and one set each of leather and mail) is shown to the owner before the rest. Palette lock, repaint pass and triangle budgets on fitted bodies and creatures stay open (2026-11-24) | [Characters, Armor & Weapons §1, §4](docs/10-art/01-characters-armor-weapons.md#4-how-armor-is-built-the-permutation-rules), [Image Pipelines P06](docs/14-asset-pipeline/01-image-pipelines.md), [3D Pipelines P13](docs/14-asset-pipeline/02-3d-pipelines.md), [Placeholders and Swapping §2a](docs/14-asset-pipeline/04-placeholders-and-swap.md), [Presentation Rules](docs/12-data/presentation-rules.md), [Architecture](docs/08-tech/architecture.md) |
| Icon style | **Classic painted**: a small hand-painted picture that fills the square, washed in one colour for its kind, with a glowing light and dark corners; no frame in the picture (2026-11-23) | [Icons](docs/10-art/06-icons.md) |
| Interface look | **Dark stone panels with brass corners, a round brass minimap, an action bar with pointed end caps, and open round unit frames** (a portrait in a ring with two slim bars, no panel) (2026-11-23) | [User Interface](docs/10-art/05-ui.md), [UI Specification](docs/08-tech/ui-specification.md) |
| Bag window | **One unified bag window that grows as bags are added.** The backpack and every equipped bag are shown together in a single window, which grows when a bag is put in the bag bar and shrinks when one is taken out; items keep their own container and slot. It grows both vertically and horizontally and keeps a chosen shape: an option "Bag layout", Portrait (the default, taller than wide) or Landscape (wider than tall), with the columns worked out from the slot count and the orientation; it is anchored at its bottom-right corner above the bag bar and kept on screen. A "Show empty slots" option, on by default: when off, all empty slots combine into one empty slot with the number remaining (2026-11-24) | [UI Specification §3](docs/08-tech/ui-specification.md#3-windows), [UI & Controls](docs/02-systems/ui-and-controls.md) |
| XP bar | **10 equal sections ("bubbles"), set directly on the top edge of the main action bar.** Thin dividers are drawn over the fill; the bar is the action bar's width and touches it with no gap; its text is centred vertically and horizontally inside the fill and never overlaps the frame. The action bars, the bag bar, the micro-menu and the chat frame sit with their bottom edges on the bottom edge of the screen, with no gap (2026-11-24) | [UI Specification §2](docs/08-tech/ui-specification.md#2-hud-layout-default-positions), [UI & Controls §2](docs/02-systems/ui-and-controls.md), [User Interface](docs/10-art/05-ui.md) |
| Abilities at levels 1 and 2 | **Very few abilities at level 1: Attack, one special attack and, for a class that heals, one basic heal; at least one ability to buy from the class trainer at level 2.** Fighter: Strike (and Battle Stance to stand in), then Battle Cry at 2. Cleric: Oath of Radiance and Mending Light, then Litany of Resolve at 2. Druid: Thornlash and Mend, then Gift of the Grove at 2. The quest that sends a new character to its trainer is offered only from level 2, when that ability can be bought (2026-11-24) | [Progression §9](docs/02-systems/progression.md#9-ability-training), [Class Framework §4](docs/03-classes/class-framework.md#4-abilities), [Fighter](docs/03-classes/fighter.md), [Cleric](docs/03-classes/cleric.md), [Druid](docs/03-classes/druid.md), [Brightmead Vale](docs/05-zones/t1-brightmead-vale.md#quests), [Embercrag Hollow](docs/05-zones/t2-embercrag-hollow.md#quests) |
| Asset machines | Three: the EVO-X3 (always on), the RTX 5070 Ti desktop and the RTX 3060 laptop. **Each runs its own Forge service and queue**, so each keeps working when the others or the network are away; a supervisor on the build machine shares the work out by what each machine has measured it can make and how fast, and brings finished assets into the game (2026-11-23; replaces the one shared queue of 2026-11-14) | [Asset Forge](docs/14-asset-pipeline/00-asset-forge.md#1-the-machines) |
| Art style and sourcing | **Stylised low-poly, hand-painted look. All art and all audio (music, sound effects, voice) are AI-generated; no licensed or bought assets, no hired composers or voice actors** (2026-11-12) | [Art Master To-Do](docs/10-art/00-art-master-todo.md#8-how-the-art-is-made) |
| World name and working title | The world, meaning all three continents together (Meridia, Khazrun and Sundrel) and the seas between, is **Halcyra**. Working title for the project: **Halcyra**, by default, until you choose a product name | [Lore](docs/01-world/lore.md) |
| Target population | **5,000 concurrent players on one realm, in one shared world with no layers**: every player in a zone sees every other, as in 2004 (2026-11-12) | [Architecture](docs/08-tech/architecture.md#9-performance-targets) |

## 9. Document map

```
MASTER_PLAN.md                      <- you are here
docs/
  01-world/        lore · factions-and-races · world-and-travel
  02-systems/      progression · combat-and-stats · items-and-loot ·
                   economy-and-social · npc-ai-and-world · pvp · ui-and-controls · rules-reference
  03-classes/      class-framework · fighter · cleric · druid
  04-professions/  gathering · crafting · secondary
  05-zones/        00-leveling-path · t1-* (2) · t2-* (4) · t3-* (2) · t4-* (3)
  06-quests/       main-chain-1-embers-of-the-brand · main-chain-2-the-hollow-crown
    text/          00-quest-text-index · bm · ec · hf · rw · st · sd · tm · ir · cf · rl · vm (one file per zone)
  07-instances/    dungeons · raid-the-hollow-throne · world-bosses
  08-tech/         architecture · data-model · roadmap · repo-and-conventions · content-schemas ·
                   database-schema · network-protocol · ui-specification · milestone-tasks ·
                   terrain-and-cutouts · build-procedure · bots-and-testing ·
                   accounts-and-live-service
  09-reference/    wow-feature-inventory
  10-art/          00-art-master-todo · 01-characters-armor-weapons · 02-creatures-npcs ·
                   03-environments-props · 04-vfx · 05-ui · 06-icons ·
                   07-named-item-index · 08-quest-art-index · 09-audio · 10-art-direction
  11-npcs/         00-npc-index · 01–07 zone rosters · 08-solhaven · 09-hammerdeep
  12-data/         00-data-index · creatures · spells · encounters · reference-tables ·
                   item-rules · game-text · spoken-lines · presentation-rules
  13-world/        00-world-layout · 01–08 zone layouts · 09-capitals-and-instances ·
                   10-world-construction
  14-asset-pipeline/  00-asset-forge, 01-image-pipelines, 02-3d-pipelines, 03-audio-pipelines, 04-placeholders-and-swap
  15-asset-manifest/  00-manifest-index · 14 level-band files · asset-manifest.csv (generated)
tools/doc-generators/   scripts that rebuild the generated documents and run the checks
```

## 10. Change log

### 0.17 - 2026-11-25
- **The dwarf starting zone is Stonewake Dale; Embercrag Hollow moves to levels 5–10 (the owner).** The owner did not want dwarves to begin in the snow: winter is a cold and harsh start, and a start should feel warm and welcoming. Shown the choices, he chose to swap the two zones. **Stonewake Dale** is now the dwarf starting zone, levels 1–5, in spring: the hill dwarves farm the valley (barley terraces, hop-yards, lambing pastures, turf-roofed longhouses, dry-stone walls) and work the mountainsides above it (quarry, sawpit and timber, herb banks, a copper adit). It is written on the starting-zone template it shares with Brightmead Vale: 18 quests with the same levels, XP and coin quest for quest (ST-01 to ST-18), the opening quest at the start point, "A Summons from Your Trainer" from level 2 with its free first rank, a level-5 mini-boss (Chief Gnarr, in the Deep Sink) and a level-5 elite (Old Bitterhorn), creatures of level 1 to 3 not aggressive, about 200–280 kills and leaving at about level 7. It starts at a new farmstead, Sunbank Steading, and keeps Hopstead, Ridgefold, the High Pastures, the Hop-Yards, the Sinks, the Old Brewery, the Millrace and its people; three NPCs are new (the Steadwife, a quarrier, a sawyer). The Stonewake Dam and its mountain-dwarf engineers stay as the zone's background and tension, and nothing is fought on the dam. **Embercrag Hollow** is now a level 5–10 zone on the template of the other three (EC-01 to EC-20, the same levels and XP quest for quest), with its snow, Coldhearth, Anvilrest, the Warrens, the Old Forge and Kiln Cave kept. The heavy dam content moved there with the Slagborn: the sappers, the powderkegs, Slagfall Gully, Blackmatch Camp, Powderkeg Pol and Sapper-Chief Dolga Blackmatch (level 10) are in Embercrag, where the cinder-charges meant for the dam are found and stopped at their source; Grolm Sootbeard and the Ever-Ember are its middle step (EC-07). The decision about the Slagborn Firebrand stands and was checked for the new levels. Players are still one dwarf race with no culture choice; they now start among the hill dwarves ([Stonewake Dale](docs/05-zones/t1-stonewake-dale.md), [Embercrag Hollow](docs/05-zones/t2-embercrag-hollow.md), [Leveling Path](docs/05-zones/00-leveling-path.md), [Embers of the Brand](docs/06-quests/main-chain-1-embers-of-the-brand.md), [quest text](docs/06-quests/text/00-quest-text-index.md), [NPC roster](docs/11-npcs/02-embercrag-stonewake-stoneheart.md), [world layouts](docs/13-world/00-world-layout.md), [Factions & Races §5](docs/01-world/factions-and-races.md), [World & Travel](docs/01-world/world-and-travel.md)).
- **What follows from it.** The two zone files are renamed for their tiers (`t1-stonewake-dale.md`, `t2-embercrag-hollow.md`) and every link follows. The build order's "dwarf starting zone first" now means Stonewake Dale: T-M3-01 and T-M3-02 build the dwarf race and Stonewake Dale, and Embercrag Hollow takes Stonewake's place among the level 5–10 zone tasks of M6 ([Milestone Task Lists](docs/08-tech/milestone-tasks.md), [Roadmap](docs/08-tech/roadmap.md), [Build Prompt](BUILD_PROMPT.md)). The Khazrun trainers swap ranks (Apprentice in Hopstead, Journeyman in Anvilrest), as do the fishing skills of the two zones' waters, the herbs and veins they hold, and their two quest recipes (Dale Pasty is now the skill 1 recipe, Seared Ram Chop the skill 25 one) ([Gathering](docs/04-professions/gathering.md), [Secondary Professions](docs/04-professions/secondary.md), [Reference Tables](docs/12-data/reference-tables.md)). The art lists keep their row ids; the zone rows Z-ST and Z-EC, the creature skins and the character-select backdrop are reworded where the swap made them wrong, and the dwarf starting zone's art that is made first is now Stonewake Dale's ([Art Master To-Do](docs/10-art/00-art-master-todo.md)). The generated documents (creature data, named item index, quest art index, the roster's quest columns, the Asset Manifest) are regenerated; the generators' own lists of zones were brought into line. The Asset Manifest has 8,994 rows in place of 8,978 (27 ids gone, 43 new: the two zones' quest icons and scenes, their set pieces and quest objects, six fog masks, the wolf cub's skin for the young bear's, the character-select backdrop), and 840 rows change zone or first-seen level, since Stonewake Dale's assets are now the ones a dwarf meets first; the level 1–2 band is three files, so there are 14 band files and the later ones are renumbered.
- **Not brought into line, because it is the build and not the specification:** the game's content, tools and tests still hold Embercrag Hollow as the built dwarf start (the zone importer names `t1-embercrag-hollow.md`; the dwarf race record starts at Coldhearth). They follow when T-M3-02 is done again for Stonewake Dale.
- **Open, for the owner:** whether Embercrag is enlarged from 1,000 m to the 1,400 m of the other level 5–10 zones when it is rebuilt; whether the south road from Stonewake Dale straight into Ironroot Highlands (10–20) is marked or guarded for new players; and Stonewake Dale has no measured bot run yet.

### 0.16 - 2026-11-24
- **Character customisation: separate hair and faces.** The four player bodies are generated bald and clean-shaven, in plain underclothes. Hair styles, facial hair and features are separate pieces attached to the head bone or skinned to the head and neck bones; faces are variants of the body's head; skin tones are tints of the body texture's skin region and hair colours are tint ramps on the hair pieces. The counts of the art list stand, and the bald bodies and a first set of pieces are shown to the owner before the full set is made. Armor on these bodies is the entry below ([Characters §1, §2](docs/10-art/01-characters-armor-weapons.md); [3D Pipelines](docs/14-asset-pipeline/02-3d-pipelines.md) P13, P21; [Placeholders and Swapping §2a](docs/14-asset-pipeline/04-placeholders-and-swap.md); [Presentation Rules §2a](docs/12-data/presentation-rules.md); [UI Specification §3](docs/08-tech/ui-specification.md)).
- **Armor on player bodies: region textures on one shared layout.** All player bodies share one texture layout: each generated, rig-fitted body (human man and woman, dwarf man and woman) is re-wrapped onto the shared region layout of the constructed template bodies, with its own texture baked into it, so it keeps its painted look. The layout is fixed rectangles for the upper arm, lower arm, hand, upper torso, lower torso, upper leg, lower leg and foot (and the head and face for customisation). Armor is region textures painted for those rectangles (a chest piece the torso and the arm regions it covers, gloves the hands and a lower-arm cuff, boots the feet and lower legs, trousers the upper and lower legs, a belt a band at the waist, bracers the lower arm), layered over the skin texture in a fixed order (shirt, chest, tabard over chest, and so on), so one armor texture fits every race and both sexes, with separate versions for men and women only where a piece needs them. Geometry swaps built into the body mesh (flared sleeves, boot tops, robe skirt, glove cuffs, tabard, cloak) are shown when an item calls for them and may come after the textures. Helms, shoulders, weapons and shields are models attached to bones; a helm hides hair and, as its race and the helm need, ears or beard; there is a "hide helm" option. Pipeline P06 makes the region textures, and a first batch (the starting cloth set and one set each of leather and mail) is shown to the owner before the rest. The open points about the armor system on fitted bodies are closed; whether the palette lock, the repaint pass and the triangle budgets apply to fitted bodies and creatures stays open. Until the re-wrapped bodies and P06's textures exist the client draws armor by an interim method, recorded in Placeholders and Swapping §2a ([Characters §1, §4](docs/10-art/01-characters-armor-weapons.md); [Image Pipelines](docs/14-asset-pipeline/01-image-pipelines.md) P06; [3D Pipelines](docs/14-asset-pipeline/02-3d-pipelines.md) P13, P21; [Placeholders and Swapping §2a, §3.1](docs/14-asset-pipeline/04-placeholders-and-swap.md); [Presentation Rules §2a, §4](docs/12-data/presentation-rules.md); [Architecture §6](docs/08-tech/architecture.md)).
- **XP bar of 10 sections, and the bars on the bottom edge.** The XP bar is divided into 10 equal sections ("bubbles"), in place of 20, by thin dividers drawn over the fill. It sits directly on the top edge of the main action bar, the same width, touching it with no gap, and its text is centred vertically and horizontally inside the fill and never overlaps the frame. The action bars, the bag bar, the micro-menu and the chat frame sit with their bottom edges on the bottom edge of the screen, with no gap. The art list's UI-H12 row still reads "20 segments", because the asset manifest's ids are generated from it ([UI Specification §2](docs/08-tech/ui-specification.md); [UI & Controls §2](docs/02-systems/ui-and-controls.md); [User Interface, The look](docs/10-art/05-ui.md)).
- **The asset list now has robe skirts and capes as parts of each body.** Robe skirts and cloaks are geometry swaps built into each of the four player body meshes, not separate models: each body carries lower-body variants (plain legs, short kilt, long robe skirt to the ankles, which hides the legs) and cape shapes (short, long, wide), with flared sleeves, glove cuffs and boot tops, all skinned to the body's rig: 9 parts for each body, 36 in all (GEO-01 to GEO-05). A robe is painted by its set's region textures, whose lower-torso and leg regions carry onto the skirt; a cape shows the cloak item's own texture. The art list no longer counts a robe skirt model for each set and body or a cloak mesh for each rig, and counts 8 unique cloak textures, as the Named Item Index does, not 5. The Asset Manifest is regenerated: 8,978 rows in place of 8,984 (the 40 robe-skirt rows and 2 cloak-mesh rows are gone, 36 geometry swap rows are added with the bodies), and its descriptions of the bodies, hair pieces, skin tones, underclothes and the XP bar now follow this version's decisions; the XP bar row keeps its id, `UI-H12-20-segments`, and is named for 10 sections. Open: a tabard part, which sets show the kilt, and which cloak takes which cape shape ([Characters §4, §5, §6, §11](docs/10-art/01-characters-armor-weapons.md); [Art Master To-Do §2](docs/10-art/00-art-master-todo.md); [Asset Manifest](docs/15-asset-manifest/00-manifest-index.md)).
- **Interface settings.** The Interface tab of the Options window holds at least Auto loot (on by default: opening a corpse opens the loot window, takes the money, then each item in turn 0.2 s apart, and closes it; a Shift-click on a corpse does the opposite of the setting: with auto loot on it opens the loot window and takes nothing, with it off it loots in that way), Show empty slots (on by default) and Bag layout (Portrait or Landscape; Portrait by default). Settings are saved for the player and survive restarting the client. Every action has a primary and a secondary key, rebindable in the Key Bindings window from the game menu. The frame-rate, latency and position read-out is hidden by default: it is shown in the tooltip of the micro-menu's system button, and on screen while switched on with its key, Ctrl+R ([UI Specification §2, §3, §4, §7](docs/08-tech/ui-specification.md); [UI & Controls §1, §2, §6](docs/02-systems/ui-and-controls.md)).
- **One bag window.** The backpack and every equipped bag are shown in a single window in place of a window per bag; it grows as bags are put in the bag bar and shrinks as they are taken out, and the backpack key, the all-bags key and every bag-bar button open it. Items keep their own container and slot, so the containers, their numbering and the database are unchanged. A "Show empty slots" option (a tick box in the window and in Options, Interface; on by default; saved with the player's settings) combines, when off, all empty slots into one empty slot with the number remaining; an item put on it goes into the first free slot. The window grows both vertically and horizontally and keeps a chosen shape, set by the option Bag layout: Portrait (the default, taller than wide) or Landscape (wider than tall), the columns worked out from the slot count and the orientation; it is anchored at its bottom-right corner above the bag bar and kept on screen ([UI Specification §2, §3, §4](docs/08-tech/ui-specification.md); [UI & Controls §2, §3, §6](docs/02-systems/ui-and-controls.md)).
- **Tutorial tips in the middle of the screen.** The tip panel (the one with "Don't show tips" and "Got it") is drawn centred horizontally, with its top edge just below the vertical centre of the screen, in place of the lower right above the bag bar; there it does not cover the character and is clear of the bag window and the bars at the bottom. Tooltips are unchanged and stay at the bottom right ([UI Specification §7](docs/08-tech/ui-specification.md#7-first-session-tutorial-tips)).
- **Few abilities at level 1, the first trainer rank at level 2.** A new character knows Attack, one special attack and, if its class heals, one basic heal, each at rank 1: Strike for the Fighter (who stands in Battle Stance), Oath of Radiance and Mending Light for the Cleric, Thornlash and Mend for the Druid. Battle Cry, Litany of Resolve and Gift of the Grove are no longer known from the start: their first rank is bought from the class trainer at level 2, at the level-2 price of the training cost curve (10c), and their later ranks keep their levels, so the values of their middle ranks in the generated spell data move slightly. Everything from level 4 up is unchanged. "A Summons from Your Trainer" (BM-03, EC-03) is a level-2 quest offered only from level 2, and its free first rank is now that level-2 rank. The open point about a level-2 rank and the cost curve is closed ([Progression §9](docs/02-systems/progression.md#9-ability-training); [Class Framework §4](docs/03-classes/class-framework.md#4-abilities); [Fighter](docs/03-classes/fighter.md), [Cleric](docs/03-classes/cleric.md), [Druid](docs/03-classes/druid.md); [Spell Data](docs/12-data/spells.md); [Brightmead Vale](docs/05-zones/t1-brightmead-vale.md#quests), [Embercrag Hollow](docs/05-zones/t2-embercrag-hollow.md#quests); [Quest Text Index](docs/06-quests/text/00-quest-text-index.md); [Milestone Task Lists](docs/08-tech/milestone-tasks.md) T-M2-07).
- **A Sex column in the NPC rosters (the owner, 2026-11-25).** Every roster table of [docs/11-npcs](docs/11-npcs/00-npc-index.md) has a last column, Sex: `M` or `F` for each NPC, and `M/F` for a group row ("×N"), whose copies alternate, the first a man. An NPC's body is set by it, in place of the pronoun-or-alternate rule ([Presentation Rules §2](docs/12-data/presentation-rules.md#2-npcs-and-humanoid-enemies-on-player-rigs)). Each value was taken from the pronouns the documents use for the NPC, then the given name, then the title. The zone importer does not read the column yet, so the generated NPC records of the two starting zones keep their earlier bodies until it does and the zones are imported again.

### 0.15 - 2026-11-24
The specification brought into line with a build made from it: what the build decided where the documents were silent, what the owner changed on seeing it, and what was found wrong. Points the owner has not yet decided are marked in place with a sentence beginning "Open:".
- **Build order: the dwarf starting zone first.** Embercrag Hollow (T-M3-01, T-M3-02) is built ahead of the rest of M2 and brought to a finished state before the build returns to the remaining M2 work and the rest of M3; the player bodies and their animations are the first art ([Milestone Task Lists](docs/08-tech/milestone-tasks.md), [Roadmap](docs/08-tech/roadmap.md), [Build Prompt](BUILD_PROMPT.md)).
- **The owner approves the art.** Approval is pipeline by pipeline: nothing is generated in number until the owner has approved the style guidelines that govern a pipeline (the style bible, the icon style bible, or the audio style guide for music, sound and voice) and its first results; the build goes on with placeholders meanwhile ([Asset Forge §7a](docs/14-asset-pipeline/00-asset-forge.md), [Build Procedure](docs/08-tech/build-procedure.md)). This replaces "no person reviews assets".
- **Asset machines: a queue each, and a supervisor.** Each machine runs its own Forge service and queue; a supervisor on the build machine shares work out by measured ability and speed, hands over what waited and delivers finished assets. Machines are named by SSH alias; files move through the service, not `rsync` ([Asset Forge §1, §4, §4a](docs/14-asset-pipeline/00-asset-forge.md)).
- **Bodies, creatures and props are generated models that keep their shape.** A painted picture is turned into a model by an image-to-3D model and the model is fitted to its rig contract (or its size box); it is not wrapped onto a template and its colour is not repainted. An NPC is one dressed body per outfit and body. 67 rig contracts, not 64 ([3D Pipelines](docs/14-asset-pipeline/02-3d-pipelines.md) P10, P12, P13, P14; [Placeholders and Swapping §2a](docs/14-asset-pipeline/04-placeholders-and-swap.md); [Art Direction §6, §8](docs/10-art/10-art-direction.md); [Characters](docs/10-art/01-characters-armor-weapons.md); [Creatures & NPCs](docs/10-art/02-creatures-npcs.md); [Presentation Rules](docs/12-data/presentation-rules.md)).
- **Icon style chosen**: classic painted, one hue per kind, full-bleed, a glowing light, dark corners, no frame and no palette lock; drawn at 512, kept at 128, shown at 64 ([Icons](docs/10-art/06-icons.md), [Image Pipelines](docs/14-asset-pipeline/01-image-pipelines.md) P02).
- **Interface look chosen**: dark stone panels with brass corners, a round brass minimap, an action bar with pointed end caps, open round unit frames; sizes as built ([User Interface](docs/10-art/05-ui.md), [UI Specification §1, §2](docs/08-tech/ui-specification.md)).
- **One walk grid for collision and navigation**, shared by server and client, in place of per-chunk collision and a navigation mesh; skirts between terrain detail levels; hand-placed and generated cutout files; the zone editor writes fixes that a rebuild replays ([Terrain and Cutouts](docs/08-tech/terrain-and-cutouts.md), [Architecture](docs/08-tech/architecture.md), [World Construction](docs/13-world/10-world-construction.md)).
- **World construction: the layout format's optional entries** (zone style, edge heights, frozen pond, ridge spine, cave mouth, heading and extent, camp placement), galleries sized to their population, indoor spacing, and the step order ([World Construction](docs/13-world/10-world-construction.md)).
- **Embercrag Hollow's layout corrected to what can be played**: Kiln Cave's shape, length and heading, where the Slagborn stand, the standing stone, the Cart Road, the larder pit, edge heights; the Brightmead mill ([Brightmead and Embercrag layout](docs/13-world/01-brightmead-embercrag.md)).
- **Content schemas**: every field, effect, aura, requirement and constants section the build added; the import commands; validation rules V09, V19, V26, V28 to V31 as checked ([Content Schemas](docs/08-tech/content-schemas.md)).
- **Protocol**: messages added for items, vendors, trainers, quests, experience, inns and the hearthstone; the initial-state batch; movement checks as built ([Network Protocol](docs/08-tech/network-protocol.md)).
- **Rules made exact**: attribute growth, miss, glancing and crushing blows, block, regeneration ([Combat](docs/02-systems/combat-and-stats.md)); who answers a call for help, flee speed, the evade limit, indoor notice range, thrown attacks, respawn from death, night hours ([NPC AI](docs/02-systems/npc-ai-and-world.md)); trainer rules, with the first rank at level 4 ([Progression §9](docs/02-systems/progression.md)); sitting, the hearthstone, cooldowns through logout ([Rules Reference](docs/02-systems/rules-reference.md)); ability kinds ([Data Index §2](docs/12-data/00-data-index.md)); item ids, rounding, quality by source, starting gear, vendor prices, world drops ([Item Rules](docs/12-data/item-rules.md)); class notes for threat, stances, Oaths and Rootgrasp.
- **Quest rules**: kill credit within 100 yards; quest objects per player; an object can wait on an earlier objective; "Speak to" the ender makes no objective ([Quest Text Index](docs/06-quests/text/00-quest-text-index.md)).
- **The questing bot** as built: when it retreats and rests, selling, repairing, line of sight, elite quests with a second bot ([Bots and Testing §3](docs/08-tech/bots-and-testing.md)). **T-M2-16** holds quest XP to the zone document and records the total.
- **Creature generator fixed**: `creatures.ps1` typed Grolm Sootbeard and Kilnmaster Bertram Soot as beasts because "bear" and "ram" matched inside their names; both are Humanoid.
- **Still open, for the owner**: the Slagborn Firebrand's damage; the starting zones' kill estimate against the measured runs (about 210 to 280 kills, level 7); whether the palette lock, repaint pass and shared-layout armor apply to fitted bodies; whether dressed bodies are the lasting NPC method; the style bible's approval; whether the interface keeps its code-drawn look or takes texture art; step height and slope on the walk grid; generated nature beyond the starting zones; the helper machine's role; assets in Git LFS or outside git; exact health or a fraction to other players; the unused quest dialog messages; a level-2 trainer rank.
- Not yet brought into line: the generated Asset Manifest (its descriptions for icons, bodies, outfits and skins still carry the earlier wording, and it has no rows for dressed bodies), the interface and icon rows of the art lists that the manifest is expanded from, and the documents for classes beyond the notes above, professions, instances and the zones after the two starting zones.

### 0.14 - 2026-11-17
- **Asset Manifest** (`docs/15-asset-manifest/`): every asset as its own row, 8,984 in all, each with a description to generate from, what it is for, its zone and the level at which a player first meets it. Grouped rows in the art lists ("×7 schools", "40 pieces") are expanded and named. The rows are **in order of first appearance**: login and character creation, then the starting zones, then outward by level to the raid.
- **The forge generates in that order**, replacing the art-block order, so the placeholders a new player sees first are replaced first. Each asset machine takes the next row its pipelines can make. The builder loads the manifest and no longer derives it from the art lists.
- Generated by `tools/doc-generators/asset_manifest.py` (Python); regenerate after any change to the art lists or data.
- **Protocol: `ExploredAreas` message added** (Network Protocol §5): on entering the world the server sends every sub-area the character has already found, so the map's fog is right at login. The specification had the single-area message only; the gap was found during a build.
- **Named Item Index corrected: 765 items, not 773.** The index generator took an item's slot from words in its name before its stated slot, so 18 rows were mis-filed (a "Hall-Cloak" as a mace, "Chain Gauntlets" as an off-hand); it now reads the stated slot first. Eight rows were not equipment at all (five recipes, a weapon oil, a boss ability and an inn's name) and are gone; seven rows named after the creature that drops the item now carry the item's own name. Item ids were renumbered.

### 0.13 - 2026-11-14
- **Art direction written** (docs/10-art/10-art-direction.md): the look in measurable terms, and how consistency is enforced. Every texture goes through one repaint pass (generator lighting removed, colours snapped to the 32-colour palette, light repainted from the mesh), every mesh through one shape pass, and style is checked by measurement.
- **Second asset machine.** The main desktop's RTX 5070 Ti (16 GB, CUDA) is Forge B and runs 3D generation, hair, rigging and animation; the EVO-X3 is Forge A and runs images, audio and the checking models. Either can be absent. New environment variables `FORGE_GPU_HOST`, `FORGE_GPU_SSH_USER`, `FORGE_GPU_SSH_KEY`.
- **One server to a cluster.** The game is designed for a cluster and the same build runs complete on a single server; growing is an edit to `deploy/topology.yaml`. The realm cap is the setting `realm.maxPlayers` (design maximum 5,000), set from measured capacity.
- **The builder prepares the machines.** Given SSH and `sudo`, it audits each machine, reuses software and models already there, and installs and downloads what is missing.
- **Build Procedure** (docs/08-tech/build-procedure.md): the progress ledger, resuming after lost context, failure and deferral rules, precedence between documents, the scripted client and automation port by which the builder sees the game, and substitutes for every test written for human testers. No task waits for a person.
- **World Construction** (docs/13-world/10-world-construction.md): rules that turn the layout tables into terrain, textures, scatter, buildings, spawn points and interiors, with checks (V27).
- **Item Rules** (docs/12-data/item-rules.md): every item's numbers follow from stated rules (V28). The stat budget gains a 0.40 scale so the formula agrees with the items stated in full.
- **Game Text** (docs/12-data/game-text.md), **Rules Reference** (docs/02-systems/rules-reference.md) and **Accounts and Live Service** (docs/08-tech/accounts-and-live-service.md) fill the remaining gaps in text, small rules and the service around the game. **Spoken Lines** (docs/12-data/spoken-lines.md) is the voice script the audio pipeline reads, with lines for every boss, twelve books and street chatter. **Bots and Testing** (docs/08-tech/bots-and-testing.md) defines the automated players the build is tested with. **Presentation Rules** (docs/12-data/presentation-rules.md) joins content to assets: which model, animation, effect, icon and sound each thing uses. The database, protocol, interface and repository layout gain what these need (reports, tickets, penalties, telemetry, launcher, `build/`, `deploy/`, `tests/plays/`). Validation rules now number 31.
- **Correction:** the task lists hold 169 tasks, not 176 as versions 0.11 and 0.12 stated. No task was removed; the earlier count was wrong. Tasks now link to the documents above wherever they depend on them.
- **Stale wording removed:** human approval of art, tests that needed testers or a beta, a fixed count of server machines, and "phasing" are replaced by what the builder itself does.
- **Optional helper machine.** The laptop (RTX 3060 Laptop GPU, 6 GB; 32 GB memory) is Forge C. It takes Blender processing, the repaint pass, checks and voice, and never runs a model that decides how an asset looks. Reached by `FORGE_AUX_HOST`, `FORGE_AUX_SSH_USER`, `FORGE_AUX_SSH_KEY`.
- **New pipeline P21: hair, beards, manes and tails**, as hair cards with spring bones (HairDeck is the first candidate). Twenty-one pipelines in all. New candidates added for images (P-H3-Image, P-JiT, NitroFusion 2 for few-step generation), matched prop sets (CoLa3D) and animation from video (FlowHMR). All are confirmed or replaced at bring-up.
- **Terrain cutouts** (docs/08-tech/terrain-and-cutouts.md): the terrain carries a hole mask, so the ground can be cut open for caves and dungeon entrances at any time. Cutouts are data records with a zone-editor tool and validation rule V26.

### 0.12 - 2026-11-12
- **Placeholders and swapping specified** (docs/14-asset-pipeline/04-placeholders-and-swap.md). Every asset has a contract written first; a placeholder and a generated asset both satisfy it. Each of the 64 rigs has its own skeleton as data and its own block-out placeholder, so there is no shared placeholder. Finished assets pass a contract check on the build machine and are renamed over their placeholders; the client loads by asset id through one service and swaps visuals in place while running. The server never loads visual assets.

### 0.11 - 2026-11-12
- **Asset Forge specified** (`docs/14-asset-pipeline/`): a dedicated GMKtec EVO-X3 generates every asset. One service with a job queue, a machine-readable asset manifest built from the art lists, placeholders for everything from the start, automatic quality gates in place of human review, a style bible that holds one look, and **twenty pipelines, one per kind of asset** (style bible, icons, UI, paintings, tiling textures, armor textures, skins, effects, skies; props and weapons, building kits, nature, characters and creatures, rigs, animation; music, ambience, sound effects, voice; fonts). Each names models to try and a fallback that needs no model.
- **New first milestone MA** (12 tasks) builds the forge before any game code; the build prompt now says so and names how the builder reaches the asset machine. 176 tasks across 16 milestones.
- Art and audio pages now defer to the forge and no longer call for a person to review assets. Fonts are constructed by the forge, not licensed.

### 0.10 - 2026-11-12
- **No layers.** Every zone exists once per realm and every player in it can see every other, as in 2004. The layers section is replaced by "One world, no layers": each zone host holds 1,500 players (capitals 2,000), crowds lower distant update rates but never hide anyone, dynamic respawn falls to 15%, quest objects are per-player, and a login queue caps the realm at 5,000.
- **The hand-over is one prompt plus these documents.** `BENCHMARK.md` (builder rules, status files, four-part scoring) is removed and replaced by [BUILD_PROMPT.md](BUILD_PROMPT.md), which holds only the prompt. There is no scoring, evaluation or pausing: the build is judged by playing it.

### 0.9 — 2026-11-12
- **Purpose stated:** the repository is a build specification to hand to an AI model with one prompt. (A benchmark brief with builder rules and scoring was added in this version and removed in 0.10.)
- **Audio is AI-generated**, like the art: music, sound effects and every voice line, with synthetic voices only.

### 0.8 — 2026-11-12
- **Not a proof of concept.** The plan now describes a full game, version 1.0, for **5,000 concurrent players on one realm**. Added: zone **layers** (identical copies of a zone, about 200 players each), a login queue, milestone **M13 Scale-out to 5,000** (process split, Redis bus, layers, staged load tests to 5,000 bots) and milestone **M14 Launch readiness** (account services, patcher, betas, runbook). 164 tasks across 15 milestones.
- **All art is AI-generated; no licensed or bought packs.** The art master page gains the generation pipeline, review gates, rules and record-keeping. Asset counts are unchanged. **Audio is AI-generated as well**: music, sound effects and every voice line, with synthetic voices only and no imitation of real people or existing music; the audio list gains its own pipeline and rules. Fonts still need an open licence.
- The world's name is confirmed as **Halcyra**: the three continents and the seas between them.

### 0.7 — 2026-11-12
- **All decisions settled** (§8). Changed by decision: dwarf cultures are NPC-only, with no culture choice for players; Druids never shapeshift (Stag Form and its class quest removed: 73 abilities, 10 class quests); raid groups give no kill XP. Confirmed: Stonewake Dale, five level 30–40 zones, mount feed price, Cleric conveniences, weapon skills. The rest accepted by default.
- **XP curve verified** against published classic-era figures at three checkpoints, including the exact 1–60 total.
- **Zone quest tables synchronised** with the quest text: every Reward cell is now copied from the quest text by script, and every zone page links to its quest text, NPC roster, layout and creature data.
- **Income targets corrected** in the economy document from the written quest rewards; the old targets could not pay for training and riding.
- Four recipes introduced by quest and reputation rewards added to the crafting document. Stale references removed (a bandage quest that never existed, old creature and talent counts, a leftover sea-zone drink name).
- Named item index: 773 items. All generated documents rebuilt; all links, spawn counts and quest XP cross-checks pass.

### 0.6 — 2026-11-12
- **World layout** added (`docs/13-world/`): continent maps with zone positions and crossings; for each of the 11 zones a grid map, sub-areas with positions and elevations, hub building positions, quest locations, 157 spawn camps (3,021 spawn points), node positions, graveyards and roads; district layouts for both capitals; room lists for the three dungeons, the raid, the Dustpit and Crownfall.
- Khazrun is fixed as lying **east** of Meridia across the Hearth Strait; Solhaven's only land gate is its north gate.
- A spawn-count check script confirms every zone creature has a camp and every kill objective has at least twice its count available.

### 0.5 — 2026-11-11
- **Technical specifications** added in `docs/08-tech/`: repository layout and conventions, content schemas, database schema, network protocol, UI specification, and per-milestone task lists with acceptance tests.
- **Technical choices fixed:** LiteNetLib for transport; hand-written message encoding; Npgsql and Dapper with plain SQL migrations; no Redis until the server is split into more than one process; xUnit.
- Generator scripts saved in `tools/doc-generators/`.

### 0.4 — 2026-11-11
- **NPC rosters** added (`docs/11-npcs/`): 356 named NPCs with vendor stock lists, trainer lists and capital city directories. The quests each NPC gives and ends are filled in by script from the quest text.
- **Build data** added (`docs/12-data/`): creature stat blocks, ability numbers and loot tables; every ability rank; encounter numbers and drop chances; flight routes, reputation rewards, Valor prices, fishing tables, world drops and recipe sources.
- **Class quests** written in full (11 quests).
- **Armor colourways** re-estimated by zone: about 550 region textures; level 1–10 sets gained shoulder and head pieces.
- **Changed rules, to resolve contradictions found while writing the data:** dungeon boss health is now set by fight length, not "×12–18 normal health"; quest coin follows the quest text table, not `level² × 1.1`; quest reputation is 25% of XP with the zone's reputation; non-native mounts need Exalted.
- Named item index regenerated: 765 items.

### 0.3 — 2026-11-11
- **Quest text written for all 296 quests** in `docs/06-quests/text/`, one file per zone: offer, tracker, progress and completion text, prerequisites, turn-in NPC, coin, named and statted reward items, quest-item drop sources and rates, and scripting notes for escorts, defend events and world-state changes. These files are now the authority for quest rewards and prerequisites; the zone tables remain the summary.
- 500 named, statted reward items now cover every quest, replacing the "green shoulders"-style placeholders. The [Named Item Index](docs/10-art/07-named-item-index.md) was regenerated: 708 named items (180 unique art, 528 tier art), and the icon total rose to about 2,050.

### 0.2 — 2026-11-10
- **Zone plan to 60** added: 5 zones for 30–40, 4 for 40–50, 2 for 50–60; planned zones fill only half of each continent.
- **Sea zone removed.** The Drowned Reach is replaced by the Riftlands, a land zone; the raid is now *The Hollow Throne*, the arena *the Dustpit*, the neutral town *Kite's Rest*, the third world boss *Gorrath*.
- **Two new 5–10 zones**, each a complete 5→10 with its own main-chain act: *Russetwood* (autumn forest beside Harrowfield) and *Stoneheart Deeps* (entirely inside the mountain, beside Stonewake).
- **Mountain and hill dwarves**: two cultures mapped onto Khazrun's zones; Stonewake re-themed as the hill-dwarf valley *Stonewake Dale*.
- **Capital ship** now sails from Solhaven Harbor into the mountain at Hammerdeep's ground-level Seagate, beside the Rootvault, whose gardens its water irrigates. It is the only ship route.
- **Random suffixes** renamed to an original convention (callings such as *of the Sentinel*; no animals).
- **Economy:** level-60 gold sink plan; epic-mount feed; respec capped at 5g with weekly decay to 1g; mail 1s.
- **Guilds and guild bank** fully specified and moved into launch scope.
- **Raids** are 10 and 20 players; no 40.
- **Group XP:** no split and no bonus; 0 XP for all if the level spread exceeds 5.
- Engine decided: Godot 4 + C#.
