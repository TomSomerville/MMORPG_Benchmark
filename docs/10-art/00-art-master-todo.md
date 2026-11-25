# Art Master To-Do (levels 1–30)

[← Master Plan](../../MASTER_PLAN.md)

The complete list of art the game needs before code begins: every texture, UI element, 3D model, animation, particle and effect for the level 1–30 launch game. **All of it is AI-generated; no licensed or bought asset packs are used** (see §8). This page is the summary; the nine linked lists hold the items by category, and the **[Asset Manifest](../15-asset-manifest/00-manifest-index.md)** expands them into one row for every single asset, with a description to generate from, in the order the forge makes them.

## 1. The lists

| # | List | What it holds | Line items |
|---|---|---|---|
| 1 | [Player Characters, Armor & Weapons](01-characters-armor-weapons.md) | Bodies, customisation, player animations, the armor appearance system and all 23 armor sets, cloaks, tabards, 145 weapon models, mounts | ≈ 1,440 assets |
| 2 | [Creatures & NPCs](02-creatures-npcs.md) | Every creature grouped by rig, every boss, every NPC outfit, critters | ≈ 62 rigs, 350 skins, 650 clips |
| 3 | [Environments & Props](03-environments-props.md) | 20 building kits, world objects, gathering nodes, nature libraries, a checklist for each of the 11 zones, 2 cities and 5 instances | ≈ 1,400 assets |
| 4 | [Spell, Particle & World Effects](04-vfx.md) | Every class ability and talent effect, item and profession effects, the creature ability library, boss mechanics, weather and feedback effects | ≈ 725 effects |
| 5 | [User Interface](05-ui.md) | Every HUD element, window, screen, map, crest, cursor and font | ≈ 650 textures, 49 paintings |
| 6 | [Icons](06-icons.md) | Every ability, talent, item, material, consumable and quest icon | ≈ 2,110 icons |
| 7 | [Named Item Index](07-named-item-index.md) | All 765 named pieces of equipment, one row each, with the art each needs (generated from the design and quest text docs) | 773 rows |
| 8 | [Quest Art Index](08-quest-art-index.md) | All 296 quests, one row each, with the item icons and world objects each implies (generated from the zone docs) | 296 rows |
| 9 | [Audio](09-audio.md) | Music, ambience, player, spell, creature, boss, voice and interface sounds | ≈ 2,000 assets |

## 2. Grand totals

| Kind of asset | Count | Where |
|---|---|---|
| Character and creature **rigs** | ≈ 64 (2 player + 62 creature/boss) | Lists 1, 2 |
| **Animation clips** | ≈ 850 (204 player and mount, 650 creature) | Lists 1, 2 |
| **3D models** — characters and creatures | 4 player bodies, 110 customisation pieces, ≈ 350 creature and NPC skins/outfits | Lists 1, 2 |
| **3D models** — armor pieces | 44 helm fits, 46 shoulder fits, 28 robe skirts, ≈ 14 unique named helms/shoulders | List 1 |
| **3D models** — weapons, shields, held items | 145 (52 tier, 93 unique) | List 1 |
| **3D models** — environment | ≈ 700 kit pieces, ≈ 220 nature models, ≈ 175 props and world objects, 23 gathering nodes | List 3 |
| **Textures** — armor regions | ≈ 550 colourway textures + ≈ 47 unique | List 1 |
| **Textures** — terrain | ≈ 80 tiling ground textures in 11 sets | List 3 |
| **Skies / lighting presets** | ≈ 45 | List 3 |
| **Particles and effects** | ≈ 725 | List 4 |
| **UI textures** | ≈ 650 | List 5 |
| **Paintings** (loading screens, maps, talent backgrounds, key art) | ≈ 60 | List 5 |
| **Icons** | ≈ 2,110 (≈ 1,150 unique paintings) | List 6 |
| **Music** | ≈ 108 tracks and stings (≈ 3.5 hours) | List 9 |
| **Ambience** | ≈ 55 beds, ≈ 160 spot sounds | List 9 |
| **Sound effects and voice** | ≈ 1,700 | List 9 |
| **Total line items to tick off** | **≈ 9,100** | |

