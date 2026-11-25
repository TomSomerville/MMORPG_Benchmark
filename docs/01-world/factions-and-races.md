# Factions & Races

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Lore](lore.md) · Next: [World & Travel](world-and-travel.md)

## 1. Design goal

Ship with **1 allegiance, 2 races**, but make allegiances and races pure data so that adding a second and third allegiance, or a new race, needs **no code change** — only new data rows, art, and a starting zone.

The single most important rule: **nothing in code may assume there are exactly one or two sides.** There is no "opposite faction". Every hostility check goes through a reaction matrix.

## 2. Two different things both called "faction"

| Concept | Name in this project | Example | Purpose |
|---|---|---|---|
| The side a player character belongs to | **Allegiance** | Concord of Dawn | Who you can group, trade, talk and fight with |
| An NPC group you earn standing with | **Reputation faction** | Solhaven, Freeholders of Kite's Rest | Vendor discounts, rewards, guard behaviour |

## 3. Allegiance system

**Allegiance record:** id, name, colour, list of member races, capital cities, default language, starting reputations, graveyard set, auction house set.

**Reaction matrix (N × N):** for every pair of allegiances, one of `Friendly`, `Neutral`, `Hostile`. Launch matrix is 1×1. The three-faction target:

| | Concord | Wildpact | Covenant |
|---|---|---|---|
| **Concord** | Friendly | Hostile | Hostile |
| **Wildpact** | Hostile | Friendly | Hostile |
| **Covenant** | Hostile | Hostile | Friendly |

