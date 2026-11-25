# World Layout — Stonewake Dale and Stoneheart Deeps

[← World Layout Index](00-world-layout.md) · Zones: [Stonewake Dale](../05-zones/t2-stonewake-dale.md) · [Stoneheart Deeps](../05-zones/t2-stoneheart-deeps.md) · Prev: [Harrowfield and Russetwood](02-harrowfield-russetwood.md) · Next: [Thornwick Marches](04-thornwick-marches.md)

Notation and rules are in the [index](00-world-layout.md).

# Stonewake Dale

| | |
|---|---|
| Size and offset | 1,400 × 1,400 m · Khazrun (1200, 4600). Each grid cell is 140 m |
| Shape | A farmed valley running north to south between Mount Khaz (north-west) and a long ridge (east). The dam closes the valley's north end; its millrace runs down the middle to Hopstead |
| Elevation | Valley floor 0–15 m · terraces up to 40 m · Ridgefold 55 m · High Pastures 80 m · dam crest 60 m |
| Landmark | Stonewake Dam, a grey wall across the north end at (900, 1270) |
| Exits | Dalegate road → Hammerdeep (100, 1400) · Bouldergate Pass → Embercrag (300, 1400) · Daleside Adit → Stoneheart Deeps (0, 800) · south road → Ironroot (700, 0) |

```
      A  B  C  D  E  F  G  H  I  J
 10   .. .. .. .. .. DM DM .. BC BC
  9   ## .. .. .. MR DM DM SG BC BC
  8   ## OB OB .. MR .. .. SG SG ##
  7   ## OB OB .. MR .. .. HP HP ##
  6   .. .. HY HY MR .. .. HP HP ##
  5   ## .. HY HY MR .. RF RF HP ##
  4   ## .. .. .. HS HS RF RF .. ##
  3   ## BT BT .. HS HS .. .. .. ##
  2   ## BT BT BT .. GS GS .. .. ##
  1   ## .. BT .. .. GS GS .. .. ##
```

## Sub-areas

| Code | Sub-area | Centre | Size | Elevation and terrain |
|---|---|---|---|---|
| HS | Hopstead | (640, 480) | 220 × 220 | Market village around a brewhouse green; two mills on the race |
| BT | The Barley Terraces | (320, 300) | 400 × 380 | Stepped fields with dry-stone walls climbing west |
| RF | Ridgefold | (970, 600) | 240 × 240 | Sheep-folds and bothies on a shoulder of the ridge |
| HP | The High Pastures | (1140, 820) | 260 × 400 | Open hill grazing up to the snow line; 4 stone bothies |
| GS | The Gravelkin Sinks | (830, 180) | 280 × 280 | 6 sinkholes opening into about 240 m of tunnel; the deepest sink at (880, 120) |
| HY | The Hop-Yards | (440, 760) | 260 × 260 | Rows of blighted hop-poles |
| OB | The Old Brewery | (270, 1050) | 240 × 240 | Stone brewhouse with a vat hall, cellar and yard |
| MR | The Millrace | Runs dam foot (780, 1200) → (640, 900) → (630, 600) → Hopstead mills | 12 m channel with a path; 6 culverts | Stone-lined, fast water, crossed by 4 slab bridges |
| DM | Stonewake Dam | (850, 1290) | 280 × 180 | Dam crest road, two sluice-houses (east and west), 3 more charge points along the crest; reservoir behind (scenery) |
| SG | Slagfall Gully | (1090, 1180) | 220 × 260 | Black scree below the mountain's forge-vents |
| BC | Blackmatch Camp | (1300, 1310) | 200 × 240 | Side canyon: floor camp, goat-track along the north wall, powder-tent on a ledge, the chief's cave at the head |

## Hubs

