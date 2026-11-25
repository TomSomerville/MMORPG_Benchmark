# Items & Loot

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Combat & Stats](combat-and-stats.md) · Next: [Economy & Social](economy-and-social.md)

## 1. Item qualities

| Quality | Colour | Source | Stat budget vs. Uncommon |
|---|---|---|---|
| Poor | Grey | Vendor trash | — |
| Common | White | Vendors, basic crafts, starting gear | Armor/damage only |
| Uncommon | Green | Quests, world drops, crafts | ×1.00 |
| Rare | Blue | Dungeon bosses, elite quests, rare crafts, PvP | ×1.25 |
| Epic | Purple | Raid, world bosses, very rare world drops | ×1.55 |
| Legendary | Orange | Reserved (one raid quest item planned post-launch) | ×1.9 |

## 2. Equipment slots (19)

Head · Neck · Shoulders · Back · Chest · Shirt · Tabard · Wrists · Hands · Waist · Legs · Feet · Ring ×2 · Trinket ×2 · Main hand · Off hand · Ranged/Relic. Plus an ammo pouch/quiver bag slot for ranged users.

Slot availability by level (classic feel): shoulders from ~L12 items, head from ~L18, trinkets/necks rare before 20.

## 3. Armor and weapon types

| Armor | Fighter | Cleric | Druid | Future |
|---|---|---|---|---|
| Cloth | ✓ | ✓ | ✓ | Warlock, mage |
| Leather | ✓ | ✓ | ✓ | Rogue, archer |
| Mail | ✓ | ✓ | — | Archer at 40 |
| Plate | L40 | L40 | — | |
| Shield | ✓ | ✓ | — | |

| Weapon | Fighter | Cleric | Druid |
|---|---|---|---|
| 1H sword / axe / mace | ✓ | ✓ (mace, sword) | mace |
| Dagger | ✓ | — | ✓ |
| 2H sword / axe / mace | ✓ | ✓ | 2H mace (L20) |
| Polearm | ✓ (L20) | ✓ (L20) | — |
| Staff | ✓ | — | ✓ |
| Bow / crossbow / gun / thrown | ✓ (pulling) | — | — |
| Held off-hand | — | — | ✓ |
| Relic (ranged slot) | — | Psalter | Charm |

Proficiencies are a list on the class record; new weapon skills are taught by a Weapon Master for 10s each.

## 4. Item level and stat budgets

- **Item level (ilvl)** ≈ required level + 5 (greens), + 8 (blues), + 12 (epics). Launch range: ilvl 1–45.
- **Every item's full numbers** (stats, armor, damage, vendor value, durability, base names for random drops) follow from the rules in **[Item Rules](../12-data/item-rules.md)**. A number stated for a named item always stands.
- **Budget:** `points = ilvl × slotWeight × qualityMult × 0.40` (the 0.40 scale matches the items whose stats are stated in full). Slot weights: chest/legs/head/2H 1.00; shoulders/hands/waist/feet 0.77; wrist/back/neck/ring 0.56; 1H/shield/off-hand 0.42–0.56; trinket custom.
- **Point costs:** 1 primary stat = 1.0; 1 Stamina = 0.67; 1 AP = 0.5; 1 spell power = 0.86; 1 healing power = 0.45; 1% crit = 14; 1% hit = 10; 1 mp5 = 2.5; 1 defense = 1.5; resist = 1.0.
- **Weapon DPS:** `ilvl × 0.55 + 2.5` for a green 1H at that ilvl; 2H ×1.3; blue +8%, epic +18%. Speeds: daggers 1.5–1.8, 1H 2.0–2.8, 2H 3.0–3.8.
- **Armor value:** by armor type and ilvl; mail ≈ 2.1 × leather ≈ 4.2 × cloth.

### Random-suffix world drops

Green world drops are generated as *base item + suffix*, so thousands of items come from a small table.

