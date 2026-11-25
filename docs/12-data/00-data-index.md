# Data — Index and Rules

[← Master Plan](../../MASTER_PLAN.md)

The build-level data that the design documents summarise: every creature's stat block and loot, every ability rank, every encounter's numbers, and the smaller lookup tables. Coding reads these files as the first content pack.

## 1. Files

| File | Holds | How it is made |
|---|---|---|
| [creatures.md](creatures.md) | 151 outdoor creature types and 76 named, rare and elite creatures: health, damage, armor, respawn, XP, 273 ability rows with numbers, loot tables | Generated from the zone creature tables by the rules in §2 |
| [spells.md](spells.md) | 73 class abilities as 152 rank rows: level, training cost, cost, cast time, cooldown, range, coefficient, effect | Generated from the class ability tables by the rules in §3 |
| [encounters.md](encounters.md) | Dungeon trash packs by room, boss timers and damage numbers, raid and world boss numbers, drop chances for every boss item | Written by hand from the instance documents |
| [reference-tables.md](reference-tables.md) | Flight routes and fares, reputation rewards, Valor prices, fishing tables, world-drop lists, recipe sources, class quests | Written by hand |
| [item-rules.md](item-rules.md) | The rules that give every item its stats, armor, damage, vendor value, durability and repair cost, and the base names for random drops | Written by hand; the builder's item generator applies them |
| [presentation-rules.md](presentation-rules.md) | Which model, skin, animation, effect, icon and sound each creature, NPC, ability and item uses, and how music and ambience play | Written by hand |
| [spoken-lines.md](spoken-lines.md) | The voice script: NPC barks by voice, story lines, announcer calls, every boss's lines, the 12 Athenaeum books and street chatter | Written by hand |
| [game-text.md](game-text.md) | System and error messages, interface labels, tutorial and loading tips, NPC stock phrases, the emote list, and the rules for any text not listed | Written by hand |

The NPC rosters, vendor stock and trainer lists are in [NPCs](../11-npcs/00-npc-index.md). Quest text and rewards are in [Quest Text](../06-quests/text/00-quest-text-index.md).

## 2. Creature rules

These are the rules the generator applies. Changing a rule changes every creature at once.

| Value | Rule |
|---|---|
| Health, melee DPS, armor | Interpolated by level from the [stat template](../02-systems/npc-ai-and-world.md#stat-templates-v0); a level 35 row (1,150 health, 50 DPS, 1,750 armor) is added for bosses |
| Casters | 80% health, 40% melee damage, 75% armor; mana = 60 + 45 × level |
| Swing speed | 2.0 s; cats, birds, spiders, bats and harpies 1.8 s; elementals 2.2 s; constructs and plants 2.4 s; giants 2.6 s |
| Damage per swing | DPS × swing speed, ±15% |
| Rare | ×1.5 health, ×1.2 damage; respawn 2–8 hours; always drops a green |
| Named quest target | ×1.5 health, ×1.2 damage; respawn 5 minutes |
| Mini-boss | ×2 health, ×1.3 damage |
| Elite | ×3 health, ×1.8 damage; respawn 7 minutes; XP ×2 |
| Group elite / chain boss | ×5 health, ×2.0 damage; XP ×3 |
| Group boss (4–5 players) | ×8 health, ×2.2 damage; respawn 15 minutes; XP ×3 |
| XP | 45 + 5 × level, before the level-difference rules in [Progression](../02-systems/progression.md) |
| Respawn | 2.5 minutes in level 1–5 zones, 5 minutes elsewhere; dynamic respawn scales this down to as little as 15% in crowded areas (there are no layers) |
| Aggro radius | 20 yards at equal level, ±1 per level of difference, minimum 5, maximum 45 |

**Ability kinds.** Each ability named in a zone table is given a kind from its name and note, and its numbers from the kind:

| Kind | Numbers |
|---|---|
| Strike | 120% of a swing; cooldown 8 s |
| Opener | 150% of a swing on the first hit; stealth openers are hidden until 8 yards |
| Area attack | 80% of a swing to everything within 5 yards; cooldown 12 s; "on death" versions reach 8 yards |
| Ranged or spell | Cast time × spell DPS, ±15%. Spell DPS is 2.2 × template DPS for casters, 1.3 × for others. Default cast 2.0 s, range 30 yards |
| Damage over time | 4 × level + 6 over 12 s in 4 ticks; cooldown 15 s |
| Drain | 2 × level + 6 per 2 s for 6 s; heals the creature or burns mana |
| Control, Root, Silence, Fear | Duration from the zone table (default 2–3 s); cooldown 20–30 s |
| Slow | 40% for 6 s unless stated; 60% of a swing |
| Heal | 12% of maximum health; 2.0 s cast, interruptible; cooldown 20 s; used below 50% health |
| Buff | +25% damage for 10 s (enrages add +30% attack speed); cooldown 30 s or at the stated health |
| Defensive, Debuff, Movement, Summon, Pull or charm, Trait | As stated in the zone table, with the default duration and cooldown shown in the row |

**Loot.** Every creature's loot follows [Items & Loot §7](../02-systems/items-and-loot.md#7-loot-generation):

| Type | Coin | Cloth or skin | Other |
|---|---|---|---|
| Humanoid, Giant | level × 3–9 copper, always | Linen to level 11, linen and wool to 14, wool to 21, wool and silk to 26, silk above; 35% | Grey junk 70% |
| Undead | Half coin, 60% of the time | Cloth at 25% | Grey junk 70% |
| Beast, Dragonkin | None | Skinnable: scraps to level 2, light leather to 16, medium to 24, heavy above | Grey junk 75% |
| Elemental, Construct, Plant, Aberration | None | — | Family grey 60–65% |
| Notable drops (from the zone table) | | | First listed 40%, others 25%, "rare" 3%; quest items at the rate in the quest text |
| World table | | | Green 0.6%, blue 0.03%, epic 0.002% from level 25, recipe 0.5–2%, bag 0.5%, consumable 4% (elites: green 8%, blue 1%) |

## 3. Spell rules

| Value | Rule |
|---|---|
| Ranks | One row per rank at the levels in the class document's "Ranks at" column |
| Values between first and last rank | Straight-line interpolation by the level at which the rank is learned |
| Training cost | The per-level curve in [Progression](../02-systems/progression.md): 10c at 2 rising to 1g 60s at 30; level 1 ranks are free; class-quest abilities cost nothing for the first rank |
| Range | From the ability text; otherwise melee for weapon attacks, 30 yards for harmful spells, 40 yards for heals and friendly spells, self for auras and self-buffs |
| Global cooldown | 1.5 s for everything except next-swing attacks, auras, toggles and passives |
| Coefficient | [Combat §6](../02-systems/combat-and-stats.md#6-spell-power-coefficients): cast time ÷ 3.5 for direct spells (instants count as 1.5 s), duration ÷ 15 for over-time effects, half each for hybrids, one-third for area effects, and a penalty of 3.75% per level for ranks learned below 20 |
| Threat | 1 per point of damage and 0.5 per point of healing unless the effect text says otherwise |
| Talents | Each talent's per-rank effect is already given in full in the class documents and is not repeated here |

All numbers are balance v0.