## 3. How permutations are covered

"Every possible permutation" is reached by combining a fixed set of parts, not by authoring each combination. The rules, and what they multiply out to:

| Permutation | Parts authored | Combinations covered |
|---|---|---|
| Player appearance | 4 bodies, 24 skins, 24 faces, 32 hair meshes, 8 colour ramps, 22 facial pieces | ≈ 46,000 distinct characters |
| Dwarf cultures | NPC outfits and voice sets only | Hallborn and Dalefolk NPCs; player dwarves have no culture choice |
| Armor on a body | 23 appearance sets × 6 body regions + helm + shoulders, in 1–7 colourways, each fitting all 4 bodies | Any mix of any pieces on any body: every set works on Human and Dwarf, male and female |
| Armor type by class | Cloth, leather, mail all wearable by rule (plate is level 40, out of scope) | Fighter and Cleric: 3 types; Druid: 2 |
| Named items | 224 unique + 541 tier-recolour | All 765 named items in list 7 |
| Unnamed and random-suffix items | Tier art by slot and level band; 16 suffixes change stats, not looks | Every random green in the game |
| Weapons in hands | 15 weapon types × 3 tiers × colourways + uniques; main hand, off hand, two-hand, ranged, sheathed | Every weapon on every body |
| Guild tabards | 40 emblems, 6 borders, 16 colours | ≈ 980,000 tabards |
| Creatures | 62 rigs re-skinned | ≈ 350 creatures and NPCs |
| NPC humanoids | ≈ 140 outfits on the 4 player bodies and customisation parts | Unlimited named and ambient NPCs |
| Spell effects | 7 school palettes × shared blocks + bespoke per ability | Every ability, rank and talent variant; ranks reuse the same effect |
| Battleground teams | Red / blue / yellow dressing | 3 teams now, 3 allegiances later |
| World states | Paired models (mill/burned mill, forge cold/lit, lantern dark/lit, beacon, graves, ward-pylons 4 states) | Every quest-driven change |
| UI | One Concord skin; palette reserved for Wildpact and Covenant | Skins swap without re-layout |

## 4. Technical targets for every asset

| Asset | Target |
|---|---|
| Style | Stylised, low-poly, hand-painted; strong silhouettes; no photo textures. Defined in full, with measurable rules, in [Art Direction](10-art-direction.md) |
| Model format | glTF 2.0 binary (.glb), metres, Y-up, one material per model where possible |
| Texture format | PNG source, power-of-two; albedo + optional emissive mask; no normal maps on small props |
| Player body | 4–6k triangles; 1024² skin atlas; LOD1 at 50% |
| Creature | 1.5–5k triangles; 512²–1024²; boss 8–12k and 2048² |
| Weapon / shield | 300–800 triangles; 256² |
| Helm / shoulder | 300–600 triangles each; shares the set's 512² |
| Building | 2–8k triangles per whole building; kit pieces share trim-sheet atlases (2048² per kit) |
| Prop | 50–600 triangles; shared 1024² prop atlases |
| Terrain | 1024² tiling, 6–8 per zone, splat-blended |
| Icons | 128² source, 64² shipped |
| UI | Authored at 2× (for 4K), 9-slice where possible, packed into atlases |
| Effects | Flipbook sheets ≤ 1024²; ≤ 150 particles per ordinary spell, ≤ 600 for boss effects |
| Naming | `chr_`, `arm_`, `wpn_`, `cre_`, `npc_`, `env_`, `prop_`, `nat_`, `vfx_`, `ui_`, `ico_` + snake_case name + `_v01`; the ID from these lists goes in the asset's metadata |
| Generation record | Every asset logged with the tool and model version, the prompt, the reference images, the seed where available, the date, and which gates it passed. No bought, licensed or CC0 packs. Before a tool is adopted, its terms are checked to confirm that output may be used commercially |

## 5. Order of work

**The order in which assets are generated is the order of the [Asset Manifest](../15-asset-manifest/00-manifest-index.md): one row per asset, in order of first appearance in the game.** The blocks below are kept as a summary of what each build milestone needs; where the two differ, the manifest's order is the one the forge follows. "Block A" now means the calibration set: the style bible plus the first row of every kind in the manifest.

