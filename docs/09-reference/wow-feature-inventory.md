# Feature Inventory vs. Classic WoW

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Roadmap](../08-tech/roadmap.md)

A checklist of the capabilities of the classic-era game this project is modelled on, with what happens to each. **Launch** = in the launch scope described in these documents. **Later** = designed for, not built. **Changed** = included with a deliberate difference. **Cut** = not planned.

The list is compiled from working knowledge of the classic feature set; treat it as a checklist to challenge, not a guarantee of completeness.

## 1. Character

| Feature | Status | Notes / doc |
|---|---|---|
| Factions (2 in WoW) | **Changed** | 1 at launch, N-capable, 3 planned — [Factions](../01-world/factions-and-races.md) |
| Races (8) with racials | **Launch** (2) | Human, Dwarf; 4 more sketched |
| Classes (9) | **Launch** (3) | Fighter, Cleric, Druid; 3 more sketched |
| Class/race restrictions | **Launch** | Data-driven matrix; all open at launch |
| Character customisation | Launch | Face, skin, hair, facial hair |
| Levels 1–60 | **Changed** | Cap 30 at launch; tables to 60 |
| Primary stats, armor, resistances | Launch | [Combat](../02-systems/combat-and-stats.md) |
| Weapon skills, defense skill | Launch | Kept by decision, 2026-11-12 |
| Talent trees (3 per class, 51 pts) | Launch | 21 points at cap 30; trees designed to 31 |
| Respec with rising cost | Launch | |
| Rested XP | Launch | |
| Hearthstone / inns | Launch | |
| Mounts at 40 / epic at 60 | **Changed** | Riding at 30; epic at 60 must be fed to keep +100% speed |
| Titles | Launch (2 story titles) | Brandbreaker, Crownbreaker |
| Achievements | Cut | Not classic |
| Dual spec, transmog, heirlooms | Cut | Not classic |

## 2. Combat

| Feature | Status | Notes |
|---|---|---|
| Tab-target, auto-attack, GCD | Launch | |
| Attack table (miss/dodge/parry/block/glance/crit/crush) | Launch | |
| Spell schools, resist, partial resist | Launch | 7 schools |
| Cast time, channel, pushback, interrupts, school lockout | Launch | |
| Buffs/debuffs, dispel types | Launch | No 16-debuff cap |
| Threat and taunts | Launch | Cleric gets a taunt (change) |
| Stances / forms | Launch (stances only) | Fighter stances. Druids do not shapeshift at all |
| Rage, mana | Launch | |
| Energy, combo points, pets, stealth, ranged auto-shot, soul shards, totems | Later | With their classes |
| Crowd control + PvP diminishing returns | Launch | |
| Five-second rule, spirit regen | Launch | |
| Spell ranks and downranking | Launch | |
| Reagents | Launch | |
| Ammo | Launch (minor) | Fighter pulling only |
| Falling, drowning, fatigue | Launch | |
| Death, corpse run, spirit healer, res sickness, durability | Launch | |
| Combat log, floating combat text | Launch | |

## 3. World

| Feature | Status | Notes |
|---|---|---|
| Seamless zones on continents | Launch | 2 continents built, 11 zones; planned zones fill only half of each continent |
| Capital cities | Launch (2) | Solhaven, Hammerdeep |
| Neutral towns | Launch | Kite's Rest (a land caravan-town) |
| Flight paths | Launch | Eyries |
| Boats / zeppelins / tram | Launch | One ship: Solhaven ↔ Hammerdeep's Seagate, sailing into the mountain |
| Day/night, weather | Launch | Cosmetic weather |
| Exploration XP, fog-of-war map | Launch | |
| Graveyards | Launch | |
| Rare spawns, elites, named mobs | Launch | |
| Treasure chests | Launch | Keys from Blacksmithing until rogues exist |
| World bosses | Launch (3) | |
| Outdoor dragons / world events | Later | |
| Holidays / seasonal events | Later | |
| Swimming | Launch | Movement only |
| Underwater content / water zones | **Cut by design** | No water zones; the sea is scenery and one ship route |
| Flying mounts | Cut | |
| Phasing | **Changed** | Players are never separated from each other: there is one world with no layers or phases. Two story changes (the relit forge, the Brandspire outpost) are per-player object states, seen by each player according to their own quest progress |

## 4. Questing