**Naming convention.** Two-stat suffixes are named after a **calling** — a walk of life in Halcyra whose reputation matches the stat pair ("Ringmail Gauntlets of the Sentinel"). No animal names are used. Single-stat suffixes name the stat plainly. School spell-power suffixes name the cosmological force (see [Lore](../01-world/lore.md#2-cosmology)).

| Suffix | Stats | Wanted by |
|---|---|---|
| of the Sentinel | Str + Sta | Fighter, Cleric tank |
| of the Duelist | Str + Agi | Fighter DPS |
| of the Pilgrim | Str + Spi | Leveling melee |
| of the Outrider | Agi + Sta | (future rogue/archer), Fighter |
| of the Scholar | Int + Sta | Casters |
| of the Sage | Int + Spi | Healers |
| of the Wayfarer | Sta + Spi | Anyone leveling |
| of the Templar | Str + Int | Cleric |
| of the Seeker | Agi + Int | (future archer) |
| of the Wanderer | Agi + Spi | — |
| of Strength / Agility / Stamina / Intellect / Spirit | Single stat | — |
| of the Choir | Nature spell power | Druid (Stormcall) |
| of the Lattice | Arcane spell power | Druid (Starweave) |
| of the Dawnflame | Holy spell power | Cleric |
| of Healing | Healing power | Healers |
| of Defense | Defense + Sta | Tanks |

Reserved for future classes: *of the Hollow* (Shadow), *of the Deep Fires* (Fire), *of the Long Cold* (Frost), *of the Marksman* (Agi + ranged attack power), *of the Shade* (Agi + crit).

## 5. Binding, uniqueness, durability

- **Bind on Pickup** (dungeon/raid/quest), **Bind on Equip** (crafted, world drops), **Bind on Use**, **Quest item**, **Unique**, **Unique-equipped**.
- **Durability** on armor and weapons: lost on use and 10% on death. At 0 the item gives no stats. Repaired at any armorer/blacksmith vendor.
- **Required level, class, profession skill, reputation** restrictions are fields on the item.
- **Sets:** set bonus records referencing item ids (raid tier sets, one dungeon set, one PvP set).
- **Use / proc effects:** items reference spells ("Use:", "Equip:", "Chance on hit:").
- **Sockets, reforging, transmog:** not in scope (not classic).

## 6. Bags, bank, inventory

| Container | Slots | Source |
|---|---|---|
| Backpack | 16 | Fixed |
| Small pouch / Linen bag | 6 | Vendor 5s / Tailoring |
| Woolen bag | 8 | Tailoring |
| Small silk pack | 10 | Tailoring |
| Digger's Haversack | 12 | Rare drop, Riftlands |
| Bank | 24 + 6 purchasable bag slots (10s, 1g, 10g, 25g, 50g, 100g) | Capitals, Kite's Rest |

Stack sizes: materials 20, consumables 5–20, ammo 200. Soulbound items cannot be traded/mailed/auctioned.

## 7. Loot generation

Each creature references a **loot table** composed of weighted groups:

| Group | Typical chance | Contents |
|---|---|---|
| Coin | 100% (humanoids), 0% (beasts) | `level × (3–9)` copper; elites ×4 |
| Vendor trash | 60–80% | Family-themed greys (wolf fangs, bent picks) |
| Quest items | 25–100% | Only for players on the quest |
| Family reagents | 15–60% | Cloth (humanoids), meat/skin (beasts), essences (elementals) |
| Consumables | 3–6% | Potions, scrolls, food |
| World green | `0.6%` normal, `8%` elite, `100%` rare mob | Random-suffix item of mob level ±2 |
| World blue | `0.03%` normal, `1%` elite | Zone blue list |
| World epic | `0.002%` normal (L25+), `0.1%` elite | 6 named epics (see below) |
| Recipes | 0.5–2% | Zone recipe list |
| Bags | 0.5% | Level-appropriate bag |
| Skinning / Mining / Herbalism from corpse | Deterministic by family | See [Gathering](../04-professions/gathering.md) |

**Chests:** spawn in mob camps (5–15 min respawn), contain coin, a consumable and a guaranteed green; some need lockpicking keys (blacksmith skeleton keys) until rogues exist.

**World epics (level 25–30):** *Thornwake Longblade* (1H sword), *Hearthbreaker* (2H mace), *Staff of the Unlit Star*, *Gallows-Rope Girdle* (leather), *Signet of the Last Emperor* (ring), *Cinderheart Pauldrons* (mail).

## 8. Group loot rules

Free-for-all · Round-robin · **Group Loot (default)** — round-robin for whites and below, roll for greens+ · Need Before Greed · Master Looter (raid default). Loot threshold configurable. Need/Greed/Pass roll window 60 s. Bind-on-Pickup confirm dialog. Raid loot is tradeable among raid members present at the kill for 2 hours.

## 9. Consumables overview

| Type | Examples | Rule |
|---|---|---|
| Food / drink | Bread, cider, spring water | Seated, out of combat, 18–30 s. Cooked food also gives a 15 min "Well Fed" Sta/Spi buff |
| Potions | Healing, mana, rage | 2 min shared potion cooldown |
| Elixirs | Stat buffs 30–60 min | One battle + one guardian elixir |
| Scrolls | Stat buffs 30 min | World drops; do not stack with class buffs of same stat |
| Bandages | First Aid | 60 s "recently bandaged" debuff; channel breaks on damage |
| Weapon stones / oils | Sharpening stones (BS), wizard oil (Ench) | 30 min weapon buff |
| Ammo | Arrows, bullets | Consumed per shot (Fighter pulling only at launch) |
| Reagents | Seed of Renewal (Druid Reawaken), Sanctified Candle (Cleric group buffs later) | Vendor-sold |

## 10. Named gear by source (index)

- Quest rewards: listed per quest in each [zone file](../05-zones/00-leveling-path.md).
- Dungeon loot tables: [Dungeons](../07-instances/dungeons.md).
- Raid loot and tier sets: [Raid](../07-instances/raid-the-hollow-throne.md).
- World boss loot: [World Bosses](../07-instances/world-bosses.md).
- Crafted gear: [Crafting](../04-professions/crafting.md).
- PvP gear: [PvP](pvp.md).
