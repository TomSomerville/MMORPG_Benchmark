# Data Model & Extensibility

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Architecture](architecture.md) · Next: [Roadmap](roadmap.md)

Every game concept is a **content record** with a stable string id. This page lists the records and their fields, and shows how the "add it later" requirements (more factions, races, classes) are met by data alone.

## 1. Static content records

| Record | Key fields | Defined in design doc |
|---|---|---|
| **Allegiance** | id, name, colour, races[], capitals[], language, start reputations, graveyard set | [Factions & Races](../01-world/factions-and-races.md) |
| **ReactionMatrix** | allegiance A × allegiance B → Friendly / Neutral / Hostile; optional per-zone overrides | same |
| **ReputationFaction** | id, name, standing thresholds, at-war flag, rewards by standing | same |
| **Race** | id, allegiance, base stats, allowed classes[], racial spells[], start zone + position, start items, model set, languages | same |
| **Class** | id, resource type, base stats + growth curve, proficiencies[], spell list (spell, level, cost), talent trees[3], class quests, colour | [Class Framework](../03-classes/class-framework.md) |
| **Resource** | id (rage, mana, energy…), max, regen rule, decay rule, gain events | [Combat](../02-systems/combat-and-stats.md) |
| **Spell** | id, name, rank, school, cost, cast time, cooldown, GCD flag, range, targeting, requirements (stance, weapon, target state), effects[], visuals, tooltip template | class files |
| **SpellEffect** | type (damage, heal, apply-aura, dispel, interrupt, summon, taunt, resurrect, teleport, energize, …), formula, coefficient, target filter | [Architecture §4](architecture.md#4-simulation) |
| **Aura** | type (periodic damage/heal, stat mod, speed mod, control, absorb, proc trigger, shapeshift, …), duration, stacks, dispel type, exclusivity group | same |
| **TalentTree / Talent** | tree id, tier, column, max rank, prerequisite, spell id per rank | class files |
| **Item** | id, name, quality, slot, type, ilvl, required level/class/skill/reputation, stats[], weapon damage/speed, armor, binding, durability, stack, vendor price, use/equip/proc spells, set id, random-suffix group | [Items & Loot](../02-systems/items-and-loot.md) |
| **ItemSet** | id, items[], bonuses by piece count (spell ids) | raid doc |
| **Creature** | id, name, level range, family, type, rank, reaction, stat template + multipliers, spells[] + AI priorities, loot table, gather table, movement type, model | zone files |
| **LootTable** | groups[] of weighted entries (item or sub-table), conditions (on quest, has profession) | Items & Loot |
| **Quest** | id, title, level, min level, tag, giver, ender, prerequisites (all/any), exclusive group, allegiance/class filter (default any), objectives[], texts, XP tag, coin, rewards, reputation, next quest | zone files |
| **Zone / SubArea** | id, continent, level range, PvP tag, weather set, music, graveyards, exploration XP | [World & Travel](../01-world/world-and-travel.md) |
| **Spawn** | position, creature or pool, respawn rule, patrol path, day/night flag | zone files |
| **WorldObject** | type (chest, node, door, quest object, mailbox, …), required skill, loot table, script | [NPC AI & World](../02-systems/npc-ai-and-world.md) |
| **Profession / Recipe** | skill line, rank caps; recipe: required skill, colour thresholds, reagents[], tool/station, output | profession files |
| **Vendor / Trainer** | NPC id → item list / spell list with prices and requirements | zone files |
| **FlightNode / Route** | node id, position, allegiance, connections + fares; ship routes + schedules | World & Travel |
| **Instance** | map, type (dungeon/raid/battleground/arena), size, lockout rule, encounters[] | instance docs |
| **Encounter** | boss creature, phases, timeline of abilities, adds, objects, enrage | instance docs |
| **Battleground** | map, teams[] (count is data — 2, **3**, or more), objectives, scoring rules, brackets | [PvP](../02-systems/pvp.md) |

## 2. Persistent (database) records

| Table group | Contents |
|---|---|
| Account | login, security, bans, settings |
| Character | name, race, class, sex, appearance, level, XP, rested XP, position, bind point, money, played time, allegiance, respec price and its last-decay date, epic-mount Fed clock |
| Character state | health/resource on logout, auras with remaining time, cooldowns |
| Inventory | item instances: content id, owner, bag/slot, stack, durability, enchant, suffix, creator, bind state |
| Progress | known spells, talents, skills (profession + weapon), recipes, reputations, explored areas, flight nodes, titles |
| Quests | active objectives progress, completed set |
| Social | friends, ignores, mail + attachments |
| Guild | guild, ranks, per-rank permissions, members and notes, event log |
| Guild bank | tabs (name, icon, note), slots → item instances, guild money, per-rank per-tab view/deposit/withdraw limits, daily usage counters, item log and money log |
| Economy | auctions, bids, transaction log |
| Instances | saved instance ids, boss kills, reset times |
| World | world-boss timers, rare timers, chest state |

## 3. How each "designed to grow" requirement is satisfied

| Requirement | Mechanism | What must be added later |
|---|---|---|
| 1 faction now → 2, 3 or more | `Allegiance` records + `ReactionMatrix`; every hostility/grouping/chat/AH/guard check goes through one function that reads them. Battleground team count is data | New allegiance records, matrix rows, capitals, start zones, per-allegiance flight/graveyard/vendor sets |
| 2 races now → elf, gnome, ogre, undead… | `Race` record; character art keyed by skeleton | Race record, racials (spells), model + animations, optional start zone |
| 3 classes now → warlock, rogue, archer… | `Class` record + spells + talents; resources and mechanics are reusable effect/aura types | Class record, spells, talents; new mechanic types once (pets, stealth, combo points, ranged auto-attack) |
| Level cap 30 → 60 | XP table, stat curves, spell ranks and talent tiers already defined to 60 | Content (zones, items, ranks); flip the cap |
| No race-locked quests | Quest filters default to "any"; the validator fails the build if any non-class quest sets a race filter | — |
| Two-continent parallel chain | Quest `exclusive group` + `prerequisites: any` | — |
| 3-team battleground now, faction teams later | Team assignment rule is data: `random-balanced` now, `by-allegiance` later | Change one field |
| Future PvP zones | Zone PvP tag: Sanctuary / Territory(x) / Contested / Free-for-all | Tag new zones |

## 4. Id and naming conventions

- Ids are lowercase, dotted by type: `spell.fighter.rend.r2`, `item.brandbreaker`, `quest.tm.36`, `creature.thornwick.cinderwight`, `zone.veilmoor`.
- Quest ids match the `ZONE-NN` codes in the zone files.
- Display names live in string tables, never in logic.
- Every record carries `since` (content version) to support patch notes and migrations.

## 5. Formula ownership

Numbers that are *rules* (XP curve, armor formula, rage conversion, item budgets) live in one "constants" content file referenced by the rules library, so balance changes are data patches, not code changes.
