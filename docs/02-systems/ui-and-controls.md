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

All bindings are rebindable: every action has a primary and a secondary key, set in the Key Bindings window opened from the game menu. Click-to-move optional. Camera collides with terrain.

## 2. HUD elements

| Element | Notes |
|---|---|
| Player frame | Portrait, name, level, health, resource bar, combat/rest/leader/PvP icons |
| Target frame | Health, resource, level and rank (elite dragon, rare silver, skull), buffs/debuffs, target-of-target, cast bar |
| Party frames (4) / raid frames | Health, resource, debuff type colours, range fade, role |
| Action bars | Main bar (12 × 6 pages), bottom-left, bottom-right, 2 right bars; stance bar (Fighter); pet bar reserved. The optional bottom-left and bottom-right bars sit side by side directly above the XP bar, the bottom-left on the left half and the bottom-right on the right half |
| Cast bar, swing timer, GCD sweep | |
| Buff / debuff row | Durations, cancel on right-click |
| Minimap | Zoom, tracking (herbs/ore/treasure/undead), quest and town icons, clock, mail and LFG indicators |
| XP bar / rested notch, reputation bar option | Sits directly on the top edge of the main action bar, the same width, touching it. Divided into 10 equal sections ("bubbles") by thin dividers over the fill; its text is centred inside the fill |
| Chat window(s) + combat log | Tabs, filters, dockable |
| Bag bar and micro-menu | The bag bar holds the backpack and 4 bags; any of its buttons opens the one bag window. The tooltip of the micro-menu's system button shows the frame rate, the latency and the player's position; that read-out is hidden by default and is drawn on screen only while switched on with its key |
| Placement at the bottom | The action bars, the bag bar, the micro-menu and the chat frame sit with their bottom edges on the bottom edge of the screen, with no gap |
| Floating combat text | Damage, heals, misses, resource gains, procs |
| Nameplates | Toggle friendly / enemy; cast bars on nameplates |
| Error text, zone banner, loot toast, level-up fanfare | |
| Quest tracker | Up to 5 watched quests (objective counts only — no map arrows, classic style) |
| Mirror bars | Breath, fatigue |
| Tooltips | Items (with compare), spells, units, UI help |

## 3. Windows

Character sheet (paper doll, stats, skills tab, reputation tab) · Spellbook & abilities (with ranks) · Talents (three trees, preview before commit) · Quest log (20) · World map (continent → zone, fog-of-war by explored sub-area, player and party pins) · Bags (one window for the backpack and every equipped bag, growing upward and to the left from its bottom-right corner as bags are added and keeping its chosen shape, Portrait (the default) or Landscape; that corner is anchored above the bag bar and the window is kept on screen; empty slots shown each in its place ("Show empty slots", on by default) or combined into one slot with a count) / bank · Vendor (buy, sell, buyback, repair) · Trainer · Loot and group-roll frames · Trade · Mail · Auction house (browse, bids, auctions) · Professions (recipe list, reagents, craft N) · Social (friends, ignore, who, guild, raid) · Group-finder board · Eyrie map · Gossip / quest dialog · Duel / invite / resurrect / summon prompts · Battleground queue, scoreboard · Inspect · Macro editor (classic-style `/cast`, `/target`, `/use`) · Key bindings (a primary and a secondary key for every action) · Options (video, audio, interface, accessibility) · Help / GM ticket · Character select & create · Login / realm list.

## 4. Feedback and feel

- Ability icons show cooldown, range (red), resource (blue-tint), usability (grey).
- Audio cues for errors ("Not enough rage"), quest accept/complete, level-up, loot rolls, whispers.
- Spell visuals: cast, channel, projectile, impact, aura; per-school colour language (Holy gold, Nature green, Arcane violet, Fire orange, Frost blue, Shadow purple-black, Physical white/red).
- Target highlight, selection circle coloured by reaction (red/yellow/green/blue).

## 5. Add-on / scripting support

Not at launch. The UI is built from data-described frames so a sandboxed add-on API can be exposed later. Macros are in.

## 6. Accessibility and options

Colour-blind palettes for quality colours and debuff types · UI scale · subtitle/speech bubbles · key-hold vs toggle options · screen-shake and flash reduction · separate volume sliders (master, music, effects, ambience, voice).

The Interface tab of the Options window holds at least: **Auto loot** (on by default: opening a corpse opens the loot window, which takes the money first and then each item in turn, one every 0.2 s, and closes after the last; an item that does not fit stays and the window stays open showing it; moving away or closing the window stops it. A Shift-click on a corpse does the opposite of the setting: with auto loot on it opens the loot window and takes nothing, with it off it opens the window and loots one item at a time in the same way) · **Show empty slots** in the bag window (on by default) · **Bag layout**, Portrait or Landscape (Portrait by default, taller than wide; Landscape is wider than tall; the columns are worked out from the slot count and the orientation). Settings are saved for the player and survive restarting the client. Sizes and positions are in the [UI Specification](../08-tech/ui-specification.md).

## 7. Art direction for UI

Stylised, readable, painterly icons; stone-and-brass frame motif for Concord. Each future allegiance gets a frame skin (Wildpact wood/vine, Covenant ash/violet glass).
