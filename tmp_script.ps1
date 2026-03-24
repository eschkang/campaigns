$lines = Get-Content 'Bush\bush.json' 
$keywords = 'senate','house_and_leadership' 
foreach ($kw in $keywords) { 
    for ($i = 0; $i -lt $lines.Count; $i++) { 
        if ($lines[$i] -match $kw) { 
            Write-Output \"$kw: line $($i+1)\" 
            break 
    } 
} 
