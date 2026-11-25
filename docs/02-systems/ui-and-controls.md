# UI & Controls

[← Master Plan](../../MASTER_PLAN.md) · Prev: [PvP](pvp.md) · Next: [Class Framework](../03-classes/class-framework.md)

## 1. Controls

| Input | Action |
|---|---|
| W/A/S/D, Q/E | Move, turn (strafe with right mouse held), strafe |
| Right mouse drag | Mouselook / steer; right-click = interact / attack |
| Left mouse drag | Orbit camera; left-click = select |
| Both mouse buttons | Run forward |
| Space / X / Num Lock | Jump / sit / autorun |
| Tab / Shift-Tab | Next / previous enemy; F1–F5 select party |
| 1–0, -, = and modifiers | Action bar slots |
| Mouse wheel | Zoom (first person to 30 yd) |
| B, C, P, N, L, M, O, K, U | Bags, character, spellbook, talents, quest log, map, social, skills, reputation |
| Enter, / , R | Chat, command, reply |
| Esc | Cancel cast / clear target / game menu |

All bindings are rebindable. Click-to-move optional. Camera collides with terrain.

## 2. HUD elements

| Element | Notes |
|---|---|
| Player frame | Portrait, name, level, health, resource bar, combat/rest/leader/PvP icons |
| Target frame | Health, resource, level and rank (elite dragon, rare silver, skull), buffs/debuffs, target-of-target, cast bar |
| Party frames (4) / raid frames | Health, resource, debuff type colours, range fade, role |
| Action bars | Main bar (12 × 6 pages), bottom-left, bottom-right, 2 right bars; stance bar (Fighter); pet bar reserved |
| Cast bar, swing timer, GCD sweep | |
| Buff / debuff row | Durations, cancel on right-click |
| Minimap | Zoom, tracking (herbs/ore/treasure/undead), quest and town icons, clock, mail and LFG indicators |
| XP bar / rested notch, reputation bar option | |
| Chat window(s) + combat log | Tabs, filters, dockable |
| Bag bar and micro-menu | |
| Floating combat text | Damage, heals, misses, resource gains, procs |
| Nameplates | Toggle friendly / enemy; cast bars on nameplates |
| Error text, zone banner, loot toast, level-up fanfare | |
| Quest tracker | Up to 5 watched quests (objective counts only — no map arrows, classic style) |
| Mirror bars | Breath, fatigue |
| Tooltips | Items (with compare), spells, units, UI help |

## 3. Windows

Character sheet (paper doll, stats, skills tab, reputation tab) · Spellbook & abilities (with ranks) · Talents (three trees, preview before commit) · Quest log (20) · World map (continent → zone, fog-of-war by explored sub-area, player and party pins) · Bags / bank · Vendor (buy, sell, buyback, repair) · Trainer · Loot and group-roll frames · Trade · Mail · Auction house (browse, bids, auctions) · Professions (recipe list, reagents, craft N) · Social (friends, ignore, who, guild, raid) · Group-finder board · Eyrie map · Gossip / quest dialog · Duel / invite / resurrect / summon prompts · Battleground queue, scoreboard · Inspect · Macro editor (classic-style `/cast`, `/target`, `/use`) · Key bindings · Options (video, audio, interface, accessibility) · Help / GM ticket · Character select & create · Login / realm list.

## 4. Feedback and feel

- Ability icons show cooldown, range (red), resource (blue-tint), usability (grey).
- Audio cues for errors ("Not enough rage"), quest accept/complete, level-up, loot rolls, whispers.
- Spell visuals: cast, channel, projectile, impact, aura; per-school colour language (Holy gold, Nature green, Arcane violet, Fire orange, Frost blue, Shadow purple-black, Physical white/red).
- Target highlight, selection circle coloured by reaction (red/yellow/green/blue).

## 5. Add-on / scripting support

Not at launch. The UI is built from data-described frames so a sandboxed add-on API can be exposed later. Macros are in.

## 6. Accessibility and options

Colour-blind palettes for quality colours and debuff types · UI scale · subtitle/speech bubbles · key-hold vs toggle options · screen-shake and flash reduction · separate volume sliders (master, music, effects, ambience, voice).

## 7. Art direction for UI

Stylised, readable, painterly icons; stone-and-brass frame motif for Concord. Each future allegiance gets a frame skin (Wildpact wood/vine, Covenant ash/violet glass).
