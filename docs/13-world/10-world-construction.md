# World Construction — from layout tables to built zones

[← World Layout Index](00-world-layout.md) · Format: [Terrain and Cutouts](../08-tech/terrain-and-cutouts.md) · Art: [Environments & Props](../10-art/03-environments-props.md) · Procedure: [Build Procedure](../08-tech/build-procedure.md)

The layout files say where everything is. This page says how the builder turns those tables into terrain, ground textures, scattered nature, buildings, spawn points and interiors, without a level designer. Every step is a rule that a program follows, so the result is repeatable: the same layout and the same seed give the same zone.

## 1. The world generator

| | |
|---|---|
| Tool | `tools/worldgen`, a command-line program in the game repository. Built in milestone M2 for Brightmead Vale and used for every later zone |
| Input | `content/zones/<zone>/layout.yaml`: the zone's layout tables (facts, grid map, sub-areas, hubs, points, camps, nodes, roads) transcribed field for field from its layout document, with the optional entries below wherever the zone is not a temperate lowland or a table leaves a place open. The validator checks the transcription against the counts in the document |
| Seed | The zone id hashed to a number. Every random choice uses it |
| Output | Under `content/zones/<zone>/`: the three terrain files (`terrain/height.r16`, `weights.png`, `holes.png`) · the walk grid `terrain/nav.bin` · `world.json` (buildings, props, interiors, spawn points, nodes, quest positions, guard posts, exits) · the generated records `generated/subareas.yaml`, `graveyards.yaml`, `cutouts.yaml` and `spawns.yaml` · the `minimap/` tiles · `report.md`. Sub-area names go to `content/strings/en/generated/<zone>.yaml` |
| Committed | Every generated file is committed. A test builds each zone again and fails if a committed file differs from what the generator writes, so none can go stale. The content pack carries the zone's ground (terrain, walk grid, `world.json`, minimap) and it is part of the content hash |
| Overrides | `content/zones/<zone>/overrides.yaml`, written by the zone editor: fixes made after generation (raise, flatten or smooth the ground here; paint this texture; add or remove this prop). The generator replays them after its own rules, in the order they were made: sculpting after heights, props after scattering, paint after textures. So regenerating never loses a fix, and the terrain files stay build products that nobody edits |
| Order | Building plots are planned first, so that heights can flatten them. Then heights (§2), hubs and buildings (§5), interiors and their cutouts (§7), spawn points, nodes and quest positions (§6), scattering (§4), ground textures (§3) and the walk grid, then the checks in §10. A zone that fails a check is regenerated after the layout, the generator or the overrides are corrected |

### Optional layout entries

A layout written from the tables alone builds a temperate lowland whose every interior lies under its own sub-area. The entries below say what a zone has that is not that. Each is optional and each default is what the rules in the rest of this page give without it.