| Feature | Status | Notes |
|---|---|---|
| Quest givers, log (20), sharing, abandon | Launch | |
| Kill / collect / deliver / explore / escort / use-item / defend | Launch | [NPC AI §6](../02-systems/npc-ai-and-world.md#6-quest-system-engine-view) |
| Chains, breadcrumbs, item-started quests | Launch | |
| Elite / dungeon / raid / class / profession quests | Launch | |
| Race-specific quests | **Cut by design** | None, ever, for leveling content |
| Faction-specific quests | Later | Field exists |
| Repeatable reputation turn-ins | Launch | Cloth |
| Daily quests | Later | |
| Quest map markers / arrows | Cut | Classic style: read the text |
| Attunements | Launch | Raid: the Vault Key |

## 5. Items & economy

| Feature | Status | Notes |
|---|---|---|
| Quality tiers, binding, durability, sets | Launch | |
| Random-suffix greens | **Changed** | Original suffix names (callings, not animals) |
| 19 equipment slots incl. relic/ranged | Launch | |
| Bags, bank, bank bag slots | Launch | |
| Vendors, buyback, repair, limited stock | Launch | |
| Auction house (faction + neutral) | Launch | |
| Mail (items, COD, delay) | Launch | |
| Player trade | Launch | |
| Copper/silver/gold | Launch | |
| Guild bank | Launch | 6 tabs, per-rank limits, logs |
| Sockets/gems, reforging | Cut | |
| Legendary items | Later | Reserved drop exists |
| Tier sets | Launch | Vaultforged (T1) |
| World-drop epics | Launch | 6 |
| Keyring, lockpicking | Later | With Rogue |

## 6. Professions

| Feature | Status | Notes |
|---|---|---|
| Mining, Herbalism, Skinning | Launch | to 225 |
| Blacksmithing, Leatherworking, Tailoring, Alchemy, Enchanting, Engineering | Launch | to 225; full recipe lists — [Crafting](../04-professions/crafting.md) |
| Cooking, Fishing, First Aid | Launch | |
| 2-primary limit | Launch | |
| Skill-up colours | Launch | |
| Specialisations | Later | |
| Artisan 300 | Later | |
| Disenchanting | Launch | |
| Jewelcrafting, Inscription, Archaeology | Cut | Not classic |

## 7. Group & social

| Feature | Status | Notes |
|---|---|---|
| Party (5), raid group, sub-groups | **Changed** | Raid group max 20 |
| Group XP split and group bonus | **Changed** | No split, no bonus: full solo XP each; 0 XP for all if the level spread exceeds 5 |
| Loot rules incl. master loot, need/greed | Launch | |
| Raid target icons, ready check | Launch | |
| Meeting stones | Launch | Summon-capable |
| LFG channel | Launch | + simple group-finder board |
| Automatic dungeon finder / teleports | Cut | |
| Chat channels, whispers, emotes, ignore | Launch | |
| Languages | Later | With 2nd allegiance |
| Friends list, /who | Launch | |
| Guilds, ranks, MOTD, tabards | Launch | 4 signatures |
| Inspect, trade, duel | Launch | |
| In-game voice | Cut | |
| Macros | Launch | |
| Add-on API | Later | |
| Barber | Launch | (not classic, cheap) |
| GM tickets, reporting | Launch | |

## 8. Instances

| Feature | Status | Notes |
|---|---|---|
| 5-player dungeons | Launch (3) | [Dungeons](../07-instances/dungeons.md) |
| Dungeon sets | **Changed** | Blues, cosmetic grouping only |
| 10-player raid | Launch (1) | [Raid](../07-instances/raid-the-hollow-throne.md) |
| 20-player raids | Later | Framework supports 10 and 20 |
| 40-player raids | **Cut by design** | Raid sizes are 10 and 20 only |
| Raid lockouts, instance caps | Launch | |
| Heroic/mythic difficulties | Cut | |

## 9. PvP

| Feature | Status | Notes |
|---|---|---|
| Duels | Launch | |
| World PvP by faction | Later | Rules in place — [PvP](../02-systems/pvp.md) |
| PvP / PvE realm types | Later | Zone tags cover it |
| Battlegrounds | **Changed** | 1 map, **three teams** (Crownfall) |
| FFA arena with chest | Launch | The Dustpit |
| Honor ranks ladder | Cut (for now) | Marks of Valor vendor instead |
| PvP gear | Launch | Contender's set |
| Rated arenas | Cut | |

## 10. UI

| Feature | Status |
|---|---|
| Unit frames, action bars, stance bar, cast bar, buffs | Launch |
| Minimap with tracking | Launch |
| World map, quest log, character sheet, spellbook, talents | Launch |
| Bags, bank, vendor, trainer, AH, mail, trade, profession windows | Launch |
| Nameplates, floating text, tooltips with compare | Launch |
| Key bindings, options, accessibility | Launch |
| Character select/create, realm list | Launch |

## 11. Deliberate differences from the model (summary)

1. Three-faction design instead of two; one faction at launch.
2. No race-locked quests; both starting zones open to all.
3. Three classes covering nine roles; no combat shapeshifting.
4. Cleric (paladin-archetype) gets a taunt, a melee strike button and AoE threat baseline.
5. Druid heal-over-time signature (Blossom) available at cap 30.
6. Level cap 30 with a complete endgame (raid, world bosses, PvP) at that cap.
7. Riding at 30; epic mounts need feed, a time-played gold sink.
8. Three-team battleground; no honor-rank grind.
9. Purification Potion (Alchemy) substitutes for the missing ally magic-dispel.
10. Guild charter needs 4 signatures; dynamic respawns for crowding.
11. Group XP is neither split nor boosted; a level spread above 5 gives the whole group 0 XP.
12. Raid sizes are 10 and 20; no 40-player raids.
13. No water zones.
14. Four 5–10 zones, each a complete 5→10, including one entirely inside a mountain.
15. Dwarves have two cultures (mountain and hill) in the world's NPCs only; player dwarves are one race with no culture choice.
16. Respec caps at 5g and decays weekly; mail costs 1s.
17. Random-suffix items use original names.
