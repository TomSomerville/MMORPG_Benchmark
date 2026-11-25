param([string]$Root)
# Documentation helper only: copies each quest's reward from the quest text files into the Reward column of the zone quest tables,
# so the zone summaries never disagree with the quest text (which is the authority).
$dot = [string][char]0x00B7; $arrow = [string][char]0x2192; $mdash = [string][char]0x2014
$enc = New-Object System.Text.UTF8Encoding($false)
$rewards = @{}
Get-ChildItem (Join-Path $Root 'docs\06-quests\text') -Filter '*-*.md' | Where-Object { $_.Name -notmatch '^(00|cq)' } | ForEach-Object {
  $id = ''
  foreach ($l in [IO.File]::ReadAllLines($_.FullName)) {
    if ($l -match '^### ([A-Z]{2}-\d\d) ') { $id = $matches[1] }
    if ($id -and $l -match '^\*\*Rewards:\*\* (.*)$') {
      $r = $matches[1] -replace ('^[\d,]+ XP(?: \([^)]*\))?(?: ' + [regex]::Escape($dot) + ' )?'), ''
      if (-not $r.Trim()) { $r = $mdash }
      $rewards[$id] = $r.Replace('|', '/')
    }
  }
}
$changed = 0; $rows = 0
Get-ChildItem (Join-Path $Root 'docs\05-zones') -Filter 't*.md' | ForEach-Object {
  $lines = [IO.File]::ReadAllLines($_.FullName)
  for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -notmatch '^\| ([A-Z]{2}-\d\d) \|') { continue }
    $id = $matches[1]; if (-not $rewards.ContainsKey($id)) { "no quest text for $id"; continue }
    $c = $lines[$i].Split('|'); if ($c.Count -lt 9) { continue }
    $rows++
    $old = ($c[7..($c.Count - 2)] -join '|').Trim()
    $tail = ''
    $m = [regex]::Match($old, '(' + [regex]::Escape($arrow) + ' (continues at )?\[[^\]]+\]\([^)]+\).*)$')
    if ($m.Success) { $tail = ' ' + $m.Groups[1].Value }
    $new = $rewards[$id] + $tail
    if ($new -ne $old) { $changed++ }
    $lines[$i] = (($c[0..6] -join '|') + '| ' + $new + ' |')
  }
  [IO.File]::WriteAllLines($_.FullName, $lines, $enc)
}
"quest rows: $rows  reward cells changed: $changed"
