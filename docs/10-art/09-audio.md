# Art To-Do 9 — Audio

[← Art Master To-Do](00-art-master-todo.md) · Prev: [Quest Art Index](08-quest-art-index.md)

Every piece of music, ambience, sound effect and voice needed for levels 1–30. ☐ = not started. Where a row covers a family, the count says how many separate sounds to produce; "×N var" means N random variations so repeats do not grate.

## 1. Direction and technical targets

| Topic | Target |
|---|---|
| Musical identity | Orchestral-folk. **Humans:** strings, woodwind, lute. **Mountain dwarves:** low brass, male choir, anvils, stone reverb. **Hill dwarves:** fiddle, pipes, hand drum. **The Hollow / imperial:** glass harmonica, bowed metal, distant choir. **Wildpact (hints):** wooden flutes, hand percussion. **Covenant (hints):** solo viol, music-box |
| Format | 48 kHz WAV masters; shipped as Ogg Vorbis (music/ambience streamed, effects in memory) |
| Loudness | Music −18 LUFS, ambience −24 LUFS, effects peak-normalised per category; one mix bus per category matching the volume sliders (master, music, ambience, effects, voice, UI) |
| Music playback | Per sub-area playlists with 30–90 s silences between tracks (classic style, not wall-to-wall); day and night variants; combat does not change music except boss themes |
| Variations | Any sound heard more than once a minute gets ≥ 3 variations plus random pitch ±5% |
| 3D sound | Mono sources with distance falloff; stereo for music, ambience beds and UI |
| Voice | No full voice-over. NPCs have short greeting/farewell barks; players have effort sounds and error lines |
| Naming | `mus_`, `amb_`, `sfx_`, `vox_`, `ui_` + snake_case + `_01` |

## 2. Music

Track lengths 1.5–3 min unless noted.

| ID | Done | Track(s) | Count |
|---|---|---|---|
| MUS-01 | ☐ | Main theme / login screen (3–4 min) | 1 |
| MUS-02 | ☐ | Character select and creation: human bed, dwarf bed | 2 |
| MUS-03 | ☐ | Brightmead Vale: day ×2, night ×1 | 3 |
| MUS-04 | ☐ | Embercrag Hollow: day ×2, night ×1 | 3 |
| MUS-05 | ☐ | Harrowfield: day ×2, night ×1 | 3 |
| MUS-06 | ☐ | Russetwood: day ×2, night ×1 | 3 |
| MUS-07 | ☐ | Stonewake Dale (hill-dwarf folk): day ×2, night ×1 | 3 |
| MUS-08 | ☐ | Stoneheart Deeps (no day/night): Great Cavern, Glowcap Grotto, the Undercut | 3 |
| MUS-09 | ☐ | Thornwick Marches: forest day, marsh, night, Brandspire | 4 |
| MUS-10 | ☐ | Ironroot Highlands: highland day, night, Deepseam, Brandforge | 4 |
| MUS-11 | ☐ | Cinderfall Barrens: flats, Emberwell oasis, night, Blackanvil Gate | 4 |
| MUS-12 | ☐ | The Riftlands: mesa day, night, Kite's Rest, Tor Vael Ruins | 4 |
| MUS-13 | ☐ | Veilmoor: moor, barrows, night, Hollowspire Grounds | 4 |
| MUS-14 | ☐ | Solhaven: city ×2, cathedral, Athenaeum, harbour | 5 |
| MUS-15 | ☐ | Hammerdeep: city ×2, Great Forge, Rootvault, Seagate | 5 |
| MUS-16 | ☐ | Inn / tavern tunes (diegetic): human ×3, mountain dwarf ×2, hill dwarf ×2, Kite's Rest ×1 | 8 |
| MUS-17 | ☐ | The ship crossing (*The Hearth-Oath*) | 1 |
| MUS-18 | ☐ | Gallowmere Crypts: ambient bed, boss theme, Brandfather theme | 3 |
| MUS-19 | ☐ | The Slagworks: ambient bed, boss theme, Forgemaster theme | 3 |
| MUS-20 | ☐ | Hollowspire Keep: ambient bed, banquet waltz, boss theme, Seraphine theme (3 phases, layered) | 4 |
| MUS-21 | ☐ | The Hollow Throne: ambient ×2, boss theme ×2, Echo Sisters (three-voice), Vaelric (3 phases, layered), victory | 7 |
| MUS-22 | ☐ | World bosses: one shared theme with three instrument variants | 3 |
| MUS-23 | ☐ | Act-boss / elite encounter theme (T1–T3) and Ashgrave finale theme | 2 |
| MUS-24 | ☐ | PvP: Crownfall preparation, battle, last-100-points intensity layer, victory, defeat; Dustpit chest-spawn sting | 6 |
| MUS-25 | ☐ | Stings (3–8 s): level up, quest complete, discovery of a new area, rare spawn nearby, death, resurrection, dungeon boss down, raid boss down, duel start, duel won, talent point gained, guild created | 12 |
| MUS-26 | ☐ | Story cues: Old Forge relit, Brandspire siege, "the shard answers", Three Envoys, the Crown goes under, the Crown shatters / epilogue | 6 |
| MUS-27 | ☐ | Ghost / corpse-run theme | 1 |
| MUS-28 | ☐ | Credits | 1 |

