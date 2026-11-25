param([string]$Root)
# Documentation helper only: expands the class ability tables into one row per rank.
$en = [string][char]0x2013; $arrow = [string][char]0x2192; $larr = [string][char]0x2190; $md = [string][char]0x00B7; $mdash = [string][char]0x2014; $minus = [string][char]0x2212
$enc = New-Object System.Text.UTF8Encoding($false)
$costs = @{ 1 = 'free'; 2 = '10c'; 4 = '1s'; 6 = '2s'; 8 = '5s'; 10 = '8s'; 12 = '12s'; 14 = '20s'; 16 = '30s'; 18 = '50s'; 20 = '60s'; 22 = '80s'; 24 = '1g'; 26 = '1g 20s'; 28 = '1g 40s'; 30 = '1g 60s' }
function Num($s) { return [double](($s -replace ',', '') -replace [regex]::Escape($minus), '-') }
function Fmt([double]$v, $dec, $sign, $neg) {
  $r = $(if ($dec) { [math]::Round($v * 2) / 2 } else { [math]::Round($v) })
  $t = $(if ($dec) { $r.ToString('0.0') } else { ([int][math]::Abs($r)).ToString('N0') })
  if ($dec) { return $t }
  if ($neg) { return $minus + $t } elseif ($sign) { return '+' + $t } else { return $t }
}
$pat = '([+' + $minus + '-]?)(\d[\d,]*(?:\.\d+)?)(?:' + $en + '(\d[\d,]*(?:\.\d+)?))?\s*' + $arrow + '\s*([+' + $minus + '-]?)(\d[\d,]*(?:\.\d+)?)(?:' + $en + '(\d[\d,]*(?:\.\d+)?))?'
function Interp($text, [double]$frac) {
  return [regex]::Replace($text, $pat, {
      param($m)
      $sg = $m.Groups[1].Value; $a1 = Num $m.Groups[2].Value; $b1 = Num $m.Groups[5].Value
      $dec = ($m.Groups[2].Value -match '\.') -or ($m.Groups[5].Value -match '\.')
      $neg = ($sg -eq $minus -or $sg -eq '-'); $plus = ($sg -eq '+')
      $o = Fmt ($a1 + ($b1 - $a1) * $frac) $dec $plus $neg
      if ($m.Groups[3].Success -and $m.Groups[6].Success) { $a2 = Num $m.Groups[3].Value; $b2 = Num $m.Groups[6].Value; $o += $en + (Fmt ($a2 + ($b2 - $a2) * $frac) $dec $false $false) }
      return $o
    })
}
$classes = @(@('fighter', 'FIG', 'Fighter'), @('cleric', 'CLE', 'Cleric'), @('druid', 'DRU', 'Druid'))
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine('# Spell Data ' + $mdash + ' every ability, every rank')
[void]$sb.AppendLine('')
[void]$sb.AppendLine($larr + ' [Data Index](00-data-index.md) ' + $md + ' Classes: [Fighter](../03-classes/fighter.md) ' + $md + ' [Cleric](../03-classes/cleric.md) ' + $md + ' [Druid](../03-classes/druid.md)')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('Generated from the ability tables in the class documents using the rules in the [Data Index](00-data-index.md#3-spell-rules). **Do not edit by hand.** One row per rank. Values between the first and last rank are interpolated in a straight line by the level at which each rank is learned. Ranks learned above level 30 are listed as reserved.')
[void]$sb.AppendLine('')
$totA = 0; $totR = 0
foreach ($cl in $classes) {
  $lines = [IO.File]::ReadAllLines((Join-Path $Root "docs\03-classes\$($cl[0]).md"))
  [void]$sb.AppendLine("## $($cl[2])")
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('| ID | Ability | Rank | Level | Training | School | Cost | Cast / cooldown | Range | GCD | Coefficient | Effect |')
  [void]$sb.AppendLine('|---|---|---|---|---|---|---|---|---|---|---|---|')
  $in = $false; $hdr = @{}; $n = 0
  foreach ($l in $lines) {
    if ($l -match '^\| Lvl \| Ability') { $in = $true; $h = $l.Split('|'); for ($k = 0; $k -lt $h.Count; $k++) { $hdr[$h[$k].Trim()] = $k }; continue }
    if ($in -and $l -match '^\|---') { continue }
    if ($in -and $l -notmatch '^\|') { $in = $false; continue }
    if (-not $in) { continue }
    $c = $l.Split('|'); $n++; $totA++
    $lvl = [int]($c[$hdr['Lvl']].Trim()); $name = $c[$hdr['Ability']].Replace('**', '').Trim()
    $cost = $c[$hdr['Cost']].Trim(); $eff = $c[$hdr['Effect']].Trim(); $ranksRaw = $c[$hdr['Ranks at']].Trim()
    $cast = ''; if ($hdr.ContainsKey('Cast / CD')) { $cast = $c[$hdr['Cast / CD']].Trim() } elseif ($hdr.ContainsKey('Cooldown')) { $cast = $c[$hdr['Cooldown']].Trim() }
    $stance = ''; if ($hdr.ContainsKey('Stance')) { $stance = $c[$hdr['Stance']].Trim() }
    $school = 'Physical'; if ($hdr.ContainsKey('School')) { $school = $c[$hdr['School']].Trim() } elseif ($cl[1] -eq 'CLE') { $school = $(if ($eff -match 'Weapon damage') { 'Physical + Holy' } else { 'Holy' }) }
    $rk = @(); foreach ($m in [regex]::Matches(($ranksRaw -replace '\([^)]*\)', ''), '\d+')) { $rk += [int]$m.Value }
    if ($rk.Count -eq 0) { $rk = @($lvl) }
    $first = $rk[0]; $last = $rk[-1]
    $quest = $eff -match 'class quest' -or $stance -match 'quest'
    for ($r = 0; $r -lt $rk.Count; $r++) {
      $totR++; $L = $rk[$r]; $frac = $(if ($last -eq $first) { 0 } else { ($L - $first) / ($last - $first) })
      $e = Interp $eff $frac; $co = Interp $cost $frac; $ca = Interp $cast $frac
      if ($stance -and $stance -ne 'any' -and $stance -ne $mdash) { $e = "[$stance] " + $e }
      $train = $(if ($L -gt 30) { 'reserved' } elseif ($quest -and $r -eq 0) { 'quest' } elseif ($costs.ContainsKey($L)) { $costs[$L] } else { $costs[$L + 1] })
      $range = $(if ($e -match '(\d+) yd') { $matches[1] + ' yd' } elseif ($cl[1] -eq 'FIG') { $(if ($e -match 'Party|Enemies within|immune|Gain |stance') { 'self' } else { 'melee' }) } elseif ($e -match '^Heal|friendly|Ally|Resurrect|resurrect') { '40 yd' } elseif ($e -match 'swing|self-buff|Party|aura|Immune|Transform|Shows|your ') { 'self' } elseif ($e -match 'Weapon damage') { 'melee' } else { '30 yd' })
      $gcd = $(if (($ca + $cost) -match 'next swing|aura|toggle|passive') { 'no' } else { 'yes' })
      $coef = $mdash
      if ($cl[1] -ne 'FIG' -and $e -match 'damage|Heal|heal') {
        $pen = $(if ($L -lt 20) { 1 - (20 - $L) * 0.0375 } else { 1 })
        $ct = [regex]::Match($ca, '^(\d+(\.\d+)?) s'); $direct = $(if ($ct.Success) { [math]::Min(1.0, [double]$ct.Groups[1].Value / 3.5) } else { 1.5 / 3.5 })
        $ot = [regex]::Match($e, 'over (?:the duration|(\d+) s)'); $hasDirect = $e -match '(Heal \d|\d Holy damage|\d Nature damage|\d Arcane damage)(?! over)' -and $e -notmatch '^\S+ \d[\d,]* (Nature|Holy|Arcane) damage over'
        if ($ca -match 'channel') { $coef = ('{0:P0} per tick' -f ([math]::Min(1.0, 10 / 15) / 5 * $pen)) -replace ' %', '%' }
        elseif ($ot.Success) {
          $d = $(if ($ot.Groups[1].Success) { [double]$ot.Groups[1].Value } else { 15 }); $o = [math]::Min(1.0, $d / 15)
          if ($e -match 'plus|instantly') { $coef = ('{0:P0} direct + {1:P0} over time' -f ($direct * 0.5 * $pen), ($o * 0.5 * $pen)) -replace ' %', '%' } else { $coef = ('{0:P0} over time' -f ($o * $pen)) -replace ' %', '%' }
        }
        elseif ($e -match 'each swing|Attackers|attackers|per second') { $coef = ('{0:P0} per hit' -f (0.1 * $pen)) -replace ' %', '%' }
        else { $coef = ('{0:P0}' -f ($direct * $pen * $(if ($e -match 'enemies inside|all party') { 1 / 3 } else { 1 }))) -replace ' %', '%' }
      }
      $id = "SPL-$($cl[1])-$('{0:D2}' -f $n)" + $(if ($rk.Count -gt 1) { "-r$($r + 1)" } else { '' })
      [void]$sb.AppendLine("| $id | $name | $($r + 1) | $L$(if ($L -gt 30) { ' (above cap)' }) | $train | $school | $co | $(if ($ca) { $ca } else { 'instant' }) | $range | $gcd | $coef | $e |")
    }
  }
  [void]$sb.AppendLine('')
}
[void]$sb.AppendLine("**Totals:** $totA abilities $md $totR rank rows.")
[IO.File]::WriteAllText((Join-Path $Root 'docs\12-data\spells.md'), $sb.ToString(), $enc)
"abilities: $totA  ranks: $totR"
