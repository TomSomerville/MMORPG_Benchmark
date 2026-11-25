# Build Prompt

[Master Plan](MASTER_PLAN.md)

This repository is a complete design specification for an MMORPG. It is meant to be handed to an AI model, together with one prompt, to see whether the model can build a full, playable game from it in a single run. There is no scoring and no evaluation harness: the result is judged by playing it.

## The prompt

Give the model this text and the whole repository, and nothing else:

> Build the game specified in this repository. `MASTER_PLAN.md` is the starting point and links to every other document; the documents are the complete specification. Build all of it, in the order given in `docs/08-tech/milestone-tasks.md`, into a full, playable MMORPG.
>
> Start with milestone MA: build the Asset Forge specified in `docs/14-asset-pipeline/` on the asset machines. You reach the first (an AMD machine with 128 GB of memory) over SSH using the environment variables `FORGE_HOST`, `FORGE_SSH_USER` and `FORGE_SSH_KEY`, and the second (an NVIDIA RTX 5070 Ti desktop) using `FORGE_GPU_HOST`, `FORGE_GPU_SSH_USER` and `FORGE_GPU_SSH_KEY`. A third, smaller helper machine (an RTX 3060 laptop) may be given as `FORGE_AUX_HOST`, `FORGE_AUX_SSH_USER` and `FORGE_AUX_SSH_KEY`. If any set is missing, build the forge on the machines you have. You have `sudo` on each: check what software and models each machine already has, and install and download whatever is missing yourself. They are yours for generating the game's art, 3D models, animation and audio; leave them running the asset queue while you build the game. The assets to make are listed one per row in `docs/15-asset-manifest/asset-manifest.csv`, each with a description to generate from; make them in the order given there, which is the order a player first meets them, so that the placeholders seen first are replaced first.
>
> The game server is designed for a cluster and must also run complete on one machine. If the environment variable `GAME_SERVER_HOSTS` lists SSH hosts, deploy to them; if it is absent, deploy on this machine as a single server.
>
> Work the way `docs/08-tech/build-procedure.md` says: keep the progress ledger in the repository, and whenever you start with no memory of the work so far, read the ledger first and carry on from it.
>
> Do not stop to ask questions or to check in. Where a document leaves something open, use its stated default. Where it calls for a person to review, test or approve something, do the check yourself as the build procedure describes and proceed. If an asset cannot be generated, the forge's fallback or a placeholder is used and you keep going. When you finish, leave a `README.md` saying exactly how to start the server and the client so the game can be played.

## What you set up before running it

| Item | Detail |
|---|---|
| The build machine | Where the model runs, with permission to run commands without asking. The model installs the .NET SDK, Godot 4 (.NET build), Docker and Git itself if they are missing |
| The asset machines | The GMKtec EVO-X3 (dedicated), the main desktop with the RTX 5070 Ti, and optionally the Lenovo laptop with the RTX 3060. Each needs only an operating system, a network connection and an SSH server. **The model checks each machine and installs and downloads whatever software and models are missing**; you do not prepare them. Ubuntu Server 24.04 on the EVO-X3 gives the best chance of its graphics card being usable; the model cannot install an operating system |
| Access | An SSH key that lets the build machine log in to each asset machine as a user with `sudo` (or administrator) rights, provided to the model as `FORGE_HOST`, `FORGE_SSH_USER`, `FORGE_SSH_KEY` (EVO-X3), `FORGE_GPU_HOST`, `FORGE_GPU_SSH_USER`, `FORGE_GPU_SSH_KEY` (desktop) and `FORGE_AUX_HOST`, `FORGE_AUX_SSH_USER`, `FORGE_AUX_SSH_KEY` (laptop) |
| Game servers (optional) | `GAME_SERVER_HOSTS`: a list of SSH hosts to deploy the game server to. With none, the game is deployed on the build machine as a single server. With one, a single server. With several, a cluster. The game runs complete in every case |
| Reboots | The model may reboot the EVO-X3 freely, and the desktop and laptop once each during setup if a driver install needs it |
| Laptop | If used, keep it plugged in and stop it sleeping |
| Internet | All machines need it, to download packages and model weights |

## What "the whole repository" means

`MASTER_PLAN.md`, everything under `docs/`, and `tools/doc-generators/` (scripts that rebuild some of the documents; they are not game code). There is no existing game code.
