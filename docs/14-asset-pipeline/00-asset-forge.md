# Asset Forge — the asset generation system

[← Master Plan](../../MASTER_PLAN.md) · Pipelines: [Images and textures](01-image-pipelines.md) · [3D models, rigs and animation](02-3d-pipelines.md) · [Audio](03-audio-pipelines.md) · [Placeholders and swapping](04-placeholders-and-swap.md) · What to make: [Art Master To-Do](../10-art/00-art-master-todo.md)

Every visual and audio asset in the game is AI-generated. This page specifies the machines that generate them, the service that runs on each, the supervisor that looks after them, and the rules every pipeline shares. The three linked pages specify one pipeline per kind of asset. **Building the Asset Forge is the first thing the builder does** (milestone MA in the [task lists](../08-tech/milestone-tasks.md)), so that assets are being produced in the background from the first day of the build.

## 1. The machines

Three machines generate assets. **Each runs its own Forge service and its own queue (§4) and needs nothing from the others while it works**, so each goes on working when another machine or the network is away. A supervisor on the build machine looks after all of them (§4a). The two large machines are complementary: one has a great deal of graphics memory but no CUDA, the other has CUDA but less memory. The third (Forge C, below) is smaller.

| | **Forge A: GMKtec EVO-X3 (always on)** | **Forge B: the main desktop** |
|---|---|---|
| Graphics | AMD Radeon 8060S, up to 96 GB of shared memory, **no CUDA** | **NVIDIA RTX 5070 Ti, 16 GB, CUDA** |
| Good at | Large models that need memory more than speed: image generation, image-to-3D through the graph runner, music, the checkers | Anything published for CUDA only: image-to-3D tools outside the graph runner, hair, auto-rigging, motion capture |
| Availability | 100%, dedicated | For model generation when it is on; it may also be the machine the build runs on |
| Runs | Its own Forge service, queue and workers, the graph runner (ComfyUI), and every method its bring-up passed | The same |
| Reached by | An SSH alias named for it in the machine list `forge/fleet.yaml` (for example `evo`). The alias is defined in the build machine's own SSH configuration; **no network address is ever written in the repository** | The same. A machine that is also the build machine is marked `local` in the list and needs no alias |
| Operating system | Ubuntu Server 24.04 preferred; the builder works with what it finds | Linux or Windows. On Windows the workers run natively (§2). The builder detects which |

**Which machine makes what is measured, not written down.** Each machine's bring-up records the methods it can run and how long each takes, and the supervisor shares the work out from those figures (§4, scheduler rule 1). The split in the table is what is expected, not a rule.

**Any machine alone is enough.** A pipeline whose model runs on no machine that is present uses its model-free fallback, and its assets are recorded as `fallback` so they can be shared out again when a machine with the model joins. With several machines present, one model job runs on each at once.

The 16 GB limit on Forge B matters: some image-to-3D models are reported to want 24 GB. Bring-up tests each one on Forge B with its lower-memory settings (half-precision weights, tiled decoding, a smaller voxel grid) and records what fits.

### Forge C: the laptop (optional helper)

| | |
|---|---|
| Machine | Lenovo laptop (model 82K8): Ryzen 9 5900HX (8 cores, 16 threads), 32 GB memory, **NVIDIA RTX 3060 Laptop GPU, 6 GB, CUDA**, about 795 GB free disk (measured 2026-11-14) |
| Reached by | An SSH alias named for it in `forge/fleet.yaml` (for example `laptop`), or `local` if the build runs on it |
| Operating system | Windows, with the workers run natively (§2), or Linux. The builder detects which |
| Runs | Its own Forge service, queue and workers, and the methods its role and its bring-up allow |

Every machine in the machine list has a **role**, and every method of a pipeline names the roles that may run it. A role A or B machine may be given any method whose test job passed on it at bring-up. A role C machine is never given a method with a model step that needs the graphics card for generation: it takes model-free makers, processing and small models. Six gigabytes is too little for image-to-3D, so as a role C machine Forge C takes:

