# Asset Pipelines 2 — 3D Models, Rigs, Animation and Hair (P10 to P15, P21)

[← Asset Forge](00-asset-forge.md) · Prev: [Images and textures](01-image-pipelines.md) · Next: [Audio](03-audio-pipelines.md)

One pipeline per kind of 3D asset. Shared rules are on the [Asset Forge](00-asset-forge.md) page. This is the part of the forge most likely to need its fallbacks on an AMD GPU, so each pipeline's fallback is specified in as much detail as its primary method.

## Shared 3D tools

| Tool | Candidates, in order | Notes |
|---|---|---|
| Image-to-3D model | **Runs on Forge B (the RTX 5070 Ti, CUDA, 16 GB).** TRELLIS.2 (MIT; uses NVIDIA-only rendering libraries, which Forge B has; reported to want 24 GB, so test its lower-memory settings) · Hunyuan3D 2.1 (check its licence: reports describe regional and user-count limits) · TripoSR (MIT; lower detail; small; also runs on CPU) | Bring-up records which run and fit |
| Scene-to-objects | CoLa3D (NeurIPS 2026; code and model published): splits one generated scene into separate object meshes in a shared frame. Used to make a **matched set** of props from a single image, so a set shares one style (P10) | Optional; Forge B |
| Clean-up | Blender background scripts: merge by distance, remove loose parts, fill holes, recalculate normals | Always |
| Retopology | QuadriFlow or Instant Meshes to a quad mesh, then triangulate to the budget; `meshoptimizer` for LODs | Always |
| UV unwrap | `xatlas`, or Blender Smart UV for hard-surface props | Always |
| Shape pass | Forge script enforcing the proportion and geometry rules in [Art Direction §2](../10-art/10-art-direction.md#2-shape-rules): scale hands, feet, heads and weapon thickness to the stated ratios, bevel hard edges, remove features under 4 cm | Always, after retopology |
| **Repaint pass** | The seven steps in [Art Direction §6](../10-art/10-art-direction.md#the-repaint-pass): bake to the final UVs at the standard pixel density, remove the generator's lighting, segment by material, recolour from the palette, repaint the game's lighting from baked occlusion and curvature, apply paint grain. **No texture is used as generated** | Always; this replaces a plain bake |
| Export | glTF binary (.glb), metres, Y-up, one material where possible | Always |

**The universal fallback is procedural modelling in Blender.** The forge keeps a library of parametric generators, one per asset family, that build a model from a few numbers and palette colours. They need no model and no GPU. A generator exists for every family listed below, so a pipeline can always produce something correct in size, pivot and naming.

## P10 — Static props and weapons (about 320: 145 weapons, 175 props and world objects)

| | |
|---|---|
| Reads | [Characters, Armor & Weapons](../10-art/01-characters-armor-weapons.md) for weapons; [Environments & Props](../10-art/03-environments-props.md) for props; the Named Item Index for unique weapons |
| Steps | 1. Generate a reference image: the object alone, three-quarter view, plain background (P02's template without the icon framing). 2. Image-to-3D. 3. Clean-up. 4. Retopologise to the budget (weapons 300–800 triangles, props 50–600). 5. UV unwrap and bake to a 256² (weapons) or atlas slot (props). 6. Normalise: scale to the real size in metres from the asset's `targets`; set the pivot (weapons: at the grip; props: at the base centre); align the forward axis. 7. Make LOD1 at 50%. 8. Export |
| Matched sets | Props that belong together (a camp's tents, crates and racks; a tavern's furniture; a forge's tools) are generated as **one image of the whole set**, turned into a scene mesh, and split into separate objects with CoLa3D where it passes bring-up. Each object then follows steps 3–8. This gives sets that match by construction |
| Weapon tiers | The 52 tier weapons are generated once each; their colourways are palette remaps of the texture (P06's method) |
| Checks | Triangle count in budget; bounding box within 10% of the target size; pivot and axis correct (a weapon's blade points along +Y from the grip); single closed surface or intentional open edges only; reads as the subject from 3 views (vision checker); held in a hand socket it does not intersect the forearm in the rest pose |
| Fallback | Parametric generators: blade (length, width, curve, guard, pommel), haft weapon (length, head type), bow, shield (shape, boss, rim), staff (length, head ornament), and prop generators for barrel, crate, sack, chest, table, bench, cart, lantern, signpost, tent, fence, well, grave marker, banner, campfire |

## P11 — Modular building kits (20 kits, about 700 pieces)

| | |
|---|---|
| Why different | Kit pieces must snap together on a grid. Generated meshes are never dimensionally exact, so **kits are built procedurally and only their surfaces are generated** |
| Reads | [Environments & Props](../10-art/03-environments-props.md): kits KIT-01 to KIT-20 and their piece lists |
| Steps | 1. For each kit, generate its trim-sheet atlas (P05) from the kit's material description: timber and plaster, dwarven cut stone, turf and dry-stone, cavern rock, brick kiln, imperial marble and brass, and so on. 2. A Blender generator builds each piece on a 2 m grid (walls 4 m wide by 3 m high, floors 4 × 4 m, door and window openings at fixed positions, roofs at 30° or 45°), mapping faces to the atlas's fixed rows. 3. A second pass adds wear by vertex displacement within 3 cm and bevels on outer edges, so pieces do not look machine-made but still meet at their borders. 4. Unique set pieces (the mill's sails, the Old Forge firebed, the Great Bore, the Hollow Throne) are made with P10 and attached at fixed sockets |
| Cavern kits | Cavern floor, wall, ceiling and pillar pieces are generated as displaced grids whose **border vertices are fixed to a shared profile**, so any two pieces join without a gap |
| Checks | Every border vertex lies on the grid to 1 mm; pieces of the same kit assemble into the test building without gaps or overlaps (an automated assembly test per kit); triangle budget per whole building; atlas rows used correctly |
| Fallback | Same generators with flat palette colours instead of the generated atlas |

## P12 — Nature: trees, rocks, plants, gathering nodes (about 240)

| | |
|---|---|
| Reads | [Environments & Props](../10-art/03-environments-props.md): 13 nature libraries; 23 gathering nodes |
| Method | Procedural with generated textures. Trees: a branching generator with parameters per species (trunk height and taper, branching angle, canopy shape, leaf card density) and leaf and bark textures from P05. Rocks: displaced icospheres with strata noise and a rock texture. Plants and herbs: crossed cards from generated plant images with the background removed. Gathering nodes: a rock or plant base with a distinct coloured feature (ore vein, bloom) so they read at a distance |
| Variants | 3–5 seeds per species; autumn, snow and ash variants by palette remap |
| Checks | Triangle budget; trunk base at the origin; leaf cards face outward; a node is distinguishable from its non-node neighbour (colour difference above a threshold in a rendered scene) |

## P13 — Characters and creatures: base models (4 player bodies, 110 customisation pieces, 62 creature rigs' base models, 18 bosses)

| | |
|---|---|
| Reads | [Characters, Armor & Weapons](../10-art/01-characters-armor-weapons.md); [Creatures & NPCs](../10-art/02-creatures-npcs.md); proportion sheets from P01 |
| Steps | 1. Generate a **turnaround sheet**: front, side and back views in a neutral pose (A-pose for bipeds, standing square for quadrupeds), conditioned on the proportion sheet for player bodies. 2. Image-to-3D from the front view, with the side and back views as extra conditioning where the model accepts several images. 3. Clean-up; make the mesh symmetric across the centre plane. 4. **Fit to the family's template mesh** where one exists (next row) so topology and UVs are standard. 5. Retopologise to budget, with edge loops at joints from the template. 6. Bake textures at 1024² (bosses 2048²). 7. Export in the rest pose |
| Template fitting | Each rig family has a hand-specified low-poly **template mesh** made procedurally (biped, dwarf biped, quadruped, bird, spider, serpent, blob, construct, plant). The generated mesh is used as a **target shape**: the template is shrink-wrapped onto it and smoothed, so the result has the template's clean topology, UV layout and joint loops with the generated creature's shape and painted detail. This is what makes rigging and shared skins reliable |
| Player bodies | The 4 bodies share one UV layout (required by the armor system). They are made by fitting the same biped template to four generated shapes. Faces are separate meshes generated with P10's method and attached at the head socket. **Hair, beards and other hair pieces are made by their own pipeline, [P21](#p21--hair-beards-manes-and-tails)** |
| Checks | Symmetric within tolerance; triangle budget; standing height equals the family's specified height; UV layout identical to the template's; no interpenetrating limbs in the rest pose; reads as the subject from 4 views |
| Fallback | The template mesh itself, scaled and proportioned by parameters from the description (bulk, limb length, head size), painted by P07. Every creature can be made this way with no 3D model at all |

## P14 — Rigs and skinning (64 rigs)

| | |
|---|---|
| Reads | The rig list in [Creatures & NPCs](../10-art/02-creatures-npcs.md); the 2 player rigs |
| Method | **Template skeletons first.** Each family's template mesh (P13) comes with a template skeleton with standard bone names and sockets (hands, head, back, hips, feet, mouth, effect points). Because P13 fits models to the template, the skeleton fits too: 1. Scale the template skeleton to the model's joints (found from the template's joint loops). 2. Skin with Blender's automatic weights. 3. Correct weights at shoulders, hips and the neck with the family's stored weight masks. 4. Run the fixed test animation (bend every joint to its limits) and measure volume loss and self-intersection |
| Alternate | UniRig (MIT) for models that do not fit any template: predicts a skeleton and weights; its bones are then renamed to the standard names |
| Checks | Standard bone names and hierarchy; all sockets present; no vertex without weights; no more than 4 bones per vertex; volume loss under 15% at joint limits; no self-intersection in the test animation |
| Fallback | A rigid rig: each body part bound to one bone with no blending. It looks stiff but always works |

## P15 — Animation clips (about 850: 204 player and mount, 650 creature)

| | |
|---|---|
| Reads | The clip lists in the two character lists; gameplay timings from [spells](../12-data/spells.md) and [creatures](../12-data/creatures.md) (swing speeds, cast times) |
| Alternate for bipeds: motion capture from generated video | Generate a short video of the motion with a video model, then recover the 3D human motion from it with **FlowHMR** (code and model published, 2026: physically plausible motion capture from a single video; its authors show exactly this text-to-video-to-motion route). Retarget to the rig as below. FlowHMR runs on Forge B; the video model runs on whichever machine has the memory for it. Use this route if no text-to-motion model passes bring-up, or for clips the text-to-motion model does badly |
| Method for bipeds | 1. Text-to-motion model, prompted from the clip's description ("a soldier swings a two-handed sword overhead, steps forward"). Candidates: a current open text-to-motion model that passes bring-up and whose licence allows commercial use. 2. Retarget to the rig's skeleton. 3. Fix foot contacts with inverse kinematics. 4. Trim to the gameplay length; place the **contact frame** (the moment a hit lands or a spell releases) at the required time. 5. For loops, blend the last 6 frames into the first |
| Method for everything else | Text-to-motion models are trained on human motion, so quadrupeds, birds, spiders, serpents, blobs, constructs and plants use **procedural animation**: a Blender generator per locomotion family builds each clip from parameters (gait pattern, stride, speed, bob, spine wave, wing beat). Attacks, hits and deaths are keyed poses from a per-family pose library with easing |
| Shared clips | A clip is made once per rig, not per creature. The 96 player clips are made for the human rig and retargeted to the dwarf rig with a height and limb-length correction |
| Checks | Length matches the data file's timing to one frame; loop error (first against last frame) under threshold; feet do not slide more than 3 cm while planted; root motion matches the movement speed for locomotion clips; no joint beyond its limit; no self-intersection |
| Fallback for bipeds | The same procedural method with a biped gait generator and pose library |

## P21 — Hair, beards, manes and tails

Hair is the part of a stylised character that image-to-3D models do worst: they produce a solid lump with no separate locks and nothing to animate. It therefore has its own pipeline.

| | |
|---|---|
| Makes | The 32 player hair meshes and 22 facial-hair pieces in the [customisation list](../10-art/01-characters-armor-weapons.md); NPC hair; and, by the same method, creature manes, crests and tails where a rig has them |
| Runs on | Forge B (CUDA) |
| Primary method | **HairDeck** (2026; code, models and a demo published): from a single image of a hairstyle it generates a set of **stylised hair cards**, each a separate ribbon with its own UVs, together with **spring-bone chains** that make the hair move, bound to the cards by geometric skinning. It is built for stylised characters, which is this game's look, and is reported to generate a set of cards in about a second |
| Steps | 1. Generate the reference: the head from P13 wearing the hairstyle, front view, in the style anchors' look; for beards, the face in three-quarter view. 2. HairDeck: image to hair cards and spring-bone chains. 3. **Fit to the head**: scale and place the card set on the rig's head socket; push any card that passes through the scalp or shoulders outward. 4. **Reduce**: merge and drop cards to the budget (hair 600–1,200 triangles, beards 300–600), keeping the outline; keep at most 6 spring chains for hair and 3 for a beard, each of 3–4 bones. 5. **Shape pass**: thicken cards to the chunky proportions in [Art Direction](../10-art/10-art-direction.md#2-shape-rules); hair reads as 5–9 large clumps, not strands. 6. **Repaint pass** with the hair ramp: hair colour is one of the 8 customisation colour ramps, applied by palette remap, so every style comes in every colour from one texture. 7. Export with the spring-bone chains as extra bones parented to the rig's `head` bone |
| Spring bones in the game | The chains are **secondary bones**: they are not part of the rig contract and no animation clip drives them. The client simulates them with a simple spring (stiffness, damping and gravity from the asset) so hair and beards sway with movement. Beyond the nearest 20 characters, and always on the lowest quality setting, the simulation is off and the hair holds its rest shape |
| Helmets | Each hair style carries a "under helm" variant flag: when a helm is equipped the hair is hidden or swapped for its short variant, as the armor system specifies |
| Checks | Triangle and bone budgets; no card intersects the head, neck or shoulders in the rest pose or at the head bone's rotation limits; outline reads as the described style from front, side and back; all cards use the shared hair UV strip so the colour ramps apply; spring chains settle (no perpetual jitter) in a 5-second simulation test |
| Alternates | Hair as part of the image-to-3D head, then separated by segmentation and retopologised (solid hair, no movement) |
| Fallback | Procedural hair: a set of 5–9 tapered clumps placed on the scalp from a style template (short, cropped, long, tied, braided, bald, plus beard templates: stubble, short, long, forked, braided), with one spring chain for long styles. Always works; plainer |
| To verify at bring-up | HairDeck's licence for commercial use; that it runs within 16 GB; whether its output for beards and manes is usable, since it was built for head hair |
