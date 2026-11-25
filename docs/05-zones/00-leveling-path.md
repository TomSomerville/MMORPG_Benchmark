# The Leveling Path: 1 to 30

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Secondary Professions](../04-professions/secondary.md)

This page is the reading guide for the journey. Read the zone files in order to walk the whole game.

## 1. The map of the journey

| Levels | Meridia route (human default) | Khazrun route (dwarf default) | Shared |
|---|---|---|---|
| 1–5 | [Brightmead Vale](t1-brightmead-vale.md) | [Embercrag Hollow](t1-embercrag-hollow.md) — mountain dwarves | Capital visit at ~5: professions |
| 5–10 | [Harrowfield](t2-harrowfield.md) **or** [Russetwood](t2-russetwood.md) | [Stonewake Dale](t2-stonewake-dale.md) (hill dwarves) **or** [Stoneheart Deeps](t2-stoneheart-deeps.md) (inside the mountain) | Class quest at 10; talents begin |
| 10–20 | [Thornwick Marches](t3-thornwick-marches.md) | [Ironroot Highlands](t3-ironroot-highlands.md) | **Dungeon 1** Gallowmere Crypts (13–16); Main Chain 2 begins at 15; Chain 1 finale at Brandspire (20) |
| 20–30 | [Veilmoor](t4-veilmoor.md) · [The Riftlands](t4-riftlands.md) | [Cinderfall Barrens](t4-cinderfall-barrens.md) | **Dungeon 2** (20–23), **Dungeon 3** (27–30); world bosses |
| 30 | — | — | Raid attunement → **The Hollow Throne**; battleground bracket 30; FFA arena |

Routes are suggestions only. **No quest is race-locked**; the ship between Solhaven Harbor and the Seagate inside Hammerdeep is free from level 1.

**Redundancy at 5–10.** Each of the four T2 zones is a complete 5→10 with its own version of the main story, so each continent offers two interchangeable zones: farmland or autumn forest on Meridia; a farmed valley or the mountain's interior on Khazrun.

