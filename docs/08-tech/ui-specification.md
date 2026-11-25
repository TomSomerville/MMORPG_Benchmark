# UI Specification

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Network Protocol](network-protocol.md) · Next: [Milestone Task Lists](milestone-tasks.md) · Design: [UI & Controls](../02-systems/ui-and-controls.md) · Art: [User Interface art list](../10-art/05-ui.md)

Layout, size and behaviour of every HUD element and window, the full default keybinding list, and every slash command. Sizes are in pixels at the reference resolution; the whole UI scales with one setting.

## 1. Global rules

| Rule | Detail |
|---|---|
| Reference resolution | 1920 × 1080. The interface is laid out at the reference and scaled to the window as one canvas, extra width or height adding space; the default window is 1280 × 720. UI scale 0.64–1.15 in options; default fits the window height |
| Look | Stone and brass: dark grey stone panels with brass corner plates and studs, a brass-ringed round minimap, an action bar with pointed end caps, and open unit frames (§2). Panels, rings, bars and caps are drawn by the client in code from one style (`UiStyle`); no frame textures are loaded. **Open:** whether this code-drawn look is final or is replaced by generated frame art (pipeline P03) is the owner's choice; the owner has liked the direction and has not approved P03's assets |
| Anchoring | Every element is anchored to a screen edge or corner, so wide and ultrawide screens only add space in the middle |
| Movable frames | Player, target, party, cast bar, buffs, chat, minimap, quest tracker and extra action bars can be unlocked and dragged; positions are saved per character. "Reset layout" restores the defaults below |
| Windows | Open at a default anchor; up to two side-by-side panels on the left (the second pushes right, classic behaviour); `Esc` closes the most recent. Windows that need an NPC close when the player moves more than 5 yards from it |
| Data-described frames | Each frame is a control with a small view-model; no gameplay logic in UI code. Frames read one client state store (`ClientState`: units, auras, casts, cooldowns, items, quests, combat log, floating text) that the network layer updates. Every control has a name, so the scripted client and the automation port can find it |
| Fonts | Body 13 px, small 11 px, headings 16 px, numbers on bars 11 px with outline, floating combat text 20–32 px |
| Colours | Item quality: grey 9D9D9D, white FFFFFF, green 1EFF00, blue 0070DD, purple A335EE, orange FF8000. Reaction: hostile red, neutral yellow, friendly green, player blue. Classes: Fighter C79C6E, Cleric F58CBA, Druid FF7D0A. Schools as in [UI & Controls §4](../02-systems/ui-and-controls.md#4-feedback-and-feel) |
| Tooltips | Appear 0.2 s after hover, anchored bottom-right by default; item tooltips show a comparison with the equipped item when Shift is held |
| Moving items | Click, then click: a left click on a slot picks up what is there (its name follows the pointer) and a left click on another slot puts it down, moving, stacking or swapping. A right click wears an item from the bags, takes off one that is worn, uses food, drink or the hearthstone, and at an open vendor sells. Clicking the world with an item in hand asks to destroy it. The same click-then-click moves spells and macros onto bars and items into trade, mail and bank windows |
| Confirmation prompts | For destroying an item, binding on equip, binding on pickup in a group, talent commit, abandoning a quest, buying a bank or guild tab, respec, deleting a character |
| Error text | Red, centre-top, up to 3 lines, each fading after 3 s, with the error sound. Text comes from the protocol's `ResultCode` strings |

## 2. HUD layout (default positions)

| Element | Anchor | Position and size | Behaviour |
|---|---|---|---|
| Player frame | Top-left | 20, 18; 320 × 96 | An open frame with no panel behind it: a round portrait 88 px across in a brass ring, with the level in a 30 px round badge at its lower right; beside it the name, a health bar (224 × 20) and a resource bar (216 × 16), slim and round-ended, with their numbers; a state line beneath (resting, in combat); icons: leader crown, master looter, PvP flag. Right-click: menu (loot method, reset instances, leave group, dungeon difficulty reserved) |
| Target frame | Top-left | 364, 18; 320 × 96 | The same frame for the target. Its portrait ring shows standing, with the word at the right under the bars: a silver ring and "Rare"; a gold ring with studs and "Elite" (elite, group elite, dungeon trash), "Rare Elite", or "Boss" (mini-boss and every boss rank); a skull for a creature 10+ levels above. Level coloured by difficulty. Cast bar under the bars (216 × 16). Up to 16 buffs then 16 debuffs beneath, 21 px each, own debuffs larger (26 px) |
| Target of target | Top-left | 510, 60; 120 × 45 | Name and health only |
| Party frames ×4 | Top-left | 20, 150 downward; 180 × 56 each, 12 px gap | Portrait, name, health, resource, up to 4 dispellable debuffs coloured by type, fade to 55% beyond 40 yards, leader and looter icons, F1–F5 select |
| Raid frames | Left | 20, 150; 8 groups of 5; 78 × 38 each | Name, class colour health bar, debuff type border, range fade; replace party frames in a raid |
| Buff row | Top-right | Left of the minimap; 32 px icons, 2 rows of 10 | Duration below each; right-click cancels; debuffs in a row beneath with a coloured border by type; flashing in the last 10 s |
| Minimap | Top-right | 20 from each edge; 170 px circle in an 8 px brass ring | Zone name above; clock, tracking, mail and group-finder buttons on the rim; zoom + and −; pings on click; shows party pins, quest giver and turn-in icons, town services, tracked nodes |
| Quest tracker | Right | Below the minimap; 240 wide | Up to 5 watched quests (by default the first five taken): title and objective counts, or the quest's tracker line where it has no objectives; a completed quest folds to its title and "(Complete)" in yellow; click opens the quest log |
| Main action bar | Bottom-centre | Centred, above the XP bar; 12 square slots of 50 px, 5 px gap, in a stone bar 673 × 68 with a brass edge and a pointed cap at each end | The ability's icon fills its slot (its name is written there while it has no icon); page arrows (6 pages); keybind text top-right of each slot; cooldown sweep; red tint out of range; blue tint lacking resource; grey unusable; yellow border for next-swing abilities when queued |
| Bottom-left and bottom-right bars | Bottom-centre | Above the main bar, left and right halves; 12 slots each | Optional (interface options) |
| Right bars 1 and 2 | Right | Vertical, 12 slots each, 36 px | Optional |
| Stance bar | Bottom-left of main bar | 3 slots of 32 px | Fighter stances; shows the active one lit |
| Pet bar | Above stance bar | Reserved; hidden at launch | |
| XP bar | Bottom | Under the action bar, 24 px narrower than it; 16 px high, notched | Purple = XP, blue = rested; rested notch; hover shows numbers. At level cap it becomes the watched reputation bar |
| Micro-menu | Bottom-right of centre | 8 buttons of 28 × 36 | Character, spellbook, talents, quest log, social, world map, main menu, help |
| Bag bar | Bottom-right | 5 slots of 36 px | Backpack plus 4 bags; free-slot count on the backpack. A click on any of the five opens or closes the one bag window (§3); a bag is put into or taken out of a bag slot here, and the bag window grows or shrinks with it |
| Cast bar | Bottom-centre | Above the main bar; 240 × 22 | Spell name, time; green flash on success, red on interrupt; a latency zone at the end |
| Swing timer | Under the cast bar | 220 × 7 | Main hand; second thin bar for off hand |
| Mirror bars | Top-centre | 200 × 18 | Breath, fatigue, feign reserved |
| Chat window | Bottom-left | 20, 20 from the bottom; 430 × 196 | Tabs: General, Combat Log; resizable; scroll with the wheel; click a name to whisper, shift-click to `/who` |
| Floating combat text | Around the character | — | Damage taken left, healing right, outgoing damage over the target; crits 150% size; scrolls up for 1.5 s |
| Nameplates | Above units | 110 × 12 health, name above | `V` enemy, `Shift+V` friendly; cast bar beneath; tapped mobs grey; current target larger. An NPC has no health bar and its role under its name; a world object only its name. Over a quest giver or ender: a gold `!` for a quest to take, a grey `!` for one too easy to matter, a gold `?` for one ready to hand in, a grey `?` for one in progress. A corpse with loot for the player carries a gold mark. **A nameplate is not drawn through the ground:** a unit on the other side of the ground from the player (in a tunnel under the player's feet, or on the surface above a player who is underground, with 2.5 m or more of land between and no opening cut) is given no nameplate, name or mark |
| Zone banner | Top-centre | — | Zone and sub-area name for 3 s on entry, coloured by PvP tag |
| Loot toast | Bottom-centre | Above the cast bar | "You receive: [item]" lines for 4 s |
| Group loot roll frames | Centre-right | 4 stacked; 300 × 70 | Item, timer bar (60 s), Need, Greed, Pass |
| Boss frame | Top-centre | 300 × 40 | Dungeon and raid bosses: name, health, phase; add frames for councils (up to 4) |
| Selection circle and target highlight | World | — | Coloured by reaction |

## 3. Windows

Sizes are the panel size. "L1" and "L2" mean the first and second left-side panel positions (16, 104 and 400, 104).

| Window | Key | Position, size | Contents and behaviour |
|---|---|---|---|
| Character | C | L1; 384 × 512 | Tabs: **Character** (paper doll with 19 slots; rotating model; stat block: primary attributes with base and bonus, melee panel, spell panel, defences, resistances; hover explains each number with its formula) · **Skills** (weapon skills, professions with bars, languages) · **Reputation** (bars per reputation; watch on XP bar; at-war toggle greyed) · **PvP** (Marks of Valor, duels won and lost, battleground record) |
| Spellbook | P | L1; 384 × 512 | Tabs: General, the three trees' abilities by school, professions. 12 spells per page. Shows rank; toggle "show all ranks". Drag to action bars. Unlearned spells available at the next trainer visit are listed greyed with their level |
| Talents | N | L1; 384 × 560 | Three tabs, one per tree, with points spent; 7 tiers × 4 columns; arrows for prerequisites; **preview mode**: points placed are pending (green) until "Learn" is pressed, "Reset" clears pending; unreachable tiers 6–7 shown with a lock and "Requires level cap increase" |
| Quest log | L | L1; 640 × 480 (wide) | Left: quests grouped by zone, coloured by difficulty, count "n / 20". Right: description, objectives with counts, rewards. Buttons: Abandon, Share, Track (max 5). Completed quests marked |
| World map | M | Full screen overlay, 1024 × 768 centred | Continent view → click a zone; fog over undiscovered sub-areas; player arrow, party pins, corpse pin, discovered eyries; zone level range in the title; right-click zooms out. Stoneheart Deeps has three layer buttons (Upper, Great Cavern, Underworks) that follow the player's height |
| Bags | B, Shift+B, F8–F12, or any bag-bar button: all open the same window | Bottom-right, above the bag bar; 8 columns wide, growing upward a row at a time | **One window for the backpack and every equipped bag together**; there is no window per bag. Its grid holds every slot of every container, the backpack's first and then each bag's in bag-bar order, so it has 16 slots with the backpack alone and grows as bags are put in the bag bar (up to 64 with four 12-slot bags) and shrinks when one is taken out. The window is a view: each item stays in its own container and slot, and the containers and their numbering are as in [Items §6](../02-systems/items-and-loot.md#6-bags-bank-inventory). Free and total slot counts in the title; item quality border; cooldown sweep on usable items; right-click uses, equips, or sells at a vendor; shift-click splits a stack or links to chat; items are moved, and placed on the action bar, by click-then-click (§1). **"Show empty slots"** tick box in the window, the same setting as in Options (Interface), on by default and saved with the player's interface settings: on, every empty slot is drawn in its place; off, only filled slots are drawn, followed by a single empty slot with the number of free slots on it, and an item put down on that slot goes into the first free slot |
| Bank | at NPC | L1; 384 × 512 | 24 slots + 6 purchasable bag slots with prices; right-click moves between bank and bags |
| Vendor | at NPC | L1; 384 × 512 | Tabs: Merchant (10 items per page, price, limited stock count, red if unusable), Buyback (12). Repair one, repair all with the cost, guild-bank repair when permitted. A right click on an item in the bags sells it |
| Trainer | at NPC | L1; 384 × 512 | Filter: available, unavailable, known. Row: icon, name, rank, cost; detail pane with tooltip and requirements; Train button. Class trainers in capitals add "Reset talents" with the current price |
| Gossip and quest dialog | at NPC | L1; 384 × 512 | Greeting text, option list with icons (gossip, vendor, trainer, taxi, bind, bank, battlemaster), quest list with state icons. Quest pages: offer (text, objectives, rewards, Accept / Decline), progress (Continue greyed until complete), completion (reward choice highlighted, Complete Quest) |
| Loot | at corpse | At the cursor; 180 × variable | Up to 4 items per page with quality colours; coin line; click to take; shift-right-click the corpse to auto-loot all |
| Trade | at player | L1; 384 × 512 | Two columns of 6 tradeable slots + 1 "will not be traded" slot each; money fields; Trade (turns the side green) and Cancel; any change clears both acceptances |
| Mail | at mailbox | L1; 384 × 512 | Tabs: Inbox (7 per page: sender, subject, days left, attachment and money icons, COD marker) and Send (recipient with autocomplete from friends and guild, subject, body, 12 attachment slots, money or COD, postage shown) |
| Auction house | at NPC | Centre; 832 × 447 | Tabs: **Browse** (name search; filters for level range, slot, type, quality, usable; 50 results per page; sortable columns; Bid and Buyout) · **Bids** · **Auctions** (drop an item, set stack, starting bid, buyout, 2 / 8 / 24 hours; deposit shown; list of own auctions with Cancel). The neutral house shows its higher cut |
| Professions | K then the profession, or its spellbook icon | L1; 384 × 512 | Skill bar; recipe list grouped by kind and coloured orange, yellow, green, grey; filters (have materials, by slot); detail: reagents with counts owned, tools; Create, Create All, count box |
| Social | O | L1; 384 × 512 | Tabs: Friends (online first, zone, level, class, notes; Add, Remove, Whisper, Invite) · Ignore · Who (search box, results, sortable) · Guild (roster with rank, note, last online; MOTD; guild info; rank editor for those with permission) · Raid (8 groups, drag to move, ready check, convert to raid) |
| Guild bank | at vault | Centre; 720 × 500 | 6 tab buttons with icons on the right; 98 slots (14 × 7) per tab; money line with Deposit and Withdraw; "Remaining withdrawals today"; tabs: Log, Money Log, Tab Info (note); Buy tab; permissions editor in the rank editor |
| Group finder board | I | L1; 384 × 512 | Post (activity: dungeon, raid, world boss, quest, battleground; role; note) and Browse (list with whisper and invite). No automatic matching and no teleport |
| Eyrie map | at NPC | Centre; 600 × 450 | Continent map with known nodes; lines show the route; hover shows the fare and time; click to fly |
| Inspect | on player | L1 | Paper doll and talents spent, read-only |
| Battleground | H | Centre; 500 × 400 | Queue (solo or group), bracket, status; in a match: scoreboard (team totals; rows: name, kills, deaths, damage, healing, hill time, crown time) |
| Macros | `/macro` | L2; 300 × 420 | 18 slots, name, icon picker, 255-character body |
| Key bindings | Game menu | Centre; 600 × 500 | Every action in §4, two keys each; reset to default; conflict warning |
| Options | Esc | Centre; 600 × 500 | Tabs: Video (resolution, window mode, quality presets, view distance, shadows, effects density, frame cap, vertical sync) · Audio (master, music, effects, ambience, voice; sound in background) · Interface (extra bars, names and nameplates, combat text, auto-loot, self-cast key, camera style, click-to-move, tutorial tips, chat timestamps, show empty slots in the bag window) · Accessibility (UI scale, colour-blind palettes, reduce flashes and shake, hold-versus-toggle, subtitles) |
| Help | Game menu | Centre; 500 × 400 | Tips, known issues, open a GM ticket: category (stuck, lost item, bug, harassment, account, other) and 500 characters of text; shows the state of the player's one open ticket (open, answered, closed) and the GM's reply ([Accounts and Live Service §4](accounts-and-live-service.md#4-support)) |
| Report | Right-click a player, a chat name or a chat line | Centre; 360 × 280 | Reason (spam, abuse, name, cheating, botting), an optional 200-character note, Report and Cancel; a "Also ignore this player" tick box, on by default. Confirmation in the system channel ([Accounts and Live Service §3](accounts-and-live-service.md#3-conduct-and-moderation)) |
| Penalty notice | At login, when a penalty applies | Centre; 420 × 240 | The penalty, its reason, when it ends, and how to appeal |
| Game menu | Esc | Centre; 200 × 280 | Help, Options, Key Bindings, Macros, Log Out, Exit Game, Return to Game |
| Barber | at NPC | Right panel over a turntable view | Hair, hair colour, facial feature; price updates; Accept / Cancel |
| Tabard designer and guild registrar | at NPC | L1 | Emblem, emblem colour, border, border colour, background; petition window with signature slots |
| Prompts | — | Centre-top; 320 × 96 | Duel, group invite, guild invite, trade request, resurrect (with timer), summon reserved, ready check, quest share, bind confirmation, roll confirmation |

The Report, Penalty notice and Help windows use the standard dialog frame and controls from the [UI art list](../10-art/05-ui.md); they need no art of their own. The Launcher uses the login screen's key art.

### Screens outside the game world

| Screen | Contents |
|---|---|
| Login | Logo and key art, account name, password, "Remember account name", Log In, Create Account (opens the registration page), Options, Quit; links to the terms and privacy pages; status line for errors; version and content hash in the corner |
| Realm list | Name, population, number of characters; Enter |
| Launcher | Before the client starts: news panel, version, a progress bar for updates, Play (enabled when files are verified), Repair, Settings (install folder, download limit), links to register an account and to the policy pages ([Accounts and Live Service §6](accounts-and-live-service.md#6-updates-versions-and-restarts)) |
| Login queue | Shown when the realm is at its player cap (`realm.maxPlayers`, at most 5,000): position in queue, estimated wait, Cancel. A dropped player who reconnects within 5 minutes keeps their place |
| Character select | Up to 10 characters listed at the right with name, level, class, zone; the selected character standing in their home capital; Enter World, Create, Delete (type DELETE to confirm), Back |
| Character create | Race buttons (Human, Dwarf), sex, class buttons (all three for both races); customisation sliders (skin, face, hair, hair colour, facial); a preview that is the live model, built as the game builds a player (the bald body with the chosen face, hair piece, facial pieces, skin tint and hair-colour tint, [Presentation Rules §2a](../12-data/presentation-rules.md#2a-player-characters)) and rebuilt as each slider moves; race and class descriptions; name field with a Random button; Accept, Back |
| Loading | One painting per zone or instance, a tip line, a progress bar |

## 4. Default keybindings

| Group | Action | Key |
|---|---|---|
| Movement | Forward, back, turn left, turn right | W, S, A, D (also arrows) |
| | Strafe left, strafe right | Q, E |
| | Jump | Space |
| | Sit or stand | X |
| | Autorun | Num Lock, and mouse button 4 |
| | Walk or run toggle | Num / |
| | Run forward | Both mouse buttons |
| Camera | Zoom in, zoom out | Mouse wheel |
| | Mouselook / steer | Hold right mouse |
| | Orbit | Hold left mouse |
| | Flip camera | Hold End |
| Targeting | Nearest enemy, previous enemy | Tab, Shift+Tab |
| | Nearest friend | Ctrl+Tab |
| | Self, party 1–4 | F1, F2–F5 |
| | Target of target, assist | F, Shift+F |
| | Clear target or cancel | Esc |
| | Attack target | T |
| | Interact with target | G |
| | Show enemy / friendly nameplates | V, Shift+V |
| Action bars | Slots 1–12 | 1–9, 0, -, = |
| | Next page, previous page | Shift+mouse wheel; Shift+2 … Shift+6 jump to a page |
| | Bottom-left bar 1–12 | Ctrl+1 … Ctrl+= |
| | Bottom-right bar 1–12 | Alt+1 … Alt+= (unbound by default beyond Alt+1–6) |
| | Stance 1, 2, 3 | Ctrl+F1, Ctrl+F2, Ctrl+F3 |
| | Self-cast modifier | Hold Alt |
| Windows | Character, spellbook, talents | C, P, N |
| | Quest log, world map | L, M |
| | Social, skills and professions, reputation | O, K, U |
| | Group finder, battleground | I, H |
| | Backpack, all bags (both open the one bag window) | B, Shift+B |
| | Bag-bar slots 1–5 (each opens the one bag window) | F8–F12 |
| | Game menu | Esc |
| Chat | Open chat, start a command, reply to last whisper | Enter, /, R |
| | Scroll chat up, down, to bottom | Page Up, Page Down, Shift+Page Down |
| Other | Toggle the whole UI | Alt+Z |
| | Screenshot | Print Screen |
| | Toggle minimap zoom in, out | Num +, Num − |
| | Push-to-show latency and frame rate | Ctrl+R |
| | Loot all while clicking a corpse | Shift held |

Every binding can be changed; each action takes a primary and a secondary key.

## 5. Slash commands

| Command | Effect |
|---|---|
| `/s`, `/say` · `/y`, `/yell` · `/e`, `/em`, `/me` | Say, yell, custom emote |
| `/p`, `/party` · `/ra`, `/raid` · `/rw` · `/g`, `/guild` · `/o`, `/officer` · `/bg` | Group and guild channels |
| `/w`, `/whisper`, `/t <name>` · `/r` | Whisper, reply |
| `/1 … /9` · `/join <channel>` · `/leave <channel>` · `/chatlist` | Numbered channels (1 General, 2 Trade, 3 LocalDefense, 4 LookingForGroup) |
| `/who [filters]` · `/friend <name>` · `/unfriend` · `/ignore` · `/unignore` | Social |
| `/invite <name>` · `/kick` · `/leave` · `/promote` · `/readycheck` · `/roll [min max]` | Groups; `/roll` defaults to 1–100 and is shown to the group |
| `/ginvite` · `/gkick` · `/gpromote` · `/gdemote` · `/gmotd <text>` · `/gquit` · `/groster` | Guild |
| `/duel` · `/forfeit` · `/yield` | Duels |
| `/trade` · `/inspect` · `/follow` · `/assist [name]` · `/target <name>` · `/cleartarget` | Interaction |
| `/cast <spell>[(Rank N)]` · `/use <item>` · `/startattack` · `/stopattack` · `/stopcasting` · `/cancelaura <name>` · `/equip <item>` | Abilities; usable in macros. One ability per key press (no conditionals at launch) |
| `/sit` · `/stand` · `/sleep` · `/kneel` and 40 other text emotes: `/wave`, `/bow`, `/cheer`, `/dance`, `/laugh`, `/cry`, `/point`, `/salute`, `/thank`, `/hello`, `/bye`, `/no`, `/yes`, `/shrug`, `/roar`, `/flex`, `/clap`, `/kiss`, `/hug`, `/beg`, `/rude`, `/chicken`, `/train`, `/applaud`, `/shy`, `/surrender`, `/talk`, `/taunt`, `/threaten`, `/violin`, `/whistle`, `/yawn`, `/cower`, `/gasp`, `/lol`, `/pray`, `/drink`, `/eat`, `/charge`, `/victory` | Emotes; with a target the text names it |
| `/afk [message]` · `/dnd [message]` | Status |
| `/played` · `/time` · `/logout` · `/camp` · `/quit` · `/exit` · `/reload` | Session |
| `/macro` · `/bind` · `/console` (GM only) | Tools |
| `/bug <text>` · `/ticket` | Support |
| `/stuck` | Teleports to the nearest graveyard after a 10 s channel; 30-minute cooldown |

## 6. Chat channels and colours

| Channel | Colour | Range |
|---|---|---|
| Say | White | 40 yards |
| Yell | Red | 300 yards |
| Emote | Orange | 40 yards |
| Whisper | Pink | Anywhere |
| Party | Light blue | Group |
| Raid, raid warning | Orange, large red centre-screen | Raid |
| Guild, officer | Green, dark green | Guild |
| General, LocalDefense | Peach | Zone |
| Trade, LookingForGroup | Peach | Capitals only; linked between the two capitals |
| Battleground | Orange | Match |
| System | Yellow | — |
| Combat log | Per event type, in its own tab | 60 yards |
| Creature say and yell | Pale yellow, red | 40 and 300 yards |

Item, spell and quest names can be shift-clicked into chat as links that open a tooltip when clicked.

## 7. First-session tutorial tips

One small panel each (380 × 132, lower right above the bag bar), shown once per character, with "Don't show tips" in options and on the panel itself. A tip is shown when its trigger condition first holds; it closes when acknowledged or after 20 seconds, and the next one due waits its turn. Which tips a character has seen is part of its interface settings: the client keeps it in its user folder by character id until interface settings are saved on the server with frame positions (T-M11-05). The tip's text names keys as they are bound.

| # | Trigger | Tip |
|---|---|---|
| 1 | First entering the world | Moving and looking |
| 2 | Within 20 yards of a quest giver with a quest to give ("!") | Talking to quest givers |
| 3 | A quest in the log | The quest log and tracker |
| 4 | A hostile target selected | Attacking and abilities |
| 5 | A loot window open | Looting; shift-click to loot all |
| 6 | A wearable item in the bags | Equipping; comparing with Shift |
| 7 | Dead | Releasing, running back, the spirit healer and its cost |
| 8 | Gaining a level | Class trainers and training costs |
| 9 | The bags-full error | Selling to vendors |
| 10 | Resting (in an inn or other rest area) | Binding the hearthstone; rested XP |
| 11 | Level 5 | Professions |
| 12 | First eyrie | Flight paths |
| 13 | Level 10 | Talent points |
| 14 | First group invite | Group loot rules and the 5-level XP rule |
| 15 | First mailbox | Mail and postage |
