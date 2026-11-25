# Art To-Do 1 — Player Characters, Armor & Weapons

[← Art Master To-Do](00-art-master-todo.md) · Next: [Creatures & NPCs](02-creatures-npcs.md)

Every asset needed to put a player character on screen at any level from 1 to 30, in any gear. ☐ = not started. IDs are stable keys for tracking.

## 1. Base bodies

Two rigs (Human, Dwarf); male and female share a rig with different meshes. The four player bodies are the most important art in the game, because players look at them every minute; they and their animations are made before any other model.

**How a body is made.** Each body is a generated model fitted to its rig's contract. A figure is painted in the game's style standing in an A-pose, an image-to-3D model makes a textured mesh of it, and the fitting step keeps that mesh: it is reduced to the triangle budget, given its own UV layout with its colour baked onto one 1024² texture, its joints are found from its outline, it is skinned, and it is carried to the contract's skeleton and rest pose so that every player clip plays on it. The result is **a single mesh with its own baked texture**. What the figure wears, its hair and its face are part of that mesh and that texture.

The constructed body a fitted body replaces is kept beside it. A skin or outfit painted for the constructed body's layout fits that mesh and no other, so a character wearing one is drawn on the constructed body until the outfit has a dressed body of its own ([Creatures & NPCs §6](02-creatures-npcs.md#6-npc-outfits-on-player-rigs)).

Open: whether the swappable head, hair and facial-hair pieces and the layered skin texture of §2 apply to fitted bodies is not decided; a fitted body is one mesh with one texture and has no route for them today.

| ID | Done | Asset | Notes |
|---|---|---|---|
| CHR-001 | ☐ | Human rig (skeleton + skin weights template) | ~55 bones incl. fingers (mitten hands), cloak chain, weapon/shield/back sockets |
| CHR-002 | ☐ | Dwarf rig | Same bone names as human for animation retargeting; own proportions |
| CHR-003 | ☐ | Human male body mesh | 4–6k triangles, one 1024² texture; one mesh at every distance |
| CHR-004 | ☐ | Human female body mesh | |
| CHR-005 | ☐ | Dwarf male body mesh | |
| CHR-006 | ☐ | Dwarf female body mesh | |
| CHR-007 | ☐ | Underwear layer ×4 bodies | Painted into the skin atlas |
| CHR-008 | ☐ | First-person arms ×4 | Optional; only if first-person zoom shows hands |
| CHR-009 | ☐ | Ghost shader variant | Used when dead; applies to any body |
| CHR-010 | ☐ | Character-select podium poses ×4 | Idle on the select screen |

## 2. Customisation permutations

| ID | Done | Option | Human M | Human F | Dwarf M | Dwarf F | Total assets |
|---|---|---|---|---|---|---|---|
| CUS-01 | ☐ | Skin tones (texture tints + hand-tuned variants) | 6 | 6 | 6 (3 Hallborn pale, 3 Dalefolk weathered) | 6 | 24 |
| CUS-02 | ☐ | Faces (head texture, small mesh morph) | 6 | 6 | 6 | 6 | 24 |
| CUS-03 | ☐ | Hair styles (meshes) | 8 | 8 | 8 | 8 | 32 |
| CUS-04 | ☐ | Hair colours (shared tint ramps) | 8 | 8 | 8 | 8 | 8 ramps |
| CUS-05 | ☐ | Facial hair / features (meshes) | 6 beards & moustaches | 4 (earrings, freckles, scar, none) | 8 beards (4 Hallborn braided, 4 Dalefolk short) | 4 (braids, sideburn-plaits, rings, none) | 22 |
| CUS-07 | ☐ | Starting outfits | 3 (one per class) | 3 | 3 | 3 | Built from tier-1 armor textures (§5) |

Possible distinct faces-on-bodies: 4 bodies × 6 skins × 6 faces × 8 hair × 8 colours × 4–8 facial = ~46,000 combinations from **110 authored assets**.

## 3. Player animation set

One set per rig (authored on Human, retargeted and hand-corrected on Dwarf): **2 × 96 clips**.

