# Art To-Do 4 — Spell, Particle & World Effects

[← Art Master To-Do](00-art-master-todo.md) · Prev: [Environments & Props](03-environments-props.md) · Next: [UI](05-ui.md)

Every visual effect needed from level 1 to 30. An effect row lists its **parts**: *Cast* (on the caster while casting), *Proj* (projectile), *Hit* (impact on target), *Aura* (persistent on a unit), *Area* (ground effect), *Weapon* (trail or glow). ☐ = not started.

## 1. Colour language and shared building blocks

| School / source | Colours | Motifs |
|---|---|---|
| Physical | White steel flash, red blood | Slash arcs, sparks, dust |
| Holy (Dawnflame) | Gold, warm white | Sunbursts, flame-halos, feathers of light |
| Nature (Verdant Choir) | Leaf green, amber | Leaves, vines, thorns, pollen, lightning in green-white |
| Arcane (the Lattice) | Violet, silver-blue | Stars, constellations, moon discs |
| Fire | Orange, ember red | Flame, cinders, smoke |
| Frost | Pale blue, white | Ice shards, mist |
| Shadow (the Hollow) | Purple-black, violet rim | Cracks, voids, inward-falling motes |
| Rage | Red | Steam, pulse |

| ID | Done | Shared block | Used for |
|---|---|---|---|
| VFX-S01 | ☐ | Cast-hand glows ×7 schools (ready / loop / release) | Every cast-time spell |
| VFX-S02 | ☐ | Generic projectile ×7 schools (bolt + trail) | Mob spells, fallbacks |
| VFX-S03 | ☐ | Generic impact ×7 schools (small / large) | All hits |
| VFX-S04 | ☐ | Generic buff-up swirl ×7 schools | Applying buffs |
| VFX-S05 | ☐ | Generic debuff cloud ×7 schools | Applying debuffs |
| VFX-S06 | ☐ | Heal sparkle (small / large) Holy and Nature | All heals |
| VFX-S07 | ☐ | Melee hit sparks, blood puff, block spark, parry clang, miss whoosh | All melee |
| VFX-S08 | ☐ | Weapon swing trails: 1H, 2H, dagger, polearm, staff | All weapon attacks |
| VFX-S09 | ☐ | Ground telegraph decals: circle, cone, line, ring, donut (enemy red, friendly blue-green) | Every avoidable ability |
| VFX-S10 | ☐ | State effects: stun stars, root vines, fear skull-wisp, sleep Z's, silence gag-glyph, slow frost-feet, daze swirl, bleed drip, poison bubbles, disease flies, burn smoulder, curse sigil, charm hearts-void, disarm flash, immune bubble, absorb shield, enrage red steam, knockback streak | All crowd control and status |
| VFX-S11 | ☐ | Interrupt / school-lockout burst | Shield Bash, Pummel, Rebuke |
| VFX-S12 | ☐ | Threat/taunt flash over target head | Taunts |

## 2. Fighter

