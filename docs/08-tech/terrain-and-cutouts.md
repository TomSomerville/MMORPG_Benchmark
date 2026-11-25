# Terrain and Cutouts — holes in the ground for caves and dungeons

[← Master Plan](../../MASTER_PLAN.md) · Related: [Content Schemas](content-schemas.md) · [World Layout](../13-world/00-world-layout.md) · [Architecture](architecture.md)

How zone terrain is stored, how the server and the client know where a character can stand, and how **holes are cut in the terrain** so that caves, mines, cellars and dungeons can be placed under or behind the ground. Cutting a hole and putting something in it is a data change: it needs no code and can be done at any time, including after launch, to insert a new dungeon.

## 1. Terrain format

| Property | Value |
|---|---|
| Representation | A height grid per zone: one height sample per metre. A 1,000 m zone is 1,001 × 1,001 samples; a 2,400 m zone 2,401 × 2,401 |
| Chunks | 64 × 64 m. Each chunk is a separate mesh, built on worker threads, handed to the scene at most two a frame, and streamed in and out by distance (dropped beyond 620 m). A chunk carries no collision of its own: collision is the walk grid, below |
| Detail levels | 4 per chunk: 1 m, 2 m, 4 m and 8 m spacing, chosen by distance (the coarser levels from 100, 200 and 400 m). Neighbours at different levels are joined by **skirts**: a strip hanging down behind each chunk edge. No crack can show, and a chunk is never rebuilt because its neighbour changed level |
| Surface | Up to 8 tiling textures per zone ([P05](../14-asset-pipeline/01-image-pipelines.md#p05--tiling-textures-terrain-trim-sheets-materials-about-80-terrain-20-kit-atlases)) blended by a weight map at 1 sample per metre |
| **Hole mask** | **One bit per grid cell (1 × 1 m). A set bit means: this cell of terrain does not exist.** See §2 |
| **Walk grid** | **`terrain/nav.bin`: where a character can stand, one cell per square metre, in layers.** Layer 0 is the open ground; each further layer is an interior under it (a mine, a cave, a cellar). A cell holds the height of its floor, or nothing if it cannot be stood on. It is the single source of collision and navigation for the server, the client and the generator's checks. See §1.1 |
| Files per zone | Under `content/zones/<zone>/terrain/`: `height.r16` (heights), `weights.png` (texture blend), `holes.png` (1-bit hole mask), `nav.bin` (the walk grid, compressed). Beside them: `world.json` (what the generator placed: buildings, props, interiors, hubs, the start point), `minimap/` tiles (256 px, one pixel to the metre, north at the top) and `report.md`. All are written by the world generator, committed, and carried in the content pack with their hashes, so they are part of the content hash checked at login |
| Who reads it | The client builds its meshes from the three terrain files. The server and the client both stand on the walk grid through the same code, so they cannot disagree |
| Interior zones | Stoneheart Deeps and all instances have no height grid; they are built from kit meshes. Cutouts are how open-world terrain connects to them |

### 1.1 The walk grid

| Property | Value |
|---|---|
| Built by | The world generator, from the heights, the hole mask, the interiors it builds and what it places. Cliffs, deep water, walls, tree trunks, rocks, hedges and buildings are cells with no floor. A building that can be entered has a floor inside and a gap at its door |
| Floor query | "The floor at this point nearest this height": of every layer's floor under or over the point, the one nearest the asker's height. Inside a cutout the nearest floor is the interior's. Where no layer has a floor, nothing can stand |
| Walking | A body 0.7 m wide may go straight from one point to another if every quarter metre of the way, and the body's half-width to either side, has a floor within a step of the last. Steps go to the eight neighbouring cells of a layer, and between layers wherever their floors meet (a mine mouth, a stair) |
| Paths | A* over the grid's cells, with corners cut wherever the body can walk straight. A 1,000 m zone is searched in well under a millisecond over the distances creatures chase |
| Server use | Movement validation (a claimed position must have a floor within 2 yards of its height: [Network Protocol §4.3](network-protocol.md#43-player-movement-cs-channel-1)), creature movement and pathfinding ([Architecture §4](architecture.md#4-simulation)), spawn placement, line of sight against the ground |
| Client use | The character controller stands on the same floor query; the camera stays in open air by it. No physics shapes are built per chunk |
| Units | The grid, like every terrain file, is in zone-local metres (x east, z north, height up, from the south-west corner). The server works in yards and converts at the boundary |
| Zones without terrain | A flat test map has no walk grid: everything in it is reachable and the floor is its plane. Interior zones and instances have no height grid; their walk grid has only interior layers and is built with them (T-M6-04) |

## 2. The hole mask

A cell whose hole bit is set is treated as absent everywhere:

| System | Effect of a hole |
|---|---|
| Rendering | The cell's two triangles are not drawn, at every detail level |
| Collision and navigation | The cell is not terrain floor in the walk grid. Whatever the interior puts in the hole (a ramp, a stair, a cave floor) is the floor instead, on the interior's own layer; a hole with nothing under it cannot be stood on |
| Line of sight and spell targeting | Rays pass through |
| Shadows and grass | No shadow casting from the missing cell; no grass or ground clutter spawns on it |
| Minimap and world map | Drawn as dark opening; an entrance icon is added if the cutout has a `link` |
| Falling checks | A position must have a floor within 2 yards of its height. Inside a cutout's volume (§3) the nearest floor is the interior's, so being below the terrain surface there is legitimate without a special case |
| Ghosts and corpse runs | A graveyard path may pass through a hole |

### Detail levels and holes

Coarser detail levels would otherwise close a small hole or tear its edge. Two rules prevent that:

1. A chunk that contains any hole cell is never drawn coarser than the **2 m** level, and is drawn at **1 m** within 150 m of the camera.
2. At every level a quad that overlaps a hole cell is left out, so a hole only ever grows slightly with distance and never closes.

### Hiding the edge

A hole cut in a height grid has a jagged square-stepped edge. Every hole is therefore covered at its rim by a **frame**: a mesh from a building kit that overlaps the terrain around the opening.

| Frame type | Kit pieces | Used for |
|---|---|---|
| Cave mouth | Rock arch pieces in 4, 6 and 8 m widths, with rubble skirts | Natural caves, burrows, lairs |
| Mine adit | Timbered portal with a lintel, 3 and 4 m wide | Mines, rail tunnels |
| Built gate | Stone gateway, door or portcullis | Crypts, keeps, city gates in a hillside |
| Sinkhole rim | Ring of overhanging rock and turf, 6–40 m across | Vertical shafts, pits, sinks |
| Cellar hatch | Trapdoor and stair-well, 2 × 3 m | Cellars under buildings |
| Crack | Narrow rock lips | Fissures, the chapel floor in Hollowspire |

The frame's outline, not the mask, is what the player sees. A hole without a frame is a validation error.

## 3. Cutouts: how holes are authored

Nobody paints hole bits by hand. A hole is declared as a **cutout** record, and the world generator rasterises all of a zone's cutouts into `holes.png`.

Cutouts live in two files, one entry per opening, with the same fields:

| File | Holds | Written by |
|---|---|---|
| `content/zones/<zone>/generated/cutouts.yaml` | The openings the zone's layout calls for (§5) | The world generator, at every build. Never edited |
| `content/zones/<zone>/cutouts.yaml` | Openings placed by hand | The zone editor's Cutout tool. The generator reads it and never writes it, so a rebuild cannot lose editor work |

| Field | Meaning |
|---|---|
| `id` | `cutout.<zone>.<name>` |
| `zone` | The zone the opening is in |
| `shape` | `box` (centre, size, rotation), `circle` (centre, radius) or `polygon` (points), in zone-local metres. This is the area of terrain removed |
| `depth` | How far below the surface the cutout's **volume** extends. Inside this volume the falling check is off, underground ambience and lighting apply, and the camera may go below terrain height |
| `frame` | The frame kit piece that covers the rim, with its position and rotation |
| `interior` | What fills the space: `generated` (the name of an interior the world generator builds from the layout's chambers and tunnels: it writes the geometry to `world.json` and the floors to a layer of the walk grid), `scene` (a path to an interior scene built from kit meshes, placed in the same zone, with no loading screen) or `none` (a pit that is just a hole with a floor mesh) |
| `link` | Optional. An instance or zone this opening leads to: `{instance: instance.gallowmere_crypts}` puts the instance portal inside the opening; `{zone: zone.stoneheart_deeps, at: ...}` makes it a seamless zone crossing |
| `floor` | For pits and shafts: the mesh or height that gives the bottom |
| `purpose` | Free text for the map tooltip and for validation messages |

```yaml
records:
  - id: cutout.brightmead.hartwell_mine
    zone: zone.brightmead
    shape: { box: { centre: [126.59, 450.79], size: [5, 8], rotation: -77.01 } }
    depth: 44
    frame: { piece: kit.mine.adit_4m, position: [130.97, 30.5, 449.78], rotation: -77.01 }
    interior: { generated: "Hartwell Mine" }
    purpose: "Hartwell Mine"
  - id: cutout.thornwick.crypt_gate
    zone: zone.thornwick
    shape: { box: { centre: [1080, 1260], size: [6, 6], rotation: 0 } }
    depth: 12
    frame: { piece: kit.crypt.gate, position: [1080, 0.5, 1257], rotation: 0 }
    interior: { scene: res://zones/thornwick/interiors/crypt_stair.tscn }
    link: { instance: instance.gallowmere_crypts }
    purpose: "Gallowmere Crypts"
```

### In the zone editor

The zone editor plugin (task T-M2-01) has a **Cutout tool**:

- Draw a box, circle or polygon on the terrain; the hole appears at once in the editor view.
- Pick a frame from the kit list; it snaps to the opening and to the terrain's slope.
- Assign an interior scene or leave it empty; assign a link if it leads to an instance.
- Moving or resizing a cutout re-cuts the terrain live. Deleting it restores the ground.
- The tool writes only the hand-placed `cutouts.yaml`. `holes.png` is always a build product, never edited.

The editor writes fixes, not terrain. Its sculpt, paint and prop tools write `content/zones/<zone>/overrides.yaml`, and its Cutout tool writes `cutouts.yaml`; nothing else. "Save and rebuild" runs the world generator, which replays the overrides after its own rules (sculpt after heights, props after scatter, paint after textures) and rasterises both cutout files. A rebuild therefore never loses a fix, and the terrain files and the walk grid stay build products.

## 4. Inserting a dungeon later

To add a new dungeon to a finished zone, with no code:

1. In the zone editor, place a cutout where the entrance should be and choose a frame.
2. Build the entrance interior (a few kit pieces: a stair or a short tunnel) as a small scene and assign it.
3. Create the instance record and its map as for any dungeon ([Content Schemas §2.11](content-schemas.md#211-instance-encounter-battleground)), and set the cutout's `link` to it.
4. Choose "Save and rebuild" (or run `worldgen <zone>`), then `content build`. The hole mask and the walk grid are regenerated; the minimap gains an entrance icon.

The same steps add a cave, a cellar, a mine or a tunnel between two zones.

Two kinds of underground space are supported, and a cutout can lead to either:

| Kind | What it is | When to use |
|---|---|---|
| **Seamless interior** | Kit geometry placed under the terrain in the same zone. Players walk in with no loading screen and everyone inside is in the shared world | Caves, mines, burrows, cellars, lairs, open-world elite areas |
| **Instance entrance** | A short seamless entry (a stair, a gate, a lift) ending at an instance portal | Dungeons and raids, which are private copies |

## 5. Cutouts in the launch game

Every opening the world layouts call for. Positions are zone-local and come from the [layout files](../13-world/00-world-layout.md).

| Zone | Cutouts |
|---|---|
| Brightmead Vale | Hartwell Mine mouth (130, 450); the cellar hole in Hobb's store shed |
| Embercrag Hollow | Gravelkin Warrens mouth (150, 690); the larder hole at Coldhearth; Kiln Cave mouth (850, 880); Blackmatch chief's cave (630, 990); Coldgate tunnel to Hammerdeep (300, 0) |
| Harrowfield | Vane Manor cellar hatch; the quarry is open terrain, not a cutout |
| Russetwood | Rootgnaw Burrows: 5 burrow mouths under the root-plates around (240, 1170) |
| Stonewake Dale | The Sinks: the mouth in the first sink (500, 240), and the four open pits around (570, 140), as sinkhole rims; Daleside Adit to Stoneheart Deeps (0, 800) and its upper drift (70, 900); Old Brewery cellar; Dalegate to Hammerdeep (100, 1400) |
| Stoneheart Deeps | An interior zone; reached through the Daleside Adit, the Long Stair from Hammerdeep's Deepgate, and the Deep Gate rail-tunnel |
| Thornwick Marches | Wolfscar Den (350, 720); **Gallowmere Crypts gate (1080, 1260), an instance entrance**; Ashgrave Estate cellar |
| Ironroot Highlands | Old Ironhide's cave (380, 1560); the root-hollow under the Singing Stones (1240, 1760); Lurker Hollows: 3 cave mouths; Deepseam Mine mouth (800, 260); the Deep Gate rail-head (640, 1960); Brandforge inner forge |
| Cinderfall Barrens | **The Slagworks Ore Lift (320, 1640), an instance entrance**; Vitrea's glass cave (1840, 1180) |
| The Riftlands | Howler Warrens: cliff caves on three levels; the Dustpit sinkhole under Kite's Rest; the Widow's Shaft (1320, 760), a 180 m vertical shaft; Jory Finn's test pit and two others on the Spoil Heaps; **the Hollow Throne entrance behind the Maw-Scar (2300, 120), an instance entrance** |
| Veilmoor | Gloomhollow: 3 bat caves; the great barrow mound door (1600, 1500) and 3 lesser mounds; the Hollowspire keep gate is a building doorway, not a terrain cutout |
| Hammerdeep | The Seagate sea-arch, Coldgate, Dalegate and Deepgate: openings in the mountain's outer shell |

About 60 cutouts in all.

## 6. Validation

Added to the content validator as rule **V26**, in five parts:

| Check | Fails when |
|---|---|
| Frame | A cutout has no frame, or the frame does not cover the whole rim of the hole |
| Walkable link | There is no continuous walkable path from the terrain outside, through the opening, onto the interior's floor (tested on the zone's walk grid) |
| No stranding | A cutout's hole overlaps a road, a spawn camp, a hub or a graveyard not meant to be inside it |
| Depth | The interior extends outside the cutout's volume. For a generated interior the world generator enforces this itself: it sizes the volume from the interior it builds |
| Instance entrances | An instance's `entrance` does not lie inside a cutout or a building |
