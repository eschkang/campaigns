import json
from pathlib import Path
data=json.loads(Path('Systems/leg.json').read_text())
for leg in data['legislation']:
    leg_id = leg.get('id','')
    if leg_id.startswith('WTP'):
        print(leg_id, leg.get('status'), leg.get('year'), leg.get('notes'))