| Entry | Meaning | Without it |
|---|---|---|
| `style.kit` | The building kit of the zone's hubs | `KIT-01` |
| `style.mailbox`, `style.eyrie` | The mailbox and the eyrie perch its hubs use | The human mailbox and perch |
| `style.trees` | The trees that are scattered (a list of nature assets). Dead trees on moor, marsh and badlands are not changed by it | Oak, seven in ten, and birch |
| `style.bush`, `style.bushes` | The bush that is scattered, and the share of the undergrowth of §4 that is kept (0 to 1) | The lowland bush; 1, all of it |
| `style.snow` | The minimap is drawn in snow colours | Not set: lowland colours |
| `style.rockSlope` | The slope, in degrees, above which rock shows through the ground (§3 rule 4). Deep snow lies on everything that can be climbed, so a snow zone sets it to 40 | 30 |
| `elevation.edges` | The height of the land beyond an open edge of the zone, by side (`south`, `west`, `north`, `east`), for step 10 of §2. A hanging valley gives its own height on the sides where it does not open onto lower ground. The zone laid out beyond that edge uses the same figure | The middle of the valley floor (halfway between `low` and `floor`) on every side |
| Sub-area `height` | The sub-area's target height in metres (step 2 of §2) | By the words of its text |
| Sub-area `pond` `{ centre, size, frozen }` | Still water the sub-area holds, an ellipse of that size. Frozen, it is a level bed a step under its shore, painted as ice, with nothing scattered on it: ground to walk on, not water. Open ponds are not built yet; one is left as land and named in the report | No pond |
| Sub-area `feature: { kind: spine, rise }` | A ridge along the sub-area's longer side. The sub-area's height is the height of its feet, and the crest stands `rise` metres over them, falling away toward both ends | No ridge; `rise` is 30 where a spine gives none |
| Sub-area `feature: { kind: hollow }` | A hollow 10 m deep between two hills, at the sub-area's centre | None |
| Interior `mouth` | Where the cave or mine opens, when that is not the sub-area's centre | The sub-area's centre |
| Interior `heading` | The direction the way in runs, as an (x, z) vector, used where no road arrives at the mouth. A road that ends within 6 m of the mouth always sets the direction | West |
| Interior `extent` `{ min, max }` | The rectangle of ground the interior may lie under, when it is not under its own sub-area ("interior under the camp") | The sub-area's rectangle |
| Interior `mound` | Metres the land rises over the way in, 15 m in from the mouth, so that a mouth on open ground opens in the face of a hummock and the tunnel goes into the ground. It needs a `heading`. A mouth cut into a hillside needs none | No mound |
| Interior `floorPerCreature` | Square metres of floor a gallery is given for each creature that lives in it (§7). Raised where the creatures shoot or cast | 64 |
| Interior `maxRadius` | The largest radius, in metres, a gallery may grow to for its population | 20 (40 m across) |
| Interior `galleries`, `tunnelMetres`, `deep: { name, diameter }`, `kit`, `light` | The counts and sizes the sub-area's text states | 1 gallery · 60 m of tunnel for each chamber · no lower level (45 m across and called "the Deep" where one is named without them) · `cave` · `torch` |
| Camp `where.at`, `where.radius` | The camp's creatures are scattered within `radius` metres of the point `at`. In a camp that also has an `interior`, they are where its `outside` creatures stand | `radius` 40. A camp with an `interior` and neither `at` with a `radius` nor an `area` stands its outside creatures about the mouth |
| Camp `where.area` `{ min, max }` | The camp's creatures (or, with an `interior`, those outside) are scattered over this rectangle | The sub-area's own shape |
| Camp `where.interior: { gallery }`, `where.outside` | The camp lives in that gallery of its sub-area's interior, except the number given as `outside` | Gallery 1; none outside |
| Camp `where.alsoInterior: { subarea, deepApproach }` | Two of the camp (never more than half of it) stand on the ramp down to that interior's lowest chamber, and count against those outside | None |
| Camp `where.apart` | Metres the camp keeps between its own creatures outdoors, when that is more than the 8 m of §6. For casters, of which two at once are one too many | No more than the rule's 8 m |
| Node part `area` `{ min, max }` | The rectangle that part of the node's positions is scattered over | The sub-areas the part names, or the whole zone |
| Node part `habitat: ice` | Positions on a frozen pond, clear of its shore (fishing holes cut in the ice). The other habitats are `roadside`, `woodland` and `footOfHills` | No habitat rule |
| Point `interior: { subarea, deep, gallery, back }` | The point lies in that chamber of the interior: in its middle, or with `back` against the wall across from the way in | Gallery 1, in the middle |
| Hub entry of kind `standingStone` or `spot` | A standing stone as a prop; or a named place with nothing built on it, where a roster can stand an NPC | — |
| Feature `asset` | The asset a named single feature is drawn with | By its kind (an oak, a willow, a fallen log) |
| Exit `onward` | Zones the exit's road leads on to, through the place it goes to (the Coldgate leads to Hammerdeep and on to Stoneheart Deeps). Used to place waiting NPCs (§5) | Only the zone named in `to` |
| Cutout `at: { hub, building }` | A hatch in the floor of that building, with a pit 3 m below it reached by a stair. The building becomes enterable | — |

### The walk grid

