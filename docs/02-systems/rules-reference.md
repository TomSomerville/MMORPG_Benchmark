# Rules Reference — small rules not stated elsewhere

[← Master Plan](../../MASTER_PLAN.md) · Related: [Combat & Stats](combat-and-stats.md) · [Progression](progression.md) · [World & Travel](../01-world/world-and-travel.md) · [UI Specification](../08-tech/ui-specification.md)

The system documents give the large rules. This page gives the small numbers a builder would otherwise have to guess: speeds, ranges, timers and skill gains. **Where another document states a value for the same thing, that document stands**; this page only fills gaps. Every value here is a field in the rules records (`movement`, `interaction`, `skills`) listed in [Content Schemas](../08-tech/content-schemas.md), so it can be tuned without code.

## 1. Movement

| Rule | Value |
|---|---|
| Run | 7 yd/s (stated in World & Travel) |
| Walk (toggle) | 2.5 yd/s |
| Backwards | 4.5 yd/s |
| Strafe | Full run speed; diagonal movement is not faster than straight |
| Swim | 4.7 yd/s forwards (stated), 2.5 yd/s backwards |
| Turning with keys | 180° per second |
| Jump | Rises 1.6 yd, in the air 0.8 s; movement direction cannot change in the air |
| Step height | Steps up to 0.5 m are climbed without jumping |
| Steep ground | Above 50° a character slides down and cannot stand |
| Falling | No damage below 15 yd. From 15 yd, damage is a share of maximum health rising in a straight line to 100% at 65 yd. Landing in water at least 2 yd deep does no damage |
| Mounted | Speeds in World & Travel. Dismount on taking damage from a player, entering combat by attacking, entering a building marked indoors, or swimming |
| Speed effects | The strongest speed increase and the strongest slow both apply, multiplied together; others of each kind are ignored |

## 2. Interaction ranges

| Action | Range |
|---|---|
| Talk to an NPC, loot a corpse, open a chest, gather a node, use a mailbox, forge or anvil | 5 yd |
| Trade, duel request | 10 yd |
| Inspect | 30 yd |
| Follow | Breaks beyond 40 yd |
| Tab targeting | The nearest hostile within 40 yd inside a 120° arc in front, then the next nearest on each press |
| Kill, loot and quest credit in a group | 100 yd from the kill (stated in Progression) |
| Quest sharing | Target within 10 yd and eligible for the quest |
| Area loot | None: each corpse is looted separately |
| Nameplates | Shown within 40 yd; names without plates to 60 yd |
| Duel area | A duel is lost by leaving a 40 yd radius around the flag for 10 s (stated in PvP) |

## 3. Timers

