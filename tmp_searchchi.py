import pathlib 
for path in pathlib.Path('.').rglob('*'): 
    if path.is_file(): 
        try: 
            text=path.read_text() 
        except Exception: 
            continue 
        if 'CHI' in text: 
            print(path) 