| ID | Done | Group | Clips |
|---|---|---|---|
| ANM-01 | ☐ | Locomotion | Idle A, Idle B (fidget), Walk, Run, Backpedal, Strafe L, Strafe R, Turn L, Turn R, Jump start, Jump loop, Jump land, Fall, Swim idle, Swim forward, Swim back |
| ANM-02 | ☐ | Stance & state | Combat idle (unarmed), Combat idle 1H, Combat idle 2H, Combat idle dual, Combat idle staff, Sit chair, Sit ground (in/loop/out), Kneel, Sleep, Stunned, Feared run, Rooted struggle, Knockdown + get up, Death, Dead pose, Ghost idle |
| ANM-03 | ☐ | Melee | 1H swing A, 1H swing B, Off-hand swing, 2H swing A, 2H swing B, Polearm thrust, Staff strike, Dagger stab, Unarmed A, Unarmed B, Shield bash, Shield block, Parry, Dodge, Hit react light, Hit react heavy, Critical-wound stagger |
| ANM-04 | ☐ | Ranged | Bow draw + loose, Gun aim + fire, Crossbow fire, Throw |
| ANM-05 | ☐ | Fighter specials | Charge run, Leap-strike (Strike/Execute), Wide cleave, Whirlwind spin, Ground stomp, Slam wind-up, Shout (Battle Cry/Roar), Taunt gesture, Stance change flourish |
| ANM-06 | ☐ | Casting | Directed cast (ready / loop / release), Omni cast (ready / loop / release), Channel loop, Instant cast one-hand, Instant cast two-hand, Heal cast (ready / loop / release), Buff self, Weapon imbue (Oath), Ground-target place, Resurrect kneel-cast |
| ANM-07 | ☐ | World actions | Loot kneel, Interact/use, Open chest, Eat, Drink, Bandage, Mining swing, Herb gather, Skinning, Fishing cast / idle / reel, Smithing hammer, Crafting generic, Read |
| ANM-08 | ☐ | Mounted | Mount up, Ride idle, Ride walk, Ride run, Ride jump, Dismount |
| ANM-09 | ☐ | Emotes (20) | Wave, Bow, Dance, Cheer, Laugh, Cry, Point, Salute, Kneel, Talk, Yes, No, Shrug, Clap, Flex, Roar, Beg, Rude, Sleep, Thank |

## 4. How armor is built (the permutation rules)

Armor never needs a model per item. Each equipped piece contributes one or more of the layers below. The texture layers are painted on one UV layout shared by all four bodies, which is the layout of the constructed bodies.

Open: whether this shared-layout layered armor system, the palette lock and the repaint pass apply to fitted bodies is not decided; each fitted body has its own UV layout and its generator's colours, so the armor layers have no route onto it today.

| Layer | Used by slots | Authored per | Fits |
|---|---|---|---|
| **Body texture region** painted over the skin atlas | Chest, Legs, Feet, Hands, Wrist, Waist, Shirt, Tabard | Appearance set × colourway | Painted once on a shared UV layout that all 4 bodies use |
| **Geometry piece** attached to the rig | Head, Shoulders (pair), belt buckle (optional), robe skirt, boot cuff, glove flare | Appearance set | 2 fits (Human, Dwarf); male/female by scale offset |
| **Cloak** | Back | Cloak design × colourway | One cloth mesh per rig (2) |
| **Weapon / shield / held item** | Main hand, Off hand, Ranged | Model × colourway | Universal (hand sockets) |

So a full armor **appearance set** = 6 texture regions + helm mesh + shoulder mesh (+ robe skirt for cloth chests) and each **colourway** is a recolour of those textures.

**Total permutations supported:** 4 bodies × every combination of 10 visible armor slots × weapons — all from the lists in §5–§9.

## 5. Armor appearance sets (levels 1–30)

Colourways are full recolours; "Head/Shoulders" says whether that tier has those pieces.

**Colourway rule (set after the quest rewards were named).** The nine general sets (C1–C3, L1–L3, M1–M3) dress 377 tier-art items, so each needs enough colourways that two rewards for the same slot from the same zone never look identical:

- Every set has one **plain** colourway for starting gear, vendor whites, crafted items and world drops.
- Level 1–10 sets add **one colourway per zone** (Brightmead, Embercrag, Harrowfield, Russetwood, Stonewake Dale, Stoneheart Deeps), each in that zone's palette, so a reward shows where it was earned.
- Level 10–20 and 20–30 sets add **two colourways per zone** (first half and second half of the zone), because those zones give the same slot two or three times.
- An item's colourway is assigned by rule from its source zone and quest level, not chosen by hand. Where a zone still gives two items of one slot and type in the same half, the second takes the neighbouring zone's colourway.
- The level 1–10 sets now have shoulder pieces (and cloth and leather head pieces), because elite quests in the 5–10 zones reward them.

