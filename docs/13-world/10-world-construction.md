# World Construction — from layout tables to built zones

[← World Layout Index](00-world-layout.md) · Format: [Terrain and Cutouts](../08-tech/terrain-and-cutouts.md) · Art: [Environments & Props](../10-art/03-environments-props.md) · Procedure: [Build Procedure](../08-tech/build-procedure.md)

The layout files say where everything is. This page says how the builder turns those tables into terrain, ground textures, scattered nature, buildings, spawn points and interiors, without a level designer. Every step is a rule that a program follows, so the result is repeatable: the same layout and the same seed give the same zone.

## 1. The world generator

| | |
|---|---|
| Tool | `tools/worldgen`, a command-line program in the game repository. Built in milestone M2 for Brightmead Vale and used for every later zone |
| Input | `content/zones/<zone>/layout.yaml`: the zone's layout tables (facts, grid map, sub-areas, hubs, points, camps, nodes, roads) transcribed field for field from its layout document. The validator checks the transcription against the counts in the document |
| Seed | The zone id hashed to a number. Every random choice uses it |
| Output | The three terrain files, prop placements, building placements, spawn points, node positions, cutouts, sub-area polygons, the navigation mesh, and the minimap tiles |
| Overrides | `content/zones/<zone>/overrides.yaml`: fixes made after generation (move this prop, flatten here). The generator applies them last, so regenerating never loses a fix |
| Order | Steps 2 to 9 below, then the checks in §10. A zone that fails a check is regenerated after the generator or the overrides are corrected |

## 2. Heights

Heights are built from control points, not sculpted.

| Step | Rule |
|---|---|
| 1. Base | The whole zone starts at 0 m, the zone's lowest point |
| 2. Sub-area targets | Each sub-area gets a target height from its "Elevation and terrain" text and the zone's "Elevation" row. A number in the text is used as given. Otherwise: "low" or "floor" = the low figure, "mid" = halfway, "high", "ridge" or "hills" = the high figure. The target applies at full strength inside the sub-area's rectangle and fades out over 80 m |
| 3. Open country (`..` cells) | Interpolated between the nearest sub-area targets, weighted by inverse distance squared |
| 4. Border cells (`##`) | Raised to the zone's highest figure plus 40 m, with a slope of at least 55° on the inward face, so they cannot be climbed. At a listed exit the border is cut by a pass 30 m wide at road height |
| 5. Water cells (`~~`) and rivers | A river follows its listed path. Its bed is carved 1.2 m below the banks where the text says wadeable or shallow, 4 m where it does not, with banks sloping at 20°. Width as listed. A flat water surface is placed 0.3 m below the bank. Lakes and sea cells are set 6 m below the water surface |
| 6. Roughness | Fractal noise is added by terrain word: tilled, flat, town ±0.3 m · grass, pasture, moor, marsh ±1.5 m · rolling, woodland ±3 m · hills, badlands ±7 m · ridge, crag, mountain ±15 m. Noise fades to zero within 15 m of roads and hubs |
| 7. Flattening | Hubs: level to within 0.5 m across the hub radius plus 10 m (a knoll keeps its height, and is levelled on top). Each building footprint: exactly flat. Graveyards and camps: slope no more than 15° |
| 8. Roads | Each road is laid along its listed path as a smooth curve, 5 m wide (tracks 3 m), cut and filled so its gradient never exceeds 15%, with a 3 m shoulder blended into the land. Bridges are placed where a road crosses a river |
| 9. Slope limits | Walkable land is smoothed until no slope outside border cells and listed cliffs exceeds 40° |
| 10. Edges | Where two zones meet, the 30 m strip on each side is blended to one shared edge profile, so the seam is invisible and walkable at every exit |

Named features in the text that have no coordinates ("a hollow between two hills", "a single cavern 45 m across") are built at the sub-area centre at the stated size.

## 3. Ground textures

Each zone uses up to 8 tiling textures from its row in [Environments & Props](../10-art/03-environments-props.md). The weight map is painted by rule, later rules overriding earlier ones:

| Order | Where | Texture |
|---|---|---|
| 1 | Everywhere | The zone's base ground (grass, ash, moss, cave floor) |
| 2 | Under tree cover denser than 40% | Forest floor |
| 3 | Sub-areas described as tilled, field, farm | Tilled earth in strips aligned to the nearest road |
| 4 | Slope above 30° | Rock; above 45°, cliff rock |
| 5 | Within 2 m of water, and river beds | Mud, sand or gravel |
| 6 | Roads and hub yards | Road surface (dirt outside towns, cobble inside a hub radius) with a 1.5 m soft edge |
| 7 | Camps and building surrounds, 4 m | Trampled dirt |
| 8 | Zone-specific (scorch around the burned mill, slag near the Slagworks) | As the sub-area text describes, radius from the feature's size |

