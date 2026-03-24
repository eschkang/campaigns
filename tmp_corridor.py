from pathlib import Path 
for i,line in enumerate(Path('Systems/leg.json').read_text().splitlines(),1): 
    if 'Corridor' in line or 'corridor' in line: 
        print(i,line.strip()) 