| ID | Done | Set | Type | Levels | Regions | Head | Shoulders | Robe skirt | Colourways | Used by |
|---|---|---|---|---|---|---|---|---|---|---|
| ARM-C1 | ☐ | Linen / homespun | Cloth | 1–10 | 6 | ✓ hood (elite rewards only) | ✓ | ✓ | 7 (plain + one per level 1–10 zone) | Starting casters, quest greens, Tailoring 1–70 |
| ARM-C2 | ☐ | Woolen | Cloth | 10–20 | 6 | ✓ hood | ✓ | ✓ | 5 (plain + two per zone) | Quest greens, Tailoring 75–120 |
| ARM-C3 | ☐ | Silk | Cloth | 20–30 | 6 | ✓ hood/circlet | ✓ | ✓ | 7 (plain + two per zone; incl. azure, storm-green, starlit violet) | Quest greens, Tailoring 125–195 |
| ARM-C4 | ☐ | Cultist / ashen vestments | Cloth | 13–23 | 6 | ✓ | ✓ | ✓ | 2 | Gallowmere + Slagworks cloth blues; Cinderbrand NPCs |
| ARM-C5 | ☐ | Hollow court silks | Cloth | 27–30 | 6 | ✓ | ✓ | ✓ | 2 | Hollowspire cloth blues; Athenaeum/crafted blues |
| ARM-L1 | ☐ | Handstitched leather | Leather | 1–10 | 6 | ✓ cap (elite rewards only) | ✓ | — | 7 (plain + one per level 1–10 zone) | Starting Druid, quest greens, Leatherworking 1–85 |
| ARM-L2 | ☐ | Dark / highland leather | Leather | 10–20 | 6 | ✓ cowl | ✓ | — | 5 (plain + two per zone) | Quest greens, Leatherworking 100–135 |
| ARM-L3 | ☐ | Heavy / dusky leather | Leather | 20–30 | 6 | ✓ | ✓ | — | 7 (plain + two per zone) | Quest greens, Leatherworking 150–205 |
| ARM-L4 | ☐ | Pelt-and-bone (beast trophies) | Leather | 5–26 | 6 | ✓ | ✓ | — | 3 | Rare/elite beast rewards (Greymaw, Scarhide, Blindmaw…) |
| ARM-L5 | ☐ | Dungeon leather | Leather | 13–30 | 6 | ✓ | ✓ | — | 3 (crypt, slag, hollow) | Dungeon leather blues |
| ARM-L6 | ☐ | Grove-keeper (crafted blues) | Leather | 30 | 6 | ✓ | ✓ | — | 3 (storm, star, bloom) | Stormcaller's / Starweaver's / Grovekeeper's |
| ARM-M1 | ☐ | Copper chain | Mail | 1–10 | 6 | — | ✓ | — | 7 (plain + one per level 1–10 zone) | Starting Fighter/Cleric, Blacksmithing 1–50 |
| ARM-M2 | ☐ | Bronze / silvered bronze | Mail | 10–20 | 6 | ✓ | ✓ | — | 5 (plain + two per zone) | Quest greens, Blacksmithing 105–130 |
| ARM-M3 | ☐ | Ironroot iron / steel | Mail | 20–30 | 6 | ✓ | ✓ | — | 7 (plain + two per zone) | Quest greens, Blacksmithing 150–200 |
| ARM-M4 | ☐ | Cinderscale (scale mail) | Mail | 27–30 | 6 | ✓ | ✓ | — | 2 | Leatherworking scale recipes, Cinderfall rewards |
| ARM-M5 | ☐ | Dungeon mail | Mail | 13–30 | 6 | ✓ | ✓ | — | 3 (crypt, slag, hollow) | Dungeon mail blues |
| ARM-M6 | ☐ | Slagborn / Blackanvil plate-look mail | Mail | 22–30 | 6 | ✓ | ✓ | — | 2 | Cinderfall elites' drops; Slagborn NPCs |
| ARM-T1F | ☐ | **Riftbreaker Battlegear** (Fighter raid set) | Mail | 30 | 6 | ✓ unique | ✓ unique | — | 1 | Raid tier set, 5 pieces |
| ARM-T1C | ☐ | **Dawnwarden Regalia** (Cleric raid set) | Mail | 30 | 6 | ✓ unique | ✓ unique | tabard-skirt | 1 | Raid tier set |
| ARM-T1D | ☐ | **Stonebloom Raiment** (Druid raid set) | Leather | 30 | 6 | ✓ unique | ✓ unique | ✓ | 1 | Raid tier set |
| ARM-P1 | ☐ | **Contender's** PvP sets ×3 classes | Mail ×2, Leather ×1 | 30 | 6 each | ✓ | ✓ | Druid ✓ | 1 each (team-neutral) | PvP vendor |
| ARM-E1 | ☐ | World-boss epic pieces | Mixed | 30 | individual | 0 | 2 (Barkhide, Cinderheart) | — | 1 | See item index: unique textures |

