from pathlib import Path 
path = Path('Bush/bush.json') 
lines = path.read_text().splitlines() 
for i,line in enumerate(lines,1): 
    if 'TTA' in line or 'Trinity' in line: 
        print(i, line.strip()) 