| Hub | Centre | Radius | Buildings and spots |
|---|---|---|---|
| Hopstead | (640, 480) | 110 | Moot-house (0, +55) · brewhouse, kitchen and eyrie on its roof (−30, +10) · *The Barley Mow* (+35, 0) · hop-yard gate (−80, +90) · smithy on the green (+10, −30) · tan-yard (−100, −50) · weaving-house (+60, −50) · physic garden (+90, +40) · cottage at the lane end (+120, −80) · market stall (−10, −5) · muster field (−60, −90) · hearth-house (+85, −10) · wanted board on the green · mailbox by the inn · graveyard (+140, +90) |
| Ridgefold | (970, 600) | 60 | Ranger bothy (0, 0) · sheep-fold (+30, +20) · lambing shed (−25, +30) |
| Dam east sluice-house | (960, 1290) | 25 | Dammaster's post |

## Points

| Point | Position | Used by |
|---|---|---|
| Crates of Stolen Stores (12 positions) | Lower Sinks tunnels | ST-06 |
| Chief Gnarr | Deepest sink (880, 120) | ST-07 |
| Tinker Sparkwright's sluice hut | (650, 880) | ST-09 |
| Millrace Culverts (6) | (770, 1150) · (720, 1050) · (670, 950) · (640, 820) · (632, 700) · (630, 600) | ST-09 |
| Set Cinder-Charges (6) | East sluice-house 2 · west sluice-house 1 · crest 3 | ST-14 |
| Brewmaster Maltby | Brewery yard (330, 990) | ST-12 |
| Blackmatch Ledger | Powder-tent (1330, 1360) | ST-16 |
| Dolga Blackmatch | Cave at the canyon head (1380, 1390) | ST-17 |
| Powderkeg Pol | Powder store (1290, 1260) | ST-19 |
| Old Bitterhorn | Ridge top (1250, 960) | ST-18 |
| Angler Pikehook | Dam-foot pool (780, 1190) | — |
| Stonesinger Furrow | Top terrace wall (160, 380) | — |
| Greedy Gund (rare) | 3 bothies on the High Pastures | — |
| Graveyards | Hopstead (780, 570) · Ridgefold (900, 680) · dam road (760, 1100) | — |
| Chests (one active) | Sink chamber · brewery cellar · Blackmatch floor tent · high bothy | — |

## Spawn camps

| Camp | Creature | Count | Where | Notes |
|---|---|---|---|---|
| ST-S01 | Feral Billy | 24 | BT, spread | |
| ST-S02 | Highland Buzzard | 14 | BT upper walls | |
| ST-S03 | Shale Bear | 20 | HP bothies, 5 at each | |
| ST-S04 | Gravelkin Sinkdweller | 24 | GS sink rims and upper tunnels | |
| ST-S05 | Gravelkin Bonechewer | 16 | GS lower tunnels | |
| ST-S06 | Dale Rustler | 20 | HP south and RF edge | |
| ST-S07 | Rustler Hound-Master | 22 | HP north | Each summons 2 hounds |
| ST-S08 | Hop-Blight Beetle | 18 | HY rows | |
| ST-S09 | Fermented Ooze | 18 | OB vat hall and cellar | |
| ST-S10 | Slagborn Sapper | 16 | DM crest and sluice-houses | Plus scripted spawns at 2 culverts |
| ST-S11 | Loose Slag Sprite | 18 | SG | |
| ST-S12 | Slagborn Powderkeg | 12 | BC: 4 goat-track, 8 floor | |
| ST-S13 | Slagborn Sapper | 8 | BC floor | |

## Nodes

| Node | Positions | Where |
|---|---|---|
| Copper Vein | 20 | Terrace walls |
| Tin Vein | 16 | Sinks 8 · dam abutments 8 |
| Dewleaf | 14 | Field margins |
| Bramblethorn | 22 | Hop-yards, terrace walls |
| Marshbloom | 22 | Millrace banks, dam-foot pool |
| Fishing | Millrace and dam-foot pool | Mussel beds at the pool for River Pearls |

## Roads

| Road | Path |
|---|---|
| Dale Road | Ironroot (700, 0) → Hopstead (640, 480) → (560, 950) → (300, 1250) → Dalegate (100, 1400) |
| Bouldergate Path | (300, 1250) → (300, 1400) |
| Adit Lane | Hopstead → Hop-Yards → Daleside Adit (0, 800) |
| Ridge Track | Hopstead → Ridgefold (970, 600) → High Pastures (1140, 820) |
| Race Path | Hopstead mills → along the millrace → dam foot → switchback up to the crest (850, 1290) |
| Canyon Track | Dam crest east end → Slagfall Gully → Blackmatch Camp mouth (1210, 1250) |