**Counts:** 23 appearance sets (counting the three PvP sets separately) · 138 texture regions authored once · **≈ 550 colourway region textures** in total · 22 helm meshes × 2 fits · 23 shoulder meshes × 2 fits · 7 robe skirts × 4 fits.

Named items that need their own unique texture or mesh on top of these are listed one by one in the [Named Item Index](07-named-item-index.md): 16 chests, 6 legs, 5 feet, 3 hands, 6 wrists, 11 belts, 6 helms, 8 shoulder pairs.

## 6. Cloaks, shirts, tabards

| ID | Done | Asset | Count |
|---|---|---|---|
| CLK-01 | ☐ | Cloak cloth mesh + sim setup | 2 (per rig) |
| CLK-02 | ☐ | Cloak designs (plain, trimmed, fur-collared, patched, pelt, scale, tattered, embroidered, hooded-look, crested, winged-membrane, burial shroud) | 12 designs × 3 colourways = 36 textures |
| CLK-03 | ☐ | Unique cloaks | 5 (see item index) |
| SHT-01 | ☐ | Shirts (brown linen, red, white formal, class starting shirt) | 4 textures |
| TAB-01 | ☐ | Guild tabard base (front/back region) | 1 template |
| TAB-02 | ☐ | Guild emblems | 40 emblem masks |
| TAB-03 | ☐ | Guild borders | 6 masks |
| TAB-04 | ☐ | Tabard colour palette | 16 swatches (data) |
| TAB-05 | ☐ | Fixed tabards: Solhaven, Hammerdeep, Thornwick Wardens, Freeholders, Athenaeum, Three Banners (PvP) | 6 textures |

Guild tabard permutations: 40 emblems × 16 emblem colours × 6 borders × 16 border colours × 16 backgrounds = ~980,000 from 46 masks.

## 7. Weapons — tier models

Three generic tiers per weapon type; each model gets 3 colourways (metal/wrap tints). Tier a = levels 1–10 (crude/copper), b = 10–20 (bronze), c = 20–30 (iron/steel).

| ID | Done | Type | Tier a | Tier b | Tier c | Models | Colourway textures |
|---|---|---|---|---|---|---|---|
| WPN-01 | ☐ | 1H sword | shortsword | arming sword | longsword | 3 | 9 |
| WPN-02 | ☐ | 1H axe | hatchet | bearded axe | war axe | 3 | 9 |
| WPN-03 | ☐ | 1H mace | club / cudgel | flanged mace | war hammer | 3 | 9 |
| WPN-04 | ☐ | Dagger | knife | dirk | stiletto | 3 | 9 |
| WPN-05 | ☐ | 2H sword | — (none below 10) | greatsword | claymore | 2 | 6 |
| WPN-06 | ☐ | 2H axe | wood axe | battle axe | greataxe | 3 | 9 |
| WPN-07 | ☐ | 2H mace | maul | great hammer | war maul | 3 | 9 |
| WPN-08 | ☐ | Polearm | — | — (level 20+) | halberd, glaive | 2 | 6 |
| WPN-09 | ☐ | Staff | walking staff | carved staff | runed staff | 3 | 9 |
| WPN-10 | ☐ | Shield | wooden round | bronze kite | steel heater, tower | 4 | 12 |
| WPN-11 | ☐ | Held off-hand | lantern | tome, totem | orb, censer | 5 | 10 |
| WPN-12 | ☐ | Bow | shortbow | — | longbow | 2 | 4 |
| WPN-13 | ☐ | Crossbow | — | light crossbow | — | 1 | 2 |
| WPN-14 | ☐ | Gun | hand-cannon | blunderbuss | rifle | 3 | 6 |
| WPN-15 | ☐ | Thrown | throwing knife, throwing axe | — | — | 2 | 2 |
| WPN-16 | ☐ | Profession tools (shown in hand during gather/craft) | mining pick, skinning knife, smith hammer, fishing pole, herb sickle, spanner | | | 6 | 6 |
| WPN-17 | ☐ | Ammo & sheaths | quiver, ammo pouch, arrow, bullet tracer mesh | | | 4 | 4 |