**Music total: ≈ 108 tracks and stings, about 3.5 hours.**

## 3. Ambience

Looping beds (60–120 s) plus one-shot "spot" sounds scattered at random.

| ID | Done | Bed | Spots |
|---|---|---|---|
| AMB-01 | ☐ | Meadow day / night (Brightmead) | Birdsong ×6, bees, cow, distant mill wheel, crickets, owl |
| AMB-02 | ☐ | Snow valley day / night (Embercrag) | Wind gusts ×4, snow creak, distant anvil, wolf howl far, ice crack |
| AMB-03 | ☐ | Farmland day / night (Harrowfield) | Crows ×3, wind in stubble, scythe, cart, dog bark, scarecrow creak |
| AMB-04 | ☐ | Autumn forest day / night (Russetwood) | Leaf-fall rustle ×4, woodpecker, axe chop far, stag bellow, owl, branch crack |
| AMB-05 | ☐ | Farm valley day / night (Stonewake Dale) | Sheep and goats ×4, ram bell, fiddle far, wind, dam spillway roar (near dam) |
| AMB-06 | ☐ | Cavern (Stoneheart Deeps): large-reverb air bed | Water drips ×6, far rail-cart rumble, pick echoes, bat chitter, rock settle, glowcap hum |
| AMB-07 | ☐ | Dark forest / marsh day / night (Thornwick) | Frogs, crows, gibbet creak, distant bell, wolf, fen bubbles |
| AMB-08 | ☐ | Highlands day / night (Ironroot) | High wind ×4, ram call, eagle cry, rockfall far, harpy screech far |
| AMB-09 | ☐ | Volcanic (Cinderfall) | Lava bubble, steam vents ×3, ash-wind, distant rumble, geyser |
| AMB-10 | ☐ | Canyon desert day / night (Riftlands) | Wind through rock ×4, kite cry, dust-devil, pebble fall, distant dig hammering |
| AMB-11 | ☐ | Moor fog day / night (Veilmoor) | Muffled wind, bog bubbles, far hound bay, lantern creak, whispering (near barrows) |
| AMB-12 | ☐ | Human village / town | Crowd murmur S/M, smith, well, children far, market cries ×4, chickens |
| AMB-13 | ☐ | Solhaven by district ×5 | Harbour (gulls, rigging, water lap), cathedral (choir far, bells), market, smithy row, library hush |
| AMB-14 | ☐ | Hammerdeep by level ×4 | Great Forge (bellows, hammer chorus), commons murmur in stone, Rootvault (running channels, pumps), Seagate (cave surf, ship creak) |
| AMB-15 | ☐ | Hill-dwarf steading | Brewhouse bubbling, livestock, fiddle |
| AMB-16 | ☐ | Kite's Rest and the Dustpit | Caravan market, rope-lift creak, arena crowd (idle, cheer, gasp, roar) |
| AMB-17 | ☐ | Interiors: inn, house, shop, mine tunnel, cave, crypt, keep hall, forge-works, imperial vault | 9 beds |
| AMB-18 | ☐ | Weather: light rain, heavy rain, thunder ×4, snow hush, wind light/strong, ash-storm, dust-storm, fog | 12 |
| AMB-19 | ☐ | Water and liquids: stream, river, waterfall, pond, harbour sea, lava flow, slag sluice, bog, sulfur pool | 9 |
| AMB-20 | ☐ | Fire and light: campfire, torch, brazier, forge fire, burning building, burning field/forest | 6 |
| AMB-21 | ☐ | Travel: ship at sea (hull, sail, wake), eagle flight wind, mine-cart ride | 3 |

