# Asset Pipelines 4 — Placeholders and Swapping In Generated Assets

[← Asset Forge](00-asset-forge.md) · Prev: [Audio and fonts](03-audio-pipelines.md)

How the game runs on stand-in assets from the first day, and how each finished asset replaces its stand-in, including in a client that is already running. This page is the authority on both.

## 1. The idea in one paragraph

Every asset has an **asset contract**: the things about it that the game depends on and that must be identical in the stand-in and the finished asset. The contract is written first, from the specification, before anything is generated. A **placeholder** is the simplest file that satisfies the contract. A **generated asset** is a better-looking file that satisfies the same contract. Because the game is built only against contracts, replacing one with the other changes how the game looks and sounds and nothing else.

## 2. There is no shared placeholder

A wolf, a bear and a human do not share a placeholder, because they do not share a skeleton. **Each asset gets its own placeholder, generated from its own contract.**

For anything with a skeleton, the contract includes the skeleton itself. The game has 67 rig contracts: the manifest's 65 rigs (2 player rigs, 62 creature and boss rigs, listed in [Creatures & NPCs](../10-art/02-creatures-npcs.md), and the horse mount), plus the ship and the mine-cart, whose moving parts need bones for their clips. Each rig has its own skeleton definition, written as data before any model exists. The placeholder for a rigged asset is a **block-out figure built from that skeleton**: one box per bone, as long as the bone, attached rigidly to it.

| Rig | Its skeleton | Its placeholder looks like |
|---|---|---|
| Human | Two legs, two arms, spine, head; hand, head and back sockets | A blocky two-legged figure 1.8 m tall |
| Dwarf | The same bone names, shorter and broader | A blocky two-legged figure 1.35 m tall |
| Canine (wolves, jackals, hounds) | Four legs, spine, neck, head, jaw, tail | A blocky four-legged figure with a tail |
| Bear | Four legs, heavy spine, short neck; can rear | A bulkier four-legged figure |
| Spider | Eight legs, two body segments | A two-box body on eight jointed sticks |
| Bird, serpent, blob, construct, plant, and the rest | Each its own | Each its own block-out |