| ID | Done | Ability | Parts |
|---|---|---|---|
| VFX-F01 | ☐ | Strike | Weapon: bright white trail; Hit: heavy spark |
| VFX-F02 | ☐ | Battle Cry | Cast: red shout-ring; Aura: brief red banner glow on party |
| VFX-F03 | ☐ | Charge | Cast: speed streak + dust trail; Hit: stun thud ring |
| VFX-F04 | ☐ | Rend | Weapon: red trail; Aura: blood drip on target |
| VFX-F05 | ☐ | Thunderous Stomp | Area: ground-crack shockwave ring, dust |
| VFX-F06 | ☐ | Hamstring | Weapon: low slash; Aura: red leg-mark slow |
| VFX-F07 | ☐ | Taunt | Cast: red finger-point streak; Hit: taunt flash |
| VFX-F08 | ☐ | Sunder | Hit: armour-crack shards; Aura: stacking crack icon over target (1–5) |
| VFX-F09 | ☐ | Bloodletting | Cast: self-cut blood spray, red steam |
| VFX-F10 | ☐ | Opening | Weapon: quick white counter-flash |
| VFX-F11 | ☐ | Shield Bash | Weapon: shield shove flash; Hit: interrupt burst |
| VFX-F12 | ☐ | Demoralizing Roar | Cast: dark red roar-cone; Aura: drooping mark on enemies |
| VFX-F13 | ☐ | Retaliate | Weapon: gold-white riposte arc |
| VFX-F14 | ☐ | Shield Block | Aura: shield rim glow; Hit: big block spark |
| VFX-F15 | ☐ | Mocking Strike | Hit: taunt flash + small laugh-glyph |
| VFX-F16 | ☐ | Disarm | Hit: weapon-spin flash; Aura: disarm icon |
| VFX-F17 | ☐ | Cleave | Weapon: wide double arc |
| VFX-F18 | ☐ | Intimidating Shout | Cast: black-red shout ring; Aura: fear on targets |
| VFX-F19 | ☐ | Pummel | Hit: fist burst + interrupt |
| VFX-F20 | ☐ | Execute | Weapon: red overhead trail; Hit: large blood burst |
| VFX-F21 | ☐ | Challenging Shout | Cast: wide red ring; Hit: taunt flash on all |
| VFX-F22 | ☐ | Whirlwind | Weapon: full 360° spinning trail, dust ring |
| VFX-F23 | ☐ | Shield Wall | Aura: stone-grey shield dome plates |
| VFX-F24 | ☐ | Slam | Cast: weapon wind-up glow; Hit: ground-shaking spark |
| VFX-F25 | ☐ | Recklessness | Aura: red flame outline, eyes glow |
| VFX-F26 | ☐ | Unbroken | Aura: red steam bursts, chain-break flash |
| VFX-F27 | ☐ | Stances ×3 | Brief flourish: Battle (white), Guard (steel-blue), Reckless (red) |
| VFX-F28 | ☐ | Last Stand (talent) | Aura: green-gold heartbeat pulse |
| VFX-F29 | ☐ | Concussive Blow | Hit: gold concussion ring, stun |
| VFX-F30 | ☐ | Shield Slam | Weapon: shield arc; Hit: dispel shatter |
| VFX-F31 | ☐ | Piercing Howl | Cast: sharp white howl ring; Aura: daze |
| VFX-F32 | ☐ | Red Mist | Aura: red haze clinging to the Fighter |
| VFX-F33 | ☐ | Bloodreave | Weapon: crimson trail; Aura: small red heal motes on hits |
| VFX-F34 | ☐ | Sweeping Strikes | Aura: twin ghost-blade orbit; Weapon: echo arc on second target |
| VFX-F35 | ☐ | Grievous Strike | Weapon: dark red trail; Aura: wound mark (healing reduced) |
| VFX-F36 | ☐ | Passive procs: Deep Wounds bleed, Enrage flare, Flurry speed lines, Blood Craze regen, Unbridled Wrath spark, Mace stun, Sword extra-swing ghost | 7 small effects |

## 3. Cleric

