from pathlib import Path 
text=Path('Old/leg.json').read_text() 
idx=text.find('CHI') 
print(idx) 
print(text[idx-200:idx+200]) 
