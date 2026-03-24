from pathlib import Path 
text = Path('Systems/leg.json').read_text() 
idx = text.lower().find('trinity') 
print('trinity found at', idx) 
if idx >= 0: 
    print(text[idx:idx+400]) 
