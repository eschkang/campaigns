from pathlib import Path 
text = Path('Bush/amerisat_global_brief.md').read_text() 
idx = text.find('KNOC') 
print(text[idx-200:idx+200]) 
