import pathlib 
for path in pathlib.Path('.').rglob('*'): 
    if path.is_file(): 
        text = path.read_text(errors='ignore') 
        if 'KNOC' in text: 
            print(path) 
