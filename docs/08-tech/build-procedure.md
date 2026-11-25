# Build Procedure — how the builder works

[← Master Plan](../../MASTER_PLAN.md) · Tasks: [Milestone Task Lists](milestone-tasks.md) · Layout: [Repository & Conventions](repo-and-conventions.md) · Prompt: [Build Prompt](../../BUILD_PROMPT.md)

The build is one unattended run that lasts weeks. No person answers questions, reviews work or plays the game during it. This page says how the builder keeps its place, what it does when something fails, how it sees the game it is building, and what it does about tests that were written for human testers. **Where this page and a task's wording disagree about who performs a check, this page wins.**

## 1. The ledger

The builder's memory is the repository, not its conversation. Two files hold the state of the run and are committed with every task.

| File | Contents |
|---|---|
| `build/ledger.md` | One row per task in [Milestone Task Lists](milestone-tasks.md): id, status, attempts, commit, evidence folder, one-line note |
| `build/decisions.md` | Every choice the documents did not settle: date, task, the question, the choice, the document it was closest to |
| `build/deferred.md` | Every task or part of a task not finished: what is missing, why, what was tried, what would finish it |
| `build/for-the-owner.md` | Things only the owner can do (§8) |
| `build/evidence/<task-id>/` | Test output, screenshots and measurements that show the acceptance test passing |

Task status is one of:

| Status | Meaning |
|---|---|
| `todo` | Not started |
| `doing` | Started; the note says what step it is on |
| `passed` | Its acceptance test passes as written |
| `passed-reduced` | Passes at a smaller size than written, because the hardware present cannot hold the full size; the measured size is in the note |
| `deferred` | Abandoned for now under §4; listed in `build/deferred.md` |

Rules:

1. Set a task to `doing` **before** starting it and to its final status **when it ends**, in the same commit as the work.
2. Never edit a past row to look better. A task that later breaks goes back to `doing`.
3. The ledger is created at the start of milestone MA with all 169 tasks as `todo`.

## 2. Starting, and starting again

The builder will lose its working context many times in a run this long. Every time it starts with no memory of the work in progress, it does this before anything else:

