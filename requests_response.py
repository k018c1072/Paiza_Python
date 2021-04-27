import requests
import pprint
import json

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'

params = {'city': 130010}

r = requests.get(url, params=params)

print(r.headers['Content-Type'])

json_data = r.json()

print(type(json_data))
# <class 'dict'>

pprint.pprint(json_data["forecasts"][0])

with open('D:/test_json.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
