# Art Direction — the look, and how every asset is held to it

[← Art Master To-Do](00-art-master-todo.md) · Made by: [Asset Forge](../14-asset-pipeline/00-asset-forge.md)

This page defines what the game looks like in rules a program can follow and check, and explains how roughly nine thousand separately generated assets are made to look like one game. It is the authority on style. The forge's style bible ([P01](../14-asset-pipeline/01-image-pipelines.md#p01--style-bible)) is generated *from* this page, not invented. The owner approves the style bible, and then the first results of each pipeline it governs, before anything is made in number.

Open: the style bible is not yet approved, so §1 to §4 are the direction it is being made to and are not final.

Open: the owner found the first style anchors, made without an image model, and the figures built from them unacceptable, and liked the image-model direction for buildings, weapons and environments; people and animals are to be redone as solid painted forms.

## 1. The look

**Stylised, hand-painted, low-polygon fantasy** in the tradition of the 2004-era online role-playing games: chunky shapes with strong silhouettes, bold saturated colour, and surfaces that look painted with a brush, not photographed. Detail lives in the painted colour, not in geometry or in lighting effects. A character should be recognisable by outline alone from forty metres.

It belongs to that family of games but is its own world. **No prompt, reference image or asset names or imitates an existing game, studio, artist, character or logo.** Halcyra's identity within the family comes from its own shapes, palettes and cultures, set out in §2 to §4.

### The five rules, in order of importance

| # | Rule | What it means in practice |
|---|---|---|
| 1 | **Shape first** | Proportions are exaggerated and outlines are simple. If a silhouette is unclear, the asset is wrong, whatever its texture looks like |
| 2 | **Paint, not photograph** | Every surface is a painted colour texture with its light and shadow painted in. No photographic textures, no fine noise, no realistic material shading |
| 3 | **One light, one palette** | All assets are painted as if lit softly from above, and all colours come from one master palette. Icons are the one exception (below) |
| 4 | **Big, medium, small** | About 70% of any surface is large calm areas, 25% medium shapes, 5% small accents. Even detail everywhere reads as noise |
| 5 | **Same grain everywhere** | Brush strokes, pixel density and edge sizes are the same scale on a boot, a barrel and a building, so things look like they were made by one hand |

