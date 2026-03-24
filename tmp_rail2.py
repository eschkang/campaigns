from pathlib import Path 
import json 
data=json.loads(Path('Bush/leg.json').read_text()) 
for item in data['legislation']: 
    if item.get('id')=='RAILS_2001_2003': 
        print(json.dumps(item, indent=2)) 
