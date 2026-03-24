import pathlib 
from pathlib import Path 
root = Path('.') 
for path in root.rglob('*'): 
    if path.is_file(): 
        try: 
            text = path.read_text() 
        except Exception: 
            continue 
        if 'KNOC' in text: 
            print(path) 