So the wolf placeholder walks on four legs with the wolf's gait, and the human placeholder walks on two, from the first day. When the generated wolf arrives it has the **same skeleton**, bone for bone, because the forge's rig-fit carries every generated model onto its rig contract's skeleton, in the contract's rest pose ([P13](02-3d-pipelines.md#p13--characters-and-creatures-base-models-4-player-bodies-110-customisation-pieces-62-creature-rigs-base-models-18-bosses) and [P14](02-3d-pipelines.md#p14--rigs-and-skinning-67-rigs)). That shared skeleton is what lets one replace the other.

Creatures that share a rig (the art lists give each rig several skins: a Vale Wolf, a Rime Wolf and a Briarwood Stalker are one canine rig) use the same block-out, each scaled to its own size and tinted its own colour so they can be told apart.

### 2a. Fitted bodies, kept templates and dressed bodies

A skeleton is shared by everything on a rig; a UV layout is not. Three kinds of model can stand on one rig contract:

| Model | Mesh and UV layout | Where it is |
|---|---|---|
| **Template** | The model-free maker's body for the rig family. All template skins of the rig share its UV layout (`uv_layout` in the rig contract) | The asset's own file until a fitted body replaces it; after that, beside it as `<name>.template.glb` |
| **Fitted body** | A generated mesh carried onto the skeleton by rig-fit: one mesh, its own baked texture, **its own UV layout**. Clothing, hair and face are part of the mesh | The asset's own file, `<name>.glb`, state `generated` |
| **Dressed body** | A fitted body made for **one outfit on one body**: that body's skeleton under a mesh that already wears the outfit | Beside the outfit's texture, named for the outfit and the body: `client/assets/outfits/<outfit file name>.<body id in lower case>.glb`, for example `….chr-005.glb` |

Rules:

1. **Placing a fitted body keeps the template.** When a generated body or creature replaces a template for the first time, the acceptance step's caller copies the template to `<name>.template.glb` before the new file is renamed into place. A skin painted for the template's layout fits that mesh and no other.
2. **Which model the client builds**, for an entity with a body and optionally a skin or outfit: if a dressed body exists for this outfit on this body, that file, whole, and the outfit texture is not applied; otherwise, if the body is `generated` and the skin or outfit is not, the kept template with the skin applied; otherwise the body's own file with the skin applied.
3. **A skin made for a fitted model** (a creature variety's tint of the fitted model's texture, [P07](01-image-pipelines.md)) is delivered as `generated`, so by rule 2 it is applied to the fitted model.
4. A dressed body is not a manifest asset of its own: it has no id, no state entry and no placeholder. Its presence beside the outfit is what the client tests.

Open: whether dressed bodies are the permanent method for NPC clothing, in which case each needs a manifest row, a contract and a state entry, or a measure for the starting zones, is the owner's decision.

## 3. Contracts

Contracts live in the repository as data and are written during milestone MA, before placeholders and before generation.

### 3.1 Rig contract (`content/rigs/<rig-id>.yaml`), one per rig

| Field | Meaning |
|---|---|
| `id`, `family` | Rig id from the art lists; template family (biped, dwarf biped, quadruped, bird, spider, serpent, blob, construct, plant, and so on) |
| `bones` | Every bone: name, parent, rest position and rotation, length. Names are fixed for the life of the project |
| `sockets` | Named attachment points and the bone each hangs from: `hand_r`, `hand_l`, `head`, `back`, `hip_l`, `hip_r`, `mouth`, `chest_fx`, `feet_fx`, `overhead` (nameplate) |
| `height`, `radius` | Standing height and body radius in metres. These also define the gameplay collision capsule, which never comes from the visual model |
| `clips` | Every animation clip the rig must have: name, length in milliseconds, loop flag, contact frame (the moment a hit lands or a spell releases), root-motion speed |
| `uv_layout` | Id of the UV layout all skins painted for this rig's template share. A fitted model has a layout of its own (§2a) |
| `scale_range` | Smallest and largest scale used by this rig's skins |

**Clip lengths and contact frames are set by rule from the clip's name**, since no per-clip table exists in the game data. The client scales playback to the weapon's speed or the spell's cast time, so the contract fixes proportions, not gameplay timing.

| Clip | Length | Contact | Root motion |
|---|---|---|---|
| Melee swing | 1.0 s | 0.4 s | — |
| Cast: ready | 0.5 s | — | — |
| Cast: loop | 1.0 s, loops | — | — |
| Cast: release | 0.6 s | 0.15 s | — |
| Walk | 1.0 s, loops | — | 2.5 yd/s |
| Run | 0.7 s, loops | — | 7 yd/s |
| Death | 2.0 s | — | — |

A clip the art lists give as one ("directed cast: ready, loop, release") is three clips in the contract. **Creature rigs name their clips more simply than player rigs** (`idle`, `attack_a`, `walk`, `run`, `death`). Where a rig has no clip of the name the game asks for, the client plays the rig's nearest: `idle_a` → `idle`, `1h_swing_a` → `attack_a`, `backpedal` and the strafes → `walk`, `jump_loop` → `run`, `dead_pose` → `death`.

### 3.2 Asset contract (the manifest entry), one per asset

| Kind of asset | What the contract fixes |
|---|---|
| Every asset | Id · file path and name · format · state file entry |
| Static model (prop, weapon, kit piece, nature) | Bounding size, the box the game places and collides with (marked `size_is: bound` where the size table has no size for the thing itself, so the box is only a limit) · pivot position · forward axis · material slot names · collision proxy (a box, capsule or the kit generator's collision mesh, defined separately from the visual model) · sockets if any (a weapon's `grip`, `tip`) |
| Rigged model | Its rig contract · scale · material slot names |
| Skin or outfit | The rig and the model whose UV layout it paints (the template's shared layout, or a fitted model's own) · texture size. An outfit may also have dressed bodies beside it (§2a) |
| Animation clip | Rig · clip name · length · loop flag · contact frame |
| Texture, icon, UI piece | Pixel size · whether it tiles · whether it has transparency · 9-slice margins for UI |
| Effect | Element sheets it uses · anchor socket · duration |
| Music, ambience | Length · loop flag and loop points · loudness target |
| Sound effect | Maximum length · where its transient falls · loop flag |
| Voice line | The line's string id · speaker · maximum length |
| Font | The code points it must contain · the pixel sizes it must be legible at |

## 4. What each placeholder is

Placeholders are produced by a script on the build machine from the contracts alone. It needs no GPU and no model, and makes all of them in a few minutes.

| Asset | Placeholder | How it can be recognised |
|---|---|---|
| Rigged model | Block-out figure from the rig contract: one box per bone, rigidly bound, with all sockets | Flat colour by creature type (beast brown, humanoid blue, undead grey, elemental orange, construct steel, plant green, aberration purple, dragonkin red, giant tan); the asset id floats above it in development builds |
| Skin or outfit | A flat tint on the rig's block-out, different per skin | Tint |
| Animation clip | **A real, moving clip** made at once by the forge's procedural animation generator for that rig family, with the contract's length and contact frame. Placeholders never stand frozen | Stiff, mechanical motion |
| Static model | A box, cylinder or wedge of the contract's bounding size with the right pivot; weapons are a box blade on a box grip so the grip sits in the hand | Flat colour by category; id label |
| Building kit piece | The kit maker's geometry with flat colours: the piece's own shape where it has one, otherwise the nearest of the maker's 40 shapes by the words of its name ([P11](02-3d-pipelines.md)). Before the kit makers exist, a grid-sized box (4 × 3 × 0.3 m at the grid origin), replaced when they do. Kits are procedural, so a piece's **shape and collision are final as soon as it has a shape of its own**; only its textures arrive later | Untextured |
| Terrain texture | Flat colour from the zone's palette with a faint grid | Grid |
| Icon, UI piece, painting | Flat colour with the asset id drawn on it; UI pieces already have correct 9-slice margins | Id text |
| Effect | One burst of plain particles in the school's colour at the right socket, lasting the right time | Plain squares |
| Music, ambience | Silence of the right length | Silence |
| Sound effect | A short soft tone, pitched by family so combat is still readable by ear | Tone |
| Voice line | No audio; the subtitle and speech bubble show the text | Text only |
| Font | The engine's built-in font | — |

## 5. Asset state

Two files in `client/assets/` describe the assets.

**`asset-index.json`** says what each asset is. It is written with the placeholders, is fixed by the contracts, and **does not change on delivery**. The client resolves an id through it, and content validation checks every asset id the content names against it.

| Field | Meaning |
|---|---|
| `id` | Asset id (the key) |
| `file` | The file's path under `client/assets/` |
| `kind` | What sort of asset it is |
| `rig`, `clip`, `loop` | For a rigged model, its rig; for a clip, its rig, clip name and loop flag; for audio, its loop flag |

**`asset-status.json`** records the state of every asset. The client, the build and the forge all read it; only the acceptance step (§6) writes it. It is the one file under `client/assets/` kept in git during the build.

| Field | Meaning |
|---|---|
| `id` | Asset id |
| `state` | `placeholder` · `generated` (made by a model method) · `fallback` (made by a pipeline's model-free fallback) · `failed` (generation gave up; the placeholder stays) |
| `hash` | Content hash of the file now in place. The client's cache key |
| `updated` | Time of the last change |
| `pipeline`, `attempts` | For reporting |

A `fallback` file never replaces a `generated` one: the acceptance step refuses a model-free result for an asset that a model has already made.

## 6. Delivery: from the forge to the game

```
A forge machine (A, B or C)            Build machine
  pipeline finishes an asset
  forge's own quality gates pass
  written to /srv/forge/out/<id>/  --pulled by the supervisor through
                                     that machine's Forge service-->  assets-src/incoming/<id>/
                                                                           |
A tool outside the queue (rig-fit)                                         |
  forge place <id> <file>  ----------------------------------------->  assets-src/incoming/<id>/
                                               acceptance step:
                                                 1. contract check (below)
                                                 2. convert to the engine's loose format if needed
                                                 3. write to a temporary file beside the target
                                                 4. rename over the placeholder (atomic)
                                                 5. update asset-status.json (state, hash)
```

**There are two doors into the acceptance step and one step.** The supervisor's delivery runs every 2 minutes and pulls what each forge machine has finished ([Asset Forge §4a](00-asset-forge.md#4a-the-supervisor)). `forge place <asset id> <file>` brings in a finished file made outside the queue, which is how rig-fitted bodies and creatures arrive ([P13](02-3d-pipelines.md)): it copies the file to `assets-src/incoming/<id>/` under the name the manifest gives it, writes a record of the method and models that made it, keeps the template it replaces (§2a), and calls the same acceptance step.

The acceptance step is the last line of defence: it re-checks the asset **against its contract**, on the build machine, whatever the forge reported.

| Contract check | If it fails |
|---|---|
| File format and name | Rejected |
| Rigged model: every contract bone present with the same name and parent; every socket present | Rejected; the placeholder stays; the forge is told to retry |
| Rigged model: rest pose within tolerance of the contract (bone lengths within 10%) | Rejected |
| Constructed model: bounding size within 10% of the contract on every axis | Rescaled to fit if within 30%; otherwise rejected |
| Generated prop: inside its contract's box, reaching it on at least one side, and filling at least 45% of every side. Where the box is a bound (`size_is: bound`): inside it and reaching it on one side ([P10](02-3d-pipelines.md)) | Rejected |
| Model: pivot and forward axis | Corrected automatically if the offset is a pure translation or a 90° turn; otherwise rejected |
| Animation: length, loop flag and contact frame equal the contract's | Retimed if within 5%; otherwise rejected |
| Texture: pixel size, tiling and transparency flags | Resized if only the size differs; otherwise rejected |
| Audio: length within tolerance, loop points present where required, loudness in range | Loudness corrected; otherwise rejected |

A rejected asset never reaches the game. The file already in place remains, the asset's state does not change, and the rejection is sent back to the forge machine that made it (`POST /assets/{asset_id}/reject`) as a retry with the reason.

## 7. How the client loads assets

**All asset access goes through one service.** No scene, script or content file refers to an asset by file path; they refer to asset ids, and `AssetService` resolves them.

| Rule | Detail |
|---|---|
| One entry point | `AssetService.GetModel(id)`, `GetSkin(id)`, `GetClip(rig, name)`, `GetTexture(id)`, `GetIcon(id)`, `GetEffect(id)`, `GetAudio(id)`. Content records already name assets by id (the `model`, `icon`, `visual` and `soundSet` fields in [Content Schemas](../08-tech/content-schemas.md)) |
| The index | The service reads `asset-index.json` (§5) at start: id to file, kind, rig, clip and loop flag. `GetClip(rig, name)` finds a clip's id through it, and returns nothing where the rig has no clip of that name |
| Templates and dressed bodies | `TemplateOf(id)` gives the kept template of a fitted body, or nothing. `DressedOf(outfitId, bodyId)` gives the dressed body made for that outfit on that body, or nothing. `GetModel` loads either in the model's place when asked, cached under its own key. The rule for which is used is in §2a |
| Loose loading | During the build, assets are **loaded at run time from loose files** in `client/assets/`, not through the engine's import step, so a changed file needs no editor and no re-export. Models load from `.glb` through the engine's run-time glTF loader, with their textures kept in memory; textures from `.png`; audio from `.ogg`. The builder confirms these run-time loaders against the pinned Godot version at milestone MA; where all three load loose, as they do in Godot 4, the acceptance step needs no converter |
| Cache | Loaded resources are cached by id and hash. A changed hash in the state file invalidates the entry |
| Never missing | Every id in the manifest has a file from the first day, so a load cannot fail for a missing file. An id not in the manifest is a build error caught by content validation rule V24 |
| Release builds | For a release, the build imports whatever is in `client/assets/` at that moment through the engine's normal import step and packs it. The run-time path and the packed path return identical resources |

### The visual is separate from the entity

Every character and creature in the client is two things: a **gameplay node** (position, collision capsule from the rig contract, nameplate, selection circle, network state) and, under it, a **visual node** built from the asset. Only the visual node is ever replaced. This is the reason a swap cannot move a creature, change what it collides with, or interrupt what it is doing.

The **server never loads visual assets at all.** It uses rig contracts for collision capsules and the zone's collision proxies for pathfinding. Nothing the forge produces can change server behaviour.

## 8. Swapping in a running client

The client watches `asset-status.json` (checked every 5 seconds in development builds; off in release builds). When an asset's hash changes, the new file is loaded on a background thread, and the swap happens on the main thread in a single frame:

| Asset | What happens at the swap | What the player sees |
|---|---|---|
| Rigged model | A new visual node is built from the new file, or from the kept template or a dressed body where §2a's rule says so. Because the skeleton is the same, the current animation and its playback time are copied across, and everything attached to sockets (weapon, shield, spell effects) is re-parented by socket name. The old visual node is then freed | The block-out becomes the creature mid-stride, still holding its weapon |
| Skin or outfit | The texture on the model's material is replaced. A dressed body already wears its outfit, so a change to the outfit's texture does nothing to it. Which model the skin sits on (§2a, rule 2) is decided when the visual node is built, so a skin delivered for a fitted model is seen on that model from the next time the node is built | The tint becomes painted detail |
| Animation clip | The clip is replaced in the rig's animation library. A clip that is playing continues from the same fraction of its length | Movement becomes natural |
| Static model, weapon | The mesh on every live instance is replaced. Collision is untouched because it comes from the contract's proxy | The box becomes the object |
| Kit textures, terrain textures | The shared material's texture is replaced, so every piece using it updates at once | A grey town gains its surfaces |
| Icon, UI piece | The texture is replaced and the controls redraw | Id labels become pictures |
| Effect | The particle definition and its sheets are replaced. Effects already playing finish with the old look | The next cast looks right |
| Sound effect, voice | The stream is replaced. Sounds already playing finish | The next one is the new sound |
| Music, ambience | The new stream is cross-faded in over 2 seconds at the next loop point | Silence gives way to music |

Order does not matter. Clips may arrive before the model (they play on the block-out), or the model before its clips (it moves with the procedural placeholder clips), or a skin before either. Each asset is swapped when it arrives, and every combination is valid because every piece obeys the same rig contract.

## 9. Seeing progress

- **Development overlay** (toggle with a debug key): counts of assets by state, the last ten swapped, and an option to float each placeholder's id above it.
- **Forge report**: `GET /report` on the forge gives the same totals from the forge's side, with failures and their reasons.
- A release build lists in its log every asset still in the `placeholder` or `failed` state.

## 10. Why this is safe for an unattended build

| Risk | Why it cannot break the game |
|---|---|
| A generated model has the wrong skeleton | The contract check rejects it; the block-out stays |
| A generated model is the wrong size or faces the wrong way | Corrected or rejected at acceptance; gameplay size comes from the contract either way |
| The forge never finishes an asset | Its placeholder is a complete, valid asset; the game ships with it and reports it |
| An asset arrives half-written | Files are renamed into place atomically, and the client loads by hash from the state file, which is written last |
| A swap happens during a fight | Only the visual node changes; the gameplay node, collision, target and animation time carry on |
| The server sees different assets from the client | The server sees none |
