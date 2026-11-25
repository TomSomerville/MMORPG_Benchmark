# Asset Forge — the asset generation system

[← Master Plan](../../MASTER_PLAN.md) · Pipelines: [Images and textures](01-image-pipelines.md) · [3D models, rigs and animation](02-3d-pipelines.md) · [Audio](03-audio-pipelines.md) · [Placeholders and swapping](04-placeholders-and-swap.md) · What to make: [Art Master To-Do](../10-art/00-art-master-todo.md)

Every visual and audio asset in the game is AI-generated. This page specifies the machine that generates them, the service that runs on it, and the rules every pipeline shares. The three linked pages specify one pipeline per kind of asset. **Building the Asset Forge is the first thing the builder does** (milestone MA in the [task lists](../08-tech/milestone-tasks.md)), so that assets are being produced in the background from the first day of the build.

## 1. The machines

Two machines generate assets, and they are complementary: one has a great deal of graphics memory but no CUDA, the other has CUDA but less memory. A third, smaller machine (Forge C, below) takes processing work off them.

| | **Forge A: GMKtec EVO-X3** | **Forge B: the main desktop** |
|---|---|---|
| Graphics | AMD Radeon 8060S, up to 96 GB of shared memory, **no CUDA** | **NVIDIA RTX 5070 Ti, 16 GB, CUDA** |
| Good at | Large models that need memory more than speed: image generation, music, the vision and audio checkers | Anything published for CUDA only, which is most 3D generation: image-to-3D, hair, auto-rigging, motion capture |
| Availability | 100%, dedicated | For model generation; it may also be the machine the build runs on |
| Runs | The Forge service, the queue, and pipelines P01–P09 and P16–P20 | A Forge worker for pipelines P10, P13, P14, P15 and P21 |
| Reached by | `FORGE_HOST`, `FORGE_SSH_USER`, `FORGE_SSH_KEY` | `FORGE_GPU_HOST`, `FORGE_GPU_SSH_USER`, `FORGE_GPU_SSH_KEY`. If the build runs on this desktop, `FORGE_GPU_HOST` is `localhost` |
| Operating system | Ubuntu Server 24.04 preferred; the builder works with what it finds | Linux, or Windows with WSL2 Ubuntu and NVIDIA's CUDA support for WSL. The builder detects which |

**Either machine alone is enough.** If Forge B is absent or a model does not fit in 16 GB, its pipelines run on Forge A where the model supports it, and otherwise use their model-free fallback. If Forge A is absent, Forge B runs everything it has memory for. With both present, two generation jobs run at once, one per machine.

The 16 GB limit on Forge B matters: some image-to-3D models are reported to want 24 GB. Bring-up tests each one on Forge B with its lower-memory settings (half-precision weights, tiled decoding, a smaller voxel grid) and records what fits.

### Forge C: the laptop (optional helper)

| | |
|---|---|
| Machine | Lenovo laptop (model 82K8): Ryzen 9 5900HX (8 cores, 16 threads), 32 GB memory, **NVIDIA RTX 3060 Laptop GPU, 6 GB, CUDA**, about 795 GB free disk (measured 2026-11-14) |
| Reached by | `FORGE_AUX_HOST`, `FORGE_AUX_SSH_USER`, `FORGE_AUX_SSH_KEY`. If the build runs on this laptop, `FORGE_AUX_HOST` is `localhost` |
| Operating system | Windows with WSL2 Ubuntu and NVIDIA's CUDA support for WSL, or Linux. The builder detects which |
| Runs | A Forge worker that takes **processing steps and small models only** (list below) |

Six gigabytes is too little for the main image model or for image-to-3D, so Forge C never runs a generation model that decides how an asset looks. That also protects the single style: every image comes from one model on Forge A. Forge C takes:

| Work | Why it fits |
|---|---|
| Blender steps of every 3D pipeline: the shape pass, UV unwrap, baking, detail levels, export | CPU work; needs no large model |
| Block-out placeholders, and the model-free 3D fallbacks (procedural Blender) | CPU work |
| The repaint pass | Image processing; light on graphics memory. Segmentation uses the small model (Mirage) |
| Technical and structural checks | CPU work |
| P19 voice generation, and the speech-recognition check on voice lines | Small speech models fit in 6 GB; confirmed at bring-up |
| HairDeck (P21), **only if** bring-up shows it fits in 6 GB and Forge B is absent or busy | Its memory need is not published |

Rules for Forge C:

1. **It is never required.** Every step it can take can also run on Forge A or B. If it is absent, slow or asleep, its jobs are reassigned after 10 minutes without a heartbeat.
2. **It takes steps, not whole pipelines.** A 3D job generates on Forge B, then its processing steps may run on Forge C. Intermediate files move by `rsync` between workers; the step is skipped to another machine if the transfer would take longer than the step.
3. **If the build runs on this laptop**, the worker uses at most 8 threads, and releases the graphics card whenever the game client is started for a test.
4. **Heat.** A laptop slows down under days of full load. The worker measures its own step times, and the queue stops sending it work whose measured time is more than three times the same step on Forge A.

### Forge A in detail

| | |
|---|---|
| Machine | GMKtec EVO-X3, dedicated 100% to asset generation |
| Processor | AMD Ryzen AI Max+ 395: 16 cores, 32 threads |
| Graphics | Integrated Radeon 8060S (architecture id `gfx1151`). **Not an NVIDIA card: there is no CUDA** |
| Memory | 128 GB unified, shared by CPU and GPU; up to 96 GB can be assigned to the GPU |
| Storage | Two M.2 slots; the forge needs 600 GB free (models about 250 GB, outputs and intermediates about 300 GB) |
| Network | Wired LAN to the build machine |
| Role | Runs the Forge service and every generation model. The language models doing the build run on a **different computer** and reach the forge only over the network |

What the hardware means for the design:

- **Large models fit.** With 64–96 GB given to the GPU, models that need 24 GB or more of graphics memory load without trouble. The limit is speed, not size.
- **It is slower than a high-end NVIDIA card**, perhaps 3–6 times slower per image. The pipelines are therefore built to run unattended for days, in priority order, with the build using placeholders until each asset lands.
- **CUDA-only code will not run.** Any model whose published code depends on CUDA-only libraries (for example NVIDIA's differentiable rasteriser) needs a port, a CPU path, or a different model. This is the single biggest risk in the forge, and is why every pipeline names a fallback and why bring-up (§9) tests each model before anything depends on it.

## 2. Software base

| Layer | Choice | Notes |
|---|---|---|
| Operating system | Ubuntu Server 24.04 LTS | The release with the most reports of working ROCm on this chip |
| GPU compute | AMD ROCm with a PyTorch build that supports `gfx1151` | Use the newest ROCm release that lists Ryzen AI Max support. Community reports note that some models need 32-bit floats forced on this chip, and that one runtime thread can spin a CPU core after GPU work; both are tolerable |
| GPU memory | The builder raises the memory the graphics driver may use to 64 GB (96 GB if large 3D or music models need it) with kernel parameters (the `amdgpu` and `ttm` memory limits), then reboots Forge A | This is reported to work on this chip without touching the firmware setting, which cannot be changed over SSH. If it does not take effect, the builder works within the memory it finds and records the limit |
| Second compute path | Vulkan, through `llama.cpp` for language and vision models | Independent of ROCm, so the checker models still run if ROCm misbehaves |
| Image and video graph runner | ComfyUI, run headless and driven through its HTTP API | One workflow file per pipeline, stored in the repository |
| 3D processing | Blender 4.x in background mode, scripted in Python | Retopology, UV unwrap, LOD, baking, export, and all procedural modelling |
| Audio processing | `ffmpeg`, `sox`, and a loudness tool (EBU R128) | Trim, loop, normalise, convert |
| Mesh utilities | `meshoptimizer` / `gltfpack`, `xatlas`, Instant Meshes or QuadriFlow | Decimation, UVs, quad remesh |
| Containers | One container image per model family | A broken model cannot damage another's dependencies |
| Service | The Forge service (§4), a small Python web service with a job queue in SQLite | |

The builder installs all of this over SSH from the provisioning scripts it writes under `forge/` in the repository. Access is given to the builder as environment variables: `FORGE_HOST`, `FORGE_SSH_USER`, `FORGE_SSH_KEY` for Forge A and `FORGE_GPU_HOST`, `FORGE_GPU_SSH_USER`, `FORGE_GPU_SSH_KEY` for Forge B, and `FORGE_AUX_HOST`, `FORGE_AUX_SSH_USER`, `FORGE_AUX_SSH_KEY` for Forge C.

### Preparing the machines is the builder's job

Decided 2026-11-14: **the builder prepares every asset machine itself.** The owner provides only SSH access to an account with `sudo` (or administrator) rights on each machine. Nothing is assumed to be installed.

| Step | What the builder does |
|---|---|
| 1. Audit | On each machine, record: operating system and version, processor, memory, graphics card and driver, graphics memory, free disk, and whether Python, containers, Blender, `ffmpeg` and the compute stack (ROCm or CUDA) are present and at what version |
| 2. Inventory models | Search the usual places for model weights already on the machine (the Hugging Face cache, ComfyUI and other tool model folders, any path in `FORGE_MODEL_DIRS`). A file is reused when its name and checksum match a model on the candidate lists; nothing is downloaded twice |
| 3. Install what is missing | Only what the audit found absent or too old. Existing software that works is left alone, and nothing unrelated to the forge is removed or upgraded |
| 4. Download models | Each model the pipelines name, from its publisher's own repository, checked against the published checksum. If a download needs an account or an accepted licence the builder does not have, that model is skipped and the next alternate is used |
| 5. Configure | Service accounts, folders, containers, the worker, start on boot |
| 6. Report | Everything found, installed, reused, skipped and failed goes in `forge/bringup-report.md` |

Rules:

1. **Work with the operating system that is there.** Linux is used directly. On Windows, the builder installs WSL2 with Ubuntu and NVIDIA's CUDA support and runs the worker inside it. The builder cannot install an operating system on a machine, so if Forge A is found running Windows it tries ROCm inside WSL2, then Vulkan-based runtimes, and records which pipelines that leaves on fallbacks.
2. **Reboots.** Forge A is dedicated and may be rebooted whenever needed. Forge B and Forge C are also someone's working computers: the builder reboots each at most once, during provisioning, and only if a driver or WSL2 install requires it.
3. **Disk.** Before downloading, check free space against the need (about 600 GB on Forge A, 150 GB on Forge B, 40 GB on Forge C). If short, download in priority order and stop before the disk has less than 50 GB free.
4. **Idempotent.** The provisioning scripts can be run again at any time and change nothing that is already correct.
5. **A machine that cannot be reached or prepared is dropped**, and the forge runs on the others.

## 3. Repository layout for the forge

```
forge/
  provision/           scripts that install the OS packages, ROCm, containers and models
  service/             the Forge service (job API, queue, scheduler, validators)
  pipelines/           one folder per pipeline P01..P21: workflow, prompt templates, post-process script, validator
  style/               the style bible: palette, reference images, prompt fragments, negative prompts
  manifest/            asset-manifest.yaml (every asset to make), converted from docs/15-asset-manifest/asset-manifest.csv
  blender/             shared Blender scripts (retopo, UV, LOD, bake, export, procedural kits, rig templates)
  tests/               smoke tests per pipeline and validator tests
```

Outputs are written on the forge under `/srv/forge/out/<asset-id>/` and synchronised to `client/assets/` on the build machine by `rsync` over SSH.

## 4. The Forge service

A single HTTP service on the forge, port 8188 is ComfyUI's, **port 8600 is the Forge's**. The builder talks only to the Forge service.

| Call | Purpose |
|---|---|
| `POST /jobs` | Queue one asset: `{asset_id, pipeline, priority, params}`. Idempotent on `asset_id` plus a hash of `params` |
| `POST /jobs/batch` | Queue many assets from the manifest by filter: block, list, pipeline or id prefix |
| `GET /jobs/{id}` | State: queued, running (with step), validating, done, failed (with reason), fallback used |
| `GET /assets/{asset_id}` | The asset's record: files, pipeline, model and version, prompt, seed, attempts, validator results |
| `GET /queue` | Counts by state and pipeline, the running job, estimated time remaining |
| `POST /jobs/{id}/retry` | Re-run with a new seed |
| `GET /health` | Which models are loaded and which pipelines passed bring-up |
| `GET /report` | Totals: assets done, failed, on fallback, placeholder; hours used per pipeline |

Scheduler rules:

1. **One GPU job at a time per machine.** Forge A and Forge B each run one generation job, so two run in parallel. The queue assigns each job to the machine its pipeline prefers (§1) and falls back to the other if that machine is absent or the model failed bring-up there. Forge C, when present, takes processing steps and small-model jobs under the rules in §1.
2. **Batch by model.** Jobs are grouped so a model is loaded once and used for many assets before the next model loads. Loading a large model takes one to several minutes.
3. **Priority order is the order of the [Asset Manifest](../15-asset-manifest/00-manifest-index.md): order of first appearance in the game.** Assets a new player sees in the starting zones are made first; level-30 assets last. Each machine takes the next row, in that order, that one of its pipelines can make, so images and audio on one machine and 3D on another advance side by side. Batching by model (rule 2) may reorder rows only within one first-seen level.
4. **CPU pipelines run in parallel** with the GPU job: Blender post-processing, audio trimming, validators, voice synthesis with CPU-capable models.
5. **Every job is resumable.** Each pipeline step writes its output to disk; a restarted job continues from the last finished step.
6. **Nothing blocks the build.** The build machine creates a placeholder for every asset in the manifest at the start (§8) and swaps in the real file when the forge finishes it.

## 5. The asset manifest

**The manifest is already written.** [Asset Manifest](../15-asset-manifest/00-manifest-index.md) lists every asset, one row each (about 9,000), with a description to generate from, what it is for, its zone and the level at which a player first meets it, **in order of first appearance**. The same rows are in `docs/15-asset-manifest/asset-manifest.csv`. The builder does not derive the list from the art lists; it loads that file.

The first forge task converts the CSV into `forge/manifest/asset-manifest.yaml`, adding the fields only the builder can decide:

| Field | Meaning | Comes from |
|---|---|---|
| `order` | Position in the order of first appearance; the queue's priority | Manifest |
| `id` | The stable asset id (`KIT-01-wall-straight`, `CRE-B01-skin-vale-wolf`, `ITM-230-icon`) | Manifest |
| `kind`, `pipeline` | What sort of asset it is and which pipeline makes it (P01 to P21, or `assemble` / `derive` for rows that need no generation) | Manifest |
| `subject` | The description to generate from | Manifest |
| `used_for`, `zone`, `first_seen_level` | What uses it, where and when it first appears | Manifest |
| `targets` | Triangle budget, texture size, duration, loudness, format | Manifest, per kind |
| `name` | File name following the naming rule in the art master page | Builder |
| `depends_on` | Other asset ids that must exist first (a rig before its animations; a kit atlas before its pieces; a set before its colourways) | Builder |
| `contract` | The asset's contract ([Placeholders and Swapping](04-placeholders-and-swap.md)) | Builder |

Row counts in the YAML must equal the CSV. If the builder finds that the game needs an asset the manifest lacks, it adds a row at the first-seen level where it belongs and records the addition in `build/decisions.md`; it never drops a row.

**The calibration set** (called "block A" elsewhere in these documents) is the style bible plus the first row of every kind in manifest order: one finished example of each kind of asset, used to prove every pipeline and gate before the rest of the queue runs.

Prompts are never written by hand per asset. Each pipeline has a **prompt template** that combines the `subject` with fixed fragments from the style bible.

## 6. Keeping one style

**The look itself, and the full account of how consistency is enforced, are in [Art Direction](../10-art/10-art-direction.md).** That page is the authority; the table below is a summary. Its two most important points: shapes come from templates and procedural generators, not from the image-to-3D model; and no texture is used as generated, because every one goes through the same repaint pass that removes the generator's lighting and colours and applies the game's.

A model generating nine thousand assets one at a time will drift unless it is held to a reference. Four mechanisms:

| Mechanism | Detail |
|---|---|
| Style bible | Made first, by pipeline P01: a palette of 32 colours, material rules, proportion sheets for humans and dwarves, eight "anchor" images that define the look, and the positive and negative prompt fragments every image pipeline uses |
| Reference conditioning | Every image generation is conditioned on two or three anchor images as well as its prompt, so the look comes from pictures, not words |
| Palette lock | After generation every colour image is remapped toward the 32-colour palette (nearest colour in a perceptual colour space, 60% blend), which pulls stray hues back into the set |
| Style check | An automatic comparison against the anchors (§7). Assets that score as a different style are regenerated |

Content rules that apply to every prompt: never name a living artist, a studio, a franchise, an existing game or a real person; never ask for a likeness; no text, logos or watermarks in images; no voice cloned from or imitating a real person.

## 7. Automatic quality gates

No person reviews assets during the build, so every pipeline ends in checks a program can run. An asset must pass all of its pipeline's checks to be accepted.

| Kind | Checks |
|---|---|
| Technical | File format, dimensions, triangle count, texture size, bone count, clip length, sample rate, loudness, loop seam error, file size |
| Structural | Mesh is closed where required and has no inverted faces or loose parts; UVs lie in 0–1 without overlap; rig has the standard bone names; animation's first and last frames match for loops; kit pieces fit the grid to 1 mm |
| Visual | A local vision-language model (run through the Vulkan path) is shown the asset, rendered from fixed angles for 3D, beside the anchors and the subject text, and answers a fixed checklist: does it show the subject; is it the anchor style; is there text or a watermark; is anything malformed. Each answer is yes or no |
| Audio | A local audio-captioning or classification model answers: does it match the description; is there speech where there should be none; is it clipped. Voice lines are transcribed by a speech-recognition model and compared with the written line |

Failure handling: on a failed check the job retries with a new seed, up to 3 attempts. After that it switches to the pipeline's **fallback** method and tries twice more. If that also fails the asset stays a **placeholder** and is listed in `GET /report`. The build never stops for an asset.

## 8. Placeholders

At the start of the build, before any generation, the build machine creates a placeholder for **every** manifest entry, so the game can be built and run immediately. The full specification, including how a finished asset replaces its placeholder in a running client, is on its own page: **[Placeholders and Swapping In Generated Assets](04-placeholders-and-swap.md)**. In brief:

- Every asset has a **contract** written first: the things the game depends on (file name, size, pivot, skeleton, sockets, clip lengths, loop points). A placeholder is the simplest file that satisfies the contract; a generated asset is a better one that satisfies the same contract.
- **There is no shared placeholder.** Each of the 64 rigs has its own skeleton, defined as data, and its placeholder is a block-out figure built from that skeleton: a wolf's has four legs and a tail, a human's two legs and two arms.
- Placeholder animations move: they are made at once by the procedural animation generator.
- A finished asset is checked against its contract on the build machine, then renamed over the placeholder. The client loads assets by id through one service and swaps the visual in place.

## 9. Bring-up: the order the builder follows

1. Audit and prepare every machine (§2, [Preparing the machines](#preparing-the-machines-is-the-builders-job)) and start the Forge service.
2. **Smoke-test every pipeline**: one small job each. For each, record whether the primary model runs on this hardware. Where it does not, try the listed alternates in order; where none runs, the pipeline is set to its fallback method. The result is written to `forge/bringup-report.md`. From here on the forge uses whatever passed.
3. Load the asset manifest (§5) and create all placeholders (§8).
4. Run P01 to make the style bible.
5. Queue the calibration set (the first row of each kind in manifest order) and check that all quality gates work end to end.
6. Queue everything else by block, and start the game build (milestone M0) while the forge runs.

## 10. Expected volume and time

These are estimates for planning, not measurements. Bring-up replaces them with measured rates.

| Pipeline group | Assets | Estimated time each | Estimated total |
|---|---|---|---|
| Icons, UI, paintings | about 2,900 | 30–90 s | 50 hours |
| Textures (terrain, armor, skins, colourways, flipbooks) | about 2,300 | 30–120 s; colourways seconds | 40 hours |
| Static models (props, weapons, kit pieces, nature) | about 1,300 | 4–12 min | 170 hours |
| Characters and creatures (models and skins) | about 470 | 10–25 min | 130 hours |
| Rigs | 64 | 20 min | 20 hours |
| Animation clips | about 850 | 3–8 min | 80 hours |
| Music | 108 | 3–6 min | 8 hours |
| Ambience and sound effects | about 1,500 | 20–60 s | 20 hours |
| Voice lines | about 250 (the count is set by [Spoken Lines](../12-data/spoken-lines.md)) | 10 s | 1 hour |
| Retries and fallbacks | | +40% | 200 hours |
| **Total** | **about 9,700 generated files** | | **about 720 hours: 30 days of continuous running** |

Those figures assume Forge A alone. With Forge B taking the 3D, hair, rig and animation pipelines (about 400 of the 720 hours) on a faster CUDA card while Forge A does images and audio in parallel, the total falls to perhaps **12 to 18 days**. Using a one- or two-step distilled image model on Forge A ([shared image tools](01-image-pipelines.md#shared-image-tools)) would cut the image hours by a further half or more. All of this is still unmeasured.

The forge therefore runs for the whole length of the build. Because the queue follows the manifest's order of first appearance, everything seen before level 6 (login, character creation, both starting zones and the capitals: about 4,100 of the 9,000 rows, but mostly the cheap ones) is done first.

## 11. Model choices and how sure they are

The pipeline pages name a primary model, alternates and a fallback for each pipeline. Those names were chosen from published information in November 2026 and **have not been run on this machine**. Two things must be checked by the builder at bring-up, and the specification is written so that either can fail without stopping the build:

- **Does it run on an AMD GPU through ROCm?** Several 3D models are published with CUDA-only components.
- **Does its licence allow commercial use of what it generates?** Licences differ and change. Several popular models carry restrictions: by region, by revenue, or by user count. The builder records the licence of every model it adopts in `forge/bringup-report.md`, and prefers MIT or Apache-licensed models wherever one passes.

The fallbacks do not depend on any model: procedural modelling in Blender, palette-based texture synthesis, and synthesised audio. They produce plainer assets, but they always work, so the game is never missing an asset for lack of a model.
