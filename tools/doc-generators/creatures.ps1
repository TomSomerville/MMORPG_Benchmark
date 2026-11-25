param([string]$Root)
# Documentation helper only: expands the zone creature tables into full stat blocks, ability numbers and loot tables.
$en = [string][char]0x2013; $x = [string][char]0x00D7; $larr = [string][char]0x2190; $md = [string][char]0x00B7; $box = [string][char]0x2610; $mdash = [string][char]0x2014; $minus = [string][char]0x2212
$enc = New-Object System.Text.UTF8Encoding($false)
$tpl = @(@(1, 42, 2.0, 20), @(5, 102, 5.5, 130), @(10, 198, 11, 400), @(15, 328, 17, 760), @(20, 484, 24, 1000), @(25, 664, 31, 1260), @(30, 896, 40, 1500), @(35, 1150, 50, 1750))
function Lerp([double]$L, [int]$col) {
  for ($i = 0; $i -lt $tpl.Count - 1; $i++) {
    if ($L -le $tpl[$i + 1][0]) { $a = $tpl[$i]; $b = $tpl[$i + 1]; return $a[$col] + ($b[$col] - $a[$col]) * ($L - $a[0]) / ($b[0] - $a[0]) }
  }
  return $tpl[-1][$col]
}
function Speed($type) {
  if ($type -match 'Giant') { return 2.6 } elseif ($type -match 'Construct|Plant') { return 2.4 } elseif ($type -match 'Elemental') { return 2.2 }
  elseif ($type -match 'cat|bird|spider|bat|harpy') { return 1.8 } else { return 2.0 }
}
function School($s) {
  if ($s -match 'fire|flame|ember|slag|torch|wax|cinder|pyro|kiln|scorch|magma|brand|burn|coal|molten') { return 'Fire' }
  if ($s -match 'frost|ice|chill|rime') { return 'Frost' }
  if ($s -match 'shadow|hollow|bone|hex|bog|curse|drain') { return 'Shadow' }
  if ($s -match 'arcane|aether|shard|crystal|zap') { return 'Arcane' }
  if ($s -match 'venom|poison|thorn|lightning|acid|spore|blight|water|tide|dust|web') { return 'Nature' }
  return 'Physical'
}
function Dur($s, $def) { $m = [regex]::Match($s, '(\d+(\.\d+)?) s'); if ($m.Success) { return $m.Groups[1].Value } else { return $def } }
function Ability($raw, [double]$L, [double]$dps, [double]$spd, [double]$hp, $caster) {
  $name = $raw; $note = ''
  $m = [regex]::Match($raw, '^(.*?)\s*\((.*)\)\s*$'); if ($m.Success) { $name = $m.Groups[1].Value.Trim(); $note = $m.Groups[2].Value.Trim() }
  $s = ($name + ' ' + $note).ToLower(); $swing = [math]::Round($dps * $spd); $sch = School $s
  $sd = $(if ($caster) { $dps * 2.2 } else { $dps * 1.3 })
  if ($s -match '^flees') { return @('Flee', 'Movement', 'Runs at 15% health for 8 s and alerts allies within 30 yd') }
  if ($s -match 'resist|immune|vulnerab|weak to') { return @($name, 'Trait', $(if ($note) { $note } else { $name })) }
  if ($s -match 'heal|mend|renewal|regrow|regenerat|grog|cauterize') { return @($name, 'Heal', "Heals $([math]::Round($hp * 0.12)) (12% of max health); 2.0 s cast, interruptible; cooldown 20 s; used below 50% health") }
  if ($s -match 'summon|calls|raises|sic |kindle corpse|hatch') { return @($name, 'Summon', "$(if ($note) { $note } else { 'Calls 1 ally of the same family within 30 yd' }); once per fight unless a cooldown is given") }
  if ($s -match 'stun|knockdown|incapacitate|gaze|petrif') { $d = Dur $note '2'; return @($name, 'Control', "Stun/incapacitate $d s; deals $swing $sch; $(if ($s -match 'cast|gaze') { '2.0 s cast, avoid by facing away or interrupting; ' })cooldown 20 s") }
  if ($s -match 'root|web|net\b|snare|entangle|bola|trap|prison|constrict') { $d = Dur $note '3'; return @($name, 'Root', "Roots $d s; range 20 yd; cooldown 20 s$(if ($s -match 'constrict') { "; $([math]::Round($L * 2 + 4)) Physical per 2 s while held" })") }
  if ($s -match 'silence|interrupt|screech|chirp|dust\b|reproach') { $d = Dur $note '3'; return @($name, 'Silence', "Silences or interrupts for $d s; range 20 yd; cooldown 25 s") }
  if ($s -match 'fear|baying') { $d = Dur $note '2'; return @($name, 'Fear', "Fear $d s; 8 yd around the creature; cooldown 30 s") }
  if ($s -match 'pull|lasso|drag|lure|beckon|charm|grip') { $d = Dur $note '0'; return @($name, 'Pull or charm', "$(if ($s -match 'charm|beckon') { "Charms $d s; breaks on damage" } else { 'Pulls the target to the creature' }); range 25 yd; cooldown 20 s") }
  if ($s -match 'drain|leech|mana burn|hollow touch|life drain') { return @($name, 'Drain', "$([math]::Round($L * 2 + 6)) $sch per 2 s for 6 s (channel); $(if ($s -match 'mana') { 'burns the same amount of mana' } else { 'heals the creature for the damage dealt' }); cooldown 18 s") }
  if ($s -match 'bleed|dot\b|poison|venom|disease|rend|rot\b|sting|burning|brand|corrode') { $tot = [math]::Round($L * 4 + 6); return @($name, 'Damage over time', "$tot $(if ($sch -eq 'Physical' -and $s -match 'poison|venom|sting') { 'Nature' } else { $sch }) over 12 s (4 ticks)$(if ($s -match 'stack') { ', stacks to 5' }); applied on hit, cooldown 15 s$(if ($note) { "; $note" })") }
  if ($s -match 'slow|hamstring|nip\b|grasp|splash') { return @($name, 'Slow', "Slows movement $(if ($note -match '(\d+)%') { $matches[1] } else { '40' })% for 6 s; deals $([math]::Round($swing * 0.6)) $sch; cooldown 12 s") }
  if ($s -match 'bolt|zap|spit|fireball|lance|shoot|throw|volley|toss|lightning|pyroblast|breath|wave|flamestrike|firebrand|pistol|lash|shriek') {
    $ct = [double](Dur $note '2.0'); if ($ct -gt 5) { $ct = 2.0 }; $dmg = [math]::Round($sd * $ct)
    $aoe = $(if ($s -match 'breath|wave|volley|flamestrike|cone|line') { '; hits all targets in the area' } else { '' })
    return @($name, 'Ranged or spell', "$([math]::Round($dmg * 0.85))$en$([math]::Round($dmg * 1.15)) $sch; $ct s cast; range 30 yd$aoe$(if ($s -match 'dodge') { '; aimed at the ground, avoidable' })")
  }
  if ($s -match 'enrage|frenzy|bloodlust|stoke|howl|applause|molten weapon|whistle|kindle|pack') { return @($name, 'Buff', "$(if ($s -match 'howl|applause|stoke|bloodlust|molten|whistle|pack') { 'Allies within 15 yd' } else { 'Self' }): +25% damage$(if ($s -match 'enrage|frenzy|kindle') { ' and +30% attack speed' }) for 10 s$(if ($note -match '(\d+)%') { "; triggers at $($matches[1])% health" } else { '; cooldown 30 s' })") }
  if ($s -match 'charge|pounce|dive|swoop|dash|ambush|stealth|burrow|backstab|silent') { return @($name, 'Opener', "$([math]::Round($swing * 1.5)) Physical on the first hit$(if ($s -match 'stealth|ambush|burrow|silent|backstab') { '; the creature is hidden until within 8 yd' } else { '; closes from 8 to 25 yd' })$(if ($note) { "; $note" })") }
  if ($s -match 'cleave|whirl|flail|sweep|swipe|stomp|slam|smash|aoe|eruption|shatter|explod|blades|pulse|ring') { return @($name, 'Area attack', "$([math]::Round($swing * 0.8)) $sch to all enemies within $(if ($s -match 'death|explod|shatter') { '8 yd, on death' } else { '5 yd' })$(if ($s -match 'telegraph|warning|eruption') { '; 2 s warning' }); cooldown 12 s$(if ($note) { "; $note" })") }
  if ($s -match 'shield|block|wall|shell|bark|stone form|defensive|ward|oath|hold|refract|glass hide|thorn hide') { return @($name, 'Defensive', "$(if ($note) { $note } else { "$minus" + '50% damage taken' }); lasts 6 s unless stated; cooldown 30 s") }
  if ($s -match 'curse|hex|armor|sunder|gnaw|spray|stare|whisper|cloud|puff|weakness|fog') { return @($name, 'Debuff', "$(if ($note) { $note } else { "$minus" + '10% armor' }); lasts 15 s; cooldown 20 s") }
  if ($s -match 'blink|flicker|flee|fade|phase|sprint|disengage|tail') { return @($name, 'Movement', "$(if ($note) { $note } else { 'Teleports or leaps 10 yd and resets its swing' }); cooldown 15 s") }
  return @($name, 'Strike', "$([math]::Round($swing * 1.2)) Physical; cooldown 8 s$(if ($note) { "; $note" })")
}
function SplitTop($s) {
  $out = @(); $depth = 0; $cur = ''
  foreach ($ch in $s.ToCharArray()) {
    if ($ch -eq '(') { $depth++ } elseif ($ch -eq ')') { $depth-- }
    if (($ch -eq ',' -or $ch -eq ';') -and $depth -eq 0) { if ($cur.Trim()) { $out += $cur.Trim() }; $cur = '' } else { $cur += $ch }
  }
  if ($cur.Trim()) { $out += $cur.Trim() }
  return $out
}
function Cloth([int]$L) { if ($L -le 11) { return 'Linen Cloth 35%' } elseif ($L -le 14) { return 'Linen Cloth 20%, Wool Cloth 20%' } elseif ($L -le 21) { return 'Wool Cloth 35%' } elseif ($L -le 26) { return 'Wool Cloth 15%, Silk Cloth 25%' } else { return 'Silk Cloth 35%' } }
function Leather([int]$L) { if ($L -le 2) { return 'Ruined Leather Scraps' } elseif ($L -le 10) { return 'Ruined Leather Scraps or Light Leather' } elseif ($L -le 16) { return 'Light Leather (Light Hide 10%)' } elseif ($L -le 24) { return 'Medium Leather (Medium Hide 10%)' } else { return 'Heavy Leather (Heavy Hide 10%)' } }
function Loot($type, [int]$lo, [int]$hi, $drops, $mult) {
  $parts = @()
  $dl = @(SplitTop $drops | Where-Object { $_ -and $_ -notmatch '^(Linen|Wool|Silk|coin|copper coins|Wool \(rare\)|Silk \(rare\)|(Light|Medium|Heavy)(/Medium|/Heavy)? (Leather|Hide)|Light Leather/Hides|Medium Leather|pelts|scraps)$' })
  if ($type -match 'Humanoid|Giant') { $parts += "Coin $($lo * 3 * $mult)$en$($hi * 9 * $mult)c (100%)"; $parts += (Cloth $hi); $parts += 'Grey junk 70%' }
  elseif ($type -match 'Undead') { $parts += "Coin $([math]::Round($lo * 1.5 * $mult))$en$([math]::Round($hi * 4.5 * $mult))c (60%)"; $parts += ((Cloth $hi) -replace '35%', '25%'); $parts += 'Grey junk 70%' }
  elseif ($type -match 'Beast|Dragonkin') { $parts += 'No coin'; $parts += 'Grey junk 75%'; $parts += "Skinning: $(Leather $hi)" }
  elseif ($type -match 'Elemental') { $parts += 'No coin'; $parts += 'Elemental grey 60%' }
  elseif ($type -match 'Construct') { $parts += 'No coin'; $parts += 'Scrap grey 65%' }
  elseif ($type -match 'Plant') { $parts += 'No coin'; $parts += 'Plant grey 65%'; $parts += 'Herbalism on corpse where the zone doc says so' }
  else { $parts += 'No coin'; $parts += 'Slime grey 65%' }
  $n = 0
  foreach ($d in $dl) { $n++; $rate = $(if ($d -match 'rare') { '3%' } elseif ($d -match 'quest|\(named\)') { 'quest rate' } elseif ($n -eq 1) { '40%' } else { '25%' }); $parts += "$(($d -replace '\s*\((rare|quest|named)\)', '').Trim()) $rate" }
  $parts += 'World table'
  return ($parts -join " $md ")
}
$zones = @{ 't1-brightmead-vale' = 'BM'; 't1-embercrag-hollow' = 'EC'; 't2-harrowfield' = 'HF'; 't2-russetwood' = 'RW'; 't2-stonewake-dale' = 'ST'; 't2-stoneheart-deeps' = 'SD'; 't3-thornwick-marches' = 'TM'; 't3-ironroot-highlands' = 'IR'; 't4-cinderfall-barrens' = 'CF'; 't4-riftlands' = 'RL'; 't4-veilmoor' = 'VM' }
$extra = @{ 'HF' = @(@('Paymaster Grice', 8, 'Humanoid', 'named')); 'RW' = @(@('Odo Ketch', 8, 'Humanoid', 'named')); 'ST' = @(@('Chief Gnarr', 8, 'Humanoid', 'named')); 'SD' = @(@('Shard-Chief Krakk', 8, 'Humanoid', 'named')); 'TM' = @(@('Preceptor Hask', 14, 'Humanoid (caster)', 'named')); 'IR' = @(@('Runner Vask', 15, 'Humanoid', 'named')) }
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine('# Creature Data ' + $mdash + ' stat blocks, abilities and loot')
[void]$sb.AppendLine('')
[void]$sb.AppendLine($larr + ' [Data Index](00-data-index.md) ' + $md + ' Rules: [NPC AI & World](../02-systems/npc-ai-and-world.md) ' + $md + ' [Items & Loot](../02-systems/items-and-loot.md#7-loot-generation)')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('Generated from the creature tables in the zone documents using the rules in the [Data Index](00-data-index.md#2-creature-rules). **Do not edit by hand**: change the zone table or the rule, then regenerate. Health and damage are given at the lowest and highest level of the creature''s range. Ability numbers are at the highest level.')
[void]$sb.AppendLine('')
$totN = 0; $totNamed = 0; $totAb = 0
foreach ($f in (Get-ChildItem (Join-Path $Root 'docs\05-zones') -Filter 't*.md' | Sort-Object Name)) {
  $code = $zones[$f.BaseName]; $lines = [IO.File]::ReadAllLines($f.FullName)
  $title = ($lines[0] -replace '^# ', '')
  $tier1 = $f.BaseName -match '^t1-'
  $cre = New-Object System.Collections.ArrayList; $named = New-Object System.Collections.ArrayList
  $in = $false
  foreach ($l in $lines) {
    if ($l -match '^\| Creature \| Lvl') { $in = $true; continue }
    if ($in -and $l -match '^\|---') { continue }
    if ($in -and $l -notmatch '^\|') { $in = $false }
    if ($in) {
      $c = $l.Split('|'); $lv = $c[2].Trim(); $m = [regex]::Match($lv, '^(\d+)(?:\D+(\d+))?')
      $lo = [int]$m.Groups[1].Value; $hi = $(if ($m.Groups[2].Success) { [int]$m.Groups[2].Value } else { $lo })
      [void]$cre.Add([pscustomobject]@{ Name = $c[1].Trim(); Lo = $lo; Hi = $hi; Type = $c[3].Trim(); Ab = $c[4].Trim().Replace('**', ''); Drops = $c[5].Trim() })
    }
    if ($l -match '^\*\*(Rares|Rares / elites|Mini-boss|Act boss|Chain boss|Chain bosses):\*\*') {
      $label = $matches[1]
      foreach ($m in [regex]::Matches($l, '\*([^*]{3,60})\*\s*\((\d+)([^)]*)\)')) {
        $nm = $m.Groups[1].Value.Trim(); if ($nm -cmatch '^[a-z]') { continue }
        $desc = $m.Groups[3].Value; $lev = [int]$m.Groups[2].Value
        if ($named | Where-Object { $_.Name -eq $nm }) { continue }
        $rank = 'Rare'; $hm = 1.5; $dm = 1.2; $resp = '2' + $en + '8 h'
        if ($desc -match 'named') { $rank = 'Named'; $resp = '5 min' }
        if ($desc -match 'elite') { $rank = $(if ($desc -match 'rare') { 'Rare elite' } else { 'Elite' }); $hm = 3.0; $dm = 1.8; if ($desc -notmatch 'rare') { $resp = '7 min' } }
        if ($label -match 'Mini-boss') { $rank = 'Mini-boss'; $hm = 2.0; $dm = 1.3; $resp = '5 min' }
        if ($label -match 'Act boss|Chain boss') { $rank = 'Chain boss (elite)'; $hm = 5.0; $dm = 2.0; $resp = '5 min' }
        if ($desc -match 'group 5|group 3' + $en + '5') { $rank = 'Group boss (elite)'; $hm = 8.0; $dm = 2.2; $resp = '15 min' }
        elseif ($desc -match 'group 3' -and $hm -lt 5) { $rank = 'Group elite'; $hm = 5.0; $dm = 2.0; $resp = '10 min' }
        $ty = 'Humanoid'
        if (($desc + $nm) -match 'wolf|\bbear\b|boar|spider|lynx|jackal|\bram\b|hyena|skitterer|Stonecrawler|fox|cat|Mirefang|Scarhide|Ironhide|Greymaw|Blindmaw|Bitterhorn|Mudtusk|Dustmaw|Whitepelt|Red Tom|Glimmerqueen|Gnawbone|Flint') { $ty = 'Beast' }
        elseif (($desc + $nm) -match 'treant|Mossback') { $ty = 'Plant' } elseif (($desc + $nm) -match 'undead|Jack|Barrow-King|Ghost|Shade|Cadoc') { $ty = 'Undead' }
        elseif (($desc + $nm) -match 'construct|Wickerman|Rattlebones') { $ty = 'Construct' } elseif (($desc + $nm) -match 'aberration|Horror') { $ty = 'Aberration' }
        elseif (($desc + $nm) -match 'Hulk|Clinker|Vitrea|Gazer') { $ty = $(if ($nm -match 'Vitrea') { 'Beast' } else { 'Elemental' }) } elseif (($desc + $nm) -match 'harpy|Kaa|Gillkin|Gravelkin|Burrowkin|Kibbler|Grawl|Hag|Pondwife') { $ty = 'Humanoid' }
        elseif (($desc + $nm) -match 'ogre|Gorm|Urgoth') { $ty = 'Giant' }
        [void]$named.Add([pscustomobject]@{ Name = $nm; Lv = $lev; Rank = $rank; Hm = $hm; Dm = $dm; Resp = $resp; Type = $ty })
      }
    }
  }
  if ($extra.ContainsKey($code)) { foreach ($e in $extra[$code]) { [void]$named.Add([pscustomobject]@{ Name = $e[0]; Lv = $e[1]; Rank = 'Named'; Hm = 1.5; Dm = 1.2; Resp = '5 min'; Type = $e[2] }) } }
  [void]$sb.AppendLine("## $title")
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('### Stat blocks')
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |')
  [void]$sb.AppendLine('|---|---|---|---|---|---|---|---|---|---|---|')
  $i = 0
  foreach ($c in $cre) {
    $i++; $totN++; $caster = $c.Type -match 'caster'; $spd = Speed $c.Type
    $hm = $(if ($caster) { 0.8 } else { 1.0 }); $dm = $(if ($caster) { 0.4 } else { 1.0 })
    $h1 = [math]::Round((Lerp $c.Lo 1) * $hm); $h2 = [math]::Round((Lerp $c.Hi 1) * $hm)
    $d1 = (Lerp $c.Lo 2) * $dm * $spd; $d2 = (Lerp $c.Hi 2) * $dm * $spd
    $dmg = "$([math]::Round($d1 * 0.85))$en$([math]::Round($d1 * 1.15))" + $(if ($c.Hi -ne $c.Lo) { " to $([math]::Round($d2 * 0.85))$en$([math]::Round($d2 * 1.15))" } else { '' })
    $arm = [math]::Round((Lerp $c.Hi 3) * $(if ($caster) { 0.75 } else { 1.0 }))
    $mana = $(if ($caster) { [string](60 + $c.Hi * 45) } else { $mdash })
    $lvl = $(if ($c.Hi -ne $c.Lo) { "$($c.Lo)$en$($c.Hi)" } else { "$($c.Lo)" })
    $hp = $(if ($c.Hi -ne $c.Lo) { "$h1$en$h2" } else { "$h1" })
    $xp = $(if ($c.Hi -ne $c.Lo) { "$(45 + 5 * $c.Lo)$en$(45 + 5 * $c.Hi)" } else { "$(45 + 5 * $c.Lo)" })
    [void]$sb.AppendLine("| CRE-$code-$('{0:D2}' -f $i) | $($c.Name) | $lvl | $($c.Type) | $hp | $dmg | $spd s | $arm | $mana | $(if ($tier1) { '2.5 min' } else { '5 min' }) | $xp |")
  }
  foreach ($n in $named) {
    $i++; $totNamed++; $caster = $n.Type -match 'caster'; $spd = Speed $n.Type
    $h = [math]::Round((Lerp $n.Lv 1) * $n.Hm * $(if ($caster) { 0.8 } else { 1.0 })); $d = (Lerp $n.Lv 2) * $n.Dm * $spd * $(if ($caster) { 0.4 } else { 1.0 })
    $xpm = $(if ($n.Rank -match 'boss|Group') { 3 } elseif ($n.Rank -match '[Ee]lite') { 2 } else { 1 })
    [void]$sb.AppendLine("| CRE-$code-$('{0:D2}' -f $i) | **$($n.Name)** ($($n.Rank)) | $($n.Lv) | $($n.Type) | $h | $([math]::Round($d * 0.85))$en$([math]::Round($d * 1.15)) | $spd s | $([math]::Round((Lerp $n.Lv 3))) | $(if ($caster) { 60 + $n.Lv * 45 } else { $mdash }) | $($n.Resp) | $((45 + 5 * $n.Lv) * $xpm) |")
  }
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('### Abilities')
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('| Creature | Ability | Kind | Effect at top level |')
  [void]$sb.AppendLine('|---|---|---|---|')
  foreach ($c in $cre) {
    if ($c.Ab -eq $mdash -or $c.Ab -eq '') { [void]$sb.AppendLine("| $($c.Name) | $mdash | $mdash | Melee only |"); continue }
    $caster = $c.Type -match 'caster'; $spd = Speed $c.Type
    $dps = (Lerp $c.Hi 2) * $(if ($caster) { 0.4 } else { 1.0 }); $hp = (Lerp $c.Hi 1) * $(if ($caster) { 0.8 } else { 1.0 })
    foreach ($a in (SplitTop $c.Ab)) { $totAb++; $r = Ability $a $c.Hi (Lerp $c.Hi 2) $spd $hp $caster; [void]$sb.AppendLine("| $($c.Name) | $($r[0]) | $($r[1]) | $($r[2]) |") }
  }
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('### Loot')
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('| Creature | Loot table |')
  [void]$sb.AppendLine('|---|---|')
  foreach ($c in $cre) { [void]$sb.AppendLine("| $($c.Name) | $(Loot $c.Type $c.Lo $c.Hi $c.Drops 1) |") }
  foreach ($n in $named) {
    $g = $(if ($n.Rank -match 'Rare') { 'Guaranteed green (100%)' } elseif ($n.Rank -match 'boss|Group|Elite') { 'World green 8%, world blue 1%' } else { 'World green 2%' })
    $coin = $(if ($n.Type -match 'Humanoid|Giant|Undead') { "Coin $($n.Lv * 12)$en$($n.Lv * 36)c $md " } else { '' })
    [void]$sb.AppendLine("| **$($n.Name)** | $coin$g $md named drop and quest items as listed in the zone and quest text documents |")
  }
  [void]$sb.AppendLine('')
}
[void]$sb.AppendLine("**Totals:** $totN creature types $md $totNamed named, rare and elite creatures $md $totAb ability rows.")
$out = Join-Path $Root 'docs\12-data\creatures.md'
New-Item -ItemType Directory -Force (Split-Path $out) | Out-Null
[IO.File]::WriteAllText($out, $sb.ToString(), $enc)
"creatures: $totN  named: $totNamed  abilities: $totAb"
