# Presentation Rules — which art, animation, effect and sound each thing uses

[← Data Index](00-data-index.md) · Art lists: [Art Master To-Do](../10-art/00-art-master-todo.md) · Asset ids and loading: [Placeholders and Swapping](../14-asset-pipeline/04-placeholders-and-swap.md) · Schema: [Content Schemas](../08-tech/content-schemas.md)

The data files say what a creature, spell or item *does*. The art lists say what assets *exist*. This page is the rule that joins them: for any content record, which model, skin, animation, effect, icon and sound it uses. The builder writes these as the `model`, `skin`, `outfit`, `visual`, `icon`, `soundSet` and `music` fields when it creates each record; the zone importer does it for a zone's creatures and NPCs. The values are ids of the [Asset Manifest](../15-asset-manifest/00-manifest-index.md). Validation rule V31 checks that every such field names an asset in the client's asset index (`client/assets/asset-index.json`), which lists every asset of the manifest, made or placeholder.

**Order of authority:** an art list that names a thing ("Worn by", "Used by", a creature listed in a rig's row, a named effect for an ability) decides. The tables below apply only to whatever the art lists do not name.

## 1. Creatures

| Field | Rule |
|---|---|
| Rig and model | The rig whose row in [Creatures & NPCs](../10-art/02-creatures-npcs.md) lists the creature. If none lists it: the rig of another creature of the same family; failing that, the family default below |
| Skin | The skin or colourway listed for it: among the rig row's skins in the asset manifest, the one named for the creature (a named creature such as Old Greymaw or Hale Morrow has a skin row of its own); else the one whose name ends with the creature's last word; else the row's nth, by the creature's place in the row. If none: the rig's skin for that zone; failing that, the rig's base skin tinted toward the zone's colour in [Art Direction](../10-art/10-art-direction.md) |
| Skins of a generated model | Where a rig's model is a generated mesh fitted to the rig, each of its skins is that model's own texture tinted for the variety, so every variety keeps the model's painted detail |
| Size | Scale 1.0. Elites 1.15, rares 1.1, named quest targets and mini-bosses 1.1, bosses as their art row says or 1.5 |
| Sound set | The rig's sound set in the [Audio list](../10-art/09-audio.md) |
| Family default rigs | Wolf-like beasts → wolf · boars and other hoofed beasts → boar · spiders and insects → spider · birds → the bird rig · fish-folk, tunnel-folk and other small humanoids → the small humanoid rig of their kind · bandits, cultists and other humans and dwarves → the Human or Dwarf player rig with an outfit (§2): the dwarf body where the group's outfit row is a dwarven one, the human body otherwise · walking dead → the skeleton or zombie rig · spirits → the ghost rig · fire, earth, slag and water beings → the elemental rig with the matching skin · built things → the construct rig · rooted plants → the plant rig |

## 2. NPCs and humanoid enemies on player rigs

| Field | Rule |
|---|---|
| Outfit | The outfit whose "Worn by" column names the NPC or its role. Otherwise by role and culture: quest giver, citizen → the culture's commoner outfit · vendor, innkeeper → merchant or apron outfit · trainer → the outfit of the class or craft taught · guard → the culture's guard outfit · scholar, priest → robes · flight master, stable keeper → handler outfit · cultist, bandit, exile → the enemy group's outfit for the zone. Where an outfit row has several outfits, the one meant is the row's nth in the asset manifest's order; where a row has one for each body, the body decides |
| Dressed body | Where a dressed whole-body model has been made for the outfit on the NPC's body, the NPC is drawn as that model whole: the body's own skeleton under a mesh that already wears the outfit, with its own texture. It is the file beside the outfit's texture named for the body (`client/assets/outfits/<the outfit's file name>.chr-00N.glb`; CHR-003 human man, CHR-004 human woman, CHR-005 dwarf man, CHR-006 dwarf woman). The outfit texture is not laid over it. Where no dressed body exists for that outfit and body, the outfit is the skin painted onto the body's template model. Open: whether dressed bodies are the lasting method for every NPC or a measure for the two starting zones is the owner's decision. |
| Race | From the roster: its culture and location (human, mountain dwarf, hill dwarf) |
| Body | The body matching the pronouns used for that NPC in the rosters, quest text or zone documents: the sentences that name the NPC are read, and whichever of "she, her" and "he, his, him" is used more decides. Where none are used anywhere, or the two are used equally, bodies alternate by roster number so that each hub has both: an even number takes the woman's body, an odd number the man's. Open: this rule puts some men's names on the woman's body and some women's names on the man's; a Sex column in the NPC rosters would settle each body; until the owner decides, the rule above stands. |
| Face, hair, skin tone | Part of the model where the NPC is drawn as a dressed body. Otherwise chosen from the customisation options by a fixed rule from the NPC's id, so the same NPC always looks the same and neighbours differ. A title or description that implies age ("Elder", "Old", "Young") picks from the older or younger options |
| Held items | A vendor or crafter holds nothing; a guard and any combat trainer hold the weapon of their kind; an NPC whose text mentions a tool or object holds it if the prop exists |
| Idle | Stand, with the work animation of the role where one exists (hammering at a forge, sweeping, reading), otherwise the idle variations |

### 2a. Player characters

A player's character is not a dressed body. It is built from its appearance (skin, face, hair, hair colour, facial), each part chosen freely of the others ([Characters, Armor & Weapons §2](../10-art/01-characters-armor-weapons.md#2-customisation-permutations); [Placeholders and Swapping §2a](../14-asset-pipeline/04-placeholders-and-swap.md#2a-fitted-bodies-kept-templates-and-dressed-bodies)).

| Part | Rule |
|---|---|
| Body | The fitted body of the character's race and sex (CHR-003 to CHR-006), which is bald and clean-shaven, in plain underclothes |
| Face | The chosen face of that body (CUS-02): its head texture on the head region of the body's texture, with its small change of shape where it has one |
| Hair | The chosen hair style's piece for that body (CUS-03), attached to the head bone or skinned to the head and neck bones. The style named bald adds no piece |
| Facial hair and features | The chosen piece for that body (CUS-05): beards, moustaches, braids, sideburn-plaits, rings and earrings as pieces that follow the head; freckles and scars drawn on the face. "None" adds nothing |
| Skin tone | The chosen tone (CUS-01), a tint of the skin region of the body's texture, the face included. Eyes, lips and clothes are not tinted |
| Hair colour | The chosen ramp (CUS-04), a tint on the hair and facial-hair pieces only. Rings and earrings keep their own colours |

## 3. Abilities

| Field | Rule |
|---|---|
| Icon | The icon listed for the ability in [Icons](../10-art/06-icons.md); each rank shares it. Spell records carry no icon field: the icon is found by its id, `ICO-<letter><n>-<slug>`, where the slug is the ability's name in lower case with apostrophes dropped and every other run of characters that are not letters or digits as one hyphen (`ICO-G2-attack` for Attack). The letter is the icon list's group, tried in this order: the class's own (F Fighter, C Cleric, D Druid), then G, F, C, D, K, E, M, Q; n is the group's section, 1 to 13. An ability with no icon of that id shows its name in its slot |
| Cast animation | Cast time above 0: the directed cast loop for a spell with a target, the two-handed raised loop for one without, then the release. Channelled: the channel loop. Instant spells: the instant cast. Shouts and roars: the shout. Stance changes: the stance flourish |
| Melee ability animation | The special attack for the equipped weapon type (one-handed, two-handed, dual, shield, staff). Abilities with a shield requirement use the shield bash |
| Effects | The effects listed for the ability in [Spell, Particle & World Effects](../10-art/04-vfx.md). If none: the generic set by school — cast-hand glow, projectile if the spell travels, impact, buff swirl for auras, ground ring for area effects |
| Projectile speed | 24 yd/s unless the ability states one; instant-hit spells have no projectile |
| Sounds | The ability's sounds in the Audio list. If none: the school's pre-cast loop, cast release and impact sounds; melee abilities use the weapon swing and an impact by the target's armor (§5) |
| Aura icon and effect | The ability's icon; a persistent effect on the unit only where the effects list gives one |

## 4. Items

| Field | Rule |
|---|---|
| Model and texture | As the [Named Item Index](../10-art/07-named-item-index.md) says: unique art, or the tier model for the slot, type and level band with the recolor for its zone or source |
| Icon | Its own icon from the index. Random-suffix drops use the tier icon for slot, type and band |
| What shows on the character | Head, shoulders, chest, hands, waist, legs, feet, wrists, back, tabard, shirt, both hands and the ranged slot. Necks, rings, trinkets and relics do not show. A "hide helm" and "hide cloak" option is per character |
| Sheathing | One-handed weapons at the hips, two-handed and staves on the back, shields on the back, bows and guns on the back |
| Sounds | Pick up and put down by material: cloth, leather, metal, wood, gem, paper, liquid, food, herb, ore |
| Consumables, materials, quest items | Icon only; no world model unless it is a world object |

## 5. Hits, steps and voices

| Event | Rule |
|---|---|
| Weapon impact | By weapon kind (blade, blunt, pierce, unarmed, claw) and the target's surface: cloth, leather, mail or plate-like, flesh, bone, stone, wood, spirit. A critical hit adds the crit accent |
| Miss, dodge, parry, block | Whoosh · whoosh · metal clash · shield thud |
| Footsteps | By the ground texture under the character (grass, dirt, stone, wood, sand or ash, snow, water shallows, cave), with a second set for mounts and for large creatures |
| Player voice | Effort sounds by race and body: attack grunt 1 in 4 swings, wound, death, jump landing from height, and the error lines for "not enough rage", "not ready", "out of range" at most once every 4 seconds |
| Creature voice | From its sound set: aggro, attack 1 in 3 swings, wound 1 in 3 hits, death, and an idle sound every 20 to 40 seconds within 30 yd of a player |

## 6. Music and ambience

| Rule | Detail |
|---|---|
| Zone music | Each sub-area's `music` is the track set listed for its zone in the Audio list: hub sub-areas use the town set, hostile sub-areas the wild set, caves and interiors the under-ground set |
| Day and night | Where the zone has both, the set changes at dawn and dusk with a 10-second cross-fade |
| Play pattern | One track, then 60 to 120 seconds of ambience only, then another; never the same track twice running |
| Combat | No combat music in the open world. Boss fights play the instance's boss track from engage to death or reset |
| Events | Level-up sting, quest complete sting, death sting, discovery chime: played over the music, which ducks by 6 dB |
| Ambience | The sub-area's ambience bed loops always; one-shot ambience sounds play at random positions around the listener at the rates in the Audio list. Weather adds its own layer |
| Inside | Entering a building or cutout volume fades outdoor ambience to 30% and applies the interior reverb |

## 7. World objects and scenery

| Thing | Rule |
|---|---|
| Quest objects | The prop named in the [Quest Art Index](../10-art/08-quest-art-index.md). A sparkle effect shows only to players who can use it |
| Gathering nodes | The node model for its kind; it shrinks away over 1 second when emptied and is absent until respawn |
| Chests, doors, levers | Open and close animations with their sounds; a lootable chest glints |
| Corpses | The death pose remains; a lootable corpse sparkles for whoever may loot it; a skinnable one is marked in its tooltip |
| Missing asset | The placeholder of its contract is used and the asset is listed in the asset status file; nothing is ever invisible or missing-texture coloured |