---

# Stoneheart Deeps

| | |
|---|---|
| Footprint and offset | 900 × 1,000 m · Khazrun (200, 5000) |
| Structure | Three cavern levels stacked under Mount Khaz. **U** Upper Galleries at +80 m · **G** the Great Cavern at 0 m (800 m across, 120 m ceiling) · **W** the Underworks at −70 m. Positions are given as level and (x, z) |
| Landmark | Lanternhold's lamps on the north wall of the Great Cavern, visible from everywhere on level G |
| Exits | Long Stair up to Hammerdeep's Deepgate (U 500, 1000) · Daleside Adit to Stonewake Dale (U 900, 400) · Deep Gate rail-tunnel to Ironroot (W 500, 0) |
| Links between levels | Long Stair (U → G at Lanternhold) · Lanternhold lift (G ↔ W) · Trestle rail-ramps (G ↔ W) · Underwarren tunnels (U ↔ G ↔ W, hostile) · Crystal Galleries stair (U ↔ G) |

```
 Side view, looking east            north (Hammerdeep) -->
 +80  U  [Adit]---Upper Galleries---Crystal Galleries (upper)---[Long Stair top]
                \                         |stair                    /
   0  G   Glowcap Grotto -- Junction -- Crystal Galleries -- LANTERNHOLD
            |underwarrens|      \trestles                       |lift
 -70  W  [Deep Gate]--Runaway Line--------Shattered Hall----the Undercut
```

## Sub-areas

| Code | Sub-area | Level | Centre | Size | Terrain |
|---|---|---|---|---|---|
| LS | The Long Stair | U → G | (500, 960) → (460, 840) | 60 wide, 220 m of stair in 4 flights | Carved stair with lamp-niches and landings |
| LH | Lanternhold | G | (450, 800) | 240 × 160 | Hall-town built into the north cavern wall on 3 terraces; lower gate at (450, 720) |
| GG | Glowcap Grotto | G | (230, 540) | 320 × 360 | Mushroom forest; tending-ring at (300, 620); deep grotto at (120, 420) |
| CJ | Cartwright's Junction | G | (600, 540) | 160 × 160 | Rail yard and turntable |
| TS | The Trestles | G → W | (720, 340) | 240 × 300 | Timber rail viaducts over a chasm; wrecked carts on the lower spans |
| UW | Gravelkin Underwarrens | U ↔ W | (320, 260) | 300 × 300 footprint, about 300 m of tunnel on 3 levels | Round gnawed tunnels; Krakk's chamber at the bottom |
| UG | Upper Galleries | U | (600, 480) | 500 × 300 | Worked-out copper galleries from the Adit to the Crystal stair |
| CG | Crystal Galleries | U and G | (790, 720) | 200 × 360 | Geode caverns; assay bench at (760, 640) on G; 12 gallery pillars |
| SH | The Shattered Hall | W | (240, 760) | 260 × 240 | Collapsed ancestral hall; sealed threshold at (330, 700) |
| RL | The Runaway Line | W | (460, 420) | 420 × 160 | A long straight of track with sidings; signal hut at (560, 470) |
| UC | The Undercut | W | (690, 800) | 320 × 320 | Six bore mouths in an arc, drafting-tent on a side ledge, ventilation crawl along the east wall, the Great Bore chamber at the north end |
| DG | Deep Gate | W | (500, 60) | 120 × 120 | Rail-head and tunnel mouth |

## Hubs

| Hub | Centre | Radius | Buildings and spots |
|---|---|---|---|
| Lanternhold | G (450, 800) | 110 | Warden's balcony, top terrace (0, +50) · *The Trimmed Wick* (−40, +20) · hall kitchen (−20, +35) · still-room (+40, +30) · market gallery (+10, 0) · wick-loft (+70, +10) · lower terrace hide-worker (−80, −20) · sick-hall (+90, −10) · drill gallery (−60, −40) · lower gate and Sapper-Sergeant (0, −80) · lift to the Underworks (+110, −60) · wanted board at the gate · mailbox by the inn · graveyard (−130, −30) |
| Cartwright's Junction | G (600, 540) | 50 | Turntable (0, 0) · rail-forge (+30, +20) · cart platform (−20, −25) |
| Mine-cart stops | Lanternhold lower gate · Junction · Deep Gate | — | 45 seconds a leg |

