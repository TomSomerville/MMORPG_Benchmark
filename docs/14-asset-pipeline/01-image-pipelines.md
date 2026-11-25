# Asset Pipelines 1 — Images and Textures (P01 to P09)

[← Asset Forge](00-asset-forge.md) · Next: [3D models, rigs and animation](02-3d-pipelines.md) · [Audio](03-audio-pipelines.md)

One pipeline per kind of 2D asset. Each lists what it reads, the steps, the models to try in order, what it writes and the checks it must pass. Shared rules (style bible, palette lock, retries, fallbacks, placeholders) are on the [Asset Forge](00-asset-forge.md) page. Model names are candidates to be confirmed at bring-up, as explained in [§11 there](00-asset-forge.md#11-model-choices-and-how-sure-they-are).

## Shared image tools

| Tool | Candidates, in order | Used for |
|---|---|---|
| Text-to-image model | A permissively licensed model that accepts reference images: Qwen-Image or FLUX.1 schnell (both Apache 2.0); then SDXL with an image-prompt adapter. **Newer candidates to test first at bring-up** (released November 2026; licences and AMD support unverified): **P-H3-Image** (open weights; a 20 GB 4-bit version; about 21 GB of graphics memory, which Forge A has and Forge B does not; 8 sampling steps; accepts up to 9 reference images, which suits the style-anchor conditioning; strongest at photographic and illustrated looks) and **P-JiT** (Apache 2.0, 2 billion parameters, small and fast, experimental) | All generation below |
| Few-step sampling | **NitroFusion 2**: a distillation that brings multimodal diffusion transformers down to **one or two sampling steps** at comparable quality, with weights and a ControlNet published. If a NitroFusion 2 version exists for the chosen image model, use it: on Forge A's slower graphics, cutting 8–30 steps to 1–2 is the largest single speed-up available. Check that the style adapter and reference conditioning still work with it; if not, use it only for the high-volume pipelines (icons, flipbook stills) | P02, P05, P08 first |
| Background removal | BiRefNet or an equivalent matting model | Icons, UI pieces, flipbook frames, reference sheets |
| Upscaler | Real-ESRGAN class 2× or 4× model | Paintings, UI at 2× |
| Tiling | The image model run with circular (wrap-around) padding, then a seam check | Terrain, trim sheets |
| Palette lock | Forge script: nearest palette colour in OKLab, 60% blend | Every colour image |
| Vision checker | A local vision-language model through `llama.cpp` | The visual gate |
| Segmentation | A small local model that detects and masks objects and regions (for example Mirage, 22 MB, released November 2026; or a Segment Anything class model) | Material masks for the repaint pass and for colourways; background removal checks |

Fallback for every image pipeline when no image model passes bring-up: **procedural painting**, a forge script that builds the image from palette colours, gradients, noise and simple vector shapes chosen by asset type and subject keywords. It is plain but consistent.

## P01 — Style bible

| | |
|---|---|
| Makes | `forge/style/`: the 32-colour palette, 8 anchor images, proportion sheets for the 4 player bodies, material swatches (cloth, leather, mail, wood, stone, metal, bark, snow, lava), and the prompt fragments every other pipeline uses |
| Reads | **[Art Direction](../10-art/10-art-direction.md)**, which defines the look in full: the five rules, proportions, surface rules, the eight palette ramps, culture and zone colours. The style bible is generated to match that page, not invented. Also the zone themes in the zone documents |
| Also makes | The **style adapter**: once the anchors and about 150 approved images exist, train a small adapter (LoRA) for the image model on them, and use it in every image pipeline together with reference conditioning. If training does not run on this hardware, skip it and rely on reference conditioning. Also the **material library** of about two dozen base materials (Art Direction §3), generated once with P05 and reused by every other pipeline |
| Steps | 1. Generate 200 candidate concept images across eight subjects: a human fighter, a dwarf cleric, a wolf, a mill, a forest clearing, a sword, a spell effect, an interior. 2. Score each with the vision checker for the style words and for mutual similarity. 3. Take the most mutually consistent set of eight, one per subject, as the anchors. 4. Extract the palette by clustering the anchors' colours to 32, then order it into ramps. 5. Generate the proportion sheets and swatches conditioned on the anchors. 6. Write the prompt fragments: a positive style line, a negative line (photo, realistic, text, watermark, logo, signature, blurry), and one line per material |
| Checks | Eight anchors exist and pass the vision checklist; palette has 32 colours with at least 4 ramps of 5; every swatch tiles |
| Runs | Once, before every other pipeline. Its outputs are frozen: regenerating the style bible means regenerating everything |

## P02 — Icons (about 2,050)

| | |
|---|---|
| Reads | [Icons list](../10-art/06-icons.md), [Named Item Index](../10-art/07-named-item-index.md), [Quest Art Index](../10-art/08-quest-art-index.md) |
| Template | "`<style>`, game icon, single `<subject>` centred, simple dark vignette background, strong silhouette, thick readable shapes, lit from upper left" with the category's fragment (ability: glowing symbol; item: object on plain ground; material: small pile) |
| Steps | 1. Generate at 512². 2. Vision check. 3. Palette lock. 4. Downscale to 128² source and 64² shipped with a sharpening pass. 5. Composite the standard icon frame |
| Variants | Recolours (tier and colourway items, potion tints, recipe quality tints) are made by hue-shifting an accepted base icon, not by regenerating |
| Checks | 128² and 64² PNG; subject readable at 32² (vision checker shown the 32² version must still name the subject); no text; not near-identical to another accepted icon (perceptual hash distance above a threshold) |
| Batching | 64 per batch; about 30 s each |

## P03 — UI frames, panels, buttons and cursors (about 650)

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
| Steps (scenes) | Generate at the model's native size in 16:9, upscale to 3840 × 2160, palette lock at 40% so paintings keep more colour range |
| Steps (maps) | Maps must match the game, so they are **rendered, not imagined**: once a zone's terrain exists, the client renders a top-down height and colour image; the image model repaints it in a parchment-map style at low strength so coastlines, roads and landmarks stay where they are; labels are added by the client from string tables, never painted in. Until the terrain exists, the map is drawn from the layout's grid map |
| Checks | Size; no text in the image; maps: road and hub positions within 2% of the layout coordinates (compared by feature points) |

## P05 — Tiling textures: terrain, trim sheets, materials (about 80 terrain, 20 kit atlases)

| | |
|---|---|
| Reads | [Environments list](../10-art/03-environments-props.md); the zone's theme and palette notes |
| Steps | 1. Generate at 1024² with wrap-around padding. 2. Palette lock. 3. Seam check: tile 4 × 4 and measure edge discontinuity and visible repetition. 4. Derive a height map from luminance for terrain blending. 5. Trim sheets: generate each strip (planks, stone courses, roof tiles, metal bands) separately and pack them into the kit's 2048² atlas at fixed rows, so kit geometry can rely on fixed UV rows |
| Checks | 1024² PNG; seam error under threshold; no single feature that repeats obviously at 4 × 4; average colour within the zone's palette ramp |
| Fallback | Noise-based procedural materials tinted from the palette |

## P06 — Armor region textures and colourways (about 550 textures)

| | |
|---|---|
| Reads | [Characters, Armor & Weapons](../10-art/01-characters-armor-weapons.md): 23 sets, 6 body regions each, on the shared body UV layout |
| Steps | 1. For each set, generate front and back views of the full outfit on the proportion sheet (P01), conditioned on the anchors. 2. Project those views onto the body mesh and bake to the shared UV layout, giving the six region textures. 3. Fix seams by inpainting across UV borders in texture space. 4. Bake once per body (4), since proportions differ |
| Colourways | Made by **palette remap**: each set's base texture is segmented into material masks (primary cloth, secondary, trim, metal), and each colourway assigns a palette ramp to each mask. The zone-based colourway rule in the armor list picks the ramps |
| Checks | Region sizes; seams invisible in renders from 8 angles on all 4 bodies; skin does not show through where the region should cover |
| Depends on | The 4 player body meshes from P13 |

## P07 — Skins and outfits: creature re-textures and NPC clothing (about 350)

| | |
|---|---|
| Reads | [Creatures & NPCs](../10-art/02-creatures-npcs.md): each rig's list of skins |
| Steps | 1. Render the rig's base model from 6 views with its UV-island map. 2. Generate the new skin as a repaint of those views (image-to-image at moderate strength) from the skin's description: colour, markings, wear, size cues. 3. Project and bake to the rig's UVs. 4. Palette lock |
| NPC outfits | Use P06's method on the player bodies, with the outfit description from the roster's role |
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