**Icons have their own style.** An icon is a tiny hand-painted picture that fills its square, cropped tight, washed in one strong hue for its kind (twelve hues), with a glowing light that is white-hot at its centre and dark corners. Icons are not drawn from the master palette, are not pulled toward it, and carry no frame. The rules and the hue table are in [Icons](06-icons.md#the-icon-style); the owner approved that style on 2026-11-23. Rules 3 and 5, the palette of §4 and the repaint pass of §6 do not apply to icons.

## 2. Shape rules

### Proportions

| Subject | Rule |
|---|---|
| Human | 6.5 heads tall (a real adult is about 7.5). Hands and feet 120% of realistic size. Broad shoulders, thick forearms and calves. Height 1.80 m |
| Dwarf | 4.5 heads tall. Height 1.35 m, shoulder width equal to a human's. Hands, feet, nose and beard oversized; head 115% |
| Weapons | Blades 150% of realistic thickness and 120% width; hafts 130% thickness; heads of maces and axes 140%. A sword's outline must read at 20 m |
| Armor | Shoulders and helms are the largest shapes and carry a set's identity. Pauldrons extend 20–40% beyond the shoulder. No thin straps or small buckles as geometry; those are painted |
| Creatures | The dangerous part is enlarged 115–130%: jaws on wolves, claws on bears, horns on rams, stingers on scorpions. Legs are thicker than life; necks shorter |
| Buildings | Walls lean and bulge slightly (up to 3° and 5 cm); roofs overhang and sag; timbers are 150% thickness. Nothing is perfectly straight except dwarven cut stone, which is deliberately square |
| Trees and rocks | Trunks are thick with few large branches; canopies are 3–7 big clumps, not individual leaves. Rocks are faceted with flat planes and clear edges |

### Geometry

- Triangle budgets are in the [technical targets](00-art-master-todo.md#4-technical-targets-for-every-asset). Budgets are a style rule as well as a performance rule: the look *is* low-polygon.
- No feature thinner than 4 cm as geometry. Edges that catch light are bevelled 1–3 cm.
- Shapes are built from clear forms: boxes, wedges, cylinders, cones. A model that looks melted, lumpy or over-smooth fails.
- Faces are smooth-shaded on organic forms and hard-edged on stone, metal and wood.

## 3. Surface rules

### What a texture contains

| Rule | Value |
|---|---|
| Maps | **Colour only**, plus an optional emissive mask for glowing parts. No normal, roughness or metallic maps |
| Painted light | Every texture is painted as if lit from directly above by a soft sky: surfaces facing up are about 15% lighter, facing down about 15% darker |
| Painted shadow | Creases, undersides and contact areas are darkened (painted ambient occlusion) |
| Edge highlights | Worn or exposed edges carry a lighter line, 10–15% above the base value, 1–2 cm wide |
| Brush grain | Visible strokes 2–6 cm long at world scale. Nothing finer than 1 cm: no pores, fibres, grit or film grain |
| Value range | Between 12% and 88% brightness. No pure black, no pure white |
| Gradients | Large areas carry a slow gradient (darker toward the ground), never a flat fill |
| Colour variation | Shadows shift toward blue-violet, lights toward warm yellow, by about 8° of hue. This is what makes a texture look painted and not merely shaded |

### Pixel density

One density for the whole game, so a crate beside a character looks equally sharp:

| Surface | Density |
|---|---|
| Characters, creatures, weapons | 256 pixels per metre |
| Props, buildings, nature | 128 pixels per metre |
| Terrain | 128 pixels per metre (a 1024² tile covers 8 m) |

### Materials

About two dozen base materials, each painted once and reused everywhere it appears, so most surfaces in the game literally share their pixels:

timber (pale, dark, charred) · plaster · thatch · slate and tile · cut stone (white, grey, dwarven dark) · rough stone · brick · turf · packed earth · cloth (plain, woven, silk) · leather (pale, dark) · mail · iron · bronze and brass · gold trim · bone · bark · snow and ice · ash and slag · lava (emissive) · crystal (emissive) · imperial marble.

## 4. Colour

### Master palette

Thirty-two colours in eight ramps of four values (shadow, base, light, highlight): warm stone · cool stone · wood · earth · foliage green · autumn orange-red · iron and steel blue-grey · accent gold. Every colour in every asset except an icon is drawn from, or pulled toward, these. The values are built by rule in a perceptual colour space, with shadows shifted toward blue-violet and lights toward yellow as §3 asks, and are fixed when the style bible is generated and frozen from then on.

### Cultures and enemies

Each group owns a small set of colours and a shape motif, so who made a thing is readable at a glance.

| Group | Colours | Shapes |
|---|---|---|
| Humans of Solhaven (Concord) | White stone, royal blue, gold | Tall, arched, pointed roofs, banners |
| Mountain dwarves (Hallborn) | Dark grey stone, iron, ember orange, brass | Square, heavy, angular knotwork, rails and lamps |
| Hill dwarves (Dalefolk) | Turf green, ochre, cream wool, pale wood | Low, rounded, turf roofs, dry-stone walls |
| Cinderbrand cult and Slagborn | Ash grey, soot black, brand orange glow | Scorched, jagged, the hand-print mark |
| The Hollow (hollowed people, the Crown) | Black, desaturated violet, cold white light | Smooth, empty, symmetrical, cracked crystal |
| Imperial Tor Vael | Pale marble, tarnished brass, arcane violet | Grand, geometric, eroded |
| Wildpact | Deep green, bark brown, amber | Grown, asymmetric, woven |
| Ashen Covenant | Ash white, charcoal, violet glass | Formal, slender |

### Zones

Each zone uses a subset of the master palette with one dominant hue, so a screenshot identifies the zone:

Brightmead: spring green and warm gold · Embercrag: snow blue-white and ember orange · Harrowfield: wheat gold and rust · Russetwood: copper, red and gold · Stonewake Dale: fresh green and grey stone · Stoneheart Deeps: lamp gold on deep teal dark, glowcap cyan · Thornwick: desaturated olive and grey-violet · Ironroot: pine green and cold grey · Cinderfall: black, sulphur yellow and lava orange · Riftlands: dust ochre and bleached sky · Veilmoor: fog grey-green with lantern gold.

### Magic

School colours are fixed: Holy gold · Nature green · Arcane violet · Fire orange · Frost blue · Shadow purple-black · Physical white and red.

## 5. One shader, one light

Much of what makes separate assets look like one game happens in the engine, not in the assets. **Every object in the world uses the same material shader and the same lighting setup.** This is a requirement of the client build.

| Element | Rule |
|---|---|
| World shader | One shader for all characters, creatures, props, buildings and terrain: the colour texture lit by a soft wrapped diffuse term (so shadows never go black), no specular highlights, no reflections. Metals get a fixed, subtle rim brightening from a mask, not real reflection |
| Sun and sky | One directional sun and a sky gradient per zone, from the zone's lighting preset. Because textures already contain painted light, the engine's light is gentle: it adds direction and time of day, not form |
| Shadows | Soft, short-range shadows; a simple round shadow under every character and creature |
| Character rim light | A faint rim on characters and creatures so they separate from the background at any time of day |
| Fog | Distance fog in the zone's colour on everything, which ties far objects together |
| Colour grade | One grading table per zone applied to the whole frame, so even an off-colour asset is pulled into the zone's range |
| Effects | Additive, bold shapes in school colours; no realistic smoke or fire |

## 6. How the forge keeps nine thousand assets consistent

A generator asked nine thousand separate times for "a stylised barrel" will give nine thousand slightly different styles. Consistency therefore **cannot come from prompts**. It comes from limiting how much of each asset the generator decides, from holding every asset to a contract (a skeleton, a size, a triangle budget), and from putting everything through the same final steps. Ten mechanisms, strongest first:

| # | Mechanism | What it does |
|---|---|---|
| 1 | **One shader, light, fog and grade** (§5) | Everything is drawn the same way, so differences between assets are reduced before any asset is made |
| 2 | **Shapes built by rule, or generated and held to a contract** | Buildings, kit pieces, terrain, trees and rocks are built by constructed generators that obey §2 exactly. Player bodies, creatures, dressed NPC bodies and props take their shape from an image-to-3D model, working from one picture painted in the game's style, and **the generated mesh is kept**. What holds it to the game is its contract: a body or creature is fitted to its rig's skeleton and rest pose, and a prop is fitted inside its contract's box. Nature for the two starting zones may also be generated and fitted inside its box |
| 3 | **The shape pass** | On a constructed model a fixed script enforces §2: scale hands, feet, heads and weapon thickness to the stated ratios; reduce to the triangle budget; bevel hard edges; remove features thinner than 4 cm. A generated model is reduced to its triangle budget. A generated body or creature is then carried, bone by bone, from where its own joints are to where the contract's are, so its height and limb lengths are the contract's. A generated prop is scaled to fit inside its box and drawn out toward the box by no more than 30% on any axis; it must fill at least 45% of every side |
| 4 | **The repaint pass** (see below) | Every constructed model's texture, every painted skin and armor region and every tiling texture goes through the same procedure, which strips the generator's own lighting and colours and re-applies the game's. A generated model keeps the colour its generator painted, baked onto the reduced mesh's own layout; a generated prop is then given painted light (lighter where it faces up, darker where it faces down or lies in a hollow) with its colours kept |
| 5 | **A shared material library** | The two dozen materials in §3 are generated once. Buildings, props and much armor use those materials through trim sheets, so they share actual pixels instead of resembling each other |
| 6 | **One pixel density** | UV layouts are scaled to the densities in §3, so nothing is blurrier or sharper than its neighbours |
| 7 | **A trained style adapter** | After the style bible exists, the forge trains a small style adapter (a LoRA) for the image model on about 150 approved images, and uses it for every image it generates, with reference images as well. All generations use the same sampler, step count and guidance settings, fixed at bring-up. If adapter training does not run on this hardware, reference conditioning alone is used |
| 8 | **Palette lock** | Every colour image except an icon is pulled toward the master palette, and each zone's and culture's assets toward its subset |
| 9 | **Measured style gates** | Each asset is measured, not judged by description: see §7 |
| 10 | **Calibration and approval before volume** | Block A makes one of each asset type first. The gate thresholds are set from those and from a spread of probe assets, then frozen (§7). The owner then approves the style bible and, pipeline by pipeline, the first results; only a pipeline with both approvals makes its assets in number |

Open: whether the palette lock and the repaint pass apply to generated bodies and creatures fitted to a rig, which today keep their generator's colours, is not decided.

### The repaint pass

Applied to every constructed model's texture, every painted skin, every armor region and every tiling texture, identically:

| Step | What happens | Why |
|---|---|---|
| 1. Bake | The generated colour is baked onto the final low-polygon mesh's UV layout | Brings every asset to the same layout and pixel density |
| 2. Remove the generator's lighting | The texture's brightness is flattened by dividing out its blurred luminance, leaving flat local colour | Generators bake in their own inconsistent lighting, which is the main reason generated assets clash |
| 3. Segment by material | The flat colour is split into material regions (skin, cloth, leather, metal, wood, stone, fur) by clustering, guided by the asset's description | Each material gets its own treatment |
| 4. Recolour from the palette | Each region is mapped onto the palette ramp for its material and its culture or zone | One palette, exactly |
| 5. Repaint the light | The game's own lighting recipe from §3 is applied from the mesh's geometry: a top-down gradient from the surface direction, darkening from a baked occlusion map, edge highlights from a baked curvature map, and the warm-light, cool-shadow hue shift | Every asset gets identical painted lighting, computed, not generated |
| 6. Paint grain | A painterly filter gives strokes at the standard 2–6 cm scale and removes anything finer than 1 cm. Where the style adapter is available, a low-strength pass through the image model with the adapter replaces the filter for a more hand-made result | Same grain everywhere |
| 7. Check | The measured gates in §7 | |

Because steps 2 to 6 are computed from geometry and the palette, and are identical for every asset, two assets that came from very different generations end with the same lighting, the same colours and the same grain. The generator contributes the *design* (where the stripes are, what the pattern is); the repaint pass contributes the *style*. A generated model does not go through these steps (mechanism 4): its style comes from the picture it was modelled from, which is painted to this page's rules.

## 7. Measured style gates

Checks the forge computes for every asset. Thresholds are set during calibration and then frozen. Block A holds one asset of each type, too few to set a band, so calibration measures block A together with a spread of probe assets of every class, generated and measured but not accepted: each upper limit is 35% above the largest value seen and each lower limit 60% of the smallest, capped so that deliberately bad test samples still fail. Passing the gates does not stand in for the owner's approval of a pipeline's first results.

| Gate | Measure |
|---|---|
| Palette | Average distance of the texture's colours from the allowed palette subset, in a perceptual colour space |
| Value range | Share of pixels outside 12–88% brightness |
| Grain | High-frequency energy of the texture at world scale: too much means photographic noise, too little means flat fill |
| Big, medium, small | The distribution of region sizes after segmenting the texture |
| Painted light | Correlation between brightness and upward-facing surface direction: it must be positive and within a band |
| Proportion | For characters and weapons: the ratios in §2, measured on the mesh |
| Silhouette | The asset is rendered as a flat black shape at the size it would be at 40 m; a vision model must still name what it is |
| Style similarity | Distance between the asset's rendered image and the anchor set in an image-embedding space |
| Line-up | The asset is rendered in the standard test scene beside five already-accepted assets of the same kind, and a vision model is asked which one does not belong. If it picks the new one twice in three trials, the asset fails |
| Scene audit | When a zone's assets are complete, the client renders it from eight fixed camera points; each view is checked for the zone's dominant hue and for any object the vision model flags as out of place |

## 8. What the generator is and is not trusted with

| Trusted to decide | Not trusted to decide |
|---|---|
| The design of a thing: what a creature's markings are, how a set of armor is cut, what a sword's guard looks like | The skeleton, the rest pose, and the height and limb lengths of anything animated: those are the rig contract's |
| Variety between assets of the same kind | Triangle count and texture size: every model is reduced to its budget |
| The shape and the painted surface of a body, a creature, a dressed NPC or a prop, from a picture in the game's style | The size of a prop: it is fitted inside its contract's box |
| | The geometry of anything that must fit a grid: kit pieces and terrain are constructed |
| | Lighting, colour palette and brush grain of constructed models, painted skins and tiling textures |

## 9. Limits

- **This will look like a stylised, hand-painted game; it will not look hand-made by a senior art team.** The repaint pass gives consistency, and consistency is what makes a game look intentional, but computed painting is plainer than an artist's. Generated models are richer to look at and less alike, which is why they are held to contracts and shown to the owner before volume.
- **Faces and hands are the weak point.** A generated body's face and hands are what its generator made, reduced to the triangle budget; a body fitted to its rig keeps the contract's proportions, and its face is part of its one painted texture.
- **Unique hero pieces are the most likely to stand out**: raid bosses, tier armor, capital landmarks. They go through the same passes, but they are also the assets players look at longest.
- **The thresholds are only as good as the calibration set.** The gates in §7 are sound in principle; their numbers come from calibration on real output, and they measure consistency, not whether the look is liked. That judgement is the owner's.
