apiToken = "73a0e30c4dd718ed0c5a327f96f31f5db2d33b5d"

import requests
import json

url = "https://api.waqi.info/feed/paris/?token="+apiToken

r = requests.get(url)
print(r.status_code)
r_json = json.loads(r.text)
# print(r_json)
print(json.dumps(r_json, indent=4, sort_keys=True))