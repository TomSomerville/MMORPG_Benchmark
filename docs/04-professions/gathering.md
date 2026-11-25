# Professions: Framework & Gathering

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Druid](../03-classes/druid.md) · Next: [Crafting](crafting.md) · [Secondary](secondary.md)

## 1. Profession framework

| Rule | Value |
|---|---|
| Primary professions | Max **2** per character: Mining, Herbalism, Skinning, Blacksmithing, Leatherworking, Tailoring, Alchemy, Enchanting, Engineering |
| Secondary professions | All three allowed: Cooking, Fishing, First Aid |
| Ranks | Apprentice 1–75 (level 5) · Journeyman 75–150 (level 10) · Expert 150–225 (level 20) · *Artisan 225–300 (level 35, reserved)* |
| Launch skill cap | **225** |
| Skill-ups | Recipe/node colour: orange = always, yellow = ~60%, green = ~25%, grey = never |
| Training cost | Apprentice 10c · Journeyman 5s · Expert 50s; recipes 50c–2g |
| Unlearning | Allowed; skill is lost |
| Recipe sources | Trainer (most), vendor (limited stock), world drop, reputation, quest |
| Crafted gear | Bind on Equip unless stated; the best craft per armor type is a **blue at 215–225** that rivals dungeon loot |

A profession is data: skill line, rank caps, and a list of **recipes** (skill required, colour thresholds, reagents, tool/station needed, output). A gathering node is a world object with a required skill and a loot table.

**Why crafting matters with only three classes:** Fighters and Clerics consume Blacksmithing (mail, weapons, shields, stones); Druids consume Leatherworking and Tailoring; everyone consumes Alchemy, Enchanting, bags, bandages and food. Cloth caster gear is deliberately competitive for Druids.

## 2. Material tiers at a glance

| Tier | Zones | Ore / bar | Stone | Herbs | Leather | Cloth | Enchanting |
|---|---|---|---|---|---|---|---|
| I (skill 1–75) | T1, T2 | Copper | Rough | Sunpetal, Hearthroot, Dewleaf, Bramblethorn | Ruined scraps, Light | Linen | Faint Dust, Lesser Spark Essence |
| II (65–150) | T2, T3 | Tin → Bronze, Silver | Coarse | Marshbloom, Gravecap, Crownleaf, Emberweed, Frostcap | Light → Medium, hides | Wool | Faint/Glimmer Dust, Greater Spark, Lesser Astral, Small Glinting Shard |
| III (125–225) | T3 high, T4, dungeons 2–3 | Iron → Steel, Gold, Starmetal | Heavy, Solid | Wyrmtongue, Veilshade, Riftbloom, Ashbloom, Ghostlily, Starpetal | Medium → Heavy, scales | Silk | Glimmer Dust, Greater Astral, Large Glinting Shard |

## 3. Mining

Requires a Mining Pick. Smelting needs a forge.

| Node | Skill | Found in | Yields |
|---|---|---|---|
| Copper Vein | 1 | Brightmead, Stonewake Dale, Harrowfield, Russetwood, Embercrag, Stoneheart Deeps | 1–3 Copper Ore; Rough Stone; rare Malachite, Tigerseye |
| Tin Vein | 65 | Harrowfield (quarry), Russetwood (kiln quarry), Embercrag (Tuskfall Ridge, the deep Warrens), Stoneheart Deeps (Crystal Galleries — richest), Thornwick, Ironroot | 1–3 Tin Ore; Coarse Stone; rare Moss Agate, Dusk Opal |
| Silver Vein | 75 | Rare spawn replacing Tin: Stoneheart Deeps, Thornwick, Ironroot | 1–3 Silver Ore; rare Moss Agate, Lesser Moonstone |
| Iron Deposit | 125 | Ironroot (Deepseam, peaks), Thornwick south, all T4 zones | 1–3 Iron Ore; Heavy Stone; rare Jade, Citrine |
| Gold Vein | 155 | Rare spawn replacing Iron: T4 zones | 1–3 Gold Ore; rare Citrine |
| Starmetal Deposit | 175 | Cinderfall (Molten Stair), Riftlands (Tor Vael Ruins), Veilmoor (barrows), The Slagworks, Hollowspire Keep | 1–2 Starmetal Ore; Solid Stone; rare Star Sapphire |
| Slag Heap (from Slag Elemental corpses) | 150 | Cinderfall | Iron Ore, Coal, Small Ember Core |

