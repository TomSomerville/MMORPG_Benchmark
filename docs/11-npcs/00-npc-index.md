# NPCs — Index, Vendor Stock and Trainer Lists

[← Master Plan](../../MASTER_PLAN.md) · Rules: [NPC AI & World](../02-systems/npc-ai-and-world.md#5-friendly-npcs) · [Economy](../02-systems/economy-and-social.md#5-vendors)

Every friendly NPC in the level 1–30 game: name, role, where they stand, what they sell or teach, which quests they give and take, and their greeting line. The rosters are one file per region:

| File | Covers |
|---|---|
| [01-brightmead-harrowfield-russetwood.md](01-brightmead-harrowfield-russetwood.md) | Meridia, levels 1–10 |
| [02-embercrag-stonewake-stoneheart.md](02-embercrag-stonewake-stoneheart.md) | Khazrun, levels 1–10 |
| [03-thornwick-marches.md](03-thornwick-marches.md) | Meridia, levels 10–20 |
| [04-ironroot-highlands.md](04-ironroot-highlands.md) | Khazrun, levels 10–20 |
| [05-cinderfall-barrens.md](05-cinderfall-barrens.md) | Khazrun, levels 20–30 |
| [06-riftlands.md](06-riftlands.md) | Meridia, levels 20–30 |
| [07-veilmoor.md](07-veilmoor.md) | Meridia, levels 20–30 |
| [08-solhaven.md](08-solhaven.md) | Human capital |
| [09-hammerdeep.md](09-hammerdeep.md) | Dwarf capital |

## 1. How to read a roster row

| Column | Meaning |
|---|---|
| ID | Content record id (`npc.bm_03`) |
| Name | Full display name. The line under the name in game is the Role |
| Short name | How quest text refers to this NPC. Used by the generator that fills the quest columns |
| Role | Title shown under the name, and the NPC's function |
| Where | Hub or sub-area, and the spot within it |
| Services | Stock lists (`STK-…`), trainer lists (`TRN-…`) and other services from this page. "+" adds single items to a stock list |
| Gives / Ends | Quest IDs this NPC offers and completes. **Filled in by script from the [quest text](../06-quests/text/00-quest-text-index.md)**; do not edit by hand |
| Greeting | The line shown when the NPC is spoken to with nothing to hand in. Service NPCs open their service window with this line above it |

Rules for all NPCs:

1. Friendly NPCs are level 30–35 and cannot be attacked at launch (one allegiance). Guards are level 35 elite.
2. Every NPC that is not a quest giver has one greeting line; quest givers have one, plus their quest text.
3. Vendors buy anything sellable. Any vendor marked **Repair** repairs all gear.
4. Prices below are base prices. Reputation discounts: Friendly 5%, Honored 10%, Revered 15%, Exalted 20% with the vendor's allegiance.
5. "×N" in a roster row means N copies of a generic NPC with a shared name pool, such as guards.

## 2. Stock lists

Prices are per item unless a stack is shown. "Limited" stock shows the quantity and restock time.

### STK-GEN — General goods (every hub)

| Item | Price | Notes |
|---|---|---|
| Small Pouch (6-slot bag) | 5s | |
| Hearth-Candle (relights a campfire) | 10c | |
| Flint and Tinder | 15c | For the Basic Campfire |
| Simple Wood | 4c | For the Basic Campfire |
| Fishing Pole | 25c | |
| Mining Pick | 85c | |
| Skinning Knife | 85c | |
| Herbalist's Sickle | 85c | Cosmetic; Herbalism needs no tool |
| Coarse Thread | 10c | |
| Empty Vial | 4c | |
| Rough Arrow (stack of 200) | 10c | Level 1 |
| Sharp Arrow (stack of 200) | 3s | Level 10 |
| Razor Arrow (stack of 200) | 10s | Level 25 |
| Small Quiver (8-slot ammo bag) | 10s | From 10–20 hubs onward |

### STK-FOOD — Food and drink (innkeepers and provisioners)

The tier sold depends on the hub: tier 1 in level 1–5 hubs, tiers 1–2 in 5–10 hubs, 2–3 in 10–20 hubs, 3–4 in 20–30 hubs, all four in capitals.

| Tier | Level | Food (health over time) | Price ×5 | Drink (mana over time) | Price ×5 |
|---|---|---|---|---|---|
| 1 | 1 | Brown Bread — 61 over 18 s | 25c | Refreshing Water — 151 over 18 s | 25c |
| 2 | 5 | Hard Cheese — 243 over 21 s | 1s 25c | Sweet Cider — 436 over 21 s | 1s 25c |
| 3 | 15 | Smoked Sausage — 552 over 24 s | 5s | Highland Melt — 835 over 24 s | 5s |
| 4 | 25 | Traveller's Pasty — 874 over 27 s | 10s | Spring Tonic — 1,080 over 27 s | 10s |

Innkeepers also sell *Tankard of Ale* (2c, cosmetic) and the local speciality named in their row.

### STK-TRADE — Trade supplies

| Item | Price | Used by |
|---|---|---|
| Coarse Thread · Fine Thread · Silken Thread | 10c · 1s · 5s | Tailoring, Leatherworking |
| Empty Vial · Leaded Vial | 4c · 40c | Alchemy |
| Weak Flux · Strong Flux | 10c · 20s | Blacksmithing |
| Coal | 5s | Smelting steel |
| Copper Rod | 1s 20c | Enchanting rods |
| Mild Spices · Hot Spices · Soothing Spices | 10c · 1s · 3s | Cooking |
| Salt | 50c | Leatherworking, Cooking |
| Red Dye · Blue Dye · Green Dye · Grey Dye · Bleach | 50c · 50c · 50c · 1s · 25c | Tailoring, Leatherworking |
| Blacksmith Hammer | 18c | Blacksmithing tool |
| Shiny Bauble (lure, +25 Fishing for 10 min) | 50c | Fishing |

Level 1–5 hubs stock only the first item of each group.

### STK-ARM — Armorer (white armor, Repair)

Sells the white (no-stat) piece for every armor slot the tier allows, in cloth, leather and mail, plus a shield. Tier follows the hub.

| Tier | Hub level | Required level | Price range per piece | Slots sold |
|---|---|---|---|---|
| a | 1–5 | 1–3 | 5c–60c | Chest, legs, feet, hands, wrist, waist; buckler |
| b | 5–10 | 6–8 | 2s–9s | Same |
| c | 10–20 | 12–16 | 9s–40s | Adds shoulders at 12 and head at 18 |
| d | 20–30 | 22–27 | 45s–1g 60s | All slots |

Price within the range follows slot weight: chest and legs are the top of the range, wrist and waist the bottom.

### STK-WPN — Weaponsmith (white weapons, Repair)

| Tier | Hub level | Required level | Types | Price |
|---|---|---|---|---|
| a | 1–5 | 1–3 | 1H sword, 1H axe, 1H mace, dagger, staff, 2H sword, 2H axe, 2H mace | 20c–1s |
| b | 5–10 | 6–8 | Same, plus shortbow | 3s–12s |
| c | 10–20 | 12–16 | Same, plus crossbow | 15s–60s |
| d | 20–30 | 22–27 | Same, plus polearm | 80s–2g 50s |

Two-handed weapons cost twice the one-handed price of the tier. Weaponsmiths also sell *Rough / Coarse / Heavy Sharpening Stone* (5c / 40c / 3s) and *Weightstone* equivalents.

### STK-REAG — Reagents

| Item | Price | Used by |
|---|---|---|
| Seed of Renewal | 20s | Druid: Reawaken |
| Sanctified Candle | 7s | Cleric: reserved for group blessings |
| Rune of Return | 10s | Reserved for future portal classes; sold but unused at launch |

### STK-STABLE — Stable and mounts (capitals only)

| Item | Price | Notes |
|---|---|---|
| Riding training (level 30) | 30g | Taught by the Riding Trainer, not the vendor |
| Horse — bay, black, chestnut, grey | 5g each | Solhaven; humans at Neutral, other races at Exalted with Solhaven |
| Ram — grey, brown, white, black | 5g each | Hammerdeep; dwarves at Neutral, other races at Exalted with Hammerdeep |
| Sack of Charger's Oats · Ram-Mash | 6g | Epic mount feed; listed but greyed out while the cap is 30 |

### STK-RECIPE — Recipe vendors

Recipes marked **(V)** in [Crafting](../04-professions/crafting.md) and [Secondary Professions](../04-professions/secondary.md). Each is sold by the vendor named in the roster row. Limited stock: 1, restocking every 2 hours, unless the roster says otherwise.

### STK-PVP — Valor quartermasters

Prices in Marks of Valor, exactly as in [PvP §5](../02-systems/pvp.md#5-marks-of-valor-and-pvp-gear). The per-piece prices are fixed in [Reference Tables](../12-data/reference-tables.md).

## 3. Trainer lists

### TRN-FIG / TRN-CLE / TRN-DRU — Class trainers

Teach every rank of every ability of that class up to the level cap, at the cost per rank in [Progression](../02-systems/progression.md) (10c at level 2 rising to 1g 60s at level 30). All class trainers teach the same list; a trainer in a level 1–5 hub does not refuse a level 30 character. Class trainers in capitals also reset talents (1g rising to 5g, decaying 1g per week).

The per-rank lists are the [Spell Data](../12-data/00-data-index.md) files.

### TRN-PROF — Profession trainers

| Code | Teaches | Ranks by hub |
|---|---|---|
| TRN-MIN | Mining | Apprentice (1–75) in level 1–5 hubs · Journeyman (to 150) in 5–20 hubs · Expert (to 225) in capitals and 20–30 hubs marked "Expert" |
| TRN-HRB | Herbalism | Same |
| TRN-SKN | Skinning | Same |
| TRN-BS | Blacksmithing | Same |
| TRN-LW | Leatherworking | Same |
| TRN-TL | Tailoring | Same |
| TRN-ALC | Alchemy | Same |
| TRN-ENC | Enchanting | Same |
| TRN-ENG | Engineering | Same |
| TRN-CK | Cooking | Same |
| TRN-FSH | Fishing | Same |
| TRN-FA | First Aid | Same |

Training costs: Apprentice 10c, Journeyman 5s, Expert 50s. Trainer-taught recipes cost 50c–2g by skill, as listed per recipe in the profession docs.

### TRN-WPN — Weapon masters (capitals)

10s per weapon skill. Solhaven teaches swords, maces, daggers, staves, bows, polearms (level 20). Hammerdeep teaches axes, maces, daggers, staves, crossbows, guns, polearms (level 20). Thrown weapons are taught by both.

### TRN-RIDE — Riding trainers (capitals)

Riding (level 30): 30g. Epic riding is listed and greyed out.

## 4. Generic NPC templates

| Template | Name pool | Behaviour |
|---|---|---|
| Guard (per hub) | "<Hub> Warden", "<Hub> Watchman", "<Hub> Ranger" and so on, as given in the roster | Level 35 elite; patrols or stands post; attacks hostile creatures within 30 yards; in capitals has a directions menu |
| Spirit Healer | "Spirit Healer" | One at every graveyard; visible only to the dead |
| Ambient citizen | Role names: Farmer, Miner, Pilgrim, Digger and so on | No interaction beyond a one-line greeting drawn from the hub's chatter list in the roster |
| Critter | Rabbit, hen, sheep, goat, rat, toad, cave cricket, lizard | Level 1; killable; no loot |

## 5. Counts

| | Count |
|---|---|
| Named NPCs | 356 |
| Generic groups (guards and similar) | 25 groups, about 240 individuals |
| NPCs that give or end at least one quest | 119 |
| Quests whose giver and ender both resolve to a roster NPC, an object or an item | 296 of 296 (checked by script) |
