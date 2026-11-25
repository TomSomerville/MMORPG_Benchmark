# Asset Pipelines 4 — Placeholders and Swapping In Generated Assets

[← Asset Forge](00-asset-forge.md) · Prev: [Audio and fonts](03-audio-pipelines.md)

How the game runs on stand-in assets from the first day, and how each finished asset replaces its stand-in, including in a client that is already running. This page is the authority on both.

## 1. The idea in one paragraph

Every asset has an **asset contract**: the things about it that the game depends on and that must be identical in the stand-in and the finished asset. The contract is written first, from the specification, before anything is generated. A **placeholder** is the simplest file that satisfies the contract. A **generated asset** is a better-looking file that satisfies the same contract. Because the game is built only against contracts, replacing one with the other changes how the game looks and sounds and nothing else.

## 2. There is no shared placeholder

A wolf, a bear and a human do not share a placeholder, because they do not share a skeleton. **Each asset gets its own placeholder, generated from its own contract.**

For anything with a skeleton, the contract includes the skeleton itself. The game has 64 rigs (2 player rigs and 62 creature rigs, listed in [Creatures & NPCs](../10-art/02-creatures-npcs.md)); each rig has its own skeleton definition, written as data before any model exists. The placeholder for a rigged asset is a **block-out figure built from that skeleton**: one box per bone, as long as the bone, attached rigidly to it.

| Rig | Its skeleton | Its placeholder looks like |
|---|---|---|
| Human | Two legs, two arms, spine, head; hand, head and back sockets | A blocky two-legged figure 1.8 m tall |
| Dwarf | The same bone names, shorter and broader | A blocky two-legged figure 1.35 m tall |
| Canine (wolves, jackals, hounds) | Four legs, spine, neck, head, jaw, tail | A blocky four-legged figure with a tail |
| Bear | Four legs, heavy spine, short neck; can rear | A bulkier four-legged figure |
| Spider | Eight legs, two body segments | A two-box body on eight jointed sticks |
| Bird, serpent, blob, construct, plant, and the rest | Each its own | Each its own block-out |