The matrix can be changed per-zone (truce in Kite's Rest) or per-event.

**What allegiance gates, and how each is built to scale to N sides:**

| Feature | Launch behaviour | N-faction behaviour (already supported by design) |
|---|---|---|
| Grouping, guilds, trade, mail | Everyone | Same allegiance only (config flag per feature) |
| Chat | One language, "Common" | Per-allegiance language; other speech is scrambled; each language is a learnable skill |
| Auction house | Concord AH in both capitals (linked) + neutral AH at Kite's Rest | One linked AH per allegiance + the neutral AH |
| Guards & towns | Concord guards attack hostile NPCs | Guards use the reaction matrix |
| Zones | Tagged `Sanctuary`, `Territory(allegiance)`, or `Contested` | Unchanged — only tags are added |
| PvP flagging | Off, except duels / arena / battleground | Flag automatically in Contested zones and enemy Territory |
| Quests | No allegiance requirement on any quest | Optional `allegiance` field on a quest; default is "any" |
| Battleground teams | Random Red / Blue / Yellow | Team = allegiance (colours already match) |
| Flight paths, innkeepers, graveyards | Concord set | Per-allegiance sets |

## 4. Reputation factions (launch)

Standing ladder (same as the genre standard): Hated → Hostile → Unfriendly → **Neutral** → Friendly (3,000) → Honored (6,000) → Revered (12,000) → Exalted (21,000).

| Reputation | Earned by | Rewards |
|---|---|---|
| **Solhaven** | Quests on Meridia, cloth turn-ins | 5–20% vendor discount; tabard at Honored |
| **Hammerdeep** | Quests on Khazrun, cloth turn-ins | Same; ram mount access at Exalted for non-dwarves |
| **Thornwick Wardens** | Thornwick quests, Gallowmere Crypts | Profession recipes, a blue cloak at Revered |
| **Freeholders of Kite's Rest** | Riftlands quests, arena chest, Blackspade kills | Neutral AH access (always), recipes, the Dustpit trinket quest |
| **The Athenaeum** | Main Chain 2, Hollowspire Keep, the raid | Raid attunement at Friendly; resistance gear and enchants up to Exalted |

Humans start Friendly with Solhaven and Neutral-high with Hammerdeep; dwarves the reverse.

## 5. Race system

**Race record:** id, name, allegiance, allowed classes, base attributes, racial traits (list of passive/active spells), starting zone, starting gear set, model/skeleton set, voice set, languages.

Because race is data, adding Elf, Gnome, Ogre or Undead means: one race record, 4–5 racial spells, a model set, and optionally a new starting zone.

### 5.1 Launch races

| | **Human** | **Dwarf** |
|---|---|---|
| Home | Meridia — starts in [Brightmead Vale](../05-zones/t1-brightmead-vale.md) | Khazrun — starts in [Stonewake Dale](../05-zones/t1-stonewake-dale.md) |
| Classes | Fighter, Cleric, Druid | Fighter, Cleric, Druid |
| Base Str / Agi / Sta / Int / Spi | 20 / 20 / 20 / 20 / 21 | 22 / 16 / 23 / 19 / 19 |
| Racial 1 | **Versatile** — Spirit +5% | **Stoneform** (active, 3 min CD) — 8 s: immune to bleed, poison and disease, armor +10% |
| Racial 2 | **Diplomat** — reputation gains +10% | **Frostborn** — Frost resistance +10 |
| Racial 3 | **Sword & Mace Training** — +5 weapon skill with swords and maces | **Axe & Gun Training** — +5 weapon skill with axes and guns |
| Racial 4 | **Keen Eye** (active, 3 min CD) — 20 s stealth detection (matters once rogues exist) | **Prospector's Nose** (toggle) — shows treasure chests on the minimap |

Class base stats are added on top of race stats; see [Class Framework](../03-classes/class-framework.md).

### 5.2 Mountain dwarves and hill dwarves

Dwarves are **one playable race with two cultures**. The split is cultural and visual, never mechanical: both use the same racials, classes and stats.

| | **Mountain dwarves — the Hallborn** | **Hill dwarves — the Dalefolk** |
|---|---|---|
| Live | Snow peaks, mountain interiors, the ground at the mountain's foot | Valleys between mountains; farmed foothills |
| Rule | The Deep Thanedom: High Thane, hall-thanes, guild-masters | The Dale-Moot: elected reeves; no nobles |
| Livelihood | Mining, smithing, engineering, rune-craft | Barley, hops, goats and rams, brewing, weaving, hunting |
| Faith | The Forge-flame (clerics of the Hall of Embers) | The Forge-flame at the hearth, and the old Stonesinger rites |
| Class leanings (flavour only) | Fighters, Clerics | Druids, Fighters |
| Look | Braided beards, soot, leather aprons, steel; pale | Shorter beards, wool and plaid, straw hats; weathered |
| Names | Craft surnames: Stonebraid, Emberhand, Sluicewright | Land and larder surnames: Ramsbell, Maltby, Panhandle |
| Says of the other | "Dirt-farmers who've forgotten the stone." | "Moles who've never seen what they're fighting for." |
| Zones | Embercrag Hollow, Hammerdeep, Stoneheart Deeps, Ironroot Hold, Deepseam | Stonewake Dale, Ramshead Lodge, the Ironroot steadings, Emberwell |

**Players are simply dwarves.** There is one dwarf race with one starting zone (Stonewake Dale) and no culture choice at character creation; a player dwarf is not marked as Hallborn or Dalefolk and nothing in the game treats them as either. The two cultures exist only in the world: in its NPCs, their dress, voices, buildings and attitudes toward each other. (Decided 2026-11-12.) A dwarf now begins among the hill dwarves, at Sunbank Steading in Stonewake Dale, in spring, and meets the mountain dwarves at levels 5–10, in Embercrag Hollow or the Stoneheart Deeps (decided 2026-11-25; the start was Embercrag Hollow before). Starting in the Dale makes a player a guest of the Dalefolk, not one of them.

**In the story:** the dam in Stonewake Dale, the Rootvault gardens in Hammerdeep and the Ironroot levies are the three places the two cultures are forced to cooperate; the Slagborn are what happens when a mountain clan stops listening to anyone.

### 5.3 Planned races (not built at launch)

| Race | Allegiance | Sketch of racials | Starting zone concept |
|---|---|---|---|
| Gnome | Concord | +5% Intellect; escape root/snare; +15 Engineering | Shares Stonewake Dale (sub-area) |
| Elf | Wildpact | +1% dodge; nature resist; out-of-combat stealth | Sael'anor deepwoods (Meridia far west) |
| Ogre | Wildpact | +5% max health; stun resist; +5 two-handed skill | Stonemaw Steppes |
| Undead (Unburied) | Covenant | Break fear/charm; shadow resist; underwater breathing; consume corpse | Vael Morrow outskirts (Sundrel) |

## 6. Race-neutral questing (hard requirement)

- **No quest checks race.** Every quest in both starting zones can be taken by either race.
- A level 1 human who takes the ship and walks to Stonewake Dale can complete it start to finish, and vice versa.
- The only race-specific thing is *where the character first appears* and the two-line introductory text of the very first quest.
- Class trainers for all three classes exist in both starting camps.
- Travel between the two starting continents is free and available from level 1 (see [World & Travel](world-and-travel.md)).

## 7. Class × race matrix and extensibility

Launch: all 3 classes × both races. The matrix is a list on the race record (`allowed classes`), so future restrictions (e.g. no Ogre Druids) are data.

## 8. Character creation

Choices: allegiance (hidden while only one exists) → race → sex/body → class → appearance (face, skin, hair style, hair colour, facial hair/markings) → name. Name rules: 2–12 letters, unique per realm, profanity filter, reserved-name list. 10 character slots per realm.
