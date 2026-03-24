from pathlib import Path 
text=Path('Bush/amerisat_global_brief.md').read_text(encoding='utf-8', errors='ignore') 
idx=text.find('KNOC') 
print(idx) 
print(text[idx-200:idx+200]) 
