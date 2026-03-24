from pathlib import Path 
text=Path('Bush/bush.json').read_text() 
for i,line in enumerate(text.splitlines(),1): 
    if 'KNOC' in line: 
        print(i,line) 
