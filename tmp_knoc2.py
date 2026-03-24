from pathlib import Path 
text = Path('Bush/leg.json').read_text() 
idx = text.find('KNOC') 
print(idx) 
print(text[idx-200:idx+200]) 
