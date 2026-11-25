param([string]$Root)
# Documentation helper only: checks the world layout spawn camps against the zone creature tables and quest kill objectives.
$dot = [string][char]0x00B7
$camps = @{}
Get-ChildItem (Join-Path $Root 'docs\13-world') -Filter '0*.md' | ForEach-Object {
  foreach ($l in [IO.File]::ReadAllLines($_.FullName)) {
    if ($l -match '^\| [A-Z]{2}-S\d\d \| ([^|]+) \| (\d+) \|') { $n = ($matches[1].Trim() -replace '\s*\(.*\)$', ''); $camps[$n] = [int]$camps[$n] + [int]$matches[2] }
  }
}
"creatures with camps: $($camps.Count)  total spawn points: $(($camps.Values | Measure-Object -Sum).Sum)"
$zoneNames = @()
Get-ChildItem (Join-Path $Root 'docs\05-zones') -Filter 't*.md' | ForEach-Object {
  $in = $false
  foreach ($l in [IO.File]::ReadAllLines($_.FullName)) {
    if ($l -match '^\| Creature \| Lvl') { $in = $true; continue }
    if ($in -and $l -match '^\|---') { continue }
    if ($in -and $l -notmatch '^\|') { $in = $false }
    if ($in) { $zoneNames += $l.Split('|')[1].Trim() }
  }
}
"zone creatures without a camp: " + (($zoneNames | Where-Object { -not $camps.ContainsKey($_) }) -join '; ')
"camps not in zone tables: " + (($camps.Keys | Where-Object { $zoneNames -notcontains $_ }) -join '; ')
$bad = 0
Get-ChildItem (Join-Path $Root 'docs\06-quests\text') -Filter '*-*.md' | Where-Object { $_.Name -notmatch '^(00|cq)' } | ForEach-Object {
  $id = ''
  foreach ($l in [IO.File]::ReadAllLines($_.FullName)) {
    if ($l -match '^### ([A-Z]{2}-\d\d)') { $id = $matches[1] }
    if ($l -match '^\*\*Tracker:\*\* (.*)$') {
      foreach ($part in ($matches[1] -split $dot)) {
        $m = [regex]::Match($part.Trim(), '^(.+?) (slain|destroyed|laid to rest|subdued|defeated) 0/(\d+)$')
        if (-not $m.Success) { continue }
        $nm = $m.Groups[1].Value; $need = [int]$m.Groups[3].Value
        if ($need -lt 4) { continue }   # single named targets and world objects are listed under Points
        $key = $camps.Keys | Where-Object { $nm -eq $_ -or $nm -eq ($_ + 's') -or $nm -eq ($_ -replace 'y$', 'ies') -or $nm -eq ($_ + 'es') -or ($nm -replace ' challengers$', ' Challenger') -eq $_ } | Select-Object -First 1
        if (-not $key) { "NO CAMP  $id  $nm x$need (expected if this is a world object)"; $bad++ }
        elseif ($camps[$key] -lt 2 * $need) { "LOW      $id  $nm need $need have $($camps[$key])"; $bad++ }
      }
    }
  }
}
"problems: $bad"