**Tier weapon totals:** 52 models · 121 colourway textures.

## 8. Weapons — unique models

From the [Named Item Index](07-named-item-index.md), every blue or epic weapon and every dungeon, raid, world-boss and PvP weapon gets its own model.

| ID | Done | Type | Unique models needed |
|---|---|---|---|
| WPU-01 | ☐ | 1H sword | 11 |
| WPU-02 | ☐ | 1H axe | 3 |
| WPU-03 | ☐ | 1H mace | 11 |
| WPU-04 | ☐ | Dagger | 4 |
| WPU-05 | ☐ | 2H sword | 4 |
| WPU-06 | ☐ | 2H axe | 5 |
| WPU-07 | ☐ | 2H mace | 7 |
| WPU-08 | ☐ | Polearm | 2 |
| WPU-09 | ☐ | Staff | 9 |
| WPU-10 | ☐ | Shield | 15 |
| WPU-11 | ☐ | Held off-hand | 6 |
| WPU-12 | ☐ | Gun | 1 |
| WPU-13 | ☐ | Class-quest weapons (level 20 and 30 rewards) | 8 (Fighter 2H + 1H pair + L30 weapon; Cleric shield + 2H mace; Druid staff ×2; L10 Cleric mace) |
| WPU-14 | ☐ | PvP Contender's weapons | 4 (1H, 2H, staff, shield) |
| WPU-15 | ☐ | World epics (6 listed in the items doc) | 3 weapons (Thornwake Longblade, Hearthbreaker, Staff of the Unlit Star) |

**Unique weapon totals:** 93 models, each with one texture.

## 9. Weapon and armor attachments & enchants (visual)

| ID | Done | Asset | Count |
|---|---|---|---|
| ATT-01 | ☐ | Weapon enchant glows (Striking white, Impact amber, Hollowbane violet, Dawnfire orange flame) | 4 effects (see [VFX](04-vfx.md)) |
| ATT-02 | ☐ | Sharpening stone / weightstone sheen | 1 shader effect |
| ATT-03 | ☐ | Wizard / mana oil shimmer | 2 |
| ATT-04 | ☐ | Shield spike mesh | 1 |
| ATT-05 | ☐ | Weapon chain mesh | 1 |
| ATT-06 | ☐ | Scope mesh (guns) | 3 sizes |
| ATT-07 | ☐ | Cleric Oath weapon glows (Radiance, Zealot, Justice, Light, Command) | 5 (see VFX) |

## 10. Mounts, forms and vehicles

| ID | Done | Asset | Notes |
|---|---|---|---|
| MNT-01 | ☐ | Horse rig + mesh | Idle, walk, run, jump, rear; rider socket |
| MNT-02 | ☐ | Horse colourways ×4 (bay, black, chestnut, grey) + tack | Level-30 mounts, Solhaven |
| MNT-03 | ☐ | Ram mount (shares the ram creature rig) + saddle | |
| MNT-04 | ☐ | Ram colourways ×4 (grey, brown, white, black) | Level-30 mounts, Hammerdeep |
| MNT-05 | ☐ | *Vault Charger* (raid drop) — armoured spectral horse | Unique texture + glow |
| MNT-07 | ☐ | Crag eagle taxi (flight path mount) + harness | Fly idle, fly forward, bank, take-off, land |
| MNT-08 | ☐ | *The Hearth-Oath* (capital ship) | Hull, deck, sails, wheel, crew stations; sails animated |
| MNT-09 | ☐ | Mine-cart (Stoneheart Deeps ride) | Cart + rider seat pose |
| MNT-10 | ☐ | Epic mounts (level 60) | **Out of 1–30 scope**; reserve: armoured warhorse ×4, armoured ram ×4 |

## 11. Totals for this document

| Category | Assets |
|---|---|
| Rigs and bodies | 2 rigs, 4 bodies |
| Customisation | 110 |
| Player animation clips | 192 (96 × 2 rigs) + 12 mount/rider |
| Armor appearance sets | 23 sets → ≈ 550 region textures, 44 helm fits, 46 shoulder fits, 28 robe skirts |
| Unique named armor pieces | 61 |
| Cloaks, shirts, tabards | 36 + 5 + 4 + 46 masks + 6 |
| Weapon models (tier + unique) | 52 + 93 = 145 |
| Weapon textures | 121 + 93 = 214 |
| Mounts / vehicles | 9 |