**Arriving at 5–10.** A player leaves a starting zone at about level 7, not the 5½–6 first planned (see [Progression §5](../02-systems/progression.md#5-xp-budget-per-tier-design-target)), so players arrive in Harrowfield, Russetwood, Stonewake Dale and Stoneheart Deeps about a level higher than those zones were first planned for. Open: the difficulty of the level 5–10 zones should be checked for arrivals at level 7; their numbers are unchanged until then.

## 2. Main chains through the zones

| Chain | Levels | Path |
|---|---|---|
| [**Embers of the Brand**](../06-quests/main-chain-1-embers-of-the-brand.md) | 1–20 | T1 (either) → T2 (any of four) → T3 (either) → Gallowmere Crypts → Brandspire (Thornwick) |
| [**The Hollow Crown**](../06-quests/main-chain-2-the-hollow-crown.md) | 15–30 | T3 (either) → Cinderfall 20–23 + The Slagworks → the Riftlands 24–27 → Veilmoor 27–30 + Hollowspire Keep → the Riftlands: raid |

The second chain deliberately walks the player through **all three** T4 zones — low band of Cinderfall, mid band of the Riftlands, high band of Veilmoor — while each zone separately offers a full 20–30 of side content.

## 3. Level-by-level expectations

| Level | Where you are | What you get | Milestone |
|---|---|---|---|
| 1 | Start camp | 2–3 abilities, white gear | First kill quest |
| 2–3 | First creature camp (mine/warrens) | New ability at 2 (trainer) | First bag |
| 4 | T1 town | Class abilities at 4; cultists appear | First caster enemies |
| 5 | T1 finale | First green weapon | Professions unlock |
| 6–7 | T2 opening areas | Class core rotation forms (Stomp / Dawnstrike / Briarskin) | Cooking, First Aid quests |
| 8–9 | T2 back half | First debuffs to cleanse; first elite quests | 8-slot bags |
| 10 | T2 finale | **Talents**; class quest (Guard Stance / Raise the Fallen / Overgrowth) | Battleground bracket 10–19 |
| 11–12 | T3 town | Interrupt (Fighter), shoulders appear | |
| 13–16 | T3 mid | **Gallowmere Crypts** blues | First group content |
| 15 | T3 | Main Chain 2 begins | |
| 16–19 | T3 back half | Taunt (Cleric), first helm, the ship between the capitals | |
| 20 | Brandspire | Chain 1 finale blue + title; class quest (Reckless Stance / Hallowed Ground / Reawaken); dual wield | Expert professions |
| 20–23 | T4 low bands | **The Slagworks** | Silk, Iron/Steel |
| 24–27 | T4 mid bands | Elite group quests; the Dustpit; neutral town | First world epics can drop (25+) |
| 27–30 | T4 high bands | **Hollowspire Keep**; Starmetal crafts; class quest weapon/relic | Pre-raid blue set complete |
| 30 | Cap | 21st talent point = signature ability; riding | Raid, world bosses, PvP gear |

## 4. Gear progression

| Level | Typical gear | Sources |
|---|---|---|
| 1–5 | White, first greens at 5 | Quests, vendors |
| 5–10 | Greens in most slots | Quests, crafting (copper/linen/light leather) |
| 10–20 | Greens + 4–6 blues | Gallowmere Crypts, elite quests, chain finale, bronze/wool crafts |
| 20–27 | Greens + blues | The Slagworks, T4 elites, iron/silk crafts |
| 27–30 | Full blue "pre-raid" set | Hollowspire Keep, Starmetal crafts, class quests, world drops |
| 30+ | Epics | The Hollow Throne (tier sets), world bosses, PvP |

## 5. Zone file template (what every zone file contains)

1. Summary table (theme, hubs, exits, instance links)
2. Sub-areas with level bands
3. Notable NPCs
4. Creature table: level, type, abilities, drops
5. Rares, elites and bosses
6. Full quest table: ID, name, level, giver, objective, XP, reward
7. Gathering and profession notes
8. Suggested flow

Quest IDs are `ZONE-NN` (BM, EC, HF, RW, ST, SD, TM, IR, CF, RL, VM) and are the stable keys used in data files.

## 6. Reward shorthand used in quest tables

- `25c`, `4s`, `1g 50s` — coin.
- "green boots (cloth/leather/mail)" — a choice of one Uncommon item per armor type, stats suited to the classes that wear it.
- *Italic names* — a unique named item (stats follow the [item budget rules](../02-systems/items-and-loot.md#4-item-level-and-stat-budgets) for its level and quality).
- "Blue choice" — a choice of Rare items.
- Every quest also gives reputation with the local faction (≈ 25% of its XP).

## 7. Quest counts

| Zone | Code | Quests | Main-chain quests |
|---|---|---|---|
| Brightmead Vale | BM | 18 | 6 (Chain 1) |
| Embercrag Hollow | EC | 18 | 6 (Chain 1) |
| Harrowfield | HF | 20 | 8 (Chain 1) |
| Russetwood | RW | 20 | 8 (Chain 1) |
| Stonewake Dale | ST | 20 | 8 (Chain 1) |
| Stoneheart Deeps | SD | 20 | 8 (Chain 1) |
| Thornwick Marches | TM | 36 | 12 (Chain 1) + 5 (Chain 2) |
| Ironroot Highlands | IR | 36 | 12 (Chain 1) + 5 (Chain 2) |
| Cinderfall Barrens | CF | 36 | 5 (Chain 2) |
| The Riftlands | RL | 36 | 8 (Chain 2) |
| Veilmoor | VM | 36 | 7 (Chain 2) |
| Class quests | — | 9 chains (3 per class) | — |
| **Total** | | **296 zone quests + class quests** | |

## 8. Beyond 30

The zone plan to level 60 — five zones for 30–40, four for 40–50, two for 50–60, and the rule that planned zones occupy only half of each continent — is in [World, Zones & Travel](../01-world/world-and-travel.md#2-full-zone-plan-160).