The generator's navigation product is a walk grid, not a polygon mesh: `terrain/nav.bin`, one cell to the metre, with a layer for the surface and one for each interior, joined at the interior's mouth. A cell is closed where the ground is cut away, is border, slopes more than 45°, or lies under more than 1.3 m of water; under a tree trunk, a rock or a length of hedge; and inside a building's walls, except the way through the door of an enterable one. Creatures find their paths over it, and the checks of §10 walk it.

It is the collision product as well. The server and the client both stand a character on the same floor, the terrain heights together with the walk grid's layers, read by the same code, so they cannot disagree; no physics shapes are built for the chunks.

### Hand-placed and generated cutouts

A zone has two cutout files. `generated/cutouts.yaml` holds the openings the generator makes for the interiors of §7 and is written again at every build. `cutouts.yaml`, beside the layout, holds the openings placed by hand in the zone editor; the generator reads it and never writes it. Both are rasterised into `terrain/holes.png`.

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
| 9. Slope limits | Carried out after step 10, so that the land gives way to the zone edge and no cliff is left standing against it. Walkable land is smoothed until no slope outside border cells and listed cliffs exceeds 40°. Road surfaces, river beds and the zone edge keep their heights; the land beside them is cut or filled |
| 10. Edges | Carried out before step 9. Where two zones meet, the 30 m strip on each side is blended to one shared edge profile, so the seam is invisible and walkable at every exit. The profile is a level with a gentle roughness (±3 m) that depends only on the position on the continent, so both zones compute the same line. The level is the middle of the zone's valley floor, or the height `elevation.edges` gives for that side (§1); within 150 m of a corner the levels of the two sides run together, so the line round the zone has no step in it. Within 20 m of an exit road the road sets the height, not the profile |

Named features in the text that have no coordinates ("a hollow between two hills", "a single cavern 45 m across") are built at the sub-area centre at the stated size. A sub-area described as a spine or ridge with ledges, whose rectangle also holds its own foot, is given the height of its foot and a `spine` feature for the crest; a frozen pond is a `pond`; a cave mouth on open ground is given a `mound` (§1, optional layout entries). These are laid on the sub-area targets before the rivers of step 5.

## 3. Ground textures

Each zone uses up to 8 tiling textures from its row in [Environments & Props](../10-art/03-environments-props.md). The weight map is painted by rule, later rules overriding earlier ones:

| Order | Where | Texture |
|---|---|---|
| 1 | Everywhere | The zone's base ground (grass, ash, moss, cave floor) |
| 2 | Under tree cover denser than 40% | Forest floor |
| 3 | Sub-areas described as tilled, field, farm | Tilled earth in strips aligned to the nearest road |
| 4 | Slope above 30°, or above the zone's `style.rockSlope` where the layout gives one | Rock; above 45°, cliff rock |
| 5 | Within 2 m of water, and river beds; the bed of a frozen pond | Mud, sand or gravel. A snow zone fills this slot with its ice texture, so a frozen pond is ice |
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

Nothing is placed: on a road or within 3 m of one · inside a building footprint or within 2 m · within 3 m of a spawn point, node, quest object or graveyard · on a slope above 40° (rocks excepted) · in water (reeds excepted) · on a frozen pond. Named single features (the fallen oak, the old oak, the willow) are placed exactly at their coordinates and are never scattered over.

The trees are oak and birch unless the layout's `style.trees` names the zone's own (frostpines in a snow zone), and `style.bushes` keeps only a share of the bushes and ferns in the table (§1, optional layout entries).

Each chunk holds at most 400 scattered objects, drawn with instancing; grass is a separate client-side layer and is not saved.

## 5. Hubs and buildings