| ID | Done | Ability | Parts |
|---|---|---|---|
| VFX-C01 | ☐ | Oath of Radiance | Cast: weapon raised, gold flare; Weapon: steady gold glow; Hit: small sun-spark per swing |
| VFX-C02 | ☐ | Mending Light | Cast: two-hand gold gather; Hit: descending light column + sparkle |
| VFX-C03 | ☐ | Litany of Resolve | Aura: faint gold shield glyph under party feet |
| VFX-C04 | ☐ | Verdict (per Oath ×6) | Proj: thrown hammer of light; Hit: variant burst — Radiance (sunburst), Zealot (red-gold brand on target), Justice (chains), Light (soft glow mark), Command (large hammer strike), and base |
| VFX-C05 | ☐ | Benediction of Might | Hit: gold fist sigil rising |
| VFX-C06 | ☐ | Dawnstrike | Weapon: gold-white trail; Hit: flare with small rays |
| VFX-C07 | ☐ | Divine Ward | Aura: full golden bubble with rotating glyphs |
| VFX-C08 | ☐ | Oath of the Zealot | Weapon: red-gold flame glow |
| VFX-C09 | ☐ | Hammer of Rebuke | Proj: spinning hammer of light; Hit: stun burst |
| VFX-C10 | ☐ | Purify | Hit: white-gold wash rising, debuff motes fall away |
| VFX-C11 | ☐ | Dawn's Mercy | Cast: hands of light; Hit: huge sunburst and feathers |
| VFX-C12 | ☐ | Benediction of Protection | Aura: gold bubble (thinner than Ward) on ally |
| VFX-C13 | ☐ | Raise the Fallen | Cast: kneeling channel, light pillar on corpse; Hit: rising motes, ghost-to-body |
| VFX-C14 | ☐ | Benediction of Wisdom | Hit: blue-gold open-book sigil |
| VFX-C15 | ☐ | Challenge of Faith | Proj: gold challenge-ray; Hit: taunt flash |
| VFX-C16 | ☐ | Righteous Bulwark | Aura: faint flame-halo behind head |
| VFX-C17 | ☐ | Litany of Thorns | Aura: gold spike ring glyph; Hit: small Holy spark on attackers |
| VFX-C18 | ☐ | Benediction of Freedom | Aura: gold wing-flickers at feet; breaks snare effects |
| VFX-C19 | ☐ | Flash of Dawn | Cast: quick one-hand flash; Hit: small light pop |
| VFX-C20 | ☐ | Hallowed Ground | Area: 8 yd golden consecrated floor with slow flame-glyphs, 8 s |
| VFX-C21 | ☐ | Exorcise | Proj: lance of light; Hit: burn-away burst on undead |
| VFX-C22 | ☐ | Sense Undead | UI/minimap only (see UI) |
| VFX-C23 | ☐ | Litany of Focus | Aura: calm blue-gold ring glyph |
| VFX-C24 | ☐ | Oath of Justice | Weapon: white-gold chain glints; Hit: stun on proc |
| VFX-C25 | ☐ | Rebuke Undead | Cast: raised symbol flash; Aura: fear + gold burn on undead |
| VFX-C26 | ☐ | Benediction of Salvation | Hit: soft white dove-light sigil |
| VFX-C27 | ☐ | Oath of Light | Weapon: soft white glow; Hit: heal motes to self |
| VFX-C28 | ☐ | Benediction of Kings (talent) | Hit: gold crown sigil |
| VFX-C29 | ☐ | Shield of Dawn | Aura: sun-disc on shield face; Hit: Holy flash on each block |
| VFX-C30 | ☐ | Dawnbreaker Shield | Proj: spinning radiant shield bouncing between 3 targets; Hit: daze flash |
| VFX-C31 | ☐ | Divine Favor | Aura: brief gold glow on hands (next heal) |
| VFX-C32 | ☐ | Light's Grace | Aura: lingering light on healed target (6 s) |
| VFX-C33 | ☐ | Dawnshock | Proj: instant gold bolt; Hit: heal or damage variant |
| VFX-C34 | ☐ | Oath of Command | Weapon: bright gold-white glow; Hit: Holy second-strike flash |
| VFX-C35 | ☐ | Litany of Sanctity | Aura: radiant sun glyph |
| VFX-C36 | ☐ | Rebuke | Hit: gold interrupt slap |
| VFX-C37 | ☐ | Avenging Dawn | Aura: wings of light, gold eyes, ground sun-ring |
| VFX-C38 | ☐ | Passive procs: Redoubt, Requital extra-attack, Vengeance flare, Illumination mana return, Eye for an Eye reflect | 5 small effects |
| VFX-C39 | ☐ | Forbearance | Aura: dim grey halo icon |

## 4. Druid