1. Read `build/ledger.md`, `build/deferred.md` and the last 30 entries of `build/decisions.md`.
2. Read `git log -30` and `git status`. Uncommitted work belongs to the task marked `doing`: finish it or discard it, never leave it.
3. Run the fast test suite (`dotnet test` without the load tests). If it fails, fixing it is the first job.
4. Ask the Forge service for its status ([Asset Forge §4](../14-asset-pipeline/00-asset-forge.md#4-the-forge-service)) and restart it if it has stopped.
5. Continue with the task marked `doing`, or the first `todo`.

It never begins by re-reading every document. It reads the documents a task links to when it starts that task.

## 3. Order and commits

| Rule | Detail |
|---|---|
| Order | Tasks are done in the order listed, milestone by milestone. A task may be taken early only if the current one is waiting on something that takes hours (a soak test, a long generation job) |
| The forge is a background lane | After MA the forge generates assets on its own. The builder checks it at the start of each milestone and whenever a task needs an asset, and never waits idle for it: the placeholder is used |
| One commit per task | Message `T-M2-04: <what was done>`. The fast test suite passes at every commit |
| Milestone tags | When a milestone's exit test passes: tag `m2-done`, and write a short entry in `build/report.md` |
| Branches | Work is on `main`. No pull requests; "recorded in the pull request" in older wording means "saved in the task's evidence folder" |
| Secrets | Passwords, keys and tokens are never committed. They live in `.env` files listed in `.gitignore`, with a committed `.env.example` |
| Tests are not weakened | A failing test is fixed by fixing the code. A test may be changed only when the specification shows the test itself is wrong, and that change is recorded in `build/decisions.md` |

## 4. When something fails

| Situation | What the builder does |
|---|---|
| An acceptance test fails | Diagnose and fix. Up to 5 distinct attempts |
| Still failing after 5 | Try one different design for the failing part. Up to 3 more attempts |
| Still failing | Mark the task `deferred`, write it up in `build/deferred.md`, leave the feature in the best working state behind a safe default (the game must still start and play), and move on |
| A task depends on a deferred task | Build it against the deferred task's interface; if that is impossible, defer it too and say why |
| End of every milestone | Re-try each deferred task once, with what has been learned since |
| A tool, download or machine is unavailable | Use the stated fallback. If none is stated, choose the nearest working substitute and record it in `build/decisions.md` |
| The hardware cannot hold a test's full size | Run it at the largest size that fits, record the size, mark `passed-reduced` |

**Tasks that may not be deferred**, because everything after them rests on them: all of M0; in M1 the spell engine, combat resolution and creature AI; in M2 terrain, spawns, inventory and the quest system. If one of these cannot be made to pass, the builder keeps working on it.

A milestone is finished when its exit test passes and each of its tasks is `passed`, `passed-reduced` or `deferred`.

## 5. When the documents are silent or disagree

1. **Silent:** choose the simplest behaviour consistent with a 2004-era game of this kind and with the nearest documented rule, and record it in `build/decisions.md`. Do not stop.
2. **Disagree:** the more specific document wins over the more general one, in this order: data files ([docs/12-data](../12-data/00-data-index.md)) and [quest text](../06-quests/text/00-quest-text-index.md) · technical specifications (docs/08-tech) · world layout and NPC rosters · zone, class and system design documents · summaries in the Master Plan. A decision with a later date wins over an earlier one. Record which was followed.
3. **A document calls for a person** (a reviewer, an art lead, a tester, a designer's approval): the builder performs the check itself by the methods in §6 and §7 and proceeds.

## 6. How the builder sees the game

The builder cannot play the game with hands and eyes, so the client is built from the start to be driven and observed by a program. Three tools, all built in M0 and extended as features arrive.

| Tool | What it is | Used for |
|---|---|---|
| **Bot** | A headless program that speaks the network protocol and plays by script (already named in the task lists as "Bot test") | Server behaviour: quests, combat, loot, economy, load |
| **Scripted client** | The real Godot client started with `--play-script <file>`. A play script is a list of steps: log in, create or pick a character, move to a point, target, press an action, open a window, click a control by its name, wait for a condition, take a screenshot, read the frame rate | Everything the player sees: rendering, HUD, windows, animation, sound triggers |
| **Automation port** | In debug builds only, the client listens on a local port and answers questions about its own state: which windows are open, the text of any control, what is targeted, the names of the animations playing, the assets loaded and whether each is a placeholder, the last 200 log lines | Checking the interface without reading pixels |

Three ways of checking what the scripted client shows, in order of preference:

1. **State check.** Ask the automation port. "The quest log lists BM-02 with the text from the quest file" is checked by reading the control's text, exactly.
2. **Golden image.** A screenshot is compared with a stored one from the last time the check passed, within a tolerance. Used to catch regressions in layout and rendering. Goldens are refreshed only when a task intentionally changes the look.
3. **Picture review.** The builder looks at the screenshot itself against a written checklist and records each item as pass or fail. Where the builder's own model cannot read images, the Forge's vision model does this through its `check` call.

**"Manual" in the task lists means: a scripted-client run with state checks and a picture review, performed by the builder, with the screenshots and the checklist saved as evidence.** No task waits for a person.

### The visual walk

At the end of every milestone from M2 on, the builder runs a visual walk of every zone and interior built so far:

| Step | Detail |
|---|---|
| Path | The scripted client follows the zone's main road and visits every hub, every sub-area centre, and every cutout, at ground level, taking a screenshot every 40 m and one from 30 m above each hub |
| Checks on every picture | No missing-texture colour · no holes in the ground except inside cutout frames · nothing floating or buried · no character in a rest pose while moving · interface readable · no error text on screen |
| Counts recorded | Share of visible assets that are still placeholders · frame rate at each point |
| Result | A report in `build/evidence/walk-<milestone>/` with the failing pictures. Failures are fixed as part of the milestone |

### Sound

Sound is checked by state, not by listening: the automation port reports which sound asset each event triggered. The audio files themselves are checked by the forge's audio gates.

## 7. Tests written for people

Some tasks and milestone exits were written for human testers. The builder runs these substitutes, and the human version is listed in `build/for-the-owner.md` as something the owner may do later.

| As written | What the builder runs |
|---|---|
| "Manual", "manual checklist" | §6: scripted client, state checks, picture review |
| "bots and testers" | Bots only, at the same count |
| Twelve testers play a three-team match (M9) | Twelve scripted clients, four per team, play a full Crownfall match to a win; a second match with 12 bots at 30 per team size limits checks the scoreboard and rewards |
| Closed playtest checklist (M11) | The full-game bot run (one bot per class, 1 to 30 on each continent), then the visual walk of the whole world, then every window in the [UI Specification](ui-specification.md) opened and state-checked |
| Closed and open beta (M14) | A 72-hour soak at the deployment's measured capacity with bots playing the realistic mix, including two rolling restarts, one backup-and-restore and one content hotfix, with no data loss. The betas with real players are the owner's |
| "Reviewed" legal and policy pages (M14) | Drafted, marked DRAFT at the top, linked from the login screen; legal review is the owner's |
| E-mail verification and password reset (M14) | Tested against a local mail catcher. Choosing a real mail provider is the owner's |

## 8. What is left for the owner

`build/for-the-owner.md` is kept up to date through the run and lists, at least: playing the game · running betas with real players · legal review of terms, privacy and code-of-conduct drafts · checking the licence of every generation model in `forge/bringup-report.md` for commercial use · renting servers and a domain · choosing a mail provider · code-signing the installer · anything in `build/deferred.md`.

## 9. What the builder leaves at the end

| File | Contents |
|---|---|
| `README.md` | Exactly how to start the server and the client on one machine, how to create an account, and how to deploy to a single server and to a cluster |
| `build/report.md` | Per milestone: what passed, what passed at reduced size, what was deferred |
| `build/ledger.md`, `build/decisions.md`, `build/deferred.md`, `build/for-the-owner.md` | As above, complete |
| `deploy/capacity.md` | Measured players per machine size |
| `forge/bringup-report.md` | What each asset pipeline ran on, with which model and licence, and the share of assets generated, fallen back or still placeholders |
| Scripts | `run-server`, `run-client`, `run-all` (server, database and one client on this machine), `deploy` |

The run is over when every milestone is finished under §4, or when the builder can make no further task pass. In both cases the files above are written first.
