from pathlib import Path 
import json 
data=json.loads(Path('Bush/leg.json').read_text()) 
for item in data.get('legislation',[]): 
    name=item.get('name','') 
    if any(keyword in name for keyword in ['Rail','RAILS','Corridor','High-speed','TRACK','Track']): 
        print(json.dumps({'id':item.get('id'),'name':item.get('name'),'year':item.get('year'),'status':item.get('status'),'summary':item.get('summary')}, indent=2)) 
