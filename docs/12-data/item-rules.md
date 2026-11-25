# Item Rules — how every item's numbers are worked out

[← Data Index](00-data-index.md) · Design: [Items & Loot](../02-systems/items-and-loot.md) · List: [Named Item Index](../10-art/07-named-item-index.md) · Schema: [Content Schemas](../08-tech/content-schemas.md)

The design documents name 765 items. Some state their numbers in full ("2H axe [30], 41 DPS, +14 Str +9 Sta"); most state only a slot and a level ("Mail legs [13]", "cloth hands, ilvl 3"). This page gives the rules that turn any such description into a complete item record, so the builder never has to invent a number. Validation rule V28 checks every item record against it.

**The first rule: a number stated in a source document is used exactly as stated.** These rules fill in only what the source leaves out. A stated stat list is complete: nothing is added to it.

## 1. Reading a description

| Notation | Meaning |
|---|---|
| `[N]` | Required level N |
| `ilvl N` | Item level N |
| `◆` | Rare (blue) quality |
| "+6 Str +5 Sta" and similar | The item's full stat list |
| "N DPS" | Weapon damage per second |
| "Cleric", "Druid", "Fighter" after a dash | Who it is meant for. It sets the stat profile (§4) but is not a class restriction unless the text says "only" |

| Missing | Filled in by |
|---|---|
| Quality | By source: vendor stock = Common · profession recipe with no stats and no ◆ = Common · recipe with stats = Uncommon · quest reward = Uncommon · elite or group quest reward, dungeon boss, PvP vendor, reputation reward = Rare · raid boss, world boss, the six world epics = Epic |
| Item level from required level | Poor and Common: equal to required level · Uncommon: +5 · Rare: +8 · Epic: +12 |
| Required level from item level | The same sums reversed, never below 1 |
| Binding | Quest reward, dungeon, raid, world boss, PvP and reputation items: bind on pickup · crafted items and world drops: bind on equip · vendor Common items: none |
| Stack size | Equipment 1 |
| Id | The `ITM-nnn` number in the [Named Item Index](../10-art/07-named-item-index.md); the content id is `item.` plus the name in lower-case words joined by hyphens |

## 2. Stat points

`points = ilvl × slotWeight × qualityMult × 0.40`

