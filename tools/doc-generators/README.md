# Document generators

These PowerShell scripts are documentation helpers, not game code. Each rebuilds one generated planning document from the hand-written design documents. Run from the project folder:

    powershell -NoProfile -ExecutionPolicy Bypass -File tools\doc-generators\<script> -Root (Get-Location).Path

| Script | Rebuilds | Reads |
|---|---|---|
| item-index.ps1 | docs/10-art/07-named-item-index.md | Zone, instance, PvP, crafting, quest text and reference-table documents |
| quest-index.ps1 | docs/10-art/08-quest-art-index.md | Zone quest tables |
| npc-quests.ps1 | The Gives and Ends columns in docs/11-npcs/0*.md | Quest text files |
| creatures.ps1 | docs/12-data/creatures.md | Zone creature tables |
| spells.ps1 | docs/12-data/spells.md | Class ability tables |

| zone-rewards.ps1 | The Reward column of every zone quest table in docs/05-zones | Quest text files |
| spawn-check.ps1 | Nothing; prints a report | World layout spawn camps, zone creature tables, quest text |

One generator is written in Python (3.10 or later), because it expands every art list into single assets:

    python tools/doc-generators/asset_manifest.py .

| Script | Rebuilds | Reads |
|---|---|---|
| asset_manifest.py | Everything in docs/15-asset-manifest: the index, the level-band files and asset-manifest.csv (one row per asset, in order of first appearance) | The art lists (docs/10-art), creature, spell, encounter and spoken-line data, zone and class documents, crafting and secondary professions, the world layout |

Run them again after changing any document they read. Run asset_manifest.py last, after any of the others. Order after a quest or reward change: zone-rewards, item-index, quest-index, npc-quests, spawn-check.