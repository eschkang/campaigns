from pathlib import Path 
import json 
data=json.loads(Path('Bush/leg.json').read_text()) 
for item in data['legislation']: 
    name=item.get('name','') 
    if any(k in name for k in ['RAILS','Rail','Track','TRACK','Corridor']): 
        print(item['id'], item['name'], item['status']) 
