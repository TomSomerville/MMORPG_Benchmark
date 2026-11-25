# Art Direction — the look, and how every asset is held to it

[← Art Master To-Do](00-art-master-todo.md) · Made by: [Asset Forge](../14-asset-pipeline/00-asset-forge.md)

This page defines what the game looks like in rules a program can follow and check, and explains how roughly nine thousand separately generated assets are made to look like one game. It is the authority on style. The forge's style bible ([P01](../14-asset-pipeline/01-image-pipelines.md#p01--style-bible)) is generated *from* this page, not invented.

## 1. The look

**Stylised, hand-painted, low-polygon fantasy** in the tradition of the 2004-era online role-playing games: chunky shapes with strong silhouettes, bold saturated colour, and surfaces that look painted with a brush, not photographed. Detail lives in the painted colour, not in geometry or in lighting effects. A character should be recognisable by outline alone from forty metres.

It belongs to that family of games but is its own world. **No prompt, reference image or asset names or imitates an existing game, studio, artist, character or logo.** Halcyra's identity within the family comes from its own shapes, palettes and cultures, set out in §2 to §4.

### The five rules, in order of importance

| # | Rule | What it means in practice |
|---|---|---|
| 1 | **Shape first** | Proportions are exaggerated and outlines are simple. If a silhouette is unclear, the asset is wrong, whatever its texture looks like |
| 2 | **Paint, not photograph** | Every surface is a painted colour texture with its light and shadow painted in. No photographic textures, no fine noise, no realistic material shading |
| 3 | **One light, one palette** | All assets are painted as if lit softly from above, and all colours come from one master palette |
| 4 | **Big, medium, small** | About 70% of any surface is large calm areas, 25% medium shapes, 5% small accents. Even detail everywhere reads as noise |
| 5 | **Same grain everywhere** | Brush strokes, pixel density and edge sizes are the same scale on a boot, a barrel and a building, so things look like they were made by one hand |

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

Thirty-two colours in eight ramps of four values (shadow, base, light, highlight): warm stone · cool stone · wood · earth · foliage green · autumn orange-red · iron and steel blue-grey · accent gold. Every colour in every asset is drawn from, or pulled toward, these. The exact values are fixed when the style bible is generated and frozen from then on.

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

A generator asked nine thousand separate times for "a stylised barrel" will give nine thousand slightly different styles. Consistency therefore **cannot come from prompts**. It comes from limiting how much of each asset the generator decides, and from putting everything through the same final steps. Ten mechanisms, strongest first:

| # | Mechanism | What it does |
|---|---|---|
| 1 | **One shader, light, fog and grade** (§5) | Everything is drawn the same way, so differences between assets are reduced before any asset is made |
| 2 | **Shapes from templates, not from the generator** | Buildings, terrain, trees and rocks are built by procedural generators that obey §2 exactly. Creatures and characters are generated only as a *target shape*, which is then wrapped by a template mesh with standard proportions and topology. The generator never has the last word on geometry |
| 3 | **The shape pass** | After template fitting, a fixed script enforces §2 on every model: scale hands, feet, heads and weapon thickness to the stated ratios; reduce to the triangle budget; bevel hard edges; remove features thinner than 4 cm |
| 4 | **The repaint pass** (the key step; see below) | **No texture is used as the generator made it.** Every texture on every asset goes through the same procedure that strips the generator's own lighting and colours and re-applies the game's |
| 5 | **A shared material library** | The two dozen materials in §3 are generated once. Buildings, props and much armor use those materials through trim sheets, so they share actual pixels instead of resembling each other |
| 6 | **One pixel density** | UV layouts are scaled to the densities in §3, so nothing is blurrier or sharper than its neighbours |
| 7 | **A trained style adapter** | After the style bible exists, the forge trains a small style adapter (a LoRA) for the image model on about 150 approved images, and uses it for every image it generates, with reference images as well. All generations use the same sampler, step count and guidance settings, fixed at bring-up. If adapter training does not run on this hardware, reference conditioning alone is used |
| 8 | **Palette lock** | Every colour image is pulled toward the master palette, and each zone's and culture's assets toward its subset |
| 9 | **Measured style gates** | Each asset is measured, not judged by description: see §7 |
| 10 | **Calibration before volume** | Block A makes one of each asset type first. The gate thresholds are set from those, then frozen, and only then does the forge start the other nine thousand |

### The repaint pass

Applied to every model's texture, every skin, every armor region and every tiling texture, identically:

| Step | What happens | Why |
|---|---|---|
| 1. Bake | The generated colour is baked onto the final low-polygon mesh's UV layout | Brings every asset to the same layout and pixel density |
| 2. Remove the generator's lighting | The texture's brightness is flattened by dividing out its blurred luminance, leaving flat local colour | Generators bake in their own inconsistent lighting, which is the main reason generated assets clash |
| 3. Segment by material | The flat colour is split into material regions (skin, cloth, leather, metal, wood, stone, fur) by clustering, guided by the asset's description | Each material gets its own treatment |
| 4. Recolour from the palette | Each region is mapped onto the palette ramp for its material and its culture or zone | One palette, exactly |
| 5. Repaint the light | The game's own lighting recipe from §3 is applied from the mesh's geometry: a top-down gradient from the surface direction, darkening from a baked occlusion map, edge highlights from a baked curvature map, and the warm-light, cool-shadow hue shift | Every asset gets identical painted lighting, computed, not generated |
| 6. Paint grain | A painterly filter gives strokes at the standard 2–6 cm scale and removes anything finer than 1 cm. Where the style adapter is available, a low-strength pass through the image model with the adapter replaces the filter for a more hand-made result | Same grain everywhere |
| 7. Check | The measured gates in §7 | |

Because steps 2 to 6 are computed from geometry and the palette, and are identical for every asset, two assets that came from very different generations end with the same lighting, the same colours and the same grain. The generator contributes the *design* (where the stripes are, what the pattern is); the repaint pass contributes the *style*.

## 7. Measured style gates

Checks the forge computes for every asset. Thresholds are set during block A calibration and then frozen.

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
| The design of a thing: what a creature's markings are, how a set of armor is cut, what a sword's guard looks like | Proportions |
| Variety between assets of the same kind | Topology, triangle count, UV layout, pixel density |
| Rough shape, as a target for template fitting | Final geometry of anything that must fit a grid or a skeleton |
| | Lighting, colour palette, brush grain |

## 9. Limits

- **This will look like a stylised, hand-painted game; it will not look hand-made by a senior art team.** The repaint pass gives consistency, and consistency is what makes a game look intentional, but computed painting is plainer than an artist's.
- **Faces and hands are the weak point.** Generated characters fitted to templates keep clean proportions but lose expression. Player faces use the customisation pieces to compensate.
- **Unique hero pieces are the most likely to stand out**: raid bosses, tier armor, capital landmarks. They go through the same passes, but they are also the assets players look at longest.
- **The thresholds are untested.** The gates in §7 are sound in principle; their numbers can only be set by calibration on real output, which is why block A exists.