**Ambience total: ≈ 55 beds and ≈ 160 spot sounds.**

## 4. Player and combat sound effects

| ID | Done | Family | Count |
|---|---|---|---|
| SFX-P01 | ☐ | Footsteps: grass, dirt, stone, wood, snow, sand, mud, leaves, metal grate, shallow water — walk and run | 10 surfaces × 4 var = 40 |
| SFX-P02 | ☐ | Movement: jump, land (light/heavy), fall damage, swim stroke ×3, dive, surface, armor rustle by type (cloth, leather, mail) | 14 |
| SFX-P03 | ☐ | Weapon swings by type: 1H blade, 2H blade, axe, mace, dagger, polearm, staff, unarmed | 8 × 3 var = 24 |
| SFX-P04 | ☐ | Weapon impacts by type on flesh, armor, wood/plant, stone/construct, bone | 8 types folded into 4 classes × 5 materials × 2 var = 40 |
| SFX-P05 | ☐ | Defence: shield block ×3, parry ×3, dodge whoosh, miss, glancing, crit accent, crushing blow | 12 |
| SFX-P06 | ☐ | Ranged: bow draw/release, crossbow, gun shot ×3, throw, arrow/bullet impact ×3 | 11 |
| SFX-P07 | ☐ | Draw and sheathe: blade, blunt, staff, shield | 8 |
| SFX-P08 | ☐ | Player vocal efforts per body (Human M/F, Dwarf M/F): attack grunt ×3, hit ×3, crit hit, death, jump, drown, laugh, cry, cheer, roar | 4 bodies × 14 = 56 |
| SFX-P09 | ☐ | Player error lines per body ("Not enough rage", "Out of range", "I can't do that yet", "Not enough mana", "Target too close", "Inventory is full", "I'm busy", "No target") | 4 × 8 = 32 |
| SFX-P10 | ☐ | Eat, drink, bandage, potion, loot coin, loot item, bag open/close, equip by type (cloth, leather, mail, weapon, jewellery), repair | 16 |
| SFX-P11 | ☐ | Mount: horse hoof walk/run by surface ×4, whinny ×3, ram hoof ×4, bleat ×3, mount up, dismount | 18 |
| SFX-P12 | ☐ | Death thud, ghost whoosh, resurrect, hearthstone channel + arrive, level-up chime (with MUS sting), rest enter | 7 |

## 5. Spell and ability sounds

Each ability in [Effects](04-vfx.md) needs up to three sounds: *cast* (loop or pre-cast), *release/travel*, *impact/aura*. Shared sounds first.

