# Quest Text — Index and Rules

[← Master Plan](../../../MASTER_PLAN.md) · Chains: [Embers of the Brand](../main-chain-1-embers-of-the-brand.md) · [The Hollow Crown](../main-chain-2-the-hollow-crown.md)

Every quest from level 1 to 30, written out in full: the text the player reads, the tracker lines, the prerequisite, the exact reward and where every quest item comes from. **These files are the authority for quest text, prerequisites and rewards.** The quest tables in the zone files are the summary; their Reward column is copied from these files by `tools/doc-generators/zone-rewards.ps1`, so the two cannot disagree. Change a reward here, then run that script.

## Files

| Zone | Levels | Quests | File |
|---|---|---|---|
| Brightmead Vale | 1–5 | BM-01 to BM-18 | [bm-brightmead-vale.md](bm-brightmead-vale.md) |
| Embercrag Hollow | 1–5 | EC | [ec-embercrag-hollow.md](ec-embercrag-hollow.md) |
| Harrowfield | 5–10 | HF | [hf-harrowfield.md](hf-harrowfield.md) |
| Russetwood | 5–10 | RW | [rw-russetwood.md](rw-russetwood.md) |
| Stonewake Dale | 5–10 | ST | [st-stonewake-dale.md](st-stonewake-dale.md) |
| Stoneheart Deeps | 5–10 | SD | [sd-stoneheart-deeps.md](sd-stoneheart-deeps.md) |
| Thornwick Marches | 10–20 | TM | [tm-thornwick-marches.md](tm-thornwick-marches.md) |
| Ironroot Highlands | 10–20 | IR | [ir-ironroot-highlands.md](ir-ironroot-highlands.md) |
| Cinderfall Barrens | 20–30 | CF | [cf-cinderfall-barrens.md](cf-cinderfall-barrens.md) |
| The Riftlands | 20–30 | RL | [rl-riftlands.md](rl-riftlands.md) |
| Veilmoor | 20–30 | VM | [vm-veilmoor.md](vm-veilmoor.md) |
| Class quests (not in any zone table) | 10, 20, 30 | CQ | [cq-class-quests.md](cq-class-quests.md) |

## How to read an entry

| Line | Meaning |
|---|---|
| Heading | Quest ID and name. The ID is the content record id (`quest.bm_02`) |
| Italic line | Quest level · prerequisite quests · giver → turn-in NPC |
| **Offer** | Text shown when the quest is offered. Also the quest-log description |
| **Tracker** | The objective lines shown in the tracker and quest log, with counts |
| **Progress** | Text shown if the player talks to the turn-in NPC before finishing |
| **Complete** | Text shown at turn-in, above the reward choice |
| **Rewards** | XP, coin, items. "Choose 1" opens the reward picker; "and" items are always given |
| **Notes** | Drop sources and rates, object locations, scripting, world-state changes |

## Global rules

