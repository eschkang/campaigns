import json
from pathlib import Path
data=json.loads(Path('Systems/leg.json').read_text())
import pprint
for leg in data['legislation']:
    if leg.get('id') in ['WTP4_2005','WTP5_2005','WTP6_2005']:
        pprint.pprint(leg)