The 0.40 is the scale that makes this formula agree with the items whose stats the documents state in full; [Items & Loot §4](../02-systems/items-and-loot.md#4-item-level-and-stat-budgets) carries the same figure.

| Slot | Weight |
|---|---|
| Chest, legs, head, two-handed weapon, staff | 1.00 |
| Shoulders, hands, waist, feet | 0.77 |
| Wrist, back, neck, ring | 0.56 |
| Shield, held off-hand | 0.56 |
| One-handed weapon, dagger | 0.42 |
| Ranged weapon, relic | 0.32 |
| Trinket | 0.70, spent on one stat or on a use effect stated by the source |

Quality multipliers and point costs are in [Items & Loot](../02-systems/items-and-loot.md): Uncommon 1.00, Rare 1.25, Epic 1.55; 1 Strength, Agility, Intellect or Spirit costs 1.0 and 1 Stamina 0.67.

- Poor and Common items have no stats.
- If the points come to less than 1, the item has no stats. From 1 to under 3, it has one stat (the profile's first).
- Otherwise two stats: 60% of the points to the first, 40% to the second, each converted at its cost and rounded down, minimum 1.
- Epic items take a third stat: 50% / 30% / 20%.

## 3. Worked example

*Larkhill Ringed Gauntlets* — "mail hands, ilvl 3", a quest reward.
Quality Uncommon; required level 1 (3 − 5, floor 1). Points = 3 × 0.77 × 1.00 × 0.40 = 0.92, under 1, so no stats. Armor (§5) = (1.3 × 3 + 4) × 4.2 × 0.625 = 20. Vendor value (§7) = 3² × 2.0 × 1.0 × 1.2 = 21 copper. Durability 30. Bind on pickup.

*A level 24 mail chest from a quest*, no stats given. Uncommon; ilvl 29. Points = 29 × 1.00 × 1.00 × 0.40 = 11.6. Profile for mail with no named user (§4), say Sentinel: Strength 60% = 6.96 → +6 Str; Stamina 40% = 4.64 ÷ 0.67 → +6 Sta. Armor = (1.3 × 29 + 4) × 4.2 × 1.00 = 175.

## 4. Stat profiles

Where the source gives no stats, the item takes a two-stat profile. If the source names a user, use the row for that user. Otherwise take the list for the item's type and choose by this rule, so the choice is repeatable: add up the character codes of the item's name and take the remainder after dividing by the length of the list.

| Item type | Profiles to choose from (first stat, second stat) |
|---|---|
| Mail armor, shield | Str + Sta · Sta + Str · Str + Int · Int + Sta |
| Leather armor | Agi + Sta · Sta + Agi · Int + Spi · Int + Sta · Str + Agi |
| Cloth armor | Int + Spi · Int + Sta · Spi + Int · Sta + Int |
| Cloak, neck, ring | Sta + Str · Sta + Int · Str + Agi · Int + Spi · Agi + Sta |
| Two-handed sword, axe, mace, polearm | Str + Sta · Str + Agi |
| One-handed sword, axe, mace | Str + Sta · Str + Agi · Sta + Str |
| Dagger | Agi + Sta · Agi + Str |
| Staff | Int + Spi · Int + Sta · Sta + Int |
| Held off-hand, relic | Int + Spi · Spi + Int |
| Bow, crossbow, gun, thrown | Agi + Sta |

| Named user | Profile |
|---|---|
| Fighter tank ("Bulwark", "tank") | Sta + Str; shields and Rare or better chest, legs and head add Defense with one-fifth of the points |
| Fighter damage | Str + Agi |
| Cleric healer | Int + Spi |
| Cleric tank or melee | Str + Int, or Sta + Str for "tank" |
| Druid healer | Int + Spi |
| Druid caster | Int + Sta |

Spell power, healing power, hit, crit and mp5 appear only where a source states them.

## 5. Armor

`armor = (1.3 × ilvl + 4) × typeMult × slotMult × qualityArmor`, rounded.

| Type | typeMult | | Slot | slotMult |
|---|---|---|---|---|
| Cloth | 1.0 | | Chest | 1.000 |
| Leather | 2.0 | | Legs | 0.875 |
| Mail | 4.2 | | Head | 0.810 |
| | | | Shoulders | 0.750 |
| | | | Feet | 0.690 |
| | | | Hands | 0.625 |
| | | | Waist | 0.560 |
| | | | Wrist | 0.440 |
| | | | Back (always cloth) | 0.500 |

`qualityArmor`: Poor 0.8 · Common 0.9 · Uncommon 1.0 · Rare 1.10 · Epic 1.22.

Shields: `armor = (18 × ilvl + 30) × qualityArmor`; block value `= ilvl × 0.4`, rounded. Necks, rings, trinkets, held off-hands and relics have no armor.

## 6. Weapons

Damage per second for an Uncommon one-handed weapon is `ilvl × 0.55 + 2.5` ([Items & Loot §4](../02-systems/items-and-loot.md#4-item-level-and-stat-budgets)). Multipliers: two-handed and staff × 1.3 · ranged × 0.75 · Poor × 0.70 · Common × 0.85 · Rare × 1.08 · Epic × 1.18.

| Type | Speed (s) | | Type | Speed (s) |
|---|---|---|---|---|
| Dagger | 1.7 | | Two-handed sword | 3.3 |
| One-handed sword | 2.4 | | Two-handed axe | 3.4 |
| One-handed axe | 2.5 | | Two-handed mace | 3.6 |
| One-handed mace | 2.6 | | Polearm | 3.2 |
| Bow | 2.6 | | Staff | 3.0 |
| Gun | 2.7 | | Crossbow | 3.0 |
| Thrown | 2.0 | | | |

A named item's speed is the table speed plus −0.2, 0 or +0.2, chosen by the name rule in §4 (remainder after dividing by 3).

`minDamage = DPS × speed × 0.75` and `maxDamage = DPS × speed × 1.25` for one-handed and ranged weapons; 0.80 and 1.20 for two-handed. Both rounded.

## 7. Vendor value and vendor price

Vendor value is what a vendor pays for the item, in copper:

`value = ilvl² × slotPrice × qualityPrice × typePrice`, rounded, minimum 1.

| Slot | slotPrice | | Quality | qualityPrice |
|---|---|---|---|---|
| Two-handed weapon, staff | 5.0 | | Poor | 0.2 |
| One-handed weapon, dagger | 4.0 | | Common | 0.5 |
| Chest, legs | 3.0 | | Uncommon | 1.0 |
| Shield, held off-hand | 2.6 | | Rare | 1.6 |
| Ranged, relic | 2.5 | | Epic | 2.6 |
| Head, shoulders | 2.4 | | | |
| Hands, feet, waist, neck, ring, trinket | 2.0 | | | |
| Wrist, back | 1.6 | | | |

`typePrice`: cloth 0.8 · leather 1.0 · mail 1.2 · everything else 1.0.

A vendor **sells** an item for 5 × its vendor value, unless the stock lists in the [NPC Index](../11-npcs/00-npc-index.md) give a price, which then stands. Quest items and anything marked "no sell value" have value 0 and cannot be sold. Materials, consumables and recipes take the prices in their own documents; where none is given, value = required level (or skill ÷ 5) × 4 copper for materials and × 10 for consumables.

## 8. Durability and repair

| Slot | Durability (Uncommon) |
|---|---|
| Two-handed weapon, staff, chest, shield | 85 |
| One-handed weapon, dagger, ranged, legs | 65 |
| Head, shoulders | 50 |
| Feet | 45 |
| Hands, waist, wrist | 30 |
| Back, neck, ring, trinket, held off-hand, relic, shirt, tabard | None |

Quality: Poor 0.7 · Common 0.8 · Uncommon 1.0 · Rare 1.15 · Epic 1.35, rounded.

| Event | Loss |
|---|---|
| Death | 10% of maximum on every equipped item (not in duels, battlegrounds or the arena) |
| Spirit healer | A further 25% on every equipped item ([Progression §10](../02-systems/progression.md#10-death)) |
| Attacking | Each swing or shot that hits: 3% chance the weapon loses 1 |
| Being hit | Each hit taken: 3% chance one random equipped armor piece loses 1; a block always tests the shield instead |
| At 0 | The item gives no stats, armor or damage, and shows red on the character window |

Repair cost per point of durability, in copper: `ilvl × 0.06 × qualityRepair × slotRepair`. `qualityRepair`: Common 0.7 · Uncommon 1.0 · Rare 1.3 · Epic 1.7. `slotRepair`: weapon 1.4 · shield 1.2 · armor 1.0. The economy audit in milestone M12 may tune the 0.06.

## 9. Random-suffix world drops

A world green is a base item plus a suffix from [Items & Loot §4](../02-systems/items-and-loot.md#random-suffix-world-drops).

| Step | Rule |
|---|---|
| Level | Required level = the creature's level − 2 to + 0, never above 30; ilvl = that + 5 |
| Slot | Chosen evenly from: chest, legs, head (required level 18+), shoulders (12+), feet, hands, waist, wrist, back, ring (15+), neck (20+), shield, each weapon type |
| Armor type | For armor slots: cloth, leather, mail with equal chance |
| Suffix | Chosen evenly from the suffixes whose stats suit the item: any suffix for jewellery and cloaks; no Intellect or Spirit suffix on two-handed axes and swords; no Strength suffix on cloth, staves or held off-hands |
| Stats | §2 points. Two-stat suffixes split 50/50; single-stat suffixes take all of it; spell-power and healing suffixes convert at the costs in Items & Loot; "of Defense" puts 40% in Defense and 60% in Stamina |
| Everything else | §5 to §8 |

Base names: prefix by required-level band, then the slot noun.

| Band | Cloth | Leather | Mail and shields | Weapons | Jewellery |
|---|---|---|---|---|---|
| 1–5 | Homespun | Rawhide | Linked | Sturdy | Tin |
| 6–10 | Weaver's | Cured | Ringmail | Balanced | Copper |
| 11–15 | Lanternwool | Trapper's | Banded | Tempered | Bronze |
| 16–20 | Marchsilk | Hardened | Scalemail | Soldier's | Silver |
| 21–25 | Duskweave | Ranger's | Warden's | Veteran's | Electrum |
| 26–30 | Starthread | Nightstitch | Ironcoat | Knight-Errant's | Gold |

| Slot | Cloth | Leather | Mail |
|---|---|---|---|
| Chest | Robe | Jerkin | Hauberk |
| Legs | Trousers | Breeches | Leggings |
| Head | Hood | Cap | Coif |
| Shoulders | Mantle | Spaulders | Pauldrons |
| Feet | Slippers | Boots | Sabatons |
| Hands | Gloves | Grips | Gauntlets |
| Waist | Sash | Belt | Girdle |
| Wrist | Cuffs | Bracers | Vambraces |

Cloaks use the cloth prefix and "Cloak" · shields the mail prefix and "Shield" · rings the jewellery prefix and "Band" · necks the jewellery prefix and "Chain" · weapons the weapon prefix and the type's plain name (Shortsword, Hand Axe, Mace, Dagger, Greatsword, Greataxe, Maul, Glaive, Staff, Bow, Crossbow, Longrifle). Art: the tier model and texture for that slot, type and band.

## 10. Tuning

These rules were written to agree with the items the documents state in full; they have not been played. Three checks during the build keep them honest, and each names the first number to change if it fails:

| Check | Where | First number to adjust |
|---|---|---|
| Role targets at level 30 ([Combat §11](../02-systems/combat-and-stats.md#11-role-balance-targets-at-level-30-v0)) with generated gear | The combat simulator, milestone M4 | The 0.40 stat scale in §2; then the Stamina share in the tank profile |
| Coin earned by level 30 against the target in [Economy & Social](../02-systems/economy-and-social.md) | The full-game bot run and economy audit, milestone M12 | `slotPrice` in §7, all rows by the same factor |
| Repair bills as a share of income | The same audit | The 0.06 in §8 |

A change is made in the `itemRules` record, recorded in `build/decisions.md`, and the item files are regenerated.

## 11. Building the item files

In milestone M2 (task T-M2-04, items and equipment) the builder writes a small generator, `tools/itemgen`, that reads the [Named Item Index](../10-art/07-named-item-index.md) and the source documents and writes one content record per item by these rules, and keeps a table of every value it derived rather than read. Re-running it after a design change regenerates the records. Items whose source text it cannot parse are listed and written by hand under the same rules.