| Work | Why it fits |
|---|---|
| The model-free 3D makers and block-out placeholders | CPU work; needs no model |
| Processing of generated files: sizing, pivots, baking, detail levels, export, the repaint pass | CPU work; light on graphics memory. Segmentation uses the small model (Mirage) |
| Technical and structural checks, and the visual and audio checkers (§7) | Small models; the image-text comparison model is under 1 GB |
| P19 voice generation, and the speech-recognition check on voice lines | Small speech models fit in 6 GB; confirmed at bring-up |
| HairDeck (P21), **only if** bring-up shows it fits in 6 GB and Forge B is absent or busy | Its memory need is not published |

Open: whether Forge C stays a role C helper, as this section specifies, or runs the image model where its test jobs pass (in the build it is listed with role B and has drawn icons) is the owner's decision.

Rules for Forge C:

1. **It is never required.** Everything it can make can also be made on Forge A or B. If it is absent or asleep, the assets given to it wait and are worked when it is back; nothing is taken from it (§4, scheduler rule 1).
2. **It takes whole assets, by the methods it can run.** A job's steps all run on the machine that holds the job, so no intermediate files cross the network; only finished assets do.
3. **If the build runs on this laptop**, the worker uses at most 8 threads, and releases the graphics card whenever the game client is started for a test.
4. **Heat.** A laptop slows down under days of full load. Its workers record their step times as they go, and the supervisor shares work out by those times and by the part of the day the machine is on, so a machine that has slowed is given less.

### Forge A in detail

| | |
|---|---|
| Machine | GMKtec EVO-X3, dedicated 100% to asset generation |
| Processor | AMD Ryzen AI Max+ 395: 16 cores, 32 threads |
| Graphics | Integrated Radeon 8060S (architecture id `gfx1151`). **Not an NVIDIA card: there is no CUDA** |
| Memory | 128 GB unified, shared by CPU and GPU; up to 96 GB can be assigned to the GPU |
| Storage | Two M.2 slots; the forge needs 600 GB free (models about 250 GB, outputs and intermediates about 300 GB) |
| Network | Wired LAN to the build machine |
| Role | The machine that is always on. Runs its own Forge service and queue and the largest models. The language models doing the build run on a **different computer** and reach the forge only over the network. If the owner runs a service of their own on it that cannot share the graphics memory with the graph runner, the machine list names that service and the supervisor leaves the graph runner stopped while it runs |

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
| Checker models | Small models in PyTorch that run on any of the machines: an image-text embedding model (SigLIP) for the visual gate, an audio-text model (CLAP), a voice-activity detector and a speech recogniser (Whisper) for the audio gate (§7) | A generative vision-language model, through `llama.cpp` on the Vulkan path, may answer the same visual checklist on a machine with the memory for it |
| Image, 3D and audio graph runner | ComfyUI, run headless and driven through its HTTP API, on every machine that makes with models, at the same version and with the same weights on each | The supervisor keeps it running (§4a). Workflows are built by the forge's code and stored in the repository |
| 3D processing | The forge's own Python mesh library: mesh operations, reading and writing glTF, fixed-angle rendering, baking, and all model-free modelling. Blender 4.x in background mode for the steps that need it (rig-fit's reduction, unwrap and bake, [P13](02-3d-pipelines.md)) | The model-free makers use no Blender API, so they run on a machine with no Blender |
| Audio processing | `ffmpeg` (its loudness filters) and Python; loudness is measured to ITU-R BS.1770 / EBU R128 by the forge's own code | Trim, loop, normalise, convert |
| Mesh utilities | `meshoptimizer` / `gltfpack`, `xatlas`, Instant Meshes or QuadriFlow | Decimation, UVs, quad remesh |
| Isolation | One container image per model family where the machine has containers; otherwise one Python environment per model family | A broken model cannot damage another's dependencies |
| Service | The Forge service (§4), a small Python web service with a job queue in SQLite, on every machine | |

The builder installs all of this over SSH from the provisioning scripts it writes under `forge/` in the repository. Access is given to the builder as an SSH alias per machine, set up in the build machine's SSH configuration and named in `forge/fleet.yaml`.

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