| Rule | Detail |
|---|---|
| Position | Each building or spot is placed at the hub centre plus its listed offset |
| Kit | Buildings are assembled from the culture's kit named for the zone in [Environments & Props](../10-art/03-environments-props.md), which the layout gives as `style.kit` with the zone's mailbox and eyrie perch (§1). Size by role: house 8 × 10 m · inn 14 × 18 m, two floors · hall, keep or lodge 16 × 22 m · forge, tannery, workshop, store 8 × 12 m, open-fronted where it is a craft · shed 5 × 6 m · stall 3 × 4 m · mill 9 × 9 m · shrine, mailbox, eyrie platform, standing stone: their prop |
| A landmark that is a building | A landmark such as a mill stands just beyond the end of the road that leads to it, its door to the road, so the road ends at its door and not under it |
| Facing | The door faces the hub centre, or the nearest road if the road is closer than the centre |
| Interiors | Inns, halls, lodges, shops and any building a roster places an NPC "in" are enterable with a furnished ground floor, and so is a building a cutout stands in (a shed with a cellar hatch). Others are closed shells |
| Paths | A 2 m path joins each door to the nearest road |
| NPC positions | From the [NPC rosters](../11-npcs/00-npc-index.md): each NPC stands at the building or spot its location names, inside if it is enterable, 1.5 m in front of the door if not, facing outward. Two NPCs at one spot stand 2 m apart. Vendors stand behind a counter or stall |
| A location the layout does not list | If a roster names a building or spot that the hub table does not have, the generator adds a building of the kind the NPC's role needs (a stall for a vendor, a house otherwise) on the nearest free ground inside the hub radius, facing the centre, and lists it in its report. No NPC is ever left unplaced |
| A location that is a route or a region | An NPC or group whose location is a route or an area and not a spot ("walls and the lit road", "every district and gate", "siege lines") patrols that route or is spread along it at even spacing; one located "aboard the ship" rides the transport and is placed on its deck |
| Guards | As listed; otherwise 2 at each road entering a hub radius |
| An NPC whose zone is not built yet | Where a quest of this zone ends with an NPC of a zone that has no content yet, the zone importer stands that NPC inside this zone until its own is built: about 15 m in from the exit that leads to its zone, beside the road and facing in. The exit is the one whose destination is that zone, or failing that the one whose `onward` list names it (§1). Importing the NPC's own zone moves it home. A zone can so be played to its end before its neighbours exist |
| Fixed services | Each hub with an inn gets a mailbox by its door; each graveyard gets a spirit healer; each eyrie gets its flight master beside the platform |

## 6. Spawn points, patrols and nodes

| Notation in the layout | What the generator does |
|---|---|
| `×N @ (x, z) rR` | N points scattered within R metres of the point (`at` and `radius` in the layout) |
| A stated part of a sub-area ("the east half and the slope down", "the west ledges above the road") | N points scattered over the rectangle the layout gives for it (`area`) |
| "spread" | N points scattered across the sub-area's polygon |
| A gallery, room or building | N points inside that interior: along the chamber's wall, then an inner ring and its middle, then along the tunnels that meet it |
| "N outside", or a mouth or approach named with an interior | That many of the camp stand outside: about the mouth, or about the place or over the rectangle the layout gives for them. The rest are inside |
| "pack" | Points in groups of the pack size, 3 m apart, groups at least 20 m apart |

Rules for every spawn point: at least 8 m from another outdoors, or further where the camp's `apart` says so · indoors as far apart as the room allows and never closer than 5 m · on ground sloping less than 30° · at least 25 m from a main road and 60 m from a hub edge unless the camp's note says otherwise · reachable on the walk grid from the zone's start point. The count of points equals the camp's listed count exactly.

Indoor spacing is tried widest first: 11 m, then 9, then 7, then 5, each closer spacing used only for the creatures still unplaced. A creature notices a character of its level at 20 yards, so creatures 5 m apart in a room are one pack that nobody alone can fight; spread through the room and its tunnels they can be fought one at a time. For the same reason a camp of casters or shooters outdoors may keep its own further apart than 8 m (`apart`, §1).

| Behaviour | Rule |
|---|---|
| Wandering | One creature in three (not packs, not casters) wanders within 8 m of its point, pausing 4 to 12 seconds |
| Patrols | A patrol listed under "Points" follows its path there and back. In each outdoor humanoid camp of 10 or more, two of the camp's own creatures (not extra ones) patrol together around the camp at its radius |
| Facing | Humanoids at camps face the nearest fire, tent or work-spot; beasts face a random direction |

