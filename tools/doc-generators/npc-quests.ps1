param([string]$Root)
# Documentation helper only: fills the Gives / Ends columns of the NPC rosters from the quest text files.
$dot = [string][char]0x00B7; $arrow = [string][char]0x2192; $dash = [string][char]0x2014
$enc = New-Object System.Text.UTF8Encoding($false)
# 1. quests
$quests = New-Object System.Collections.ArrayList
foreach ($f in (Get-ChildItem (Join-Path $Root 'docs\06-quests\text') -Filter '*-*.md' | Where-Object { $_.Name -notmatch '^00-' })) {
  $lines = [IO.File]::ReadAllLines($f.FullName)
  for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^### ([A-Z]{2}-\d\d) ') {
      $id = $matches[1]; $meta = $lines[$i + 1].Trim('*')
      $parts = $meta -split (' ' + [regex]::Escape($dot) + ' ')
      $ge = ($parts[2..($parts.Count - 1)] -join ' ')
      $sp = $ge -split (' ' + [regex]::Escape($arrow) + ' ')
      [void]$quests.Add([pscustomobject]@{ Id = $id; Giver = $sp[0]; Ender = $(if ($sp.Count -gt 1) { $sp[1] } else { '' }); G = 0; E = 0 })
    }
  }
}
# 2. NPCs
function MakeRx($short) {
  $alts = @()
  foreach ($a in ($short -split ' / ')) {
    $t = $a.Trim() -split ' '
    if ($t.Count -eq 1) { $alts += '(?<![\w-])' + [regex]::Escape($t[0]) + '(?![\w-])' }
    else { $alts += '(?<![\w-])' + [regex]::Escape(($t[0..($t.Count - 2)] -join ' ')) + ' (\S+ )?' + [regex]::Escape($t[-1]) + '(?![\w-])' }
  }
  return ($alts -join '|')
}
$classEnders = @{ 'BM-03' = @('NPC-BM-02', 'NPC-BM-03', 'NPC-BM-04'); 'EC-03' = @('NPC-EC-02', 'NPC-EC-03', 'NPC-EC-04') }
$named = 0; $groups = 0; $withQuests = 0
foreach ($f in (Get-ChildItem (Join-Path $Root 'docs\11-npcs') -Filter '0*.md' | Where-Object { $_.Name -notmatch '^00-' })) {
  $lines = [IO.File]::ReadAllLines($f.FullName)
  for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -notmatch '^\| (NPC-[A-Z]{2,3}-\d\d) \|') { continue }
    $c = $lines[$i].Split('|'); $nid = $c[1].Trim(); $short = $c[3].Trim()
    if ($c[2] -match [char]0x00D7) { $groups++ } else { $named++ }
    $gives = @(); $ends = @()
    if ($short -ne $dash -and $short -ne '') {
      $rx = MakeRx $short
      foreach ($q in $quests) {
        if ($q.Giver -cmatch $rx) { $gives += $q.Id; $q.G++ }
        if ($q.Ender -cmatch $rx) { $ends += $q.Id; $q.E++ }
      }
    }
    foreach ($k in $classEnders.Keys) { if ($classEnders[$k] -contains $nid) { $ends += $k; ($quests | Where-Object { $_.Id -eq $k }).E++ } }
    if ($gives.Count + $ends.Count -gt 0) { $withQuests++ }
    $c[7] = ' ' + $(if ($gives.Count) { ($gives | Sort-Object) -join ', ' } else { $dash }) + ' '
    $c[8] = ' ' + $(if ($ends.Count) { ($ends | Sort-Object) -join ', ' } else { $dash }) + ' '
    $lines[$i] = $c -join '|'
  }
  [IO.File]::WriteAllLines($f.FullName, $lines, $enc)
}
"named NPCs: $named  generic groups: $groups  NPCs with quests: $withQuests  quests: $($quests.Count)"
$objRx = 'Item:|object|board|poster|granted|[Ss]tone \(|Ledger|Gown|Page|Cache'
foreach ($q in $quests) {
  if ($q.G -eq 0 -and $q.Giver -notmatch $objRx) { "UNMATCHED GIVER $($q.Id): $($q.Giver)" }
  if ($q.E -eq 0 -and $q.Ender -notmatch $objRx) { "UNMATCHED ENDER $($q.Id): $($q.Ender)" }
  if ($q.G -gt 2) { "MULTI GIVER $($q.Id) x$($q.G): $($q.Giver)" }
  if ($q.E -gt 3) { "MULTI ENDER $($q.Id) x$($q.E): $($q.Ender)" }
}