So the wolf placeholder walks on four legs with the wolf's gait, and the human placeholder walks on two, from the first day. When the generated wolf arrives it has the **same skeleton**, bone for bone, because the forge fits every generated model to its rig's template ([P13](02-3d-pipelines.md#p13--characters-and-creatures-base-models-4-player-bodies-110-customisation-pieces-62-creature-rigs-base-models-18-bosses) and [P14](02-3d-pipelines.md#p14--rigs-and-skinning-64-rigs)). That shared skeleton is what lets one replace the other.

Creatures that share a rig (the art lists give each rig several skins: a Vale Wolf, a Rime Wolf and a Briarwood Stalker are one canine rig) use the same block-out, each scaled to its own size and tinted its own colour so they can be told apart.

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
| `uv_layout` | Id of the UV layout all skins of this rig share |
| `scale_range` | Smallest and largest scale used by this rig's skins |

### 3.2 Asset contract (the manifest entry), one per asset

| Kind of asset | What the contract fixes |
|---|---|
| Every asset | Id · file path and name · format · state file entry |
| Static model (prop, weapon, kit piece, nature) | Bounding size · pivot position · forward axis · material slot names · collision proxy (a box, capsule or the kit generator's collision mesh, defined separately from the visual model) · sockets if any (a weapon's `grip`, `tip`) |
| Rigged model | Its rig contract · scale · material slot names |
| Skin or outfit | The rig and UV layout it paints · texture size |
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
| Building kit piece | The kit generator's real geometry with flat colours. Kits are procedural from the start, so their **shape and collision are final on day one**; only their textures arrive later | Untextured |
| Terrain texture | Flat colour from the zone's palette with a faint grid | Grid |
| Icon, UI piece, painting | Flat colour with the asset id drawn on it; UI pieces already have correct 9-slice margins | Id text |
| Effect | One burst of plain particles in the school's colour at the right socket, lasting the right time | Plain squares |
| Music, ambience | Silence of the right length | Silence |
| Sound effect | A short soft tone, pitched by family so combat is still readable by ear | Tone |
| Voice line | No audio; the subtitle and speech bubble show the text | Text only |
| Font | The engine's built-in font | — |

## 5. Asset state

One file, `client/assets/asset-status.json`, records the state of every asset. The client, the build and the forge all read it; only the acceptance step (§6) writes it.

| Field | Meaning |
|---|---|
| `id` | Asset id |
| `state` | `placeholder` · `generated` · `fallback` (made by a pipeline's model-free fallback) · `failed` (generation gave up; the placeholder stays) |
| `hash` | Content hash of the file now in place. The client's cache key |
| `updated` | Time of the last change |
| `pipeline`, `attempts` | For reporting |

## 6. Delivery: from the forge to the game

```
Forge (EVO-X3)                         Build machine
  pipeline finishes an asset
  forge's own quality gates pass
  written to /srv/forge/out/<id>/  --rsync-->  assets-src/incoming/<id>/
                                               acceptance step:
                                                 1. contract check (below)
                                                 2. convert to the engine's loose format if needed
                                                 3. write to a temporary file beside the target
                                                 4. rename over the placeholder (atomic)
                                                 5. update asset-status.json (state, hash)
```

Synchronisation runs every 2 minutes. The acceptance step is the last line of defence: it re-checks the asset **against its contract**, on the build machine, whatever the forge reported.

| Contract check | If it fails |
|---|---|
| File format and name | Rejected |
| Rigged model: every contract bone present with the same name and parent; every socket present | Rejected; the placeholder stays; the forge is told to retry |
| Rigged model: rest pose within tolerance of the contract (bone lengths within 10%) | Rejected |
| Model: bounding size within 10% of the contract | Rescaled to fit if within 30%; otherwise rejected |
| Model: pivot and forward axis | Corrected automatically if the offset is a pure translation or a 90° turn; otherwise rejected |
| Animation: length, loop flag and contact frame equal the contract's | Retimed if within 5%; otherwise rejected |
| Texture: pixel size, tiling and transparency flags | Resized if only the size differs; otherwise rejected |
| Audio: length within tolerance, loop points present where required, loudness in range | Loudness corrected; otherwise rejected |

A rejected asset never reaches the game. The placeholder remains, the asset's state stays `placeholder`, and the rejection is sent back to the forge as a retry with the reason.

## 7. How the client loads assets

**All asset access goes through one service.** No scene, script or content file refers to an asset by file path; they refer to asset ids, and `AssetService` resolves them.

| Rule | Detail |
|---|---|
| One entry point | `AssetService.GetModel(id)`, `GetSkin(id)`, `GetClip(rig, name)`, `GetTexture(id)`, `GetIcon(id)`, `GetEffect(id)`, `GetAudio(id)`. Content records already name assets by id (the `model`, `icon`, `visual` and `soundSet` fields in [Content Schemas](../08-tech/content-schemas.md)) |
| Loose loading | During the build, assets are **loaded at run time from loose files** in `client/assets/`, not through the engine's import step, so a changed file needs no editor and no re-export. Models load from `.glb` through the engine's run-time glTF loader; textures from `.png`; audio from `.ogg`. The builder confirms these run-time loaders against the pinned Godot version at milestone MA, and writes a small converter in the acceptance step for any type that cannot be loaded loose |
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
| Rigged model | A new visual node is built from the new file. Because the skeleton is the same, the current animation and its playback time are copied across, and everything attached to sockets (weapon, shield, spell effects) is re-parented by socket name. The old visual node is then freed | The block-out becomes the creature mid-stride, still holding its weapon |
| Skin or outfit | The texture on the model's material is replaced | The tint becomes painted detail |
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