Quest objects and quest points are placed at the positions in the layout's "Points" table. Where a point is described by place and not by coordinates ("second gallery of the mine", "orchard rows"), the stated number of positions is scattered inside that place, at least 6 m apart. A quest object that no layout table mentions is placed in the sub-area its quest text names, beside the camp of the creatures the same quest involves, and is listed in the generator's report.

Gathering nodes take their counts from the layout's node table and are placed where its "Where" column says, by kind: ore on slopes above 20° or against rock, at least 30 m apart · herbs by their habitat words (roadside, woodland, water's edge, foot of hills), at least 20 m apart · fishing pools on water at least 4 m deep. Rare spawn points and chest positions are placed at the listed points.

## 7. Caves and mines inside zones

A cave or mine listed as a sub-area interior (for example Hartwell Mine: three galleries, about 220 m of tunnel, a deep cavern) is built from the cave or mine kit and joined to the surface by a cutout ([Terrain and Cutouts](../08-tech/terrain-and-cutouts.md)).

| Rule | Detail |
|---|---|
| Shape | A chain of chambers ("galleries", "caverns") joined by tunnels. Chambers are 18 to 30 m across unless a size is given; tunnels 5 m wide and 4 m high. Galleries are 7 m high, a named lower level 12 m |
| Size to population | A gallery is made as large as what lives in it needs: 64 m² of floor for each creature the camps place in it (`floorPerCreature`), up to 40 m across (`maxRadius` 20), when that is more than the size above. If a gallery of that size does not fit, one midway is tried, then the size above. An interior whose creatures shoot or cast asks for more floor and a wider limit, so that those along its wall stand out of each other's notice |
| Mouth and way in | The mouth is the sub-area's centre, or the `mouth` the layout gives. The tunnel goes in the way the road arrives at the mouth; where no road ends there, by the layout's `heading`. It runs level for 8 m through the opening, then down. On open ground the land is raised over the way in (`mound`) so the mouth opens in a slope |
| Length | Tunnel lengths are set so the total matches the stated length within 10% |
| Depth | Each gallery is 4 to 6 m lower than the last, by ramps of at most 20°, and its roof is always at least 1.5 m under the ground above. The way out of a chamber is level as far as its wall; the ramp belongs to the tunnel. A named lower level ("the Deep") is reached by a ramp from the last gallery |
| Fit | The whole interior stays inside its cutout volume and under the surface sub-area it belongs to, or under the rectangle the layout gives as its `extent` where the text puts it elsewhere ("interior under the camp"). A chamber for which no room is found is named in the report |
| Cellars | A hatch the layout lists in the floor of a building (`at: { hub, building }`) opens on a pit 3 m below the floor, as wide as the building allows, reached by a stair that goes down 3 m in 4 m |
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
| Reachability | Every hub, quest point, spawn point, node, graveyard, cutout, chamber, enterable building and exit is reachable on the walk grid from the zone's start point |
| Roads | Every road is continuous, at most 15% gradient, and no scattered object stands on it |
| Counts | Spawn points, nodes, chests, rare points, buildings and NPCs match the layout and roster counts exactly |
| Slopes | No walkable area steeper than 40°; no climbable route over a border |
| Safety | No hostile spawn inside the distances in §6 unless the camp's note allows it; every graveyard within 450 m of every quest point |
| Seams | Height difference across every zone edge under 0.2 m; every exit walkable in both directions |
| Stuck spots | A bot walking 2,000 random paths never becomes trapped or falls out of the world |
| Sightline | The zone's landmark is visible from at least 60% of road positions |
| Performance | The scripted client holds its frame-rate target at every point of the [visual walk](../08-tech/build-procedure.md#the-visual-walk) |

## 11. Maps

The minimap is rendered from the built zone, looking straight down, at 1 pixel per metre, in tiles of 256 pixels, in snow colours where the layout's `style.snow` is set. The client draws its minimap and its zone map from these tiles. The map art in the art lists is made from the same world data and never painted free, so every map matches the real ground.
