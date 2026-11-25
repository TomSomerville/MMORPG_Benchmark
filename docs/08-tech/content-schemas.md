# Content Schemas

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Repository Layout](repo-and-conventions.md) · Next: [Database Schema](database-schema.md) · Records overview: [Data Model](data-model.md)

The exact shape of every YAML file under `content/`. Each record type has its fields, their types, and one worked example taken from the design documents. The validator (§4) rejects anything that does not match.

## 1. Conventions for all files

| Rule | Detail |
|---|---|
| One record per file, or a list | A file holds either one record or `records: [...]`. Small related records (a zone's spawns) share a file |
| Ids | Lowercase, dotted: `<type>.<scope>.<name>[.r<rank>]`. Quest ids are `quest.<zone>.<nn>`; NPC ids `npc.<zone>.<nn>`; creature ids `creature.<zone>.<name>` |
| Text | No display text in records. `name`, `description` and quest texts are keys into `content/strings/en/*.yaml`; the key defaults to the id plus a suffix (`.name`, `.offer`, …) and need not be written |
| References | A field typed `ref<spell>` holds the id of a spell record. The validator checks that it exists |
| Numbers | Integers unless marked `float`. Durations in milliseconds, written with a unit suffix that the loader converts: `1500ms`, `30s`, `5m`, `2h`. Money in copper with a suffix: `25c`, `1s50c`, `2g` |
| Percentages | Written as numbers: `35` means 35% |
| Formulas | Strings in a small expression language over named inputs: `"ilvl * 0.55 + 2.5"`. Only `+ - * / ( ) min max floor round` and the inputs listed for that field |
| `since` | Content version that introduced the record. Defaults to the pack version |
| Level ranges | `{min: 3, max: 4}` or a single number |

Field types used below: `id`, `ref<type>`, `int`, `float`, `bool`, `string`, `duration`, `money`, `enum(...)`, `list<T>`, `map<K,V>`, `formula`.

## 2. Record types

### 2.1 constants.yaml

One file. Every number that is a rule.

| Section | Holds |
|---|---|
| `xp.levelTable` | XP to next level, levels 1–59 |
| `xp.questTable` | Standard quest XP by level 1–60; difficulty multipliers |
| `xp.kill` | `base: "45 + 5 * level"`; level-difference modifiers; elite and dungeon multipliers; group rule (`splitAmongParty: false`, `maxLevelSpread: 5`) |
| `combat` | Armor formula constants, crit and dodge per Agility by class, attack table base chances, glancing and crushing rules, spell hit, global cooldown, pushback |
| `resources` | Rage conversion constants, mana regeneration by class, five-second rule |
| `threat` | Per-action threat, stance multipliers, switch thresholds (110 / 130) |
| `items` | Slot weights, quality multipliers, stat point costs, weapon DPS formula, armor formulas by type |
| `creatures` | Stat template rows; rank multipliers; swing speeds by type; ability-kind formulas |
| `economy` | Quest coin table, repair cost, auction cut, mail postage, respec price and decay, training cost curve, mount feed |
| `world` | Run speed, aggro radius rule, leash, corpse timers, respawn defaults, day length |
| `caps` | Level cap, quest log size, buff and debuff caps, bag and bank sizes |
| `movement` | Walk, backwards, swim and turn speeds, jump, step height, slide angle, fall damage ([Rules Reference §1](../02-systems/rules-reference.md#1-movement)) |
| `interaction` | Interaction ranges and timers, camera limits ([Rules Reference §2, §3, §6](../02-systems/rules-reference.md#2-interaction-ranges)) |
| `skills` | Weapon and defense skill gain, profession skill-up chances, food and drink tiers ([Rules Reference §4, §5](../02-systems/rules-reference.md#4-weapon-and-defense-skill)) |
| `itemRules` | Every table in [Item Rules](../12-data/item-rules.md): stat scale, profiles, armor and price multipliers, durability, repair, base names |
| `service` | Name rules, chat limits, report thresholds, penalty lengths, idle timers ([Accounts and Live Service](accounts-and-live-service.md)) |

```yaml
caps:
  level: 30
  questLog: 20
combat:
  armor: { base: 400, perAttackerLevel: 85, capPercent: 75 }
  globalCooldown: 1500ms
xp:
  kill: { base: "45 + 5 * level", eliteMult: 2.0, dungeonEliteMult: 2.5 }
  group: { splitAmongParty: false, maxLevelSpread: 5 }
```

### 2.2 Allegiance, reaction matrix, reputation

| Record | Field | Type | Notes |
|---|---|---|---|
| allegiance | `id` | id | `allegiance.concord` |
| | `colour` | string | Hex |
| | `races` | list<ref<race>> | |
| | `capitals` | list<ref<zone>> | |
| | `startReputations` | map<ref<reputation>, int> | |
| reactions | `matrix` | map<pair, enum(friendly, neutral, hostile)> | Symmetric; one entry per unordered pair, including self |
| | `zoneOverrides` | list<{zone, pair, reaction}> | Optional |
| reputation | `id`, `thresholds` | id, map<standing, int> | Friendly 3000 … Exalted 21000 |
| | `questShare` | int | Percent of quest XP granted as reputation (25) |
| | `rewards` | list<{standing, item or recipe or perk, price}> | From [Reference Tables §2](../12-data/reference-tables.md#2-reputation) |

```yaml
id: allegiance.concord
colour: "#3A6EA5"
races: [race.human, race.dwarf]
capitals: [zone.solhaven, zone.hammerdeep]
startReputations: { reputation.solhaven: 0, reputation.hammerdeep: 0 }
```

### 2.3 Race and class

| Record | Field | Type |
|---|---|---|
| race | `id`, `allegiance` | id, ref<allegiance> |
| | `baseStats` | {str, agi, sta, int, spi} |
| | `classes` | list<ref<class>> |
| | `racials` | list<ref<spell>> |
| | `start` | {zone, position, facing, bindInn} |
| | `startItems` | list<ref<item>> by class |
| | `rig`, `voiceSet` | string |
| class | `id`, `resource` | id, ref<resource> |
| | `baseStats`, `growthPerLevel` | {str, agi, sta, int, spi} (growth is float) |
| | `baseHealth`, `baseMana` | map<level, int> at 1, 10, 20, 30 (interpolated) |
| | `armor`, `weapons` | list<enum> |
| | `spells` | list<{spell, level, source: enum(trainer, quest, start)}> |
| | `talentTrees` | list<ref<talentTree>> (exactly 3) |
| | `colour` | string |

```yaml
id: class.fighter
resource: resource.rage
baseStats: { str: 3, agi: 0, sta: 2, int: 0, spi: 0 }
growthPerLevel: { str: 1.35, agi: 0.8, sta: 1.2, int: 0.15, spi: 0.4 }
baseHealth: { 1: 60, 10: 200, 20: 430, 30: 690 }
armor: [cloth, leather, mail, shield]
weapons: [sword1h, axe1h, mace1h, dagger, sword2h, axe2h, mace2h, staff, bow, crossbow, gun, thrown]
spells:
  - { spell: spell.fighter.strike.r1, level: 1, source: start }
  - { spell: spell.fighter.rend.r1, level: 4, source: trainer }
talentTrees: [talents.fighter.bulwark, talents.fighter.reaver, talents.fighter.greatarms]
```

### 2.4 Spell, effect and aura

| Field | Type | Notes |
|---|---|---|
| `id` | id | `spell.<owner>.<name>.r<rank>` |
| `rank`, `learnLevel` | int | |
| `trainCost` | money | Omitted for quest and start spells |
| `school` | enum(physical, holy, nature, arcane, fire, frost, shadow) | |
| `cost` | {resource, amount} or {resource, percentBase} | `amount` may be `all` |
| `castTime` | duration | 0 for instant |
| `channel` | {duration, tickEvery} | Optional |
| `cooldown` | duration | |
| `gcd` | bool | Default true |
| `range` | {min, max} in yards, or `melee`, `self` | |
| `target` | enum(self, enemy, friend, friendDead, groundArea, cone, party, none) | |
| `requires` | {stance, weaponType, shield, targetHealthBelow, targetType, outOfCombat, afterEvent} | All optional |
| `nextSwing` | bool | Replaces the next auto-attack |
| `effects` | list<effect> | Applied in order |
| `threat` | {flat, perDamage, perHeal} | Optional override |
| `visual`, `icon` | string | Art ids from the [art lists](../10-art/00-art-master-todo.md) |

Effect fields: `type`, `amount` ({min, max} or formula), `coefficient` (float), `school` (defaults to the spell's), `target` (defaults to the spell's), `radius`, `maxTargets`, `aura` (ref or inline), `chance`.

Effect types (complete list for launch): `damage` · `weaponDamage` (percent + bonus) · `heal` · `applyAura` · `removeAura` · `dispel` (magic, curse, disease, poison; count) · `interrupt` (lockout duration) · `taunt` · `threat` · `energize` (grant resource) · `drainResource` · `resurrect` · `summon` · `teleport` · `charge` · `knockback` · `pull` · `instakill` · `createItem` · `learnSpell` · `openLock` · `script` (named hook).

Aura fields: `id`, `duration`, `maxStacks`, `dispelType`, `exclusiveGroup`, `breakOnDamage`, `tickEvery`, `effects` (list of aura effects).

Aura effect types (complete list for launch): `periodicDamage` · `periodicHeal` · `periodicEnergize` · `modStat` · `modAttackPower` · `modSpellPower` · `modHealingPower` · `modArmor` · `modResist` · `modDamageDonePercent` · `modDamageTakenPercent` · `modHealingReceivedPercent` · `modAttackSpeedPercent` · `modCastSpeedPercent` · `modMoveSpeedPercent` · `modCritPercent` · `modHitPercent` · `modDodgePercent` · `modBlockPercent` · `modThreatPercent` · `modCostPercent` · `stun` · `root` · `fear` · `sleep` · `incapacitate` · `silence` · `disarm` · `charm` · `immuneSchool` · `immuneMechanic` · `absorb` · `reflect` · `procOnHit` · `procOnHitTaken` · `procOnCast` · `procOnCrit` · `procOnBlock` · `onSwingBonusDamage` · `shapeshift` · `stance` · `tracking` · `stealth` · `detectStealth` · `partyAura` · `forceAttacker` · `cannotFlee` · `noRegen` · `script`.

```yaml
id: spell.fighter.rend.r2
rank: 2
learnLevel: 10
trainCost: 8s
school: physical
cost: { resource: resource.rage, amount: 10 }
castTime: 0ms
gcd: true
range: melee
target: enemy
requires: { stance: [battle, guard] }
effects:
  - type: applyAura
    aura:
      id: aura.fighter.rend.r2
      duration: 10s
      tickEvery: 2s
      dispelType: none
      effects:
        - { type: periodicDamage, total: 34, school: physical, bleed: true }
icon: ico_abi_fighter_rend
visual: vfx_f_rend
```

### 2.5 Talent tree and talent

| Field | Type |
|---|---|
| `id`, `class`, `name`, `role` | id, ref<class>, string key, enum(tank, healer, damage) |
| `talents` | list<{id, tier (1–7), column (1–4), maxRank, requires: ref<talent>, ranks: list<ref<spell>>}> |

```yaml
id: talents.fighter.bulwark
class: class.fighter
role: tank
talents:
  - { id: talent.fighter.bulwark.shield_specialization, tier: 1, column: 2, maxRank: 5,
      ranks: [spell.talent.fig.shieldspec.r1, spell.talent.fig.shieldspec.r2, spell.talent.fig.shieldspec.r3,
              spell.talent.fig.shieldspec.r4, spell.talent.fig.shieldspec.r5] }
```

### 2.6 Item, item set, random suffix

| Field | Type | Notes |
|---|---|---|
| `id` | id | |
| `quality` | enum(poor, common, uncommon, rare, epic, legendary) | |
| `slot` | enum(head, neck, shoulders, back, chest, shirt, tabard, wrist, hands, waist, legs, feet, ring, trinket, mainHand, offHand, oneHand, twoHand, ranged, relic, bag, ammo, none) | |
| `type` | enum(cloth, leather, mail, shield, sword1h, …, consumable, reagent, tradeGood, recipe, quest, key, junk, container, tool, mount) | |
| `ilvl`, `requiredLevel` | int | `requiredLevel` defaults to `ilvl − 5` for greens, `− 8` blues, `− 12` epics, minimum 1 |
| `stats` | map<stat, int> | str, agi, sta, int, spi, attackPower, spellPower, healingPower, critPercent, hitPercent, defense, blockValue, mp5, resistances |
| `weapon` | {speed, dps: optional} | DPS derived from `ilvl`, quality and type if omitted |
| `armor` | int, optional | Derived from `ilvl`, type and slot if omitted |
| `binding` | enum(none, pickup, equip, use, quest) | |
| `unique` | int, optional | Maximum carried |
| `durability` | int, optional | Derived by slot and quality if omitted |
| `stack` | int | Default 1 |
| `sellPrice`, `buyPrice` | money | `sellPrice` derived from `ilvl`, slot and quality if omitted |
| `spells` | list<{trigger: enum(use, equip, onHit), spell, chance, cooldown}> | |
| `requires` | {class, skill, skillLevel, reputation, standing} | |
| `set` | ref<itemset> | |
| `suffixGroup` | ref<suffixGroup> | For random-suffix bases |
| `bagSlots` | int | Containers |
| `startsQuest` | ref<quest> | |
| `appearance` | {set, colourway} or {model} | From the art lists; colourway assigned by rule if omitted |
| `icon` | string | |

```yaml
id: item.quest.tm36.brandbreaker
quality: rare
slot: twoHand
type: sword2h
ilvl: 28
stats: { str: 18, sta: 25 }
weapon: { speed: 3.5 }
binding: pickup
appearance: { model: wpn_brandbreaker }
icon: ico_itm_brandbreaker
```

Item set: `id`, `items` (list), `bonuses` (list<{pieces, spell}>). Suffix group: `id`, `suffixes` (list<{name key, stats as budget shares, weight}>).

### 2.7 Creature and loot table

| Field | Type | Notes |
|---|---|---|
| `id` | id | |
| `level` | range | |
| `type` | enum(beast, humanoid, undead, elemental, construct, dragonkin, giant, plant, aberration, critter) | |
| `family` | string | Social group and skinning family |
| `rank` | enum(normal, named, rare, miniBoss, elite, rareElite, groupElite, groupBoss, dungeonTrash, dungeonBoss, raidBoss, worldBoss) | |
| `caster` | bool | Applies the caster template |
| `template` | {healthMult, damageMult, armorMult} | Defaults from rank; explicit values override |
| `health`, `damage`, `armor`, `mana` | int / {min, max} | Optional hard overrides (bosses) |
| `swing` | duration | Default by type |
| `reaction` | enum(hostile, neutral, friendly) or ref<allegiance> | |
| `resist`, `immune` | map<school, int> / list | |
| `spells` | list<{spell, priority, cooldown, initialDelay, condition}> | Conditions: `healthBelow`, `targetCasting`, `enemiesInRange`, `allyHealthBelow`, `onEngage`, `onDeath` |
| `ai` | enum(melee, caster, ranged, kiter, stationary, script:<name>) | |
| `flees` | bool | Default true for humanoids |
| `social` | bool | Assists same family within 10 yards |
| `movement` | enum(ground, swim, fly, burrow, none) | |
| `aggroRadiusMod` | int | Yards added to the standard radius |
| `loot` | ref<lootTable> | |
| `gather` | {skinning, mining, herbalism: ref<lootTable>} | |
| `xpMult` | float | Default by rank |
| `respawn` | duration or {min, max} | |
| `model`, `soundSet` | string | |

Loot table: `id`, `coin` ({min, max, chance}), `groups` (list). Each group: `chance` (percent that the group rolls), `pick` (how many entries, default 1), `entries` (list<{item or table, weight, count: {min, max}, condition}>). Conditions: `onQuest: <id>`, `hasSkill: <id>`, `firstKillOnly`.

```yaml
id: creature.hf.cinderstuffed_scarecrow
level: { min: 7, max: 8 }
type: construct
family: scarecrow
rank: normal
resist: { fire: -50 }
spells:
  - { spell: spell.creature.flail_two_targets, priority: 1, cooldown: 12s }
ai: melee
loot: loot.hf.cinderstuffed_scarecrow
respawn: 5m
model: cre_scarecrow_cinder
---
id: loot.hf.cinderstuffed_scarecrow
groups:
  - { chance: 65, entries: [ { table: loot.junk.construct } ] }
  - { chance: 70, entries: [ { item: item.questitem.hf09.cinder_heart, condition: { onQuest: quest.hf.09 } } ] }
  - { chance: 100, entries: [ { table: loot.world.level_7_8 } ] }
```

### 2.8 NPC, vendor stock, trainer list

| Record | Field | Type |
|---|---|---|
| npc | `id`, `role` (string key), `zone`, `position`, `facing` | |
| | `services` | list<enum(vendor, repair, trainer, innkeeper, flightMaster, banker, guildBank, auctioneer, mailbox, stable, ridingTrainer, weaponMaster, battlemaster, guildMaster, tabardVendor, barber, spiritHealer, quartermaster)> |
| | `stock` | list<ref<stockList>> plus `extra` (list<{item, price, limited: {count, restock}, condition}>) |
| | `trains` | list<ref<trainerList>> |
| | `greeting` | string key |
| | `gossip` | list<{text key, action, condition}> |
| | `moves` | list<{position, condition}> (for NPCs that relocate by quest state) |
| | `count`, `namePool`, `patrol` | For generic groups |
| | `appearance` | {rig, outfit} |
| stockList | `id`, `items` (list<{item, price, limited}>), `tierByHub` | |
| trainerList | `id`, `kind` (class, profession, weapon, riding), `class` or `profession`, `maxRank` | Contents come from the class or recipe records |

Quests are not listed on the NPC; the quest record names its giver and ender.

```yaml
id: npc.bm.05
role: role.quartermaster
zone: zone.brightmead
position: [412.0, 31.5, 880.2]
services: [vendor, repair]
stock: [stock.general, stock.food.t1, stock.armor.a, stock.weapon.a]
greeting: npc.bm.05.greeting
appearance: { rig: human_m, outfit: npc_quartermaster_a }
```

### 2.9 Quest

| Field | Type | Notes |
|---|---|---|
| `id`, `level`, `minLevel` | id, int, int | `minLevel` defaults to `level − 3` |
| `tag` | enum(normal, elite, dungeon, raid, class, breadcrumb) | |
| `chain` | enum(none, mc1, mc2) | |
| `giver`, `ender` | ref<npc> or {object} or {item}; `ender` may be a list (any of) | |
| `requires` | {all: [...], any: [...], level, class, reputation} | |
| `exclusiveGroup` | string | A or B variants |
| `objectives` | list<objective> | |
| `grantsOnAccept` | list<{item, count}> | |
| `xp` | int | The exact value from the quest text |
| `coin` | money | |
| `rewards` | {fixed: [...], choice: [...], spells: [...], title, reputation: map, unlocks: [...]} | Class-variant rewards use `{item, class}` |
| `next` | ref<quest> | |
| `raidAllowed` | bool | Default false |
| `timer` | duration | Optional |
| `script` | string | Named hook for escorts and events |

Objective types: `kill` {creatures, count} · `collect` {item, count} · `interact` {object, count} · `useItem` {item, on: object or creature or area} · `explore` {area} · `talk` {npc, gossipOption} · `escort` {npc, to} · `defend` {target, waves or duration} · `deliver` {item, to} · `castOn` {spell, creature, count} · `subdue` {creatures, count, atHealthPercent} · `event` {name}.

Texts are in `strings/en/quests_<zone>.yaml` under `<id>.title`, `.offer`, `.progress`, `.complete`, and `.objective.<n>`.

```yaml
id: quest.bm.07
level: 3
tag: normal
chain: mc1
giver: npc.bm.01
ender: npc.bm.01
requires: { all: [quest.bm.04] }
objectives:
  - { type: interact, object: object.bm.grain_sack, count: 6 }
xp: 200
coin: 1s
rewards:
  choice: [item.quest.bm07.arming_sword, item.quest.bm07.shrine_mace, item.quest.bm07.walking_staff]
```

### 2.10 Zone, sub-area, spawn, world object, node

| Record | Fields |
|---|---|
| zone | `id`, `continent`, `level` (range), `pvpTag` (sanctuary, territory:<allegiance>, contested, freeForAll), `weather` (list<{state, weight}>), `music`, `ambience`, `sizeMetres`, `scene` (Godot scene path), `interior` (bool), `dayNight` (bool), `terrain` (paths to `height.r16`, `weights.png` and the built `holes.png`) |
| cutout | `id`, `shape` (box, circle or polygon of terrain to remove), `depth`, `frame` (kit piece covering the rim), `interior` (scene or none), `link` (instance or zone it leads to), `floor`, `purpose`. Specified in full in [Terrain and Cutouts](terrain-and-cutouts.md). **This is how holes are cut in the map to place caves and dungeons** |
| subarea | `id`, `zone`, `level` (range), `volume` (polygon + height range), `music`, `restArea` (bool), `explorationXp` (derived), `graveyard` (ref) |
| graveyard | `id`, `zone`, `position`, `spiritHealer` |
| spawn | `id`, `zone`, `position` or `area` (radius), `creature` or `pool` (list<{creature, weight}>), `count`, `respawn`, `patrol` (list of points) or `wander` (radius), `time` (day, night, any), `group` (spawns that link as a pack) |
| object | `id`, `type` (chest, questObject, door, lever, mailbox, forge, anvil, campfire, book, signpost, meetingStone, fishingPool, transport), `position`, `channel` (duration), `respawn`, `perPlayer` (bool), `loot`, `requires` {quest, skill, key}, `states` (list), `script` |
| node | `id`, `kind` (mining, herb), `resource` (ref<item>), `skill`, `positions` (list), `activeShare` (percent populated), `respawn`, `rareReplacement` {node, chance} |

```yaml
records:
  - { id: spawn.bm.pasture_pups, zone: zone.brightmead, area: { centre: [430, 30, 905], radius: 45 },
      creature: creature.bm.vale_wolf_pup, count: 10, respawn: 150s, wander: 12 }
  - { id: spawn.bm.old_greymaw, zone: zone.brightmead, position: [612, 44, 1203],
      creature: creature.bm.old_greymaw, count: 1, respawn: 7m, patrol: [[612,44,1203],[640,45,1230],[598,43,1241]] }
```

### 2.11 Instance, encounter, battleground

| Record | Fields |
|---|---|
| instance | `id`, `type` (dungeon, raid, battleground, arena), `size`, `level` (range), `entrance` {zone, position}, `scene`, `lockout` (none, hourlyCap:5, weekly), `reset`, `packs` (list<{room, members, patrol}>), `encounters` (list<ref>) |
| encounter | `id`, `boss` (ref<creature> or list), `health`, `phases` (list<{at: healthPercent or time, name}>), `timeline` (list<{phase, every or at, spell, target rule}>), `adds`, `objects`, `enrage` {at, effect}, `loot` {picks, table, extras} |
| battleground | `id`, `scene`, `teams` (list<{id, colour, base}>), `teamSize` {min, max}, `brackets`, `assignment` (randomBalanced, byAllegiance), `objectives`, `scoring` (map<event, points>), `winScore`, `timeLimit`, `rewards` |

```yaml
id: encounter.gallowmere.holt
boss: creature.gallowmere.gravedigger_holt
health: 13500
phases: [ { at: 100, name: main } ]
timeline:
  - { phase: main, every: 9s, spell: spell.boss.holt.shovel_sweep, target: currentTank }
  - { phase: main, every: 20s, spell: spell.boss.holt.dig_up }
  - { phase: main, at: { healthPercent: 50 }, spell: spell.boss.holt.six_feet_under, target: randomNonTank }
enrage: { at: 8m, effect: spell.boss.enrage }
loot: { picks: 2, table: loot.gallowmere.holt }
```

### 2.12 Profession and recipe

| Record | Fields |
|---|---|
| profession | `id`, `kind` (gathering, crafting, secondary), `ranks` (list<{name, maxSkill, requiredLevel, cost}>) |
| recipe | `id`, `profession`, `skill`, `thresholds` {yellow, green, grey} (defaults: skill + 25, + 50, + 75), `reagents` (list<{item, count}>), `tool`, `station` (forge, anvil, fire, none), `output` {item, count}, `source` (trainer, vendor, drop, reputation, quest), `trainCost` |

```yaml
id: recipe.blacksmithing.copper_chain_belt
profession: profession.blacksmithing
skill: 35
reagents: [ { item: item.bar.copper, count: 6 } ]
tool: item.tool.blacksmith_hammer
station: anvil
output: { item: item.crafted.copper_chain_belt, count: 1 }
source: trainer
trainCost: 1s
```

### 2.13 Travel

`eyries.yaml`: list<{id, zone, position, npc, requires}>. `routes.yaml`: list<{a, b, fare, duration, path}>. `ship.yaml`: {stops, period, crossing, path}.

### 2.14 Strings

```yaml
quest.bm.07.title: "The Stolen Seed-Grain"
quest.bm.07.offer: "Hobb's candles are one thing. This is another. ..."
quest.bm.07.objective.1: "Grain Sacks recovered"
npc.bm.05.greeting: "Everything's counted, so don't think I won't notice."
```

Tokens in strings: `<name>`, `<class>`. The validator rejects `<race>`.

## 3. Where each planning document goes

| Planning document | Content folder | How |
|---|---|---|
| [creatures.md](../12-data/creatures.md) | `creatures/`, `loot/`, `spells/creature/` | `content import creatures` |
| [spells.md](../12-data/spells.md) and the class talent tables | `spells/<class>/`, `talents/` | `content import spells`; effects are then written by hand per ability |
| [Quest text files](../06-quests/text/00-quest-text-index.md) | `quests/`, `strings/en/quests_*.yaml`, `items/quest/` | `content import quests` |
| [NPC rosters](../11-npcs/00-npc-index.md) | `npcs/`, `vendors/`, `trainers/` | `content import npcs`; positions added in the zone editor |
| [Named Item Index](../10-art/07-named-item-index.md) | `items/` | `content import items` |
| [encounters.md](../12-data/encounters.md) | `instances/`, `encounters/` | By hand |
| [reference-tables.md](../12-data/reference-tables.md) | `travel/`, `reputations/`, `items/pvp/`, `loot/world/` | By hand |
| Crafting and gathering documents | `professions/`, `recipes/` | `content import recipes` |

Positions, patrol paths and sub-area volumes come from the [World Layout](../13-world/00-world-layout.md) tables and are placed by the world generator under the rules in [World Construction](../13-world/10-world-construction.md). The zone editor is for inspecting the result and recording fixes as overrides.

## 4. Validation rules

`content validate` fails the build on any of these.

| # | Rule |
|---|---|
| V01 | Every `ref<>` resolves to an existing record of the right type |
| V02 | Ids are unique and match the naming pattern for their type |
| V03 | Every record has every required field; no unknown fields |
| V04 | Every string key used has an English string; no string contains `<race>` |
| V05 | No quest other than `tag: class` sets a class filter; **no quest sets a race filter** |
| V06 | Every quest's giver and ender exist; every prerequisite exists; the prerequisite graph has no cycles |
| V07 | Every quest is reachable: some path of prerequisites leads to it from quests with none |
| V08 | Exclusive groups: every member shares the same `next` |
| V09 | Quest XP equals the standard table value times an allowed multiplier for its tag (tolerance 2%) |
| V10 | Every `collect` objective's item has a source: a loot entry conditioned on that quest, an object, or a vendor |
| V11 | Every `kill` objective's creature has at least one spawn, with count × 1.5 ≥ the objective count |
| V12 | Item stats are within 10% of the budget for ilvl, slot and quality; trinkets are exempt |
| V13 | Every "choose 1" quest reward set has an option usable by each of the three classes |
| V14 | Creature level range lies within its zone's range ± 3, except instance and world-boss creatures |
| V15 | Every spell's rank chain has strictly rising `learnLevel`; rank 1 exists |
| V16 | Every talent tree has 7 tiers; prerequisites point to a lower tier; rank spell count equals `maxRank` |
| V17 | Loot group chances are 0–100; weights are positive; no table references itself |
| V18 | Every recipe's reagents and output exist; `skill` ≤ the profession's maximum rank |
| V19 | Every vendor item has a price; limited stock has a restock time |
| V20 | Every zone has at least one graveyard; every sub-area lies inside its zone |
| V21 | Every eyrie is reachable from its continent's capital by routes |
| V22 | Every encounter's spells exist; phase triggers descend; loot picks ≤ table size |
| V23 | Every reaction pair is defined for every pair of allegiances |
| V24 | Every item, spell and creature names an icon or model that exists in `client/assets` (warning until the art block for that milestone is due, then an error) |
| V25 | No literal display text appears in any non-string file |
| V26 | Every terrain cutout has a frame covering its rim, a walkable path through it, an interior that stays inside its volume, and does not swallow a road, camp, hub or graveyard; every instance entrance lies inside a cutout or a building ([Terrain and Cutouts §6](terrain-and-cutouts.md#6-validation)) |
| V27 | Every generated zone and instance passes the construction checks: reachability, road gradient, exact counts, slopes, spawn safety distances, seams, no stuck spots ([World Construction §10](../13-world/10-world-construction.md#10-checks)) |
| V28 | Every item record has stats, armor or damage, vendor value, durability and required level that agree with [Item Rules](../12-data/item-rules.md), unless its source document states the value explicitly |
| V29 | Every string id used by code or content exists in the string table, and no string in the table is unused ([Game Text](../12-data/game-text.md)) |
| V30 | Every objective of every quest resolves, through the objective locator, to at least one position reachable from the quest giver ([Bots and Testing §3](bots-and-testing.md#3-how-the-quester-plays)) |
| V31 | Every `model`, `visual`, `icon`, `soundSet` and `music` field names an asset id in the asset manifest, chosen by [Presentation Rules](../12-data/presentation-rules.md) |

The validator also writes three reports to `build/reports/`: XP available per zone against XP needed, coin entering and leaving per level, and stat budget outliers.