1. **Text tokens.** `<name>` = character name, `<class>` = class name. No text refers to the player's race; every quest reads the same for every race.
2. **Minimum level.** A quest can be accepted from 3 levels below its quest level (minimum 1). Dungeon quests ([D]) from 2 below.
3. **Prerequisites.** "Requires" lists quests that must be *completed*. "—" means none. Chain variants that satisfy the same step are written "A or B".
4. **Availability marker.** Givers show the quest marker only when level and prerequisites are met.
5. **Quest-item drops.** Quest items drop only for players on the quest, and each group member on the quest gets their own roll. The rate is given per quest. Rates below 100% are tuned so the quest takes 1.3–1.6 kills per item.
6. **Kill credit.** A kill counts for the player who tapped the creature and for every living party member within 100 yards of it, the same distance as shared kill XP ([Progression §2](../../02-systems/progression.md#2-kill-xp)). Raid groups get no quest credit except for raid quests.
7. **World objects.** A clickable quest object can be used only by a character who is on its quest. Using it is a 3-second channel, lost on moving or on being struck, unless a note says otherwise. Every quest object is per player: once a character has used one it is gone for that character alone and stays for everyone else, so there is no respawn timer and a crowd cannot empty a quest. A character's used objects are there again when the quest is taken again, abandoned or handed in. Where a note makes an object usable only after an earlier step (the Slag Crucible after Sootbeard's death, EC-16), the object cannot be used until that objective of its quest is complete.
8. **Coin.** The coin stated in each entry is final. The baseline it was drawn from:

| Quest level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Coin | 25c | 50c | 1s | 1s 50c | 2s | 2s 50c | 3s | 3s 50c | 4s | 5s |

| Quest level | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| Coin | 6s | 7s | 8s | 9s 50c | 11s | 12s 50c | 14s | 16s | 18s | 20s |

| Quest level | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|---|---|
| Coin | 22s | 25s | 28s | 31s | 34s | 37s | 40s | 42s | 50s | 55s |

   Talk and delivery quests pay half. Elite and dungeon quests pay 1.5×. A quest that gives a consumable bundle or a bag instead of gear may pay less.

9. **Reward items.** Every reward item is named and given as: *Name* (slot or weapon type, item level, stats). All quest rewards are Bind on Pickup.
   - White items (levels 1–4) have armor or damage only.
   - Greens use the budget in [Items & Loot](../../02-systems/items-and-loot.md#4-item-level-and-stat-budgets) at item level = quest level + 5; blues at quest level + 8.
   - **Armor and weapon damage are not written per item.** They are derived at content-build time from item level, armor type, slot and weapon speed using the Items & Loot formulas, so they cannot drift from the budget. Weapon speed is given because it is a design choice.
   - Each "choose 1" set covers the three classes: at least one option each for Fighter, Cleric and Druid.
10. **Replay and abandon.** Abandoning a quest removes its quest items. Items granted at accept are re-granted when the quest is taken again.
11. **Failure.** Escort and defend quests fail if the escorted NPC dies or the player goes beyond 80 yards; the quest can be abandoned and retaken at once.
12. **Reputation.** Every quest grants reputation equal to 25% of its XP (minimum 10) with the reputation of its zone, as listed in [Reference Tables §2](../../12-data/reference-tables.md#2-reputation). Fixed reputation amounts written in a quest's rewards are added on top.
13. **Tracker lines and objectives.** Each part of a Tracker line is one objective, with one exception: "Speak to" or "Report to" the NPC who ends the quest is the hand-in itself and makes no objective. A quest whose only line is that one has no objectives; its line is still shown in the tracker. Objectives may be done in any order: ordered objectives are not supported, so where a note says "in order" (the footprint triggers of EC-11) the order is not enforced. The one dependency there is belongs to world objects: an object can wait on an earlier objective of its quest (rule 7).

## Counts

| Zone file | Quests |
|---|---|
| BM, EC | 18 each |
| HF, RW, ST, SD | 20 each |
| TM, IR, CF, RL, VM | 36 each |
| **Total** | **296** — every quest ID in the zone tables has exactly one entry here (checked by script) |

## Things these files added to the design

Writing the text needed a few details the zone files did not have. They are decided here and should be copied back into the zone files when those are next edited.

- **New minor NPCs:** Lady Chamberlain Edith Marr (Marrowind Keep, TM-24) · Hall-Steward Borin Oathkeeper (Thane's Hall, IR-15) · Goodwife Marla Sedge (Mistral Hollow, TM-34) · Quartermaster Eydis (Emberwell, CF-36).
- **Named quest targets given a level and place:** Paymaster Grice, Odo Ketch, Chief Gnarr, Shard-Chief Krakk (level 8, 5–10 zones) · Preceptor Hask (14) · Runner Vask (15).
- **Third reward options** added wherever a zone table offered only two, so each class has a usable choice.
- **Boss last words** for the act bosses of Main Chain 1 and the bosses of Main Chain 2.
- **Dialogue flags** `rl14_ysolde` and `rl14_corvane` (RL-14), stored for future faction content.
- **Raid-credit exceptions:** the three world-boss quests (CF-34, RL-34, VM-35) and RL-36.

## Not yet done

- Reward item stats are budget-correct by formula but untested; they are "balance v0" like every other number.
- The [Named Item Index](../../10-art/07-named-item-index.md) now includes the quest reward items (765 named items in all); regenerate it after any reward change.
- The 10 class quests are written in [cq-class-quests.md](cq-class-quests.md). Profession quests do not exist at launch.