| Smelt | Skill | Reagents |
|---|---|---|
| Copper Bar | 1 | 1 Copper Ore |
| Tin Bar | 65 | 1 Tin Ore |
| Bronze Bar ×2 | 65 | 1 Copper Bar + 1 Tin Bar |
| Silver Bar | 75 | 1 Silver Ore |
| Iron Bar | 125 | 1 Iron Ore |
| Gold Bar | 155 | 1 Gold Ore |
| Steel Bar | 165 | 1 Iron Bar + 1 Coal (vendor) |
| Starmetal Bar | 175 | 1 Starmetal Ore |

Node respawn 5–10 min; each zone has ~40–70 possible node positions with ~40% populated at a time. Tracking: *Find Minerals* (minimap).

## 4. Herbalism

*Find Herbs* tracking. No tool needed.

| Herb | Skill | Habitat | Zones |
|---|---|---|---|
| Sunpetal | 1 | Open meadow, roadsides | Brightmead, Stonewake Dale (field margins) |
| Hearthroot | 1 | At the foot of hills and rocks | Brightmead, Stonewake Dale (feet of the terrace walls) |
| Dewleaf | 15 | Under trees | T1 edges; all T2 zones (richest in Russetwood; Glowcap Grotto only in the Deeps) |
| Bramblethorn | 50 | Hedgerows, fences, ruins | Harrowfield, Russetwood, Embercrag (the sheltered south wall of Anvilrest) |
| Marshbloom | 70 | Stream and channel banks | Embercrag (forge-warmed melt-pools), Russetwood streams, Harrowfield coast, Thornwick fen |
| Gravecap | 85 | Graveyards, crypts, near undead | Thornwick (Gallowmere), Gallowmere Crypts |
| Crownleaf | 100 | Forest clearings | Thornwick, Ironroot |
| Emberweed | 115 | Warm rock, near forges and vents | Ironroot (Brandforge), Cinderfall |
| Frostcap | 125 | Snow line, night-blooming | Ironroot peaks |
| Wyrmtongue | 150 | Cliffs and ledges | All T4 zones |
| Veilshade | 160 | Fog hollows, barrows | Veilmoor |
| Riftbloom | 170 | Canyon walls and ledges | Riftlands |
| Ashbloom | 185 | Ash fields, lava banks | Cinderfall |
| Ghostlily | 205 | Around spirits and hollowed ground | Veilmoor (Hollowspire grounds), Hollowspire Keep, Tor Vael Ruins |
| Starpetal | 210 | Rare: replaces any T4 herb 3% of the time; guaranteed 1–2 in each dungeon 3 run | T4 |

Some corpses can be "herbed": Bog Shamblers (Marshbloom, Crownleaf), Grimroot's saplings (Veilshade).

## 5. Skinning

Requires a Skinning Knife. A looted Beast or Dragonkin corpse can be skinned once by anyone after the owner loots.

**Skill needed:** mob level 1–10 → 1; level 11–20 → `(level − 10) × 10`; level 21+ → `level × 5`.

| Product | From mobs of level | Notes |
|---|---|---|
| Ruined Leather Scraps | 1–10 | 3 scraps → 1 Light Leather (Leatherworking) |
| Light Leather | 3–16 | |
| Light Hide | 8–16 (10%) | Cured for armor kits and blues |
| Medium Leather | 15–27 | |
| Medium Hide | 17–27 (10%) | |
| Heavy Leather | 25–33 | |
| Heavy Hide | 26–33 (10%) | |
| Sharp Fang, Thick Wolf Pelt | Wolves | Alchemy (Rage Potion), Leatherworking |
| Mirejaw Hide | Mirejaws, Fen Lurkers | Leatherworking (water-resistant boots) |
| Rimewing Scale | Rimewing Whelps (Ironroot) | Frost-resist cloak |
| Cinder Scale | Cinder Skinks, Cinderwing Drakes (Cinderfall) | Mail-from-scales recipes |
| Rift Wyrm Hide | Rift Wyrms (Riftlands) | Nature-resist gear |
| Pristine Hide of the Beast | Rare beasts, world boss adds | Blue Leatherworking recipes |

## 6. Design notes

- **Node sharing:** first come, first served (classic). Dynamic respawn scales node density with zone population.
- **Gathering gives no XP.**
- **Economy loop:** every crafted recipe above skill 150 needs at least one material from a T4 zone or a dungeon, so max-level characters keep a reason to be in the world.
- **Gems and rare drops** (Malachite … Star Sapphire) are used by Blacksmithing, Engineering and Enchanting rods; there is no Jewelcrafting.