| ID | Done | Ability | Parts |
|---|---|---|---|
| VFX-D01 | ☐ | Thornlash | Cast: green hand-swirl; Proj: whipping thorn-vine bolt; Hit: thorn burst and leaves |
| VFX-D02 | ☐ | Mend | Cast: green gather; Hit: rising leaves and green light |
| VFX-D03 | ☐ | Gift of the Grove | Hit: leaf-crown sigil descending |
| VFX-D04 | ☐ | Starbrand | Hit: instant falling star-spark; Aura: violet brand mark that pulses per tick |
| VFX-D05 | ☐ | Renewal | Aura: slow green leaf spiral around target, 12 s |
| VFX-D06 | ☐ | Briarskin | Aura: faint thorn outline; Hit: thorn prick on attackers |
| VFX-D07 | ☐ | Rootgrasp | Area: roots erupt and wrap target legs; breaking animation |
| VFX-D08 | ☐ | Overgrowth | Cast: two-hand bloom; Hit: burst of flowers; Aura: small blossoms orbit |
| VFX-D09 | ☐ | Cleanse Toxin | Hit: green wash drawing out purple bubbles |
| VFX-D10 | ☐ | Glimmer Mark | Aura: sparkling silver outline on target |
| VFX-D11 | ☐ | Stinging Swarm | Proj: insect cloud flies to target; Aura: buzzing swarm |
| VFX-D12 | ☐ | Lull Beast | Cast: soft green-blue wave; Aura: sleep mist and Z's |
| VFX-D13 | ☐ | Astral Lance | Cast: long two-hand star-gather (3.5 s, constellation forms); Proj: bright violet-white lance from above; Hit: star-burst |
| VFX-D15 | ☐ | Reawaken | Cast: seed planted; Hit: sapling of light grows from corpse, burst of petals |
| VFX-D16 | ☐ | Lift Curse | Hit: silver wash breaking a dark sigil |
| VFX-D17 | ☐ | Barkward | Aura: bark plates over skin |
| VFX-D18 | ☐ | Squall | Area: 10 yd storm — dark cloud, rain, green-white lightning strikes, wind streaks, 10 s |
| VFX-D19 | ☐ | Wellspring | Hit: blue-green water-of-light fountain on target; Aura: droplets rising |
| VFX-D20 | ☐ | Stillwater | Cast: channel with arms raised; Area: calm rippling pool of green light under the party, gentle rain of motes |
| VFX-D21 | ☐ | Blossom (talent) | Aura: 1–3 flower buds on target; Hit: bloom burst when it expires |
| VFX-D22 | ☐ | Nature's Swiftness | Aura: green wind-swirl on hands |
| VFX-D23 | ☐ | Harvest | Hit: HoT leaves sucked inward then burst of gold-green |
| VFX-D24 | ☐ | Nature's Grasp | Aura: vine bracelet on Druid; triggers Rootgrasp |
| VFX-D25 | ☐ | Call Lightning | Cast: raised hand, cloud forms; Proj: green-white bolt from sky then chain arcs to 2 more; Hit: scorch |
| VFX-D26 | ☐ | Heart of the Storm | Aura: faint storm-ring glyph |
| VFX-D27 | ☐ | Starfall | Area: 4 waves of falling stars on up to 3 targets, violet trails |
| VFX-D28 | ☐ | Astral Convergence | Aura: orbiting constellation, moon disc behind the Druid |
| VFX-D29 | ☐ | Passive procs: Seedling end-heal, Evergreen double tick, Static Charge daze, Eye of the Storm clearcast glow, Astral Alignment star-glint, Celestial Focus stun | 6 small effects |

## 5. Items, consumables, professions