1. **Work with the operating system that is there.** Linux is used directly. On Windows the service and workers run natively, in user space: portable builds of the tools and a Python environment with the CUDA build of PyTorch, in a forge folder under the account's home. That needs no administrator rights and no reboot; WSL2 is not required. Paths this specification gives as `/srv/forge/...` are that folder on such a machine. The builder cannot install an operating system on a machine, so if Forge A is found running Windows it tries ROCm inside WSL2, then Vulkan-based runtimes, and records which pipelines that leaves on fallbacks.
2. **Reboots.** Forge A is dedicated and may be rebooted whenever needed. Forge B and Forge C are also someone's working computers: the builder reboots each at most once, during provisioning, and only if a driver install requires it.
3. **Disk.** Before downloading, check free space against the need (about 600 GB on Forge A, 150 GB on Forge B, 40 GB on Forge C). If short, download in priority order and stop before the disk has less than 50 GB free.
4. **Idempotent.** The provisioning scripts can be run again at any time and change nothing that is already correct.
5. **A machine that cannot be reached or prepared is dropped**, and the forge runs on the others.

## 3. Repository layout for the forge

```
forge/
  provision/           scripts that install the OS packages, the compute stack, the graph runner and models
  service/             the Forge service (job API, queue, workers, validators), delivery, and the supervisor
  pipelines/           one folder per pipeline P01..P21: methods, prompt templates, post-process steps, checks
  lib/                 the forge's own libraries: mesh, glTF, render, paint, palette, contracts, placeholders, rig-fit, synthesis
  style/               the style bible: palette, reference images, prompt fragments, gate thresholds; and the icon style bible
  manifest/            asset-manifest.yaml (every asset to make), converted from docs/15-asset-manifest/asset-manifest.csv
  blender/             shared Blender scripts
  tests/               smoke tests per pipeline and validator tests
  fleet.yaml           the machine list: each machine's role, SSH alias, workers, and whether it is paused
  approvals.yaml       what the owner has approved, with the date of each approval (§7a)
```

Outputs are written on each forge machine under `/srv/forge/out/<asset-id>/`. The supervisor pulls finished assets through that machine's Forge service (`GET /assets?since=`, then each file) into `assets-src/incoming/` on the build machine, or copies them directly when the machine is the build machine. The transfer is one-way, takes changed files only, and writes each file beside its target and renames it. Neither `client/assets/` nor `assets-src/` is kept in git during the build: both are rebuilt from the contracts or delivered again from the forge.

## 4. The Forge service

Every asset machine runs the same HTTP service over its own queue database; port 8188 is ComfyUI's, **port 8600 is the Forge's**. A service listens on its own machine only, and the build machine reaches another machine's service through an SSH tunnel. The builder talks only to Forge services, and in ordinary running through the supervisor (§4a).

| Call | Purpose |
|---|---|
| `POST /jobs` | Queue one asset: `{asset_id, pipeline, priority, params}`. Idempotent on `asset_id` plus a hash of `params` |
| `POST /jobs/batch` | Queue many assets from the manifest by filter: list, pipeline, zone or id prefix |
| `GET /jobs/{id}` | State: queued, running (with step), validating, done, failed (with reason), fallback used |
| `GET /assets/{asset_id}` | The asset's record: files, pipeline, model and version, prompt, seed, attempts, validator results |
| `GET /assets?since=` · `GET /assets/{asset_id}/files/{name}` | The assets finished since a time, and one file of an asset. Delivery to the build machine uses these |
| `POST /assets/{asset_id}/reject` | The build machine's acceptance step refused the asset: it is queued again with a new seed and the reason kept |
| `GET /queue` | Counts by state and pipeline, the running job, estimated time remaining |
| `GET /timings` | Measured seconds per pipeline step on this machine |
| `POST /jobs/{id}/retry` · `POST /jobs/retry-failed` | Re-run one job, or every failed job, with a new seed |
| `GET /health` | Which models are loaded and which methods passed bring-up |
| `GET /report` | Totals: assets done, failed, on fallback, placeholder; hours used per pipeline |
| `POST /workers/heartbeat` · `POST /workers/claim` · `POST /jobs/{id}/step-done` · `POST /jobs/{id}/step-failed` · `POST /jobs/{id}/validated` | The worker protocol: a worker reports that it is alive, claims the next step it can run, and reports each step's result and the checks' verdict |
| `GET /jobs/{id}/work.tar` · `PUT /jobs/{id}/work.tar` | A job's step files as one tar archive, for a worker that does not share the service's disk |