| Rule | Value |
|---|---|
| Away | Marked AFK after 5 minutes with no input |
| Idle logout | Logged out after 30 minutes AFK. In a battleground, 2 minutes with no movement or action allows an AFK report |
| Release | A dead player may release at once, and is released automatically after 6 minutes. The wait before resurrecting after repeated deaths is in [Progression §10](progression.md#10-death) |
| Player corpse | Stays until the player returns to life. Bones are left for 15 minutes as scenery |
| Resurrection by another player | An offer lasts 60 s. Returning to life by spell restores the health and mana the spell states |
| Loot roll window | 60 s (stated in Items & Loot) |
| Trade | Both must accept; any change to either side clears both acceptances |
| Summon offer (meeting stone) | 2 minutes to accept |
| Instance exit when not in the group | Removed to the entrance after 60 s |
| Cast queue | 400 ms (stated in Architecture) |
| Combat log | Keeps the last 2,000 lines |
| Channel join | Joining or leaving a zone moves the player between that zone's General and LocalDefense automatically |

## 4. Weapon and defense skill

| Rule | Value |
|---|---|
| Cap | 5 × level (stated in Combat & Stats) |
| Starting value | Weapons a class starts with: 5 at level 1. A newly trained weapon type: 1 |
| Weapon skill gain | On each hit that lands on a creature that is not grey to the player: chance = `1 − skill / cap`, never less than 5% and 0% at cap. One point per gain |
| Defense skill gain | On each attack received from a creature that is not grey, hit or avoided: half the chance above |
| Players | No skill is gained from fighting other players |

## 5. Food and drink

The four vendor tiers are defined in the [NPC Index, STK-FOOD](../11-npcs/00-npc-index.md); the figures are repeated here because every other food and drink item (quest rewards, cooked food, drops) restores by the tier of its required level. A source document that states a figure for an item stands.

| Required level | Food restores | Drink restores | Over |
|---|---|---|---|
| 1 | 61 health | 151 mana | 18 s |
| 5 | 243 health | 436 mana | 21 s |
| 15 | 552 health | 835 mana | 24 s |
| 25 | 874 health | 1,080 mana | 27 s |

The restoration is spread evenly over the time, stops on standing, moving or entering combat, and needs the character seated (eating seats the character). The "Well Fed" bonus from cooked food is given after 10 seconds of eating. Vendor prices are in the stock lists.

## 6. Camera and view

| Rule | Value |
|---|---|
| Distance | From first person (0) to 30 yd, by mouse wheel (stated in UI & Controls); default 12 yd |
| Pitch | −80° to +80° |
| Field of view | 60° vertical, fixed |
| Collision | The camera moves in to stay out of terrain and walls, and returns smoothly |
| Indoors | Maximum distance is 15 yd inside buildings, caves and instances |
| Draw distance | Terrain to the option's view distance (default 500 m); characters and creatures to 100 m (interest range); large landmarks always |

### Graphics presets and the target computer

The Options window offers four presets; each sets the values below, and any value can then be changed on its own. On first start the client picks a preset from the graphics card's memory.

| Setting | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Chosen on first start when graphics memory is | under 3 GB | 3–5 GB | 6–9 GB | 10 GB or more |
| Terrain view distance | 300 m | 500 m | 700 m | 1,000 m |
| Shadows | Off (blob under characters) | Sun only, 1 cascade | Sun, 3 cascades | Sun, 4 cascades, plus the 4 nearest lights |
| Textures | Half size | Full | Full | Full |
| Grass and ground clutter | Off | 40% | 100% | 100%, to 80 m |
| Effects density | 50% | 75% | 100% | 100% |
| Characters at full detail (the rest use the low-detail model) | 20 | 40 | 60 | 100 |
| Water | Flat tint | Reflection of sky | Sky and terrain | Sky, terrain and characters |
| Anti-aliasing | Off | FXAA | MSAA ×2 | MSAA ×4 |
| Frame cap | 60 | 60 | 60 | Display rate |

| | Minimum | Recommended |
|---|---|---|
| Target | Low preset, 30 frames a second at 1080p | High preset, 60 frames a second at 1080p |
| Processor | 4 cores, 2015 or later | 6 cores, 2019 or later |
| Memory | 8 GB | 16 GB |
| Graphics | 2 GB, DirectX 12 or Vulkan capable (GTX 1050 class) | 6 GB (GTX 1660 or RX 5600 class) |
| Disk | 20 GB | 20 GB on a solid-state drive |
| Network | 1 Mbit/s, under 250 ms | Under 100 ms |
| System | Windows 10 or 11, 64-bit | Same |

These are targets for the build to meet and measure with the `crowd` and `visual-walk` plays, not measurements. The language at launch is English; all text is in string tables so that a language is added by adding a table.

## 7. Other small rules

| Topic | Rule |
|---|---|
| Sitting | A seated character stands when attacked, and the first hit against a seated character is a critical hit |
| Swimming and combat | Abilities work while swimming. Mounts cannot swim |
| Water breathing | 60 s (stated), then 10% of health each 2 s; the bar refills at the surface in 5 s |
| Eating, drinking, bandaging and mounting | Not in combat |
| Ghosts | See the world desaturated; can see and speak only to other ghosts and the spirit healer; cannot be attacked; move at +25% speed (stated) |
| Target of target | Shown beside the target frame |
| Auto-attack | Starts on right-click or any damaging ability; stops on changing to a friendly target or pressing stop. A swing waits while out of range or not facing, and happens as soon as both are true |
| Stacking in bags | Picking up an item fills an existing stack first, then the first empty slot in bag order |
| Buyback | The last 12 items sold (stated in Economy), until logout |
| Soulbound trade | None, except raid loot among those present for 2 hours (stated in Items & Loot) |
| Level-up | Health and resource are restored to full |
| Spell ranks and downranking | Every rank a character has learned stays in the spellbook and can be cast. A lower rank uses its own cost, cast time and base values. Its spell-power coefficient is multiplied by `(level at which the next rank is learned + 5) ÷ caster level`, never above 1; the highest rank known is never reduced |
| Raid markers | The group leader and assistants can place one of 8 marker icons on a unit; each icon is on one unit at a time and is seen by the whole group |
| Threat display | None at launch: no threat or damage meter is built in |
| Minimum level to mail or trade | None, but see the account limits in [Accounts and Live Service](../08-tech/accounts-and-live-service.md) |
