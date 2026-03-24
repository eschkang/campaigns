import json 
from pathlib import Path 
data=json.loads(Path('Systems/leg.json').read_text()) 
import pprint 
for leg in data['legislation']: 
    if leg.get('id')=='WTP6': 
        pprint.pprint(leg) 