| ID | Done | Effect | Notes |
|---|---|---|---|
| VFX-I01 | ☐ | Potion drink (red, blue, purple, green, orange) | 5 tints |
| VFX-I02 | ☐ | Elixir / scroll buff-up | 2 |
| VFX-I03 | ☐ | Eating / drinking loop (crumbs, droplets); Well Fed pop | 3 |
| VFX-I04 | ☐ | Bandage channel | 1 |
| VFX-I05 | ☐ | Weapon enchant glows: Striking, Impact, Hollowbane, Dawnfire | 4 |
| VFX-I06 | ☐ | Sharpening / oil sheen | 3 |
| VFX-I07 | ☐ | Engineering: dynamite fuse + explosion ×4 sizes, bomb stun, target dummy pop, clockwork ram charge + blast, resuscitator shock, parachute | 10 |
| VFX-I08 | ☐ | Protection-potion absorb shells (Fire, Frost, Shadow) | 3 |
| VFX-I09 | ☐ | Swiftness speed lines; water-breathing bubbles; Purification wash | 3 |
| VFX-I10 | ☐ | Trinket and proc effects (≈ 20 named trinkets): generic "use" flash ×7 schools + 6 bespoke (Hollowed Heart, Acorn of the First Oak, Heart of the Cinder Wyrm, Eye of the Maw, Vitrea's Lens reflect, Shard of the Hollow Crown) | 13 |
| VFX-I11 | ☐ | Chance-on-hit weapon procs: Fire, Shadow, Nature, life-steal | 4 |
| VFX-I12 | ☐ | Gathering: mining sparks and chips, herb pick sparkle, skinning, node glint, fishing splash + bobber ripple | 6 |
| VFX-I13 | ☐ | Crafting: anvil sparks, forge fire, alchemy bubbling, enchanting rune-circle, disenchant dissolve, tailoring thread, cooking steam, engineering sparks | 8 |
| VFX-I14 | ☐ | Hearthstone channel + teleport | 2 |
| VFX-I15 | ☐ | Mount summon puff; epic-mount hungry indicator (reserved) | 2 |

## 6. Creature ability library

Every mob ability in the zone tables maps to one of these reusable effects.

| ID | Done | Effect | Used by (examples) |
|---|---|---|---|
| VFX-M01 | ☐ | Bite / claw / gore swipes (3) | All beasts |
| VFX-M02 | ☐ | Charge dust line | Boars, rams, stags |
| VFX-M03 | ☐ | Howl / roar / screech rings (3) | Canines, bears, harpies, bats, owls |
| VFX-M04 | ☐ | Web spit, web root, web drop-line | Spiders |
| VFX-M05 | ☐ | Poison spit and venom cloud | Spiders, scorpions, beetles |
| VFX-M06 | ☐ | Thrown objects: rock, pick, dynamite, net, bola, torch, coal, spear, satchel, boulder, pistol shot, arrow, crossbow bolt | Humanoids (13 projectiles) |
| VFX-M07 | ☐ | Fire: Hot Wax, Cinder Bolt, Fireball, Pyroblast, Flamestrike, Flame Ward, Flame Ring, ground fire patch, Searing Brand DoT | Cultists, mages |
| VFX-M08 | ☐ | Slag: Slag Bolt, Slag Spit pool, Slag Wave line, Molten Armor/Weapon, slag death-pool | Slagborn, elementals |
| VFX-M09 | ☐ | Frost: Frost Nip, Mist Bolt, Frost Breath cone, Chilling Touch | Sprites, whelps, wights |
| VFX-M10 | ☐ | Shadow/Hollow: Hollow Touch, Hollow Whisper DoT, Shadow Bolt, Bone Bolt, Life Drain beam, Mana Burn, Empty Stare | Hollowed, undead |
| VFX-M11 | ☐ | Arcane: Arcane Zap, Aether Lance, Arcane Cleave, Blink | Wisps, magisters, sentinels |
| VFX-M12 | ☐ | Nature (enemy): Lightning Bolt, Entangle, Spore Puff, Bog Bolt, Thorn Hide reflect | Hexers, shamblers, hags |
| VFX-M13 | ☐ | Curses and hexes (3 sigils): weakness, slowness, fog/−hit | Hexers, hags, witches |
| VFX-M14 | ☐ | Healing (enemy): Healing Tide, Stitch Flesh, Cauterize, Mend Mistress | Casters |
| VFX-M15 | ☐ | Petrifying Gaze beam + stone-skin on victim | Skinks, gazers |
| VFX-M16 | ☐ | Stone Form / Shell / Bark Skin hardening | Gargoyles, snappers, treants |
| VFX-M17 | ☐ | Burrow in / burst out, constrict coils | Worms, wyrms, borers |
| VFX-M18 | ☐ | Stealth shimmer in/out, ambush flash | Cats, cutthroats, lurkers |
| VFX-M19 | ☐ | Summon / call-for-help glyph; raise-corpse green fire | Many |
| VFX-M20 | ☐ | Explosions: Powderkeg death, Cinderwight death, Shatter, Overload | Suicide/on-death mobs (3 s warning ring) |
| VFX-M21 | ☐ | Enrage / frenzy / Bloodlust on allies | Many |
| VFX-M22 | ☐ | Ooze split and acid splash; Corrode | Oozes |
| VFX-M23 | ☐ | Breath weapons: fire cone, frost cone, grit cone | Drakes, hounds, wyrms |
| VFX-M24 | ☐ | Machine: whirling blades, rail charge sparks, steam vent, break-down smoke | Constructs |
| VFX-M25 | ☐ | Spectre: phase out/in, wail ring, charm beckon, silence shriek | Spectres |
| VFX-M26 | ☐ | Rune of Fire ground trap; Lay Charge fuse bomb | Runesmiths, Blastwrights |
| VFX-M27 | ☐ | Dust Devil, water/mist pet swirl | Hexwrights |
| VFX-M28 | ☐ | Flee indicator, evade/reset shimmer, elite/rare ground ring | All |

## 7. Boss and encounter effects

| ID | Done | Encounter | Bespoke effects |
|---|---|---|---|
| VFX-B01 | ☐ | T1/T2 act bosses (Morrow, Sootbeard, Vane, Blackmatch, Soot, Deepdrill) | Searing Brand; Kindle enrage; Fuse Line (travelling fire line); Satchel Toss; kiln flame-jet pattern; Drill Sweep + Steam Vent + valve shut-off |
| VFX-B02 | ☐ | Urgoth, Hedda, Ashgrave | Earthshaker; boulder throw; Rune Circle (lit/unlit runes); Brand of Obedience; Flame Ring; **chest-split shard reveal**, Hollow Pulse; shard dissolve |
| VFX-B03 | ☐ | Gallowmere Crypts | Grave-plot open; Six Feet Under pull; Dirge stacking notes; Loose Stitch detach; Discord mark; Wail + Circle of Candles (lit/snuffed); Sorrow HoT; Sermon of Ash cone; Ashen Nova; self-brand phase change |
| VFX-B04 | ☐ | The Slagworks | Double Shift enrage wave; ledger throw; Engulf platform sink; cooling-grate steam + crust hardening; Stoke beam; Bellows Blast; Fetch drag; Hammer of the Forge + Ringing; Quench splash; Sparks pulse; Shard Resonance expanding rings; slag flood stages |
| VFX-B05 | ☐ | Hollowspire Keep | Portcullis slam; glowing key throw; toast shockwave; four course themes; Overdue ink-chase; Redact ink pools; Index glowing shelf + school-immunity shell ×4; Oath of Hollow + dark Verdict; Unhallowed Ground; Hollow Ward; three Shard beams (Ambition fire sweep, Memory mirror-copy, Hunger drain tether); Imperial Decree glyphs ×3; Courtly Step; Crown's Shadow pulse; **Crown assembly and floor-split finale** |
| VFX-B06 | ☐ | The Hollow Throne | Ward-pylon cracks (4 states) + room collapse; Seismic Slam; Rockfall lanes; Ward Pulse; Beckon; Chain Squall; Downdraft pull + Crush; Harmony heal-tether; Ballista Volley lanes; Entomb; falling slabs/arches; Undermine ledge collapse; Grit Breath; egg hatch; swallow + spit-out; Aether Polarity (Flow/Ebb marks, explosion); Recitation cast-bar aura; Hollow Lance; Mirror of Years; Imperial Edict ×2; kneeling courtiers; five Crown-shard burdens (5 auras + tethers); Hollow Echo; collapse rings; Earthen Wrath; Bury; **Crown shatter finale** |
| VFX-B07 | ☐ | Grimroot | Root Lash; Gallows Vines hoist; Rotfall circles; sapling heal-tether; bark split + Dying Rage |
| VFX-B08 | ☐ | Pyrraxis | Flame Breath; Tail Sweep; Wing Buffet; strafing fire lines; Ashfall DoT + geyser steam cleanse; plateau burn-in |
| VFX-B09 | ☐ | Gorrath | Maw inhale vortex; coil eruptions ×4; Landslide; Dust Plume; burrow-away escape |
| VFX-B10 | ☐ | Other elites (Wickerman burn, Deepseam Horror, Barrow-King raise + Grave Chill, Morrigan pistol volley + powder kegs, Brannoch, Behemoth rubble prison) | 10 |

## 8. World, environment and feedback effects

| ID | Done | Effect |
|---|---|---|
| VFX-W01 | ☐ | Level-up burst (gold pillar, ring, sparkles) |
| VFX-W02 | ☐ | Quest markers: available "!" (gold), in-progress "?" (grey), complete "?" (gold), repeatable (blue), class quest (class colour), low-level (dim) |
| VFX-W03 | ☐ | Quest object sparkle; lootable corpse sparkle; chest glint |
| VFX-W04 | ☐ | Loot fountain for rare+ drops (blue, purple beams) |
| VFX-W05 | ☐ | Selection circles (friendly green, neutral yellow, hostile red, player blue), target arrow, raid target icons ×8 above heads |
| VFX-W06 | ☐ | Death: body fade, ghost-world desaturation post-effect, spirit-healer glow, resurrection burst |
| VFX-W07 | ☐ | Rest state Zzz, AFK tag, PvP flag icon, duel flag plant + countdown 3-2-1, duel win banner |
| VFX-W08 | ☐ | Weather: light rain, heavy rain, snow light/heavy, fog banks, ground mist, ashfall, ash-storm, dust-storm, falling leaves (Russetwood, 3 colours), wind streaks, aurora (Embercrag night) |
| VFX-W09 | ☐ | Ambient: fireflies, pollen, dust motes in light-shafts, cave drips, chimney smoke, forge sparks, torch/brazier/lantern/candle flames, campfire, embers over lava, sulfur steam, geysers, waterfall mist, glowcap spores, crystal glints, will-o'-wisps, crows scatter |
| VFX-W10 | ☐ | Water and liquid: ripples, footstep splashes, swim wake, lava bubbles, slag flow, bog bubbles |
| VFX-W11 | ☐ | Footsteps: dust, snow prints, leaf scatter, mud splats (4) |
| VFX-W12 | ☐ | Fire states: burning building, burning field, burning forest, douse steam |
| VFX-W13 | ☐ | Teleports: instance portal swirl, hearth, battleground port, summon (meeting stone) |
| VFX-W14 | ☐ | Travel: eagle take-off feathers, ship wake and sail flutter, mine-cart sparks, rope-lift |
| VFX-W15 | ☐ | PvP: Crown relic glow + bearer aura (growing with stacks), hill control ring ×3 team colours + contested, shrine capture beams ×3, team-colour player outline, Pitmaster's Chest spawn beam, free-for-all red rim on arena floor |
| VFX-W16 | ☐ | World-boss spawn omens: unnatural fog thickening (Veilmoor), ash-storm (Cinderfall), dust-storm (Riftlands) |
| VFX-W17 | ☐ | Story world-states: Old Forge relight, Brandspire beacon out, Tor Vael storm clearing after the raid |
| VFX-W18 | ☐ | Post-processing: per-zone colour grade (11), underwater tint, low-health vignette, stun blur, ghost desaturation, drunk wobble |

## 9. Totals for this document

| Category | Effects |
|---|---|
| Shared building blocks | 12 groups ≈ 110 pieces |
| Fighter | 36 rows ≈ 50 effects |
| Cleric | 39 rows ≈ 55 effects |
| Druid | 29 rows ≈ 45 effects |
| Items, consumables, professions | ≈ 85 |
| Creature ability library | 28 groups ≈ 110 effects |
| Boss and encounter effects | ≈ 150 |
| World, environment, feedback | ≈ 120 |
| **Total** | **≈ 725 effects** |