| ID | Done | Family | Count |
|---|---|---|---|
| SFX-S01 | ☐ | Shared cast loops per school (Holy, Nature, Arcane, Fire, Frost, Shadow) + pre-cast + release | 6 × 3 = 18 |
| SFX-S02 | ☐ | Shared impacts per school, small and large | 12 |
| SFX-S03 | ☐ | Shared buff-up, debuff-apply, dispel, heal-tick, damage-tick per school | 20 |
| SFX-S04 | ☐ | State sounds: stun, root, fear, sleep, silence, slow, interrupt, immune "tink", absorb, enrage, knockback, taunt | 12 |
| SFX-S05 | ☐ | **Fighter** — one bespoke set per ability row VFX-F01–F36: shouts ×5 (voiced per body), Charge rush, Stomp, Whirlwind, Execute, Shield Wall, stance changes, etc. | ≈ 50 |
| SFX-S06 | ☐ | **Cleric** — per row VFX-C01–C39: Oath ignite ×5, Verdict hammer, Mending Light, Hallowed Ground loop, Divine Ward shell, Dawn's Mercy, Avenging Dawn, etc. | ≈ 55 |
| SFX-S07 | ☐ | **Druid** — per row VFX-D01–D29: Thornlash whip, Renewal leaf loop, Rootgrasp, Stinging Swarm buzz, Astral Lance, Squall storm loop, Call Lightning, Starfall, Stillwater, etc. | ≈ 45 |
| SFX-S08 | ☐ | Items and professions: potion, elixir, scroll, enchant apply, weapon-proc ×4, trinket use ×7, dynamite fuse + blast ×4, bombs, gadgets ×5, mining ×3, herb pick, skinning, fishing cast/bobber/splash/reel, anvil ×3, forge, alchemy bubbling, enchanting hum, disenchant, sewing, cooking sizzle | ≈ 50 |

## 6. Creature sounds

Standard set per rig: idle/breath ×2, aggro, attack ×3, wound ×2, death, special ×1–2 (≈ 10 sounds). Skins of the same rig share sounds, pitched by size.

| ID | Done | Group | Rigs | Sounds |
|---|---|---|---|---|
| SFX-C01 | ☐ | Beasts (canine, boar, spider, bear, cat, ram/goat, stag, fox, bird, bat, snapper, mirejaw, lizard, scorpion, beetle, rat, worm, strider, drake) | 19 | ≈ 190 |
| SFX-C02 | ☐ | Humanoid creatures (Burrowkin, Gravelkin, Gillkin, ogre, Howler, harpy) — gibberish voice sets | 6 | ≈ 70 |
| SFX-C03 | ☐ | Undead and aberrations (skeleton rattle, shambler groan, spectre wail, ooze, horror) | 5 | ≈ 50 |
| SFX-C04 | ☐ | Elementals, constructs, plants (sprite, hulk, gargoyle, scarecrow, machine, animated armour, shambler, treant) | 8 | ≈ 80 |
| SFX-C05 | ☐ | Critters | 11 | 22 |
| SFX-C06 | ☐ | Creature ability library (one sound set per group VFX-M01–M28) | — | ≈ 90 |
| SFX-C07 | ☐ | Human and dwarf enemy combat voices: male ×3, female ×2 per rig (aggro ×3, attack ×3, wound ×2, death, flee) | — | 10 voices × 10 = 100 |

## 7. Boss and encounter sounds

| ID | Done | Encounter | Needs |
|---|---|---|---|
| SFX-B01 | ☐ | Act bosses and zone elites (≈ 25 named) | Aggro line + death line each (voiced, 1 sentence) = 50 lines; 12 bespoke mechanic sounds |
| SFX-B02 | ☐ | Gallowmere Crypts (4 bosses) | Voice: aggro, 2 mechanic callouts, kill-player, death per boss = 20 lines; the Stitched Choir's six-voice out-of-tune hymn (layered loop); 12 mechanic sounds |
| SFX-B03 | ☐ | The Slagworks (4 bosses) | 20 lines; Molten Maw roars; machinery set; slag flood; 14 mechanic sounds |
| SFX-B04 | ☐ | Hollowspire Keep (5 bosses) | 30 lines incl. Seraphine's three-phase dialogue and "He is awake" ending; polite applause loop; banquet toast; ink; 18 mechanic sounds |
| SFX-B05 | ☐ | The Hollow Throne (6 bosses) | 45 lines incl. Vaelric's phase lines and last line; Ward Strain crack ×4 + collapse; 30 mechanic sounds |
| SFX-B06 | ☐ | World bosses (3) | Spawn omen, roar ×3, mechanic sounds ×6 each, death = ≈ 30 |