## 4. Trees, rocks, grass and clutter

Placed by Poisson-disc scattering with the zone seed. Density by the sub-area's terrain word:

| Terrain word | Trees per hectare | Rocks per hectare | Bushes and ferns per hectare | Grass |
|---|---|---|---|---|
| Dense woodland, forest | 120 | 10 | 150 | Sparse |
| Woodland, orchard (orchards in rows) | 70 | 6 | 80 | Medium |
| Pasture, meadow, rolling grass | 4 | 4 | 15 | Thick |
| Fields, tilled | 1 (hedge lines along strip edges) | 0 | 10 | None on tilled strips |
| Hills, ridge, highland | 15 | 40 | 30 | Medium |
| Moor, marsh | 8 (dead or stunted) | 10 | 60 reeds | Thick, wet |
| Badlands, ash, barrens | 2 (dead) | 60 | 10 | None |
| Town, hub | Only the trees named in the hub table | 0 | Garden plots as named | Mown |

Nothing is placed: on a road or within 3 m of one · inside a building footprint or within 2 m · within 3 m of a spawn point, node, quest object or graveyard · on a slope above 40° (rocks excepted) · in water (reeds excepted). Named single features (the fallen oak, the old oak, the willow) are placed exactly at their coordinates and are never scattered over.

Each chunk holds at most 400 scattered objects, drawn with instancing; grass is a separate client-side layer and is not saved.

## 5. Hubs and buildings

| Rule | Detail |
|---|---|
| Position | Each building or spot is placed at the hub centre plus its listed offset |
| Kit | Buildings are assembled from the culture's kit named for the zone in [Environments & Props](../10-art/03-environments-props.md). Size by role: house 8 × 10 m · inn 14 × 18 m, two floors · hall, keep or lodge 16 × 22 m · forge, tannery, workshop, store 8 × 12 m, open-fronted where it is a craft · shed 5 × 6 m · shrine, mailbox, eyrie platform: their prop |
| Facing | The door faces the hub centre, or the nearest road if the road is closer than the centre |
| Interiors | Inns, halls, lodges, shops and any building a roster places an NPC "in" are enterable with a furnished ground floor. Others are closed shells |
| Paths | A 2 m path joins each door to the nearest road |
| NPC positions | From the [NPC rosters](../11-npcs/00-npc-index.md): each NPC stands at the building or spot its location names, inside if it is enterable, 1.5 m in front of the door if not, facing outward. Two NPCs at one spot stand 2 m apart. Vendors stand behind a counter or stall |
| A location the layout does not list | If a roster names a building or spot that the hub table does not have, the generator adds a building of the kind the NPC's role needs (a stall for a vendor, a house otherwise) on the nearest free ground inside the hub radius, facing the centre, and lists it in its report. No NPC is ever left unplaced |
| A location that is a route or a region | An NPC or group whose location is a route or an area and not a spot ("walls and the lit road", "every district and gate", "siege lines") patrols that route or is spread along it at even spacing; one located "aboard the ship" rides the transport and is placed on its deck |
| Guards | As listed; otherwise 2 at each road entering a hub radius |
| Fixed services | Each hub with an inn gets a mailbox by its door; each graveyard gets a spirit healer; each eyrie gets its flight master beside the platform |

## 6. Spawn points, patrols and nodes

| Notation in the layout | What the generator does |
|---|---|
| `×N @ (x, z) rR` | N points scattered within R metres of the point |
| "spread" | N points scattered across the sub-area's polygon |
| A gallery, room or building | N points inside that interior, along its walls and at its junctions |
| "pack" | Points in groups of the pack size, 3 m apart, groups at least 20 m apart |

Rules for every spawn point: at least 8 m from another outdoors and 5 m indoors · on ground sloping less than 30° · at least 25 m from a main road and 60 m from a hub edge unless the camp's note says otherwise · reachable on the navigation mesh from the zone's start point. The count of points equals the camp's listed count exactly.

| Behaviour | Rule |
|---|---|
| Wandering | One creature in three (not packs, not casters) wanders within 8 m of its point, pausing 4 to 12 seconds |
| Patrols | A patrol listed under "Points" follows its path there and back. In each humanoid camp of 10 or more, two of the camp's own creatures (not extra ones) patrol together around the camp at its radius |
| Facing | Humanoids at camps face the nearest fire, tent or work-spot; beasts face a random direction |

Quest objects and quest points are placed at the positions in the layout's "Points" table. Where a point is described by place and not by coordinates ("second gallery of the mine", "orchard rows"), the stated number of positions is scattered inside that place, at least 6 m apart. A quest object that no layout table mentions is placed in the sub-area its quest text names, beside the camp of the creatures the same quest involves, and is listed in the generator's report.

