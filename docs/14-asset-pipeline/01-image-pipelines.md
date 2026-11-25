# Asset Pipelines 1 — Images and Textures (P01 to P09)

[← Asset Forge](00-asset-forge.md) · Next: [3D models, rigs and animation](02-3d-pipelines.md) · [Audio](03-audio-pipelines.md)

One pipeline per kind of 2D asset. Each lists what it reads, the steps, the models to try in order, what it writes and the checks it must pass. Shared rules (style bible, palette lock, the owner's approval, retries, fallbacks, placeholders) are on the [Asset Forge](00-asset-forge.md) page. Model names are candidates to be confirmed at bring-up, as explained in [§11 there](00-asset-forge.md#11-model-choices-and-how-sure-they-are).

## Shared image tools

| Tool | Candidates, in order | Used for |
|---|---|---|
| Text-to-image model | **In use: Z-Image Turbo**, run through ComfyUI at 8 sampling steps from a text prompt (its licence is recorded in the bring-up report for the owner to confirm). Other candidates: a permissively licensed model that accepts reference images: Qwen-Image or FLUX.1 schnell (both Apache 2.0); then SDXL with an image-prompt adapter. **Newer candidates to test first at bring-up** (released November 2026; licences and AMD support unverified): **P-H3-Image** (open weights; a 20 GB 4-bit version; about 21 GB of graphics memory, which Forge A has and Forge B does not; 8 sampling steps; accepts up to 9 reference images, which suits the style-anchor conditioning; strongest at photographic and illustrated looks) and **P-JiT** (Apache 2.0, 2 billion parameters, small and fast, experimental) | All generation below |
| Few-step sampling | **NitroFusion 2**: a distillation that brings multimodal diffusion transformers down to **one or two sampling steps** at comparable quality, with weights and a ControlNet published. If a NitroFusion 2 version exists for the chosen image model, use it: on Forge A's slower graphics, cutting 8–30 steps to 1–2 is the largest single speed-up available. Check that the style adapter and reference conditioning still work with it; if not, use it only for the high-volume pipelines (icons, flipbook stills) | P02, P05, P08 first |
| Background removal | BiRefNet or an equivalent matting model | Icons, UI pieces, flipbook frames, reference sheets |
| Upscaler | Real-ESRGAN class 2× or 4× model | Paintings, UI at 2× |
| Tiling | Forge script that closes the seams of a generated picture: each edge is cross-faded into the picture's own middle (the picture shifted by half its width), first across, then down; then a seam check | Terrain |
| Palette lock | Forge script: nearest palette colour in OKLab, 60% blend, toward the zone's ramps where the asset belongs to a zone; then the result is held inside the style's value range | Every colour image **except icons** (P02) |
| Vision checker | An image-text embedding model (SigLIP base), comparing the image against "yes" and "no" descriptions for each checklist question ([Asset Forge §7](00-asset-forge.md#7-automatic-quality-gates)) | The visual gate |
| Segmentation | A small local model that detects and masks objects and regions (for example Mirage, 22 MB, released November 2026; or a Segment Anything class model) | Material masks for the repaint pass and for colourways; background removal checks |

Fallback for every image pipeline when no image model passes bring-up: **procedural painting**, a forge script that builds the image from palette colours, gradients, noise and simple vector shapes chosen by asset type and subject keywords. It is plain but consistent.

## P01 — Style bible

| | |
|---|---|
| Makes | `forge/style/`: the 32-colour palette, 8 anchor images, proportion sheets for the 4 player bodies, material swatches (cloth, leather, mail, wood, stone, metal, bark, snow, lava), and the prompt fragments every other pipeline uses. The **icon style bible** (`forge/style/icon-style.json`, specified under [P02](#p02--icons-about-2050)) is kept beside it and approved separately |
| Reads | **[Art Direction](../10-art/10-art-direction.md)**, which defines the look in full: the five rules, proportions, surface rules, the eight palette ramps, culture and zone colours. The style bible is generated to match that page, not invented. Also the zone themes in the zone documents |
| Also makes | The **style adapter**: once the anchors are approved and about 150 approved images exist, train a small adapter (LoRA) for the image model on them, and use it in every image pipeline together with reference conditioning. If training does not run on this hardware, or the image model in use takes no reference images, skip it and rely on the prompt fragments. None is trained until the anchors are approved. Also the **material library** of about two dozen base materials (Art Direction §3), generated once with P05 and reused by every other pipeline |
| Steps | 1. **Build the palette by rule**, not from pictures: the eight ramps of Art Direction §4 (warm stone, cool stone, wood, earth, foliage, autumn, steel, gold), four values each, computed in OKLCh with shadows shifted toward blue-violet and lights toward yellow. That is the 32 colours; it is written to `forge/style/palette.json`. 2. **Make the anchors with the image model**: several candidates for each of the eight anchor subjects the Asset Manifest names, prompted from Art Direction's own words. People and animals are painted as solid, rounded forms, not flat drawings, and each is shown with the 3D model image-to-3D makes of it, because a 3D model must be able to come from the anchor. 3. Score the candidates with the vision checker for the style words and for mutual similarity, and put the most consistent of each subject on the review page. 4. **The owner chooses or refuses** ([Asset Forge §7a](00-asset-forge.md#7a-the-owners-approval)). 5. Generate the proportion sheets and swatches to match the chosen anchors. 6. Write the prompt fragments: a positive style line, a negative line (photo, realistic, text, watermark, logo, signature, blurry), and one line per material. 7. Calibrate the style gates on the result ([Asset Forge §7](00-asset-forge.md#7-automatic-quality-gates)) |
| Without an image model | A model-free painter can make a stand-in bible, enough to bring up the gates and the model-free makers. It is never the game's look: anchors and figures made that way were refused by the owner |
| Checks | Eight anchors exist and pass the vision checklist; palette has 32 colours in 8 ramps of 4; every swatch tiles |
| Runs | Once, before every other pipeline. Its outputs are frozen when the owner approves them: putting a different bible into use means calibrating the gates again and regenerating everything made from the old one, and is done only on the owner's word |
| Status, 2026-11-25 | The palette's eight ramps are accepted by the owner. The owner approved the candidate bible made by the image model for buildings, props, weapons and environments; its anchors are the human cottage, the mountain dwarf hall, the hill dwarf steading, the sword, staff and shield, the forest clearing and the gothic ruin. People and creatures (player bodies, NPCs and creatures) are not judged by the style bible: they are generated, fitted to their rig and approved batch by batch. Each pipeline the style bible governs still shows a first batch before it makes its assets in number ([Asset Forge §7a](00-asset-forge.md#7a-the-owners-approval)) |

## P02 — Icons (about 2,050)

Icons do not follow the general style bible. They have their own, the **icon style bible** (`forge/style/icon-style.json`), which the owner approved on 2026-11-23 together with a 36-icon reference set. P02 needs that approval and its own, and has both.

| | |
|---|---|
| Reads | [Icons list](../10-art/06-icons.md), [Named Item Index](../10-art/07-named-item-index.md), [Quest Art Index](../10-art/08-quest-art-index.md), through each icon's manifest row; the icon style bible |
| Sizes | **Drawn at 512², kept at 128², shown at 64².** The model paints at 512, a quarter of the work of 1024 and far more than the icon keeps |
| Template | "`<frame>`: `<subject>`. `<look with the kind's hue>`." Frame: "a square painting completely filled with paint from edge to edge, an extreme close-up cropped so tightly that the subject is cut off by the edges of the picture, no empty background, no border, no writing, no numbers". Look: "a tiny hand-painted fantasy game ability picture, rough opaque digital brush strokes, very high contrast, the whole picture washed in `<hue>`, a bright glowing light inside the picture with a white-hot centre, dark corners" |
| Subject | From the manifest row's description. An item is the item itself, close up. **An ability is asked for as a scene, not an emblem**: "a painted scene of `<what it does>`, shown by a `<shape>` in motion, a fantasy ability"; a request for a symbol or emblem comes back as letter-like glyphs. A subject is described by what it is made of and its period, or the model draws the modern thing. **Quoted names are taken out of prompts**: a model asked for a name in quotes writes the word. A row that gives an entry no subject of its own (a bare number) is not sent to the model |
| Steps | 1. Choose the icon's kind (below) and build the prompt. 2. Generate at 512². 3. If the picture has a pale border or sits on a flat tile, draw it again with another seed, up to three times. 4. Reduce to 128². Nothing else is done to it: **no palette lock, no added grain, no frame** |
| Variants | Recolours (tier and colourway items, potion tints, recipe quality tints) are made by hue-shifting an accepted base icon, not by regenerating |
| Checks | 128² PNG; painted to the edges (no pale border, no flat tile); subject readable at 32² (the vision checker shown the 32² version must still match the subject); no text; not near-identical to another accepted icon (perceptual hash distance above a threshold). The general style bible's palette and grain gates are not applied to icons |
| Fallback | The model-free icon painter, for a machine with no image model and for entries with no subject of their own |
| Rate | About 5 s each at 512² on Forge A (measured) |

The rules of the icon style:

1. **A tiny painting that fills the whole square.** The subject is cropped tight and runs off the edges. No empty background.
2. **One strong colour washes the whole icon**, set by what the icon is (table below), so a bar of icons can be read by colour.
3. **A bright glowing light inside the picture**, white-hot at its centre, and **dark corners**.
4. **Rough opaque brush strokes and very high contrast**, so the shape still reads at 64 pixels.
5. An ability shows the thing it does; an item shows the item, close up, in its kind's colour.
6. **No writing, numbers, borders, tiles or frames.** The interface draws the slot; the icon is only the picture.
7. **One uniform background colour, `#141418` (near-black), for every icon.** Where a picture does not reach an edge, the gap is that colour, the same for every icon and not a colour per kind.
8. The style is described in the prompt by its properties only. No existing game, studio or artist is named, and no existing icon is copied.

| Kind | The icon is washed in | Which icons |
|---|---|---|
| physical | steel grey and blood red | Abilities with no school word of their own |
| holy | blazing gold and white | Abilities named for light, blessing, healing, prayer, oaths; cleric abilities by default |
| nature | vivid emerald green | Abilities named for thorns, roots, poison, storm, growth, the moon; druid abilities by default |
| fire | fiery orange and deep red | Abilities named for fire, flame, burning, embers |
| frost | icy blue and white | Abilities named for frost, ice, chill, snow |
| arcane | bright violet and magenta | Abilities named for the arcane, magic, mana, runes |
| shadow | deep purple and black | Abilities named for shadow, curses, fear, death, draining |
| equipment | warm brown and dull steel | Weapons, armor and every item no other kind claims |
| consumable | rich crimson and dark glass green | Potions, elixirs, flasks, bandages, scrolls |
| material | earthy brown and copper | The crafting-material rows |
| food | warm golden brown | The cooking rows; meat, bread, fish, cheese, ale |
| quest | old gold and parchment | Quest items |

The kind is chosen from the icon's own name and what it shows, never from wording that every row shares.

## P03 — UI frames, panels, buttons and cursors (about 650)

The interface in the game today is **drawn in code by the client** in the stone-and-brass look the owner chose as its direction ([User Interface list](../10-art/05-ui.md)), and uses none of P03's textures. The owner's liking of that direction is not an approval to make P03's assets, so P03 is held ([Asset Forge §7a](00-asset-forge.md#7a-the-owners-approval)). The method below is what P03 does when it is approved. Icons are not framed by any pipeline: the interface draws the slot round the picture.

Open: whether the code-drawn interface is final, or P03's texture art is still wanted, is the owner's decision.

| | |
|---|---|
| Reads | [User Interface list](../10-art/05-ui.md), [UI Specification](../08-tech/ui-specification.md) for sizes |
| Method | UI needs exact edges, so it is **built, not painted whole**. 1. Generate material textures for the frame motif (worn brass, grey stone, dark leather, parchment) with P05. 2. A forge script assembles each frame as a 9-slice from those materials: corners, edges, fill, bevel and inner shadow, at 2× size. 3. Ornaments (crests, corner flourishes, class and faction emblems) are generated as single centred images, background removed, and composited |
| Checks | Exact pixel size from the UI specification; 9-slice borders tile without a seam when stretched to 3 sizes; text areas have enough contrast for the body font (WCAG 4.5:1 against the fill); alpha edges clean |
| Fallback | Flat panels with a 2-pixel border in palette colours |

## P04 — Paintings: loading screens, maps, talent backgrounds, key art (about 60)

| | |
|---|---|
| Reads | [User Interface list](../10-art/05-ui.md); zone themes; the [world layout](../13-world/00-world-layout.md) for maps |
| Steps (scenes) | Each loading screen, the login key art, the intro panels and the talent backgrounds is painted from **one scene line per place**, taken from what the world documents say of that place and held in a table in the pipeline. 1. Generate at half the final size (1920 × 1088 for a wide painting, cut to 16:9; 1024² for a square one). Wide scenes keep the horizon in the lower half and the upper left third calm; square ones are quiet enough to lie behind an interface; no people in the foreground. 2. Palette lock (60%, toward the zone's ramps) and hold to the style's value range. 3. Bring up to the contract's size (3840 × 2160 for wide paintings) |
| Steps (maps) | Maps must match the game, so they are **drawn from the world's own data, never painted by the image model**: the world generator writes top-down map tiles for each zone (one pixel to the metre, north at the top) and the map is made from those, so coastlines, roads and landmarks are where the game has them. Labels are added by the client from string tables, never painted in. Until a zone's terrain exists, its map is drawn from the layout's grid map |
| Checks | Size; no text in the image; maps: road and hub positions within 2% of the layout coordinates (compared by feature points) |

## P05 — Tiling textures: terrain, trim sheets, materials (about 80 terrain, 20 kit atlases)

| | |
|---|---|
| Reads | [Environments list](../10-art/03-environments-props.md); the zone's theme and palette notes |
| Steps | 1. Terrain: generate at 1024², the ground seen from directly above, filling the picture edge to edge, in even light with no cast shadows and no single object standing out. 2. Close the seams by cross-fade (shared tools). 3. **Reduce contrast by 30%** about the picture's mean colour: ground is what everything else stands on, and stays calm. 4. Palette lock toward the zone's ramps. 5. Seam check: tile 4 × 4 and measure edge discontinuity and visible repetition. 6. **No height map is written.** The contract is one PNG; the client derives the blend height from the texture's luminance when it loads it. 7. Trim sheets and ramps have a layout to keep, so they are not painted whole by the model: each strip (planks, stone courses, roof tiles, metal bands) is made separately and packed into the kit's 2048² atlas at fixed rows, so kit geometry can rely on fixed UV rows |
| Checks | 1024² PNG; seam error under threshold; no single feature that repeats obviously at 4 × 4; average colour within the zone's palette ramp |
| Fallback | Noise-based procedural materials tinted from the palette |

## P06 — Armor region textures and colourways (about 550 textures)

| | |
|---|---|
| Reads | [Characters, Armor & Weapons](../10-art/01-characters-armor-weapons.md): 23 sets, 6 region pieces each (chest, legs, feet, hands, wrist, waist), painted for the shared region layout of the player bodies ([Characters §4](../10-art/01-characters-armor-weapons.md#4-how-armor-is-built-the-permutation-rules)): fixed rectangles for the upper arm, lower arm, hand, upper torso, lower torso, upper leg, lower leg and foot |
| Steps | 1. For each set, generate front and back views of the full outfit on the proportion sheet (P01), conditioned on the anchors. 2. Project those views onto a body on the shared layout and bake to that layout, giving the set's region textures, each inside the rectangles its piece covers (a chest piece the torso and the arm regions it covers, gloves the hands and a cuff on the lower arm, boots the feet and lower legs, trousers the upper and lower legs, a belt a band at the waist, bracers the lower arm). 3. Fix seams by inpainting across UV borders in texture space. 4. One texture serves every race and both sexes, since all player bodies share the layout; a separate version for men or for women is painted only where a piece needs one |
| In the game | The client lays a character's region textures over its skin texture in a fixed order (shirt, chest piece, tabard over the chest piece, and so on). Shapes a texture cannot make are geometry swaps built into the body mesh, and helms and shoulders are attached models ([P13](02-3d-pipelines.md)) |
| First results | Under the approval rule a first batch, the starting cloth set and one set each of leather and mail, is made and shown to the owner. The rest is made only after he approves it ([Asset Forge §7a](00-asset-forge.md)). The owner approved the first batch on 2026-11-25, "for tonight, may revisit", and P06 is made in number |
| Colourways | Made by **palette remap**: each set's base texture is segmented into material masks (primary cloth, secondary, trim, metal), and each colourway assigns a palette ramp to each mask. The zone-based colourway rule in the armor list picks the ramps |
| Checks | Region sizes; seams invisible in renders from 8 angles on all 4 bodies; skin does not show through where the region should cover |
| Depends on | The 4 player body meshes from P13, **re-wrapped onto the shared region layout**. A body made by rig-fit ([P13](02-3d-pipelines.md)) comes out with a UV layout of its own; each player body is re-wrapped onto the template bodies' shared layout, with its own texture baked into it, and these textures fit it from then on. They also fit the template body, which is kept beside the fitted one ([Placeholders and Swapping §2a](04-placeholders-and-swap.md#2a-fitted-bodies-kept-templates-and-dressed-bodies)) |

## P07 — Skins and outfits: creature re-textures and NPC clothing (about 350)

| | |
|---|---|
| Reads | [Creatures & NPCs](../10-art/02-creatures-npcs.md): each rig's list of skins |
| Steps (a rig-fitted base model) | Where the rig's base model is a generated mesh fitted by rig-fit ([P13](02-3d-pipelines.md)), each skin is **that model's own baked texture, tinted for the variety**: the texture multiplied by one colour per variety (a grey wolf, a paler pup, a near-black stalker), on the model's own UV layout. A named creature has its own skin row and its own tint |
| Steps (a repainted skin) | For a skin that needs markings a tint cannot give: 1. Render the rig's base model from 6 views with its UV-island map. 2. Generate the new skin as a repaint of those views (image-to-image at moderate strength) from the skin's description: colour, markings, wear, size cues. 3. Project and bake to the rig's UVs. 4. Palette lock |
| NPC outfits | Two forms. A **painted outfit** is a texture on the template body's shared UV layout, made by P06's method with the outfit description from the roster's role. A **dressed body** is a whole generated body already wearing the outfit, made by P13's route for one outfit on one body; where one exists the client uses it in place of body plus texture ([Placeholders and Swapping §2a](04-placeholders-and-swap.md#2a-fitted-bodies-kept-templates-and-dressed-bodies)) |
| Checks | Same UV layout as the base; distinct from the base skin (colour histogram distance above a threshold) so players can tell creatures apart; no seams |

## P08 — Effect flipbooks and particle textures (about 725 effects from about 120 sheets)

| | |
|---|---|
| Reads | [Spell, Particle & World Effects](../10-art/04-vfx.md) |
| Method | Effects are assembled from a small library. 1. Generate **element sheets**: flame, smoke, spark, leaf, petal, dust, water splash, ice shard, holy ray, arcane rune, shadow wisp, lightning, magic ring. Each is an 8 × 8 flipbook at 1024², made by generating a short looping clip of the element on black (an image-to-video model if one passes bring-up; otherwise frames made by animating a generated still with procedural distortion), then removing the background by luminance. 2. Each effect in the list is then a **particle definition** (a data file: which elements, colours from the school palette, emission, size, speed, lifetime) written by the builder from the effect's description. No generation per effect |
| Checks | Sheet size and frame count; loop: last frame flows into the first; alpha clean; particle count within the budget in the technical targets |
| Fallback | Procedural sheets from noise and simple shapes |

## P09 — Skies and lighting presets (about 45)

| | |
|---|---|
| Reads | [Environments list](../10-art/03-environments-props.md); zone weather tables |
| Method | Skies are procedural with generated detail. 1. A gradient sky per zone and time of day from the palette. 2. Cloud layers generated as tiling textures (P05). 3. Lighting presets (sun colour and angle, ambient, fog colour and distance) derived by rule from the zone theme and stored as data |
| Checks | Horizon seamless; fog colour matches the sky at the horizon; brightness within the range that keeps nameplates readable |
