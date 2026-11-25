# Asset Pipelines 3 — Audio and Fonts (P16 to P20)

[← Asset Forge](00-asset-forge.md) · Prev: [3D models, rigs and animation](02-3d-pipelines.md) · Next: [Placeholders and swapping](04-placeholders-and-swap.md) · What to make: [Audio list](../10-art/09-audio.md)

One pipeline per kind of audio, and one for fonts. Shared rules are on the [Asset Forge](00-asset-forge.md) page. All audio is delivered as 48 kHz OGG Vorbis, mono for positional sounds and voice, stereo for music and ambience beds.

## Shared audio tools

| Tool | Candidates, in order | Used for |
|---|---|---|
| Text-to-music | ACE-Step 1.5 (MIT); then another permissively licensed music model that passes bring-up | P16 |
| Text-to-sound | Stable Audio Open (check its licence: reports describe a revenue threshold and registration); then any permissively licensed text-to-audio model that passes bring-up | P17, P18 |
| Text-to-speech | Kokoro (Apache 2.0; runs on CPU; no voice cloning); then Qwen3-TTS (Apache 2.0) using designed voices only | P19 |
| Speech recognition | Whisper class model | Checks voice lines against the script |
| Audio–text similarity | A CLAP class model | Checks that a sound matches its description |
| Processing | `ffmpeg`, `sox`, EBU R128 loudness | Trim, fade, loop, normalise |

**Fallback for all audio: synthesis.** The forge has a small synthesis library that makes sound from oscillators, noise, filters and envelopes, with no samples and no model: impacts, whooshes, magical tones, footsteps by surface, wind, rain, fire, and simple instrument voices (plucked string, bowed string, flute, horn, drum, choir pad) for music. It is plainer than generated audio, but it is always available and never infringes anything.

## P16 — Music (about 108 tracks and stings)

| | |
|---|---|
| Reads | The music table in the [Audio list](../10-art/09-audio.md): per track, its zone or event, mood, culture and length |
| Template | "`<culture instruments>`, `<mood>`, `<tempo>`, instrumental, orchestral game music, no vocals" with the culture's instrument line from the audio list (humans: strings and woodwind; mountain dwarves: low brass and choir; hill dwarves: fiddle and pipes) and a fixed key and tempo range per zone so a zone's tracks belong together |
| Steps | 1. Generate 3 takes per track at the target length plus 10 s. 2. Pick the take with the best audio–text similarity and no detected vocals (unless a choir is asked for). 3. Trim to length on a bar line. 4. Loops: find a loop point by self-similarity and crossfade 2 s; non-loops: fade the tail over 4 s. 5. Normalise to −18 LUFS integrated, true peak under −1 dB |
| Stings | Level-up, quest complete, death, discovery and boss stingers are generated at 3–8 s with the same instrument lines |
| Checks | Length within 2 s of target; loudness in range; loop seam inaudible (spectral difference across the seam under threshold); no speech detected; similarity to its description above threshold; **not similar to any other accepted track beyond a threshold**, so zones do not share a melody by accident |
| Fallback | Rule-based composition played by the synthesis library: a chord progression and melody generated from the mood (mode, tempo, density) and voiced with the culture's synthesised instruments |

## P17 — Ambience (about 55 beds and 160 spot sounds)

| | |
|---|---|
| Reads | The ambience tables in the Audio list; zone weather and sub-area descriptions |
| Steps (beds) | 1. Generate 3 segments of 30–45 s from the bed's description ("wind through pine trees, distant ram bleating, no music"). 2. Layer and crossfade them into a 90 s stereo loop. 3. Loop-seam check. 4. Normalise to −28 LUFS |
| Steps (spots) | Single sounds of 1–6 s (a crow, a hammer on an anvil, a creaking sign), 3 variations each, mono, trimmed to the sound with 10 ms fades |
| Checks | No music and no speech detected; loop seam inaudible; loudness in range; matches the description |

## P18 — Sound effects (about 1,500: player and combat, spells, creatures, bosses, interface)

| | |
|---|---|
| Reads | Sections 4 to 9 of the Audio list; the effect list for spell sounds; animation contact frames from P15; cast times from the spell data |
| Steps | 1. Generate from the row's description with the family's fragment (melee: "single dry impact, close, no reverb"; spell cast: "rising magical shimmer"; interface: "short soft click"). 2. Make 3–5 variations by seed. 3. Trim to the first transient with a 5 ms fade in; cut the tail at −60 dB. 4. **Fit to timing**: cast loops are cut to loop cleanly; impact sounds are aligned so the transient falls on the animation's contact frame; channelled spells get a loop and a release tail. 5. Normalise by family (combat −16 LUFS, interface −22 LUFS) |
| Creature voices | Per rig: idle, aggro, attack ×2, hurt ×2, death. Generated from the creature's description, then pitch-shifted by size for the rig's skins (larger is lower) |
| Checks | Length under the family's maximum (interface 0.5 s, impacts 1.5 s); starts within 10 ms of the file start; no clipping; no speech; variations differ from each other; matches the description |
| Fallback | The synthesis library's generator for the family |

## P19 — Voice lines (about 250: NPC barks, boss lines, story lines, announcer)

| | |
|---|---|
| Reads | **[Spoken Lines](../12-data/spoken-lines.md)**, which holds the words of every voiced line and the pronunciation list, and sets the count; the voice tables in the Audio list for the voice sets; the NPC rosters for who speaks |
| Voices | The audio list's voice sets (by culture, sex and age band) are each a **designed synthetic voice**: a fixed blend of the speech model's stock voices plus pitch and rate settings, stored in `forge/pipelines/P19/voices.yaml`. **No voice is cloned from a recording of any person.** Bosses get their own blends with a processing chain (pitch, reverb, a doubled low octave for the Hollow King) |
| Pronunciation | `forge/pipelines/P19/pronunciation.yaml` lists every proper name in the game with a phonetic spelling. It is applied to the text before synthesis so a name never sounds two ways |
| Steps | 1. Apply the pronunciation list. 2. Synthesise with the speaker's voice. 3. Transcribe with the speech-recognition model and compare with the script; retry on a mismatch. 4. Trim silence, normalise to −20 LUFS, apply the speaker's processing chain |
| Checks | Transcript matches the script (word error rate under 5%, names excepted); length within a plausible range for the word count; no clipping |
| Fallback | No audio; the line is shown as a subtitle and speech bubble, which the game does for every line anyway |

## P20 — Fonts (3 typefaces)

| | |
|---|---|
| Need | A title serif, a body sans and a number face, with Latin Extended coverage ([User Interface list](../10-art/05-ui.md)) |
| Method | Fonts must be exact and legible at 11 pixels, which image generation does not deliver, so they are **constructed**: a forge script builds each typeface parametrically (stem weight, x-height, serif shape, contrast, width) from geometric strokes, in the manner of a parametric type design, and exports TrueType with FontForge. The parameters are chosen once to suit the style bible: a sturdy slab-serif title face, a humanist sans, and tabular numerals |
| Checks | All required code points present; no overlapping contours; consistent side bearings; legible at 11, 13 and 16 pixels (rendered samples pass an optical character recognition check) |
| Fallback | If the constructed fonts fail the legibility check, the game uses the engine's built-in default font, and this is the one place the game would ship a non-generated asset |