Ordered so that each block unlocks a build milestone in the [Roadmap](../08-tech/roadmap.md) and the earliest blocks are the smallest.

| Block | Art to finish | Unlocks milestone | Rough share of total |
|---|---|---|---|
| **A — Style guide** | Palette, one finished example of each asset type (1 body, 1 creature, 1 building, 1 weapon, 1 spell effect, 5 icons, 1 window) | Sets the bar for everything else | 1% |
| **B — Core kit** | Human rig + male body, canine and boar rigs, player locomotion and melee/cast clips, tier-a weapons, ARM-C1/L1/M1, shared VFX blocks, HUD and core windows, fonts, cursors | M0–M1 (movement and combat on a test map) | 8% |
| **C — Brightmead Vale** | KIT-01/02/06/12/13/15, temperate nature, Z-BM rows, its 12 creatures, Burrowkin, Gillkin, Ashhand outfits, level 1–10 class effects and icons, quest/vendor/trainer UI | M2 (vertical slice) | 10% |
| **D — Second race and travel** | Dwarf rig and bodies, KIT-04, Embercrag, both capitals, the ship and sea route, eagle taxi, map paintings | M3 | 12% |
| **E — Classes complete** | All remaining ability and talent effects and icons, talent backgrounds | M4 | 8% |
| **F — Professions** | Nodes, material and consumable icons, tier-b/c armor and weapons, crafting UI, named crafted items | M5 | 9% |
| **G — 5–10 and 10–20 zones** | Harrowfield, Russetwood (autumn library), Stonewake Dale (KIT-05), Stoneheart Deeps (KIT-07, cavern flora), Thornwick, Ironroot and their creatures and outfits | M6 | 18% |
| **H — Dungeon 1** | KIT-08, Gallowmere Crypts, its bosses and effects, dungeon armor sets | M7 | 4% |
| **I — 20–30 zones and dungeons 2–3** | Cinderfall, Riftlands (KIT-11, KIT-19), Veilmoor, KIT-09/10, The Slagworks, Hollowspire Keep | M8 | 17% |
| **J — PvP** | The Dustpit, Crownfall, team dressing, PvP sets, scoreboard UI | M9 | 3% |
| **K — Endgame** | The Hollow Throne, raid bosses and effects, tier sets, world bosses, mounts | M10 | 8% |
| **L — Polish** | Guild tabards and guild bank UI, emotes, critters, weather, loading screens, remaining icons | M11 | 2% |

## 6. What is not in these lists

- **Levels 31–60** — plate armor, epic mounts, the 11 future zones, future races and classes. Reserved names appear where they affect today's assets (elf rig, faction UI skins).
- **Marketing art** beyond the logo and login key art.
- **Minimap tiles and navmesh** — generated from the built zones, not hand-made.

## 7. Keeping the lists true

Lists 7 and 8 are generated from the design documents; regenerate them whenever items or quests change. Lists 1–6 are hand-written against the design documents as of version 0.2 of the [Master Plan](../../MASTER_PLAN.md); when a zone, creature or ability changes, change its row here in the same edit.

**The full list, one row per asset, is the [Asset Manifest](../15-asset-manifest/00-manifest-index.md)**, generated from these lists and the design data by `tools/doc-generators/asset_manifest.py`. Where a row here stands for several assets ("×7 schools", "40 pieces"), the manifest names each one, and its count (8,984 rows) replaces the estimates below. Regenerate the manifest after changing any list.

All counts are planning estimates meant for scoping and tracking. Counts given as exact (765 named items, 296 quests, 214 class icons, 145 weapon models) come from the documents; counts marked ≈ are sums of the ranges in each list.

## 8. How the art is made

Decided 2026-11-12: **every visual asset is AI-generated. No licensed, bought or CC0 asset packs are used.** The assets are produced by the **[Asset Forge](../14-asset-pipeline/00-asset-forge.md)**: two machines (a GMKtec EVO-X3 and an RTX 5070 Ti desktop) running twenty-one pipelines, one per kind of asset, built as the first step of the game build. **That specification is the authority on how each asset is made.** No person reviews assets during the build: every review gate named in the table below is carried out by the forge's automatic checks. The table is kept as a summary of what each kind of asset must achieve.