Gathering nodes take their counts from the layout's node table and are placed where its "Where" column says, by kind: ore on slopes above 20° or against rock, at least 30 m apart · herbs by their habitat words (roadside, woodland, water's edge, foot of hills), at least 20 m apart · fishing pools on water at least 4 m deep. Rare spawn points and chest positions are placed at the listed points.

## 7. Caves and mines inside zones

A cave or mine listed as a sub-area interior (for example Hartwell Mine: three galleries, about 220 m of tunnel, a deep cavern) is built from the cave or mine kit and joined to the surface by a cutout ([Terrain and Cutouts](../08-tech/terrain-and-cutouts.md)).

| Rule | Detail |
|---|---|
| Shape | A chain of chambers ("galleries", "caverns") joined by tunnels. Chambers are 18 to 30 m across unless a size is given; tunnels 5 m wide and 4 m high |
| Length | Tunnel lengths are set so the total matches the stated length within 10% |
| Depth | Each gallery is 4 to 6 m lower than the last, by ramps of at most 20°. A named lower level ("the Deep") is reached by a ramp from the last gallery |
| Fit | The whole interior stays inside its cutout volume and under the surface sub-area it belongs to |
| Light | A torch, candle or glowing mineral every 12 m, of the kind the text names |

## 8. Dungeons, the raid and other instances

Each instance is built from its room table in [Capitals and Instances](09-capitals-and-instances.md).

| Rule | Detail |
|---|---|
| Rooms | Each room is built from the instance's kit at exactly the listed size. "Round" rooms use the given figure as diameter. Ceiling height is 8 m, or half the room's shorter side if that is greater, up to 25 m |
| Listed features | Every counted feature (6 grave-plots, 4 slag levers, 5 ward-pylons, 12 seats) is placed, evenly spaced along the wall or in the pattern the encounter in [Encounter Data](../12-data/encounters.md) needs. These are gameplay objects, not decoration |
| Connections | Rooms are joined as the "Connects to" column says, by doorways 5 m wide. Where two rooms cannot touch, a corridor 6 m wide joins them. Corridor lengths are set so the total walkable length matches the stated figure within 10% |
| Layout | Rooms are laid out in order along a main line, turning 90° where needed to avoid overlap. Optional rooms branch off to the side. Stated height changes (a stair descending 25 m) are honoured; otherwise each room is level with the last |
| Boss rooms | Clear floor with no pillars except listed features. A door closes behind the group when the boss is engaged and opens on a kill or a wipe |
| Packs | The listed number of trash packs per room, spaced evenly along the path through it: 22 m apart where the room allows and never closer than 12 m, and as far from a boss's starting position as the room allows. One pack in four patrols between its neighbours. Pack contents come from [Encounter Data](../12-data/encounters.md) |
| Entrance and exit | The instance portal is just inside the first room. After the last boss a shortcut (door, lift or portal) returns the group to the entrance |
| Shortcuts | Built where the table lists them, opening on the stated condition |

The battleground and the arena are built the same way from their tables. Stoneheart Deeps, the interior zone, uses the zone rules (§5, §6) for content and the cave rules (§7) for shape, at the sizes in its layout file.

## 9. Capitals

Districts are sub-areas; their buildings and spots are placed by §5 from the capital's tables. Streets are roads 6 m wide (lanes 3 m) joining every district and gate. Solhaven's walls follow its outline with the listed gates; Hammerdeep is an interior built ring by ring from its kit at the listed sizes, with the lifts where listed. Ambient citizens walk the streets on loops, 1 per 15 m of street, never entering shops.

## 10. Checks

The generator refuses to finish a zone until all of these pass. They are validation rule V27 in [Content Schemas](../08-tech/content-schemas.md).

| Check | Requirement |
|---|---|
| Reachability | Every hub, quest point, spawn point, node, graveyard, cutout and exit is reachable on the navigation mesh from the zone's start point |
| Roads | Every road is continuous, at most 15% gradient, and no scattered object stands on it |
| Counts | Spawn points, nodes, chests, rare points, buildings and NPCs match the layout and roster counts exactly |
| Slopes | No walkable area steeper than 40°; no climbable route over a border |
| Safety | No hostile spawn inside the distances in §6 unless the camp's note allows it; every graveyard within 450 m of every quest point |
| Seams | Height difference across every zone edge under 0.2 m; every exit walkable in both directions |
| Stuck spots | A bot walking 2,000 random paths never becomes trapped or falls out of the world |
| Sightline | The zone's landmark is visible from at least 60% of road positions |
| Performance | The scripted client holds its frame-rate target at every point of the [visual walk](../08-tech/build-procedure.md#the-visual-walk) |

## 11. Maps

The minimap is rendered from the built zone, looking straight down, at 1 pixel per metre, in tiles. The zone map and world map paintings in the art lists are generated by the forge using that render as the guide image, so painted maps match the real ground.
