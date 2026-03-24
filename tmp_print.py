from pathlib import Path 
lines=Path('Bush/bush.json').read_text().splitlines() 
for i in range(14,44): 
    print(str(i+1).zfill(4) + ': ' + lines[i]) 