### Pipeline by asset type

| Asset | Steps | Review gate before it is accepted |
|---|---|---|
| Style guide (block A) | Generate a large set of concept images; pick the look; fix the palette, line weight, proportions and material rules; produce one finished example of every asset type | The style bible passes the forge's checks against [Art Direction](10-art-direction.md) and is frozen. Everything after is judged against it |
| Concept and reference sheets | For each rig, set, kit and creature family: front, side and back views generated from the style guide and the description in these lists | Matches the style guide; silhouette readable at game distance |
| 3D models (characters, creatures, props, kit pieces, weapons) | Image-to-3D or text-to-3D generation from the reference sheet, then automatic and manual retopology to the triangle budget, UV unwrap to the shared layout, texture generation or projection, palette correction | Triangle count and texture size within the targets in §4; no holes or inverted faces; UVs on the shared layout; reads correctly beside an approved asset |
| Rigs and skinning | Automatic rigging to one of the 64 standard skeletons, then weight clean-up | Deforms cleanly through a fixed test animation |
| Animation | Generated motion (text-to-motion or video-to-motion) retargeted to the rig, then trimmed, looped and timed to the gameplay values (swing speeds, cast times) | Loops without a pop; contact frames land on the gameplay timing; feet do not slide |
| Armor region textures and colourways | Generated once per set on the shared body layout; colourways produced by palette remap, not regeneration | Seams invisible on all 4 bodies |
| Terrain and tiling textures | Generated tileable, then checked for repetition at 4 × 4 tiles | No visible seam or repeat |
| Icons | Generated in batches from a fixed icon prompt template per category, on the standard frame | Readable at 32 px; no text or stray symbols; consistent lighting direction |
| UI frames and paintings | Generated, then vectorised or cleaned for 9-slice use; paintings upscaled to target size | Slices tile; text areas clear |
| Effects | Flipbook sheets generated per element (flame, leaf, spark, smoke), assembled into particle systems by hand | Reads at the school's colour; within the particle budget |

### Rules

| Rule | Detail |
|---|---|
| One style | Every generation uses the style guide's reference images and palette. An asset that looks like a different game is regenerated, not blended in |
| Regenerate before repairing | If an asset needs more than about an hour of hand repair, it is regenerated with a better reference |
| No real people, brands or existing games | Prompts never name a living artist, a studio, a franchise or a real person, and outputs are checked for look-alikes of existing characters. This protects the game legally and keeps it original |
| Acceptance | Each list's ☐ is ticked only after the asset has passed the forge's gates and the acceptance check in the game engine ([Placeholders and Swapping](../14-asset-pipeline/04-placeholders-and-swap.md)), not in the generator. No person approves assets during the build |
| Hand work | Where a step above says "manual" or "by hand", the builder's scripts do it; nothing waits for an artist |
| Records | The generation record in §4 is kept for every asset, so any asset can be reproduced or replaced |
| Tool terms | A tool is used only if its terms allow commercial use of its output. The check is recorded once per tool and version |
| Disclosure | The game states that its art is AI-generated wherever a store or platform requires it; a statement is part of the launch checklist (task T-M14-09) |

### What this changes in the lists

Nothing is removed. The counts in §2 are the same whether an asset is bought or generated. What changes is where the effort goes: less on acquisition, more on the style guide (block A), on clean-up of generated meshes and rigs, and on review. The three areas where generation is weakest today, and so where most hand work should be expected, are **rigging and skinning**, **looping gameplay animation**, and **keeping modular building kits dimensionally exact** so pieces snap together.

### Audio and fonts

- **Audio is decided:** music, sound effects and voice lines are all AI-generated too (2026-11-12). The audio pipeline and rules are in [Audio](09-audio.md#how-the-audio-is-made).
- **Fonts** are constructed by the forge's font pipeline ([P20](../14-asset-pipeline/03-audio-pipelines.md#p20--fonts-3-typefaces)), not taken from a licensed typeface. The engine's built-in font is the fallback.