## 8. NPC voice barks

Short spoken lines (1–4 words). Each voice has: greeting ×3, farewell ×2, annoyed ×2, vendor ×1. **The words of every line, and the boss lines, are in [Spoken Lines](../12-data/spoken-lines.md)**, which also sets the final count of voiced lines.

| ID | Done | Voice set | Count |
|---|---|---|---|
| VOX-01 | ☐ | Human male ×3 (commoner, soldier, scholar), human female ×3 | 6 voices × 8 = 48 |
| VOX-02 | ☐ | Mountain dwarf male ×2, female ×2 | 4 × 8 = 32 |
| VOX-03 | ☐ | Hill dwarf male ×2, female ×2 (softer, rural accent — the audible half of the culture split) | 4 × 8 = 32 |
| VOX-04 | ☐ | Guards (human, dwarf): greeting, warning, attack call | 2 × 6 = 12 |
| VOX-05 | ☐ | Elf envoy, ogre (Mugga, Hrokk), Covenant legate — unique short sets | 3 × 6 = 18 |
| VOX-06 | ☐ | Story lines (subtitled, voiced once): Hale Morrow's last words, Ashgrave's two lines, the scholars' key lines, Three Envoys, Seraphine's diary line, Vaelric's last line | ≈ 20 lines |
| VOX-07 | ☐ | Announcers: battleground (start, Crown taken, Crown dropped, hill captured ×3 teams, shrine captured, 100 points left, win/lose), Dustpit Pitmaster (chest soon, chest open, champion), world-boss zone yell | ≈ 22 lines |

## 9. Interface sounds

| ID | Done | Family | Count |
|---|---|---|---|
| UIA-01 | ☐ | Buttons: click, hover tick, tab, checkbox, slider, dropdown, close | 7 |
| UIA-02 | ☐ | Windows open/close: character, spellbook (page), talents, quest log (parchment), map (unroll), bags (per bag type), bank vault, guild vault, mail, auction, vendor, trainer, trade | 14 pairs = 28 |
| UIA-03 | ☐ | Quests: accept, objective tick, complete, abandon, quest text page | 5 |
| UIA-04 | ☐ | Items: pick up / drop by material (cloth, leather, metal, wood, gem, paper, food, liquid, herb, ore), split stack, sell (coins), buy, repair | 24 |
| UIA-05 | ☐ | Money: coins small/large, loot coin | 3 |
| UIA-06 | ☐ | Social: whisper received, party invite, guild invite, friend online, ready check, raid warning, group-roll start, roll won, duel request, trade request | 10 |
| UIA-07 | ☐ | Mail: new mail, send, open letter; auction: bid, outbid, sold | 6 |
| UIA-08 | ☐ | Talents and training: point spent, talent learned, spell learned, profession skill-up, recipe learned | 5 |
| UIA-09 | ☐ | Alerts: error buzz, cooldown-not-ready, low health heartbeat, breath warning, PvP queue ready, instance reset, map ping | 7 |
| UIA-10 | ☐ | Login: enter world, character select rotate, create character, delete, realm select | 5 |

## 10. Totals for this document