## Points

| Point | Position | Used by |
|---|---|---|
| Lamp-keeper Wickfast | U (500, 970), top landing | SD-02 |
| Ore Crates in wrecked carts (12) | TS lower spans | SD-06 |
| Shard-Chief Krakk | UW bottom chamber, W (330, 200) | SD-07 |
| Gallery Pillars (6 with charges) | CG, G level | SD-09 |
| Thane's threshold (Ancestor-speaker) | W (330, 700) | SD-10, SD-11 |
| Rune-wright's signal hut | W (560, 470) | SD-12 |
| Bore Mouths (6) | UC arc, W (560–820, 700–760) | SD-14 |
| Survey Plans | Drafting-tent, W (820, 840) | SD-16 |
| Vigga Deepdrill and the Great Bore (3 valves) | W (690, 930) | SD-17 |
| Fusewright Odd | Powder magazine, W (590, 880) | SD-19 |
| Old Blindmaw | Deep grotto, G (120, 420) | SD-18 |
| Glimmerqueen (rare) | 3 geodes in CG | — |
| Graveyards | Lanternhold (320, 770) · Junction (650, 600) · Underworks lift foot, W (560, 740) | — |
| Chests (one active) | Underwarren chamber · Shattered Hall dais · trestle cart · Undercut crawl | — |

## Spawn camps

| Camp | Creature | Count | Where | Notes |
|---|---|---|---|---|
| SD-S01 | Lanternwing Bat | 24 | LS niches and UG | |
| SD-S02 | Rail Rat | 16 | TS and CJ sidings | Pairs |
| SD-S03 | Glowcap Shambler | 20 | GG, spread | |
| SD-S04 | Pale Cave Bear | 16 | GG west half | |
| SD-S05 | Gravelkin Underdweller | 24 | UW upper and middle tunnels | |
| SD-S06 | Gravelkin Shardchewer | 14 | UW lower tunnels and TS lower spans | |
| SD-S07 | Crystal Skitterer | 20 | CG, both levels | Camouflaged on walls |
| SD-S08 | Restless Ancestor | 24 | SH | |
| SD-S09 | Rogue Rail-Golem | 18 | RL, patrolling the track | Charge along the rails |
| SD-S10 | Rock Borer | 16 | RL sidings and the tunnel to DG | Burrowed |
| SD-S11 | Geode Sprite | 18 | CG lower level and the stair | |
| SD-S12 | Slagborn Tunneler | 18 | UC bore mouths, 3 each | Plus scripted spawns at 2 pillars |
| SD-S13 | Slagborn Blastwright | 14 | UC: 4 ventilation crawl, 10 main bore | |

## Nodes

| Node | Positions | Where |
|---|---|---|
| Copper Vein | 18 | UG |
| Tin Vein | 26 | CG 18 · UW 8 |
| Silver Vein | Replaces a tin vein in CG 12% of the time | |
| Dewleaf | 10 | GG |
| Glowcap (cooking) | From Shamblers only | |
| Fishing | None | |

## Routes

| Route | Path |
|---|---|
| Lantern Road (lit, safe) | Long Stair → Lanternhold → Junction → Trestle upper span → Adit branch up to U |
| Grotto Path (lit to the tending-ring) | Lanternhold → (300, 620) |
| Gallery Stair | Junction → Crystal Galleries G → U |
| Lower Road (lamps out; lit again after SD-17) | Lanternhold lift foot → Shattered Hall threshold, and → Runaway Line → Deep Gate |
| Bore Road | Lift foot → the Undercut |
| Rail | Lanternhold lower gate → Junction → Trestles ramp down → Runaway Line → Deep Gate → tunnel to Ironroot |
