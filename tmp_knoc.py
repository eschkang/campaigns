from pathlib import Path 
text = Path('Bush/bush.json').read_text() 
for idx,line in enumerate(text.splitlines(),1): 
    if 'KNOC' in line: 
        print(idx, line.strip()) 