| Category | Assets |
|---|---|
| Music tracks and stings | ≈ 108 (≈ 3.5 hours) |
| Ambience beds / spot sounds | ≈ 55 / ≈ 160 |
| Player and combat effects | ≈ 280 |
| Spell and ability sounds | ≈ 260 |
| Creature sounds | ≈ 600 |
| Boss and encounter sounds and lines | ≈ 290 (165 voiced lines) |
| NPC and announcer voice | ≈ 185 lines |
| Interface sounds | ≈ 100 |
| **Total** | **≈ 2,000 audio assets** |

## 11. Order of work

Follows the art blocks in the [Art Master To-Do](00-art-master-todo.md#5-order-of-work): interface and core combat sounds with block B; Brightmead music and ambience with block C; dwarf voices, capitals and ship with block D; class ability sounds with block E; each zone's music, ambience and creatures with its zone block; boss voice and themes with their instance blocks. Voice generation is batched late (blocks I–K) once the text is final.

## How the audio is made

Decided 2026-11-12: **all audio is AI-generated: music, ambience, sound effects and every voice line. No licensed libraries, no hired composers or voice actors.** The audio is produced by the **[Asset Forge](../14-asset-pipeline/00-asset-forge.md)**, pipelines [P16 to P19](../14-asset-pipeline/03-audio-pipelines.md), which is the authority on how each sound is made. **The owner approves the audio style guide, and then the first results of each audio pipeline, before any music, ambience, sound effect or voice line is made in number** ([Asset Forge §7a](../14-asset-pipeline/00-asset-forge.md#7a-the-owners-approval)). The other review gates below are carried out, asset by asset, by the forge's automatic checks.

| Asset | Steps | Review gate |
|---|---|---|
| Audio style guide | Generate candidate themes and a palette of instruments per culture (section 1); fix tempo ranges, loudness targets and the mix reference | The owner approves it before any music, ambience, sound effect or voice line is made in number |
| Music tracks and stings | Text-to-music generation from the track brief in section 2, in the culture's instrument palette; several takes per track; edit to length; make loop points or a clean tail; master to the loudness target | Loops or ends cleanly; fits the palette; no vocals unless the brief asks for a choir; no recognisable melody from existing music |
| Ambience beds and spots | Text-to-sound generation; layer and trim; loop beds at 60–120 s | No audible loop seam; no speech-like artefacts |
| Sound effects | Text-to-sound generation in batches by family (impacts, casts, footsteps by surface, creature calls); 3–5 variations each; trim to the animation and spell timings in the data files | Starts on the frame; reads at game volume beside music; variations are distinct |
| Creature voices | Generated per rig (62 sets), then pitch-shifted for size variants | Matches the rig's size and temper |
| NPC and boss voice lines | Text-to-speech from the written lines in the quest text and encounter files, using designed synthetic voices, one per voice set in section 8 | Correct pronunciation of names (a pronunciation list is kept); emotion matches the line; no clipped words |
| Interface sounds | Generated and trimmed to under 0.5 s | Distinct from each other at low volume |

### Rules

| Rule | Detail |
|---|---|
| Synthetic voices only | Every voice is a designed synthetic voice. **No voice is cloned from, or prompted to imitate, a real person**, living or dead, and no line imitates a known performance |
| No imitation of existing music | Prompts never name an artist, composer, band, film or game. Outputs are checked by ear for a recognisable existing melody and regenerated if one is heard |
| Pronunciation list | One list of every proper name in the game (Halcyra, Khazrun, Solhaven, Vaelric, Ghul'thar and the rest) with its intended pronunciation, used for every voice generation so a name never sounds two ways |
| Records | Tool and model version, prompt, seed where available, date and approver for every asset, as for the art |
| Tool terms | A tool is used only if its terms allow commercial use of its output, checked once per tool and version |
| Regenerate before repairing | A take that needs heavy editing is regenerated |
| Disclosure | The AI-generated content statement in the launch checklist (task T-M14-09) covers audio as well as art |

The counts in section 10 do not change. The work moves from recording sessions to generation, selection and editing; the weakest areas to expect hand work on are **seamless music loops**, **consistent character voices across many lines**, and **timing effects to animation**.