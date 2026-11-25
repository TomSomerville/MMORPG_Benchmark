param([string]$Root)
# Documentation helper only: lists every quest objective and the art it implies.
$box = [string][char]0x2610; $larr = [string][char]0x2190
$itemRx = '\b(Collect|Recover|Bring|Gather|Take|Steal|Carry|Deliver|Return|Present|Assemble)\b'
$objRx = '\b(Destroy|Defuse|Douse|Relight|Inspect|Examine|Cleanse|Retune|Sample|Remove|Search|Read|Consecrate|Collapse|Use|Open|Burn|Defend|Escort|Scout|Survey|Explore|Investigate|Follow|Find|Lay|Subdue|Step|Ride|Hear|Witness|Enter|Slip|Descend|Board|Cross|Walk|Reach|Travel)\b'
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine('# Art To-Do 8: Quest Art Index')
[void]$sb.AppendLine('')
[void]$sb.AppendLine($larr + ' [Art Master To-Do](00-art-master-todo.md) | Prev: [Named Item Index](07-named-item-index.md)')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('Every zone quest from level 1 to 30 with the art its objective implies, extracted automatically from the zone documents. **Item icon** = the quest hands the player, or asks them to collect or carry, a named item that needs an inventory icon. **World object / scene** = something in the world the player clicks, defends, follows or visits that must be modelled or staged. Kill and talk objectives need only the creatures and NPCs already listed in [Creatures and NPCs](02-creatures-npcs.md). Regenerate after any quest change.')
[void]$sb.AppendLine('')
$all = New-Object System.Collections.ArrayList
$zones = Get-ChildItem (Join-Path $Root 'docs\05-zones') -Filter 't*.md' | Sort-Object Name
foreach ($z in $zones) {
  foreach ($raw in [IO.File]::ReadAllLines($z.FullName)) {
    if ($raw -notmatch '^\| ([A-Z]{2}-\d\d) \|') { continue }
    $c = $raw.Split('|')
    if ($c.Count -lt 8) { continue }
    $id = $c[1].Trim(); $name = $c[2].Replace('**', '').Trim(); $obj = $c[5].Trim() -replace '\]\((t\d-)', '](../05-zones/$1'
    $needItem = $obj -match $itemRx
    $needObj = $obj -match $objRx
    $need = @()
    if ($needItem) { $need += 'Item icon' }
    if ($needObj) { $need += 'World object / scene' }
    if ($need.Count -eq 0) { $need += 'None beyond creatures and NPCs' }
    [void]$all.Add([pscustomobject]@{ Zone = $z.BaseName; Id = $id; Name = $name; Obj = $obj; Need = ($need -join ' + '); Item = $needItem; World = $needObj })
  }
}
$tot = $all.Count; $ni = @($all | Where-Object { $_.Item }).Count; $nw = @($all | Where-Object { $_.World }).Count
[void]$sb.AppendLine("**Totals:** $tot quests | $ni need at least one quest-item icon | $nw need a world object or staged scene.")
[void]$sb.AppendLine('')
foreach ($g in ($all | Group-Object Zone)) {
  [void]$sb.AppendLine("## $($g.Name)")
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('| Quest | Done | Name | Objective | Art implied |')
  [void]$sb.AppendLine('|---|---|---|---|---|')
  foreach ($r in $g.Group) { $ln = ('| {0} | ' + $box + ' | {1} | {2} | {3} |') -f $r.Id, $r.Name, $r.Obj, $r.Need; [void]$sb.AppendLine($ln) }
  [void]$sb.AppendLine('')
}
[IO.File]::WriteAllText((Join-Path $Root 'docs\10-art\08-quest-art-index.md'), $sb.ToString(), (New-Object System.Text.UTF8Encoding($false)))
"quests: $tot  item: $ni  world: $nw"
