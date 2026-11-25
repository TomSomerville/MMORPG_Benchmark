param([string]$Root)
$dia = [string][char]0x25C6; $box = [string][char]0x2610; $larr = [string][char]0x2190
# Documentation helper only: scans the design docs for named items and writes an art index.
$kw = 'mail|leather|cloth|sword|mace|axe|dagger|staff|shield|ring|neck|trinket|cloak|off-hand|polearm|bow|gun|relic|belt|wrist|bag|shoulders|head|chest|legs|feet|hands|2H|1H|toy|waist'
$nameKw = 'Cloak|Mantle|Mitts|Gloves|Robe|Hauberk|Jerkin|Vest|Hood|Cowl|Staff|Blade|Hammer|Maul|Buckler|Band|Signet|Charm|Pendant|Locket|Beads|Lantern|Girdle|Cord|Sash|Bracers|Greaves|Pauldrons|Spaulders|Helm|Boots|Sabatons|Treads|Leggings|Kilt|Trousers|Wraps|Cestus|Grips|Knot|Insignia|Keepsake|Shield|Bulwark|Wall|Rampart|Cutlass|Sceptre|Rod|Slippers|Greatcoat|Loop|Girdle|Seal|Torc|Crest|Parasol|Hat|Tabard|Saddlebag|Haversack'
function Slot($s) {
  $t = $s.ToLower()
  if ($t -match 'trinket|insignia|knot') { return 'Trinket' }
  if ($t -match '\bring\b|band\b|signet|loop\b|seal\b') { return 'Ring' }
  if ($t -match 'neck|pendant|locket|beads|torc|gorget|keepsake') { return 'Neck' }
  if ($t -match 'relic|psalter|charm of') { return 'Relic' }
  if ($t -match 'bag|haversack') { return 'Bag' }
  if ($t -match 'tabard') { return 'Tabard' }
  if ($t -match 'shield|buckler|bulwark|rampart|\bwall\b|crest\b|keystone|portcullis|tray') { return 'Shield' }
  if ($t -match 'off-hand|lantern|tome|marginalia') { return 'Off-hand' }
  if ($t -match 'polearm|halberd') { return 'Polearm' }
  if ($t -match 'staff') { return 'Staff' }
  if ($t -match 'dagger') { return 'Dagger' }
  if ($t -match '2h sword|greatsword') { return '2H sword' }
  if ($t -match '2h axe|greataxe') { return '2H axe' }
  if ($t -match '2h mace|2h\)|maul|\(2h') { return '2H mace' }
  if ($t -match '\b2h\b|scythe') { return '2H mace' }
  if ($t -match '1h sword|sword|cutlass|blade') { return '1H sword' }
  if ($t -match '1h axe|axe') { return '1H axe' }
  if ($t -match '1h mace|mace|sceptre|hammer') { return '1H mace' }
  if ($t -match '\bbow\b|shortbow') { return 'Bow' }
  if ($t -match '\bgun\b|rifle|blunderbuss|hand-cannon') { return 'Gun' }
  if ($t -match 'cloak|cape') { return 'Cloak' }
  if ($t -match 'head|hood|cowl|helm|hat|crown|goggles') { return 'Head' }
  if ($t -match 'shoulder|mantle|pauldron|spaulder') { return 'Shoulders' }
  if ($t -match 'chest|robe|hauberk|jerkin|vest|vestments|breastplate|doublet|greatcoat|gown|harness|tunic|cuirass|armor|apron|coat|ringmail') { return 'Chest' }
  if ($t -match 'legs|leggings|kilt|trousers|legguards|greaves|pants') { return 'Legs' }
  if ($t -match 'feet|boots|sabatons|treads|slippers|sandals|waders') { return 'Feet' }
  if ($t -match 'hands|gloves|mitts|gauntlets|grips|cestus') { return 'Hands' }
  if ($t -match 'wrist|bracers|wraps') { return 'Wrist' }
  if ($t -match 'belt|waist|girdle|cord|sash|cinch|bandolier') { return 'Waist' }
  return 'Other'
}
# The slot stated at the start of a description ("mail hands, ilvl 11", "back, ilvl 30") wins over any word in the item's name.
function DescSlot($d) {
  if (-not $d) { return $null }
  $t = $d.ToLower()
  if ($t -match 'crafting reserve|crafting material|^quest( item)?$') { return 'Other' }
  if ($t -match '^(blue |epic )?back\b') { return 'Cloak' }
  $m = [regex]::Match($t, '^(blue |epic )?(cloth|leather|mail)\s+(chest|legs|feet|hands|wrist|waist|head|shoulders|belt|boots|gloves|bracers|helm|cloak)(?![/\w])')
  if (-not $m.Success) { return $null }
  switch ($m.Groups[3].Value) {
    'belt' { return 'Waist' } 'boots' { return 'Feet' } 'gloves' { return 'Hands' } 'bracers' { return 'Wrist' } 'helm' { return 'Head' } 'cloak' { return 'Cloak' }
    default { $w = $m.Groups[3].Value; return $w.Substring(0, 1).ToUpper() + $w.Substring(1) }
  }
}
function Need($slot, $unique) {
  switch -Regex ($slot) {
    'Trinket|Ring|Neck|Relic|Bag|Other' { return 'Icon only' }
    'Tabard' { return 'Tabard texture + icon' }
    'Head|Shoulders' { if ($unique) { return 'Unique 3D piece + texture + icon' } else { return 'Tier 3D piece, recolor + icon' } }
    'Chest|Legs|Feet|Hands|Wrist|Waist' { if ($unique) { return 'Unique body texture + icon' } else { return 'Tier body texture, recolor + icon' } }
    'Cloak' { if ($unique) { return 'Unique cloak texture + icon' } else { return 'Cloak design recolor + icon' } }
    default { if ($unique) { return 'Unique model + texture + icon' } else { return 'Tier model, recolor + icon' } }
  }
}
$seen = @{}; $rows = New-Object System.Collections.ArrayList
$files = Get-ChildItem (Join-Path $Root 'docs') -Recurse -Filter *.md | Where-Object { $_.FullName -match '05-zones|07-instances|pvp\.md|items-and-loot|reference-tables' }
foreach ($f in $files) {
  $src = $f.BaseName
  $uniqueSrc = $src -match 'dungeons|raid-|world-bosses|pvp|reference-tables'
  foreach ($raw in [IO.File]::ReadAllLines($f.FullName)) {
    $line = $raw.Replace('**', '')
    $blue = $line -match 'Blue|blue |Epic|epic '
    foreach ($m in [regex]::Matches($line, '\*([^*|]{3,70})\*(\s*\(([^)]{1,110})\))?')) {
      $name = $m.Groups[1].Value.Trim(); $desc = $m.Groups[3].Value.Trim()
      if ($name -cmatch '^[a-z0-9]') { continue }
      # "*Creature* (8 rare - *Item*, off-hand)": the item is the inner name, not the creature
      $im = [regex]::Match($desc, [string][char]0x2014 + ' \*([^*]+)\*,?\s*(.*)$')
      $fromInner = $im.Success
      if ($im.Success) {
        $from = 'dropped by ' + $name + ' (' + $desc.Substring(0, $im.Index).Trim() + ')'
        $name = $im.Groups[1].Value.Trim(); $rest = $im.Groups[2].Value.Trim()
        if ($rest) { $desc = $rest + '; ' + $from } else { $desc = $from }
      }
      # Not equipment: recipes, consumables, boss abilities written in italics, and inn names
      if ($name -match '^(Plans|Pattern|Recipe|Formula|Schematic|Manual):') { continue }
      if ($desc -match '^(weapon oil|Blacksmithing|Leatherworking|Tailoring|Alchemy|Enchanting|Engineering|Cooking|First Aid)\b') { continue }
      if ($desc -match '^tank$') { continue }
      if ((-not $desc) -and ($line -match '\binn\b')) { continue }
      $isTableLoot = $false
      if ((-not $desc) -and ($src -match 'world-bosses')) { $tm = [regex]::Match($line, '^\| \*' + [regex]::Escape($name) + '\* \| ([^|]+) \| ([^|]+) \|'); if ($tm.Success) { $desc = $tm.Groups[1].Value.Trim() + ', ' + $tm.Groups[2].Value.Trim(); $isTableLoot = $true } }
      $ok = ($desc -match $kw) -or ($name -match $nameKw) -or $isTableLoot -or ($fromInner -and (Slot($name)) -ne 'Other')
      if (-not $ok) { continue }
      if ($desc -match 'inn|Use — |Fire damage to|every |aura|stun|cast\b' -and $desc -notmatch $kw) { continue }
      if ($seen.ContainsKey($name)) { continue }
      $seen[$name] = 1
      $slot = DescSlot $desc
      if (-not $slot) { $slot = Slot("$desc $name"); if ($slot -eq 'Other') { $slot = Slot($name) } }
      $u = $uniqueSrc -or $blue
      [void]$rows.Add([pscustomobject]@{ Name = $name; Slot = $slot; Desc = $desc; Src = $src; Need = (Need $slot $u); Unique = $u })
    }
  }
}
# Quest reward items from the quest text files (items already found in the zone docs are kept under their zone)
$qcount = 0
foreach ($f in (Get-ChildItem (Join-Path $Root 'docs\06-quests\text') -Filter '*-*.md' | Where-Object { $_.Name -notmatch '^00-' } | Sort-Object Name)) {
  $src = 'quest-text-' + $f.BaseName
  foreach ($raw in [IO.File]::ReadAllLines($f.FullName)) {
    if ($raw -notmatch '^\*\*Rewards:') { continue }
    $line = $raw.Replace('**', '')
    $blue = $line -match '\(blue\)|\(epic\)|blue ring|blue neck'
    foreach ($m in [regex]::Matches($line, '\*([^*]{3,70})\* \(([^)]{1,200})\)')) {
      $name = $m.Groups[1].Value.Trim(); $desc = $m.Groups[2].Value.Trim()
      if ($desc -notmatch 'ilvl|-slot bag') { continue }
      if ($desc -match 'fishing pole') { continue }
      if ($seen.ContainsKey($name)) { continue }
      $seen[$name] = 1
      $slot = DescSlot $desc
      if (-not $slot) { $slot = Slot($desc) }
      [void]$rows.Add([pscustomobject]@{ Name = $name; Slot = $slot; Desc = $desc; Src = $src; Need = (Need $slot $blue); Unique = $blue })
      $qcount++
    }
  }
}
# Crafted equipment from crafting.md
$cf = Join-Path $Root 'docs\04-professions\crafting.md'
foreach ($raw in [IO.File]::ReadAllLines($cf)) {
  $c = $raw.Split('|')
  if ($c.Count -ge 6 -and $c[1].Trim() -match '^\d+$' -and $c[4] -match '\[\d' -and $c[4] -match $kw) {
    $name = ($c[2] -replace '\*\*\([^)]*\)\*\*', '' -replace '\(.*?\)', '').Replace($dia, '').Trim()
    if ($seen.ContainsKey($name)) { continue }; $seen[$name] = 1
    $u = $c[2].Contains($dia); $desc = $c[4].Trim(); $slot = DescSlot ($desc.Replace('*', ''))
    if (-not $slot) { $slot = Slot("$desc $name") }
    [void]$rows.Add([pscustomobject]@{ Name = $name; Slot = $slot; Desc = $desc; Src = 'crafting'; Need = (Need $slot $u); Unique = $u })
  }
}
# Crafted equipment from the five-column table in crafting.md section 6a (skill, profession, recipe, reagents, result)
foreach ($raw in [IO.File]::ReadAllLines($cf)) {
  $c = $raw.Split('|')
  if ($c.Count -ge 7 -and $c[1].Trim() -match '^\d+$' -and $c[2].Trim() -match '^(Blacksmithing|Leatherworking|Tailoring|Engineering|Alchemy|Enchanting)$' -and $c[5] -match '\[\d') {
    $name = ($c[3] -replace '\*\*\([^)]*\)\*\*', '' -replace '\(.*?\)', '').Replace($dia, '').Trim()
    if ($seen.ContainsKey($name)) { continue }; $seen[$name] = 1
    $desc = $c[5].Trim() + '; ' + $c[2].Trim() + ' ' + $c[1].Trim(); $slot = DescSlot $desc
    if (-not $slot) { $slot = Slot("$desc $name") }
    [void]$rows.Add([pscustomobject]@{ Name = $name; Slot = $slot; Desc = $desc; Src = 'crafting'; Need = (Need $slot $true); Unique = $true })
  }
}
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine('# Art To-Do 7: Named Item Index')
[void]$sb.AppendLine('')
[void]$sb.AppendLine($larr + ' [Art Master To-Do](00-art-master-todo.md) · Prev: [Icons](06-icons.md)')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('Every named piece of equipment in the level 1-30 design documents, extracted automatically from the zone, instance, PvP, crafting and quest text docs, with the art each one needs. Sources named "quest-text-..." are quest rewards first named in the [Quest Text](../06-quests/text/00-quest-text-index.md) files. "Tier" means the generic model or texture for that slot and level band defined in [Characters, Armor & Weapons](01-characters-armor-weapons.md); "Unique" means its own asset. Regenerate this file after any design change. Unnamed "green boots"-style rewards and random-suffix drops use tier art and need no entry.')
[void]$sb.AppendLine('')
$tot = $rows.Count; $uq = @($rows | Where-Object { $_.Unique }).Count
[void]$sb.AppendLine("**Totals:** $tot named items · $uq need unique art · $($tot - $uq) use tier art with a recolor · every one needs its own icon.")
[void]$sb.AppendLine('')
[void]$sb.AppendLine('| Slot | Named items | Unique art |')
[void]$sb.AppendLine('|---|---|---|')
foreach ($g in ($rows | Group-Object Slot | Sort-Object Name)) { [void]$sb.AppendLine("| $($g.Name) | $($g.Count) | $(@($g.Group | Where-Object { $_.Unique }).Count) |") }
[void]$sb.AppendLine('')
$i = 0
foreach ($g in ($rows | Group-Object Src | Sort-Object Name)) {
  [void]$sb.AppendLine("## Source: $($g.Name)")
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('| ID | Done | Item | Slot | As described | Art needed |')
  [void]$sb.AppendLine('|---|---|---|---|---|---|')
  foreach ($r in ($g.Group | Sort-Object Slot, Name)) { $i++; [void]$sb.AppendLine((('| ITM-{0:D3} | ' + $box + ' | {1} | {2} | {3} | {4} |') -f $i, $r.Name, $r.Slot, $r.Desc.Replace('|', '/'), $r.Need)) }
  [void]$sb.AppendLine('')
}
$out = Join-Path $Root 'docs\10-art\07-named-item-index.md'
New-Item -ItemType Directory -Force (Split-Path $out) | Out-Null
[IO.File]::WriteAllText($out, $sb.ToString(), (New-Object System.Text.UTF8Encoding($false)))
"items: $tot  unique: $uq  new from quest text: $qcount"
$rows | Group-Object Slot | Sort-Object Name | ForEach-Object { "$($_.Name): $($_.Count) (unique $(@($_.Group | Where-Object { $_.Unique }).Count))" }
