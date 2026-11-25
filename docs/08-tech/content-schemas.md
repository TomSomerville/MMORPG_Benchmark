# Content Schemas

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Repository Layout](repo-and-conventions.md) · Next: [Database Schema](database-schema.md) · Records overview: [Data Model](data-model.md)

The exact shape of every YAML file under `content/`. Each record type has its fields, their types, and one worked example taken from the design documents. The validator (§4) rejects anything that does not match.

## 1. Conventions for all files

| Rule | Detail |
|---|---|
| One record per file, or a list | A file holds either one record or `records: [...]`. Small related records (a zone's spawns) share a file |
| Ids | Lowercase letters, digits and underscores, in dotted parts (no hyphens): `<type>.<scope>.<name>[.r<rank>]`. Quest ids are `quest.<zone>.<nn>`; NPC ids `npc.<zone>.<nn>`; creature ids `creature.<zone>.<name>`; a named item is `item.named.<name_with_underscores>` and a random-suffix base `item.world.l<NN>_<key>` |
| Text | No display text in records. `name`, `description` and quest texts are keys into `content/strings/en/*.yaml`; the key defaults to the id plus a suffix (`.name`, `.offer`, …) and need not be written |
| References | A field typed `ref<spell>` holds the id of a spell record. The validator checks that it exists |
| Numbers | Integers unless marked `float`. Durations in milliseconds, written with a unit suffix that the loader converts: `1500ms`, `30s`, `5m`, `2h`. Money in copper with a suffix: `25c`, `1s50c`, `2g` |
| Percentages | Written as numbers: `35` means 35% |
| Formulas | Strings in a small expression language over named inputs: `"ilvl * 0.55 + 2.5"`. Only `+ - * / ( ) min max floor round` and the inputs listed for that field |
| `since` | Content version that introduced the record. Defaults to the pack version |
| Generated records | Records written by a generator or importer (§3) live in a `generated/` folder beside the hand-written ones and are committed. They are never edited by hand: the source document or the generator is changed and the command run again, and a test holds the committed files to what the command writes |
| Positions | In a zone with terrain, positions in records are zone-local metres (x east, height, z north, from the south-west corner), as the layout documents give them. The server works in yards and converts when it loads the zone |
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
| `world` | Run, walk, backwards and swim speeds, the interest cell size, aggro radius rule, leash, respawn defaults, day length |
| `sim` | The zone tick (`tickMs`) |
| `death` | Release timer, corpse reclaim distance and health, ghost speed, the delays for repeated deaths |
| `caps` | Level cap, quest log size, buff and debuff caps, bag and bank sizes |
| `movement` | The server's movement checks (`speedTolerance`, `slackYards`, `teleportYards`, `strikesPerMinute`, `inputHz`: [Network Protocol §4.3](network-protocol.md#43-player-movement-cs-channel-1)) and the turn speed, jump, step height, steep angle and fall distances of [Rules Reference §1](../02-systems/rules-reference.md#1-movement) |
| `interaction` | Interaction ranges in yards: use, trade, inspect, follow, tab-targeting, group credit, quest sharing, nameplates, duel area; camera limits ([Rules Reference §2, §6](../02-systems/rules-reference.md#2-interaction-ranges)) |
| `timers` | Idle timers: seconds with no input until a character is marked away, seconds away until it is logged out, the battleground report timer (Rules Reference §3) |
| `hearth` | The hearthstone's cooldown and cast time |
| `skills` | Weapon and defense skill gain, profession skill-up chances, food and drink tiers ([Rules Reference §4, §5](../02-systems/rules-reference.md#4-weapon-and-defense-skill)) |
| `itemRules` | Every table in [Item Rules](../12-data/item-rules.md): stat scale, profiles, armor and price multipliers, durability, repair, base names |
| `service` | Name lengths; ticket, logout, link-lost, ping and timeout seconds; chat limits, report thresholds, penalty lengths; `service.reservedWords`, the words no character name may contain beyond the names the content reserves by rule; `service.profanity`, the word list of the name and chat filter ([Accounts and Live Service §2](accounts-and-live-service.md#2-names)) |

A section is filled in by the milestone that first needs it. The rules library carries the same values as defaults.

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
| | `start` | {zone, position, facing, bindInn}. A new character is placed at the start point of that zone's generated world (`world.json`); `position` is the same point in yards, and a test holds the two together |
| | `startItems` | list<ref<item>> by class |
| | `rig`, `voiceSet` | string |
| class | `id`, `resource` | id, ref<resource> |
| | `baseStats`, `growthPerLevel` | {str, agi, sta, int, spi} (growth is float) |
| | `baseHealth`, `baseMana` | map<level, int> at 1, 10, 20, 30 (interpolated) |
| | `armor`, `weapons` | list<enum> |
| | `spells` | list<{spell, level, source: enum(trainer, quest, start)}> |
| | `talentTrees` | list<ref<talentTree>> (exactly 3) |
| | `startingGear` | list<ref<item>>: what a new character of the class wears and carries |
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
| `cost` | {resource, amount} or {resource, percentBase} | `amount` may be `all`. With `resource: resource.health` the cost is `percentBase` percent of base health |
| `castTime` | duration | 0 for instant |
| `channel` | {duration, tickEvery} | Optional |
| `cooldown` | duration | |
| `cooldownGroup` | string | Spells that name the same group share the cooldown (`stance`: the three stances) |
| `gcd` | bool | Default true |
| `range` | {min, max} in yards, or `melee`, `self` | |
| `target` | enum(self, enemy, friend, friendDead, groundArea, cone, party, none) | |
| `requires` | {stance, weaponType, shield, targetHealthBelow, targetType, outOfCombat, afterEvent, reagent, targetWithoutAura, casterAuraGroup} | All optional. `reagent`: an item that must be carried. `targetWithoutAura`: an aura family the target (the caster, where there is no target) must not hold. `casterAuraGroup`: an exclusive group of which the caster must hold an aura |
| `nextSwing` | bool | Replaces the next auto-attack |
| `entersCombat` | bool | Casting it puts the caster in combat even when it harms nobody |
| `passive` | bool | Never cast: its effects hold while it is known (talent ranks) |
| `effects` | list<effect> | Applied in order |
| `threat` | {flat, perDamage, perHeal} | Optional override |
| `visual`, `icon` | string | Art ids from the [art lists](../10-art/00-art-master-todo.md) |

Effect fields: `type`, `amount` ({min, max}, a number, a formula, or the name of a source: `casterMaxHealth` or `targetMaxHealth`, taken at `percent` percent), `coefficient` (float), `school` (defaults to the spell's), `target` (defaults to the spell's), `radius`, `maxTargets`, `aura` (ref or inline), `chance`. By type: `weaponDamage` takes `percent` and `bonus`; `interrupt` takes `lockout`; `dispel` takes `types` and `count`; `energize` and `drainResource` take `resource`; `removeAura` takes `family`; `summon` takes `creature` and `count`; `script` takes the hook's name in `script` and, for the two built-in hooks below, `group`.

Effect types (complete list for launch): `damage` · `weaponDamage` (percent + bonus) · `heal` · `applyAura` · `removeAura` · `dispel` (magic, curse, disease, poison; count) · `interrupt` (lockout duration) · `taunt` · `threat` · `energize` (grant resource) · `drainResource` · `resurrect` · `summon` · `teleport` · `charge` · `knockback` · `pull` · `instakill` · `createItem` · `learnSpell` · `openLock` · `script` (named hook).

Built-in `script` hooks: `consumeAura` removes the caster's aura of the exclusive group named in `group` and applies that aura's `onConsume` effects to the target; `refreshAuras` restarts the full duration of every aura of that group the caster has on the target.

Aura fields: `id`, `duration`, `maxStacks`, `dispelType`, `family` (auras of one family do not stack and a higher rank replaces a lower; defaults to the id without its rank), `exclusiveGroup` (auras of one group replace each other, per caster), `exclusivePerTarget` (bool: the group allows one aura on the target whoever cast it), `breakOnDamage`, `breakChance` (percent chance that a damaging hit breaks an aura that breaks on damage; default 100), `onConsume` (list of effects applied when a `consumeAura` effect uses the aura up), `harmful` (bool; defaults from the effect that applies it), `tickEvery`, `effects` (list of aura effects), `icon`, `visual`.

An aura written inline in a spell's effect is a record of type `aura` like one in a file of its own: it has an id and a handle, so the protocol can name it.

Aura effect fields: `type`, `amount`, `total` (a periodic effect may give its total over the full duration in place of a per-tick amount; each tick carries its fraction forward so the ticks sum to the total exactly), `school`, `stat`, `coefficient`, `resource`.

Aura effect types (complete list for launch): `periodicDamage` · `periodicHeal` · `periodicEnergize` · `modStat` · `modAttackPower` · `modSpellPower` · `modHealingPower` · `modArmor` · `modResist` · `modDamageDonePercent` · `modDamageTakenPercent` · `modHealingReceivedPercent` · `modAttackSpeedPercent` · `modCastSpeedPercent` · `modMoveSpeedPercent` · `modCritPercent` · `modHitPercent` · `modDodgePercent` · `modBlockPercent` · `modThreatPercent` · `modCostPercent` · `stun` · `root` · `fear` · `sleep` · `incapacitate` · `silence` · `disarm` · `charm` · `immuneSchool` · `immuneMechanic` · `absorb` · `reflect` · `procOnHit` · `procOnHitTaken` · `procOnCast` · `procOnCrit` · `procOnBlock` · `onSwingBonusDamage` · `shapeshift` · `stance` · `tracking` · `stealth` · `detectStealth` · `partyAura` · `forceAttacker` · `cannotFlee` · `noRegen` · `script` · `pacify` (cannot attack or use harmful abilities) · `modDamageTakenFlat` (a fixed amount added to each hit of a school the holder takes) · `modAllStatsPercent` (a percentage of every attribute the unit has of its own; health, mana, attack power, armor, dodge and crit follow).

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
| `index` | string | The item's number in the [Named Item Index](../10-art/07-named-item-index.md) (`ITM-nnn`), on generated records |
| `stated` | list<string> | The fields the item's source document states outright (`ilvl`, `requiredLevel`, `stats`, `blockValue`, `speed`, `dps`, `damage`, `armor`, `sellPrice`, `durability`). Rule V28 lets a stated value stand and recomputes every other number |
| `notes` | string | Description text from the source that names an effect not yet built (a proc, a use). Not shown to players |

`weapon` also carries `min` and `max`, the damage of one swing, written by the item generator from the DPS and the speed.

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

Item set: `id`, `items` (list), `bonuses` (list<{pieces, spell}>). Suffix: `id`, `stats` (map<stat, float>: each stat's share of the base item's budget). Suffix group: `id`, `suffixes` (list<{suffix, weight}>). A random-suffix item is a base item record plus a suffix chosen when it drops; the suffix is stored on the item instance and its stats are worked out from the base item's budget, so no item-times-suffix records exist.

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
| `spells` | list<{spell, priority, cooldown, initialDelay, condition}> | Conditions: `healthBelow`, `targetCasting`, `enemiesInRange`, `allyHealthBelow`, `onEngage`, `onDeath`, and `once` (used once in a fight; the mark clears when the creature next engages) |
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
| `skin` | string | The skin asset drawn on the model: a variety of the rig's creature; a named creature has its own |
| `scale` | float | Size against the model's own; default 1 |

Loot table: `id`, `coin` ({min, max, chance}), `groups` (list). Each group: `chance` (percent that the group rolls), `pick` (how many entries, default 1), `entries` (list<{item or table or world, weight, count: {min, max}, condition}>). An entry `world: green` rolls a random-suffix world drop for the creature's level ([Item Rules §9](../12-data/item-rules.md)). Conditions: `onQuest: <id>`, `hasSkill: <id>`, `firstKillOnly`. An `onQuest` entry is put on a corpse only if the one whose kill it is still needs it, and is shown only to a player who does.

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
| npc | `id`, `role` (string key), `zone`, `position` (or `positions`, a list, for a group that stands in several places), `facing`, `level` | |
| | `services` | list<enum(vendor, repair, trainer, innkeeper, flightMaster, banker, guildBank, auctioneer, mailbox, stable, ridingTrainer, weaponMaster, battlemaster, guildMaster, tabardVendor, barber, spiritHealer, quartermaster)> |
| | `stock` | list<ref<stockList>> plus `extra` (list<{item, price, lot, limited: {count, restock}, condition}>). `condition: { questDone: <quest> }` offers the line only to a character who has done that quest: other characters are not sent it and are refused if they ask for it |
| | `trains` | list<ref<trainerList>> |
| | `greeting` | string key |
| | `gossip` | list<{text key, action, condition}> |
| | `moves` | list<{position, condition}> (for NPCs that relocate by quest state) |
| | `count`, `namePool`, `patrol` | For generic groups |
| | `appearance` | {rig, outfit} |
| stockList | `id`, `items` (list<{item, price, lot, limited}>), `tierByHub` | A line sells a lot of `lot` items (default 1) at `price` for the lot: five loaves for 25c. With no `price` the item's `buyPrice` stands, and failing that five times its vendor value |
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
| `giver`, `ender` | ref<npc> or {object} or {item}; `ender` may be a list (any of) | An ender may be written `{npc, class}`: it ends the quest only for that class, and the mark over its head, its gossip list and the hand-in all respect it |
| `requires` | {all: [...], any: [...], level, class, reputation} | |
| `exclusiveGroup` | string | A or B variants |
| `autoAccept` | bool | Granted at character creation: a level 1 character with no quest taken or done is given it on entering the zone where its ender stands. Its giver is written as its ender, so one who abandons it can take it again |
| `objectives` | list<objective> | |
| `grantsOnAccept` | list<{item, count}> | |
| `xp` | int | The exact value from the quest text |
| `coin` | money | |
| `rewards` | {fixed: [...], choice: [...], spells: [...], title, reputation: map, unlocks: [...]} | Class-variant rewards use `{item, class}`. `unlocks` are story flags set at hand-in (`freeTraining`: the next rank bought from a trainer costs nothing) |
| `next` | ref<quest> | |
| `raidAllowed` | bool | Default false |
| `timer` | duration | Optional |
| `script` | string | Named hook for escorts and events |

Objective types: `kill` {creatures, count} · `collect` {item, count} · `interact` {object, count} · `useItem` {item, on: object or creature or area} · `explore` {area} · `talk` {npc, gossipOption} · `escort` {npc, to} · `defend` {target, waves or duration} · `deliver` {item, to} · `castOn` {spell, creature, count} · `subdue` {creatures, count, atHealthPercent} · `event` {name}.

The quest engine runs `kill`, `collect`, `interact`, `talk`, `deliver` and `explore`. The other six types are part of the schema and are built in T-M6-01; until then rule V30 rejects a quest that uses one. Objectives are not ordered: any may be done first. A `kill` objective names `creatures` (a list) or one `creature`. A `collect` count is what the character carries, up to the number asked, and what was collected is taken at hand-in. A quest whose only task is to speak to its own ender has no objectives.

Texts are in `strings/en/quests_<zone>.yaml` (for an imported zone, under `strings/en/generated/`) under `<id>.title`, `.offer`, `.progress`, `.complete`, and `.objective.<n>`. A quest with no objectives has `<id>.tracker`, the line the tracker shows in their place ("Speak to …"). A quest with more than one ender may have a completion text for each, `<id>.complete.<name>`.

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
| zone | `id`, `continent`, `level` (range), `pvpTag` (sanctuary, territory:<allegiance>, contested, freeForAll), `weather` (list<{state, weight}>), `music`, `ambience`, `sizeMetres`, `scene` (Godot scene path), `interior` (bool), `dayNight` (bool), `terrain` (paths to `height.r16`, `weights.png`, the built `holes.png` and the walk grid `nav.bin`) |
| cutout | `id`, `zone`, `shape` (box, circle or polygon of terrain to remove), `depth`, `frame` (kit piece covering the rim), `interior` (scene or none), `link` (instance or zone it leads to), `floor`, `purpose`. Specified in full in [Terrain and Cutouts](terrain-and-cutouts.md). **This is how holes are cut in the map to place caves and dungeons** |
| subarea | `id`, `zone`, `level` (range), `volume` (`{rect: {centre: [x, z], size: [w, d]}}` in zone-local metres, or a polygon with a height range), `music`, `restArea` (bool), `explorationXp` (derived: the sub-area's level × 15; written as `0` for a square that only marks a place, such as an inn's rest area or a quest's trigger, which is named on the banner and minimap, gives nothing when found, is not recorded and is not part of the map's fog), `graveyard` (ref). A character is in the smallest rectangle that holds it. A `restArea` sub-area with no volume makes its whole zone a rest area |
| graveyard | `id`, `zone`, `position`, `spiritHealer` |
| spawn | `id`, `zone`, `position`, `points` (a list) or `area` (centre and radius), `creature` or `pool` (list<{creature, weight}>), `count`, `respawn`, `patrol` (list of points) or `wander` (radius), `facing` (degrees clockwise from north), `time` (day, night, any), `group` (spawns that link as a pack). The world generator writes one spawn record for each point it places (`generated/spawns.yaml`) |
| object | `id`, `type` (chest, questObject, door, lever, mailbox, forge, anvil, campfire, book, signpost, meetingStone, fishingPool, transport), `zone`, `position` or `positions` (one entity for each), `channel` (duration: using it is a cast of that length, standing still), `respawn`, `perPlayer` (bool: used by one character, it is gone for that character only), `loot`, `requires` {quest, objective (the number of an objective of that quest, counted from 1, that must be done first), skill, key}, `states` (list), `script`, `model` |
| layout | `id`, `zone`, and the zone's layout tables transcribed from [docs/13-world](../13-world/00-world-layout.md): the world generator's input. Its entries are specified in [World Construction §1](../13-world/10-world-construction.md) |
| overrides | `id`, `zone`, `sculpt`, `paint`, `props`: the fixes made in the zone editor, which the world generator replays after its own rules ([Terrain and Cutouts §3](terrain-and-cutouts.md#3-cutouts-how-holes-are-authored)) |
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
| A zone's documents together: its rows of [creatures.md](../12-data/creatures.md), its [NPC roster](../11-npcs/00-npc-index.md), its [quest text file](../06-quests/text/00-quest-text-index.md), its zone page, and its generated world | Under each folder's `generated/`: `creatures/`, `loot/`, `spells/creature/`, `npcs/`, `quests/`, quest items, world objects, the zone's extra sub-areas, and `strings/en/generated/` | `content import zone <code>` (`bm`, `ec`, …), run after `worldgen` has built the zone |
| [spells.md](../12-data/spells.md) and the class talent tables | `spells/<class>/`, `talents/` | By hand per ability |
| [Game Text](../12-data/game-text.md) | `strings/en/generated/game-text.yaml` (`err.<Code>`, `sys.*`, `tip.<n>`, `load.<n>`, `emote.<name>.none` and `.target`, `npc.stock.<role>.<n>`) | `content import text` |
| [Named Item Index](../10-art/07-named-item-index.md) and the [Item Rules](../12-data/item-rules.md) | `items/generated/`: the named items, the white vendor armor and weapons, the random-suffix world-drop bases. Rows that cannot be parsed are listed in `items/generated/unparsed.md` with the reason | `itemgen` |
| A zone's [layout tables](../13-world/00-world-layout.md), as `zones/<zone>/layout.yaml` | The zone's terrain files, walk grid, `world.json`, `generated/*.yaml` (sub-areas, graveyards, cutouts, spawns), minimap tiles, `report.md`, and `strings/en/generated/<zone>.yaml` | `worldgen <zone>` |
| [encounters.md](../12-data/encounters.md) | `instances/`, `encounters/` | By hand |
| [reference-tables.md](../12-data/reference-tables.md) | `travel/`, `reputations/`, `items/pvp/`, `loot/world/` | By hand |
| Crafting and gathering documents | `professions/`, `recipes/` | `content import recipes` |

Positions, patrol paths and sub-area volumes come from the [World Layout](../13-world/00-world-layout.md) tables and are placed by the world generator under the rules in [World Construction](../13-world/10-world-construction.md). The zone editor is for inspecting the result and recording fixes as overrides.

What the zone importer decides, for every zone:

| Topic | Rule |
|---|---|
| Order | Zones are imported in the order they are built. A material an earlier zone's creatures already drop is written once, by the first zone, and later zones' loot tables use it |
| Creatures | One record for each kind, rare and named creature of the zone. Where a document's number differs from the rule the record carries the document's number (`xpMult`, `swing`). Abilities are written as spells by kind ([Data Index §2](../12-data/00-data-index.md#2-creature-rules)); a named creature's come from its quest's notes or the zone document's own line for it. A creature all of whose places are indoors is written `aggroRadiusMod: -8` |
| NPCs | One record for each roster row. Services come from the roster's stock and trainer codes. Places are matched by words between the roster's "Where" and the buildings, hub features and points of the generated world; several at one door stand in a row |
| Models and outfits | Asset ids are the Asset Manifest's, chosen by [Presentation Rules](../12-data/presentation-rules.md): a creature's `skin` is the skin of its own name on its row, an NPC's outfit its row's by calling |
| Quests | Objectives come from the quest's tracker line. "Speak to" or "Report to" the quest's own ender is the handing in and makes no objective (the line is kept as `<id>.tracker`). "Deliver X to Y" hands X over on accepting (`grantsOnAccept`). A quest whose text suggests more than one player is tagged `elite`. Coin is written in copper |
| Enders in zones not built yet | An ender whose zone has no records yet is placed inside the zone being imported, at the exit that leads toward its own zone; importing that zone moves it home |
| Quest places | A quest's trigger point is a 40 m square sub-area with `explorationXp: 0`. A world object a quest names is placed at the layout point of that name |

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
| V09 | Quest XP equals the standard table value for the quest's level times a multiplier in the range allowed for its tag (tolerance 2%): `breadcrumb` 0.25 to 0.5 · `normal` 0.25 to 1.25, or to 2.0 when the quest has a `chain` (a main chain's finale) · `elite` 1.5 to 2.0 · `dungeon` 2.0 to 2.5 · `raid` 3.0 · `class` 0.25 to 2.0 |
| V10 | Every `collect` objective's item has a source: a loot entry conditioned on that quest, an object, or a vendor |
| V11 | Every `kill` objective's creature has at least one spawn, with count × 1.5 ≥ the objective count |
| V12 | Item stats are within 10% of the budget for ilvl, slot and quality; trinkets are exempt |
| V13 | Every "choose 1" quest reward set has an option usable by each of the three classes |
| V14 | Creature level range lies within its zone's range ± 3, except instance and world-boss creatures |
| V15 | Every spell's rank chain has strictly rising `learnLevel`; rank 1 exists |
| V16 | Every talent tree has 7 tiers; prerequisites point to a lower tier; rank spell count equals `maxRank` |
| V17 | Loot group chances are 0–100; weights are positive; no table references itself |
| V18 | Every recipe's reagents and output exist; `skill` ≤ the profession's maximum rank |
| V19 | Every stock line resolves to a price (its own `price`, or the item's `buyPrice`, or its vendor value); a `lot` is no larger than the item's stack; limited stock has a count and a restock time; an NPC with stock has the `vendor` or `quartermaster` service |
| V20 | Every zone has at least one graveyard; every sub-area lies inside its zone |
| V21 | Every eyrie is reachable from its continent's capital by routes |
| V22 | Every encounter's spells exist; phase triggers descend; loot picks ≤ table size |
| V23 | Every reaction pair is defined for every pair of allegiances |
| V24 | Every item, spell and creature names an icon or model that exists in `client/assets` (warning until the art block for that milestone is due, then an error) |
| V25 | No literal display text appears in any non-string file |
| V26 | Every terrain cutout has a frame covering its rim, a walkable path through it (found on the zone's walk grid), an interior that stays inside its volume, and does not swallow a road, camp, hub or graveyard; every instance entrance lies inside a cutout or a building ([Terrain and Cutouts §6](terrain-and-cutouts.md#6-validation)). The interior-inside-its-volume part is enforced by the world generator, which sizes the volume from the interior it builds |
| V27 | Every generated zone and instance passes the construction checks: reachability, road gradient, exact counts, slopes, spawn safety distances, seams, no stuck spots ([World Construction §10](../13-world/10-world-construction.md#10-checks)) |
| V28 | Every equipment record (an item with an `ilvl`) has required level, stats, block value, armor, weapon speed, DPS and damage, vendor value and durability that are exactly what [Item Rules](../12-data/item-rules.md) give, except the fields listed in its `stated`, which stand as its source document wrote them. Also: equipment does not stack; Poor and Common items have no stats; a random-suffix base has no stats of its own; only a weapon has weapon numbers. Trinkets and tabards are exempt from the stat check |
| V29 | Every string id used by code or content exists in the string table, and no string in the table is unused ([Game Text](../12-data/game-text.md)). Used by code: every id the client and server source names, and `err.<Code>` for every `ResultCode`. Used by content: a `.name` for every record a player sees (item, creature, NPC, zone, object, suffix, class, race, resource, allegiance, spell by family, sub-area with a volume) and every quest's texts and objective lines. A string is unused if no code names it, no record owns it, no field holds it, and it is not a row of Game Text's own tables (kept for systems not built yet). The rule runs when `content validate` is given the game's own content beside its source; test fixtures are checked without it |
| V30 | Every objective of every quest resolves, through the objective locator, to at least one position reachable from the quest giver ([Bots and Testing §3](bots-and-testing.md#3-how-the-quester-plays)). Reachable means: in the same zone as the giver and, where the zone has terrain, joined to it by a path on the zone's walk grid. The giver and every ender must have a position in the world, and an ender in the giver's zone must be reachable from it. An objective of a type the quest engine does not run (§2.9) fails the rule |
| V31 | Every `model`, `skin`, `outfit`, `visual`, `icon`, `soundSet` and `music` value, at any depth of any record, names an asset id in the asset manifest, chosen by [Presentation Rules](../12-data/presentation-rules.md). The manifest the validator reads is the client's asset index, `client/assets/asset-index.json`, which lists every asset of the Asset Manifest, generated or still a placeholder |

The validator also writes three reports to `build/reports/`: XP available per zone against XP needed, coin entering and leaving per level, and stat budget outliers.