Scheduler rules:

1. **One model job at a time per machine, and an asset belongs to one machine.** Assignment is measured. Each machine's bring-up records the methods it can run and their seconds, and its workers record step times as they go. An asset may go only to a machine that has the **best method any machine has for it** (a model method before the model-free fallback); among those it goes to the machine that would **finish it soonest**, counting what that machine already has to do, its number of workers and the part of the day it is on. An asset then stays with the machine it was given to: nothing is taken back from a machine that is away, which keeps two machines from making the same thing. If a machine is gone for good its share is given out again by an explicit command (`fleet queue --redo`). The fallback of one machine never replaces what another machine's model made.
2. **No batching by model.** A queue keeps strictly to the manifest's order. Within one first-seen level the manifest already puts each kind of asset together, so a machine changes model only where the kind changes. (Preferring the model already loaded was tried and dropped: it sent a level's sounds ahead of its icons.)
3. **Priority order is the order of the [Asset Manifest](../15-asset-manifest/00-manifest-index.md): order of first appearance in the game.** A job's priority is its first-seen level and then its position in the manifest. Assets a new player sees in the starting zones are made first; level-30 assets last. Each machine's workers take the next row of its queue, in that order, that they can make, so the machines advance side by side.
4. **Processing runs in parallel** with the model job. Workers are separate processes, each running one step at a time; one worker per machine takes the model steps and the rest take processing: sizing and baking, audio trimming, the checks, voice synthesis with CPU-capable models.
5. **Every job is resumable.** Each pipeline step writes its output to disk; a restarted job continues from the last finished step.
6. **Nothing blocks the build.** The build machine creates a placeholder for every asset in the manifest at the start (§8) and swaps in the real file when the forge finishes it.
7. **Nothing is shared out in number before the owner's approval** (§7a).

### 4a. The supervisor

One supervisor process runs on the build machine (`python -m forge fleet start`). It reads the machine list, `forge/fleet.yaml`, which gives each machine its role (§1), its SSH alias or `local`, its number of workers, the part of a day it is expected to be on, whether it makes with models through the graph runner, and whether the owner has paused it. **Every two minutes** it looks at every machine that is not paused and:

| Step | What it does |
|---|---|
| Sees which answer | A machine that does not answer is "away". That is normal, not an error |
| Restarts | Starts a Forge service, a worker or a graph runner that is stopped. The queue takes up at its last finished step |
| Pushes code | Gives a machine the forge code when the committed forge code has changed |
| Hands over | Gives each machine the assets assigned to it. Those for a machine that is away wait on the build machine and are handed over when it is back |
| Delivers | Pulls finished assets and passes each through the acceptance step ([Placeholders and Swapping §6](04-placeholders-and-swap.md#6-delivery-from-the-forge-to-the-game)) into the game |
| Records | How far each machine has got, and what each gave up on and why |

A paused machine is given nothing and is not started; its queue is kept.

| Command | Purpose |
|---|---|
| `fleet start` · `fleet stop` | Start or stop the supervisor. Stopping it does not stop the machines, which go on with their queues |
| `fleet status` | Each machine: on or away, queue counts, what waits on the build machine for it |
| `fleet plan` | Which machine is best for each kind of asset, from the measured times |
| `fleet queue` | Share out every asset the game has no delivered file for, by rule 1 and subject to §7a. Filters by pipeline, zone or id prefix; `--calibration` for the calibration set; `--fallbacks` to make again with a model what a fallback made; `--redo` to share out again what a lost machine held; `--dry-run` to show what would be made |
| `fleet measure` | Time again what a machine can make |
| `fleet push` | Give the machines the working copy's forge code now |
| `fleet failed` · `fleet retry-failed` | The assets a machine gave up on, grouped by reason; queue them again with a new seed |

Only the supervisor writes the fleet's state; the commands leave their requests for it to pick up. The fleet goes on generating while the game is built and tested; it is not stopped to run tests.

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

**The look itself, and the full account of how consistency is enforced, are in [Art Direction](../10-art/10-art-direction.md).** That page is the authority on the look; the tables below say what the pipelines do to hold it.

Where an asset's shape and surface come from depends on what it is:

| Asset | Shape | Surface |
|---|---|---|
| Player bodies, creatures, dressed NPC bodies ([P13, P14](02-3d-pipelines.md)) | The image-to-3D model's mesh, kept, and fitted to the rig contract by rig-fit | The generated model's own colour, baked onto the reduced mesh as made. No repaint pass |
| Props; nature where the generated method is approved ([P10, P12](02-3d-pipelines.md)) | The image-to-3D model's mesh, kept, stood upright and sized to its contract's box | The generated texture, palette-locked, with the game's light painted in (lighter where it faces up, darker where it faces down or lies in a hollow). Its colours are kept; no repaint by material |
| Building kits, and everything made by a model-free maker | Constructed on the grid or from parameters | The repaint pass of [Art Direction §6](../10-art/10-art-direction.md): coloured by material from the palette, with the game's light |
| Terrain, paintings, textures | — | The image model's picture, palette-locked |
| Icons ([P02](01-image-pipelines.md)) | — | The image model's picture as painted, made small. Icons follow their own style bible and are **not** palette-locked |

Open: whether the palette lock, the repaint pass and the triangle budgets of Art Direction apply to rig-fitted bodies and creatures, which today keep the generated model's colours as made, is the owner's decision.

A model generating nine thousand assets one at a time will drift unless it is held to a reference. Four mechanisms:

| Mechanism | Detail |
|---|---|
| Style bible | Made first, by pipeline P01: a palette of 32 colours built by rule, material rules, proportion sheets for humans and dwarves, eight "anchor" images that define the look, and the positive and negative prompt fragments every image pipeline uses. The owner approves it (§7a). Icons have a second, separate bible, the icon style bible |
| Style words and references | Every image prompt is built from the style bible's fixed fragments, never written by hand. Where the image model accepts reference images, generation is also conditioned on two or three anchor images, so the look comes from pictures as well as words |
| Palette lock | After generation a colour image is remapped toward the palette (nearest colour in a perceptual colour space, 60% blend; the zone's ramps where the asset belongs to a zone), which pulls stray hues back into the set. It applies to textures, terrain, paintings and the textures of generated props, and not to icons |
| Style check | An automatic comparison against the anchors and the frozen gate thresholds (§7). Assets that score as a different style are regenerated |

Content rules that apply to every prompt: never name a living artist, a studio, a franchise, an existing game or a real person; never ask for a likeness; no text, logos or watermarks in images; no voice cloned from or imitating a real person.

## 7. Automatic quality gates

No person reviews assets one by one, so every pipeline ends in checks a program can run. An asset must pass all of its pipeline's checks to be accepted. The checks decide each asset; the owner decides, once per pipeline, whether what it makes is wanted at all (§7a).

| Kind | Checks |
|---|---|
| Technical | File format, dimensions, triangle count, texture size, bone count, clip length, sample rate, loudness, loop seam error, file size |
| Structural | Mesh is closed where required and has no inverted faces or loose parts; UVs lie in 0–1 without overlap; rig has the standard bone names; animation's first and last frames match for loops; kit pieces fit the grid to 1 mm |
| Visual | An image-text embedding model (SigLIP base) compares the asset, rendered from fixed angles for 3D, against the subject text and the anchors. It answers a fixed checklist: does it show the subject; is it the anchor style; is there text or a watermark; is anything malformed. Each question is a comparison of the image against a "yes" description and "no" descriptions, and each answer is yes or no. Style similarity, the silhouette gate and the line-up use the same embeddings. A generative vision-language model may answer the same checklist where a machine has the memory for one |
| Audio | An audio-text model (CLAP) scores whether a sound matches its description; a voice-activity detector (Silero VAD) finds speech where there should be none; clipping and loudness (ITU-R BS.1770) are measured by the forge's own code. Voice lines are transcribed by a speech-recognition model (Whisper base.en) and compared with the written line |

The style thresholds are set by calibration, not by hand: the calibration set plus a spread of probe assets of each class are generated and measured, each upper limit is put 35% above the largest value seen and each lower limit at 60% of the smallest, capped so that deliberately bad test samples still fail, and the result is frozen in `forge/style/gates.json`.

Failure handling: on a failed check the job retries with a new seed, up to 3 attempts. After that it switches to the pipeline's **fallback** method and tries twice more. If that also fails the asset stays a **placeholder** and is listed in `GET /report`. Every failed attempt is recorded with its reason, so what a method keeps failing on can be counted. An asset keeps its model-free version in the game until a generated one passes every gate. The build never stops for an asset.

### 7a. The owner's approval

**Nothing is made in number until the owner has approved it.** Approval is given pipeline by pipeline, and a pipeline needs two things approved: the style guidelines that govern it, and its own first results. There are three sets of style guidelines: the **style bible** for pictures, textures and models; the **icon style bible** for icons; and the **audio style guide** ([Audio](../10-art/09-audio.md#how-the-audio-is-made)) for music, ambience, sound effects and voice. No pipeline is exempt: music and voice wait for the audio style guide as the visual pipelines wait for theirs. Until a pipeline is approved the queue makes only the guidelines themselves and the calibration set (§5).

| Rule | Detail |
|---|---|
| The record | `forge/approvals.yaml`: a date for each set of style guidelines (the style bible, the icon style bible, the audio style guide) and a date per pipeline. An empty entry means not approved. **Only the owner's own word puts a date there**; the builder never infers an approval |
| What the queue does | `fleet queue` shares out an asset only if its pipeline carries a date and its style guidelines do. Everything else is held back and reported as held, by pipeline |
| What the owner looks at | A review page written by `python -m forge review`: the style bible (palette, anchors, swatches) and each pipeline's first results, side by side with any candidate that would replace them |
| Scope | An approval is the owner's word on what that pipeline makes, given by eye on its results. It may be limited, for example to named zones. The owner may also release a pipeline for a named part of the game ahead of its style guidelines, by an instruction that says so; it is recorded as such and covers that part only |
| Refusal | What the owner refuses is recorded beside the approvals in the owner's words, and the pipeline stays held until new first results are shown |

Status on 2026-11-24: P02 (icons) has both approvals, its first results and the icon style bible, and is made in number. P12 (nature) is released for the two starting zones only, by instruction ahead of the style bible. The first results of P16 (music) and P19 (voice lines) are approved, but the audio style guide has not yet been put to the owner, so both are held until it is approved. The style bible is not approved, and every other pipeline is held.

Open: the style bible is not yet approved; the model-free anchors were refused and a candidate made by the image model is with the owner, so the pipelines that depend on it stay held.

Open: P12's approval was given by instruction for the two starting zones before its results had been looked at; whether it stands and extends to other zones waits on the owner seeing them.

## 8. Placeholders

At the start of the build, before any generation, the build machine creates a placeholder for **every** manifest entry, so the game can be built and run immediately. The full specification, including how a finished asset replaces its placeholder in a running client, is on its own page: **[Placeholders and Swapping In Generated Assets](04-placeholders-and-swap.md)**. In brief:

- Every asset has a **contract** written first: the things the game depends on (file name, size, pivot, skeleton, sockets, clip lengths, loop points). A placeholder is the simplest file that satisfies the contract; a generated asset is a better one that satisfies the same contract.
- **There is no shared placeholder.** Each of the 67 rigs (65 in the manifest, plus the ship and the mine-cart, whose moving parts need bones) has its own skeleton, defined as data, and its placeholder is a block-out figure built from that skeleton: a wolf's has four legs and a tail, a human's two legs and two arms.
- Placeholder animations move: they are made at once by the procedural animation generator.
- A finished asset is checked against its contract on the build machine, then renamed over the placeholder. The client loads assets by id through one service and swaps the visual in place.

## 9. Bring-up: the order the builder follows

1. Audit and prepare every machine (§2, [Preparing the machines](#preparing-the-machines-is-the-builders-job)), start the Forge service on each, and start the supervisor (§4a).
2. **Smoke-test every pipeline on every machine**: one small job each. For each, record whether the primary model runs on that hardware and how long it takes. Where it does not, try the listed alternates in order; where none runs, the pipeline is set to its fallback method there. The result is written to `forge/bringup-report.md`, and the measured times are what assignment uses (§4, rule 1). From here on the forge uses whatever passed.
3. Load the asset manifest (§5) and create all placeholders (§8).
4. Run P01 to make the style bible, write the review page, and put it to the owner (§7a).
5. Queue the calibration set (the first row of each kind in manifest order), check that all quality gates work end to end, calibrate the style thresholds (§7), and add each pipeline's first results to the review page.
6. Start the game build (milestone M0) at once; it does not wait for the owner. As the owner approves each pipeline, queue that pipeline's assets, in manifest order, while the build goes on with placeholders.

## 10. Expected volume and time

These are estimates for planning, not measurements. Bring-up replaces them with measured rates.

| Pipeline group | Assets | Estimated time each | Estimated total |
|---|---|---|---|
| Icons, UI, paintings | about 2,900 | 30–90 s | 50 hours |
| Textures (terrain, armor, skins, colourways, flipbooks) | about 2,300 | 30–120 s; colourways seconds | 40 hours |
| Static models (props, weapons, kit pieces, nature) | about 1,300 | 4–12 min | 170 hours |
| Characters and creatures (models and skins) | about 470 | 10–25 min | 130 hours |
| Rigs | 67 | 20 min | 20 hours |
| Animation clips | about 850 | 3–8 min | 80 hours |
| Music | 108 | 3–6 min | 8 hours |
| Ambience and sound effects | about 1,500 | 20–60 s | 20 hours |
| Voice lines | about 250 (the count is set by [Spoken Lines](../12-data/spoken-lines.md)) | 10 s | 1 hour |
| Retries and fallbacks | | +40% | 200 hours |
| **Total** | **about 9,700 generated files** | | **about 720 hours: 30 days of continuous running** |

Those figures assume Forge A alone, and count running time only, not time a pipeline spends held for the owner's approval (§7a). With Forge B taking a share of the model work (about 400 of the 720 hours are 3D, hair, rig and animation) on a faster CUDA card while Forge A works in parallel, the total falls to perhaps **12 to 18 days**. Using a one- or two-step distilled image model on Forge A ([shared image tools](01-image-pipelines.md#shared-image-tools)) would cut the image hours by a further half or more. All of this is still unmeasured.

The forge therefore runs for the whole length of the build. Because the queue follows the manifest's order of first appearance, everything seen before level 6 (login, character creation, both starting zones and the capitals: about 4,100 of the 9,000 rows, but mostly the cheap ones) is done first.

## 11. Model choices and how sure they are

The pipeline pages name a primary model, alternates and a fallback for each pipeline. Those names were chosen from published information in November 2026; a name counts as run only where a pipeline page says it is the method in use or the bring-up report records it. Two things must be checked by the builder at bring-up, and the specification is written so that either can fail without stopping the build:

- **Does it run on an AMD GPU through ROCm?** Several 3D models are published with CUDA-only components.
- **Does its licence allow commercial use of what it generates?** Licences differ and change. Several popular models carry restrictions: by region, by revenue, or by user count. The builder records the licence of every model it adopts in `forge/bringup-report.md`, and prefers MIT or Apache-licensed models wherever one passes.

The fallbacks do not depend on any model: procedural modelling by the forge's own mesh library, palette-based texture synthesis, and synthesised audio. They produce plainer assets, but they always work, so the game is never missing an asset for lack of a model.
