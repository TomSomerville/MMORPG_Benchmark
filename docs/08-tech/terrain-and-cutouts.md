# Terrain and Cutouts — holes in the ground for caves and dungeons

[← Master Plan](../../MASTER_PLAN.md) · Related: [Content Schemas](content-schemas.md) · [World Layout](../13-world/00-world-layout.md) · [Architecture](architecture.md)

How zone terrain is stored, and how **holes are cut in it** so that caves, mines, cellars and dungeons can be placed under or behind the ground. Cutting a hole and putting something in it is a data change: it needs no code and can be done at any time, including after launch, to insert a new dungeon.

## 1. Terrain format

| Property | Value |
|---|---|
| Representation | A height grid per zone: one height sample per metre. A 1,000 m zone is 1,001 × 1,001 samples; a 2,400 m zone 2,401 × 2,401 |
| Chunks | 64 × 64 m. Each chunk is a separate mesh with its own collision and is streamed in and out by distance |
| Detail levels | 4 per chunk: 1 m, 2 m, 4 m and 8 m spacing, chosen by distance; chunk edges are stitched so neighbours at different levels meet without cracks |
| Surface | Up to 8 tiling textures per zone ([P05](../14-asset-pipeline/01-image-pipelines.md#p05--tiling-textures-terrain-trim-sheets-materials-about-80-terrain-20-kit-atlases)) blended by a weight map at 1 sample per metre |
| **Hole mask** | **One bit per grid cell (1 × 1 m). A set bit means: this cell of terrain does not exist.** See §2 |
| Files per zone | `height.r16` (heights), `weights.png` (texture blend), `holes.png` (1-bit hole mask), under `content/zones/<zone>/terrain/` |
| Who reads it | The client builds meshes and collision from it. The server builds its collision and navigation mesh from the **same three files**, so both always agree |
| Interior zones | Stoneheart Deeps and all instances have no height grid; they are built from kit meshes. Cutouts are how open-world terrain connects to them |

## 2. The hole mask

A cell whose hole bit is set is treated as absent everywhere:

| System | Effect of a hole |
|---|---|
| Rendering | The cell's two triangles are not drawn, at every detail level |
| Collision | No collision: players, creatures and projectiles pass through |
| Navigation mesh | The cell is not walkable terrain; whatever geometry is placed in the hole (a ramp, a stair, a cave floor) provides the walkable surface instead |
| Line of sight and spell targeting | Rays pass through |
| Shadows and grass | No shadow casting from the missing cell; no grass or ground clutter spawns on it |
| Minimap and world map | Drawn as dark opening; an entrance icon is added if the cutout has a `link` |
| Falling checks | The "fell through the world" safety check is disabled inside a cutout's volume (§3), because being below the terrain surface there is legitimate |
| Ghosts and corpse runs | A graveyard path may pass through a hole |

### Detail levels and holes

Coarser detail levels would otherwise close a small hole or tear its edge. Two rules prevent that:

1. A chunk that contains any hole cell is never drawn below the **2 m** level, and the hole's cells are always drawn at **1 m** within 150 m of the camera.
2. At coarser levels a hole cell removes every triangle that overlaps it, so a hole only ever grows slightly with distance and never closes.

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

Nobody paints hole bits by hand. A hole is declared as a **cutout** record, and the build rasterises all cutouts into `holes.png`.

`content/zones/<zone>/cutouts.yaml`, one entry per opening:

| Field | Meaning |
|---|---|
| `id` | `cutout.<zone>.<name>` |
| `shape` | `box` (centre, size, rotation), `circle` (centre, radius) or `polygon` (points), in zone-local metres. This is the area of terrain removed |
| `depth` | How far below the surface the cutout's **volume** extends. Inside this volume the falling check is off, underground ambience and lighting apply, and the camera may go below terrain height |
| `frame` | The frame kit piece that covers the rim, with its position and rotation |
| `interior` | What fills the space: `scene` (a path to an interior scene built from kit meshes, placed in the same zone, with no loading screen) or `none` (a pit that is just a hole with a floor mesh) |
| `link` | Optional. An instance or zone this opening leads to: `{instance: instance.gallowmere_crypts}` puts the instance portal inside the opening; `{zone: zone.stoneheart_deeps, at: ...}` makes it a seamless zone crossing |
| `floor` | For pits and shafts: the mesh or height that gives the bottom |
| `purpose` | Free text for the map tooltip and for validation messages |

```yaml
records:
  - id: cutout.bm.hartwell_mine
    shape: { box: { centre: [130, 450], size: [5, 8], rotation: 80 } }
    depth: 40
    frame: { piece: kit.mine.adit_4m, position: [132, 12.0, 450], rotation: 80 }
    interior: { scene: res://zones/brightmead/interiors/hartwell_mine.tscn }
    purpose: "Hartwell Mine"
  - id: cutout.tm.crypt_gate
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
- The tool writes only `cutouts.yaml`. `holes.png` is always a build product, never edited.

## 4. Inserting a dungeon later

To add a new dungeon to a finished zone, with no code:

1. In the zone editor, place a cutout where the entrance should be and choose a frame.
2. Build the entrance interior (a few kit pieces: a stair or a short tunnel) as a small scene and assign it.
3. Create the instance record and its map as for any dungeon ([Content Schemas §2.11](content-schemas.md#211-instance-encounter-battleground)), and set the cutout's `link` to it.
4. Run `content build`. The hole mask, collision and navigation mesh are regenerated; the minimap gains an entrance icon.

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
| Embercrag Hollow | Gravelkin Warrens mouth (150, 690); the larder hole at Coldhearth; Kiln Cave mouth (850, 880); Coldgate tunnel to Hammerdeep (300, 0) |
| Harrowfield | Vane Manor cellar hatch; the quarry is open terrain, not a cutout |
| Russetwood | Rootgnaw Burrows: 5 burrow mouths under the root-plates around (240, 1170) |
| Stonewake Dale | The six Sinks around (830, 180), as sinkhole rims; Daleside Adit to Stoneheart Deeps (0, 800); Old Brewery cellar; Blackmatch chief's cave (1380, 1390); Dalegate to Hammerdeep (100, 1400) |
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
| Walkable link | There is no continuous walkable path from the terrain outside, through the opening, onto the interior's floor (tested on the generated navigation mesh) |
| No stranding | A cutout's hole overlaps a road, a spawn camp, a hub or a graveyard not meant to be inside it |
| Depth | The interior scene extends outside the cutout's volume, so part of it would be below un-cut terrain where the falling check is on |
| Instance entrances | An instance's `entrance` does not lie inside a cutout or a building |
