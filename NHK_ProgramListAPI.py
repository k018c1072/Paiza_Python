import pandas as pd
import json
import pprint
import datetime
import requests

url = "https://api.nhk.or.jp/v2/pg/list/"

params = {'key': 'uzPe6DqvGerLvLAqBezxZgTrnWV85XAS'}

area = input("エリアを入力してください＞")
service = input("サービスを入力してください＞")
# 現在時刻
dt_now = str(datetime.date.today())

# Request URL
url += area + "/" + service + "/" + dt_now + ".json"
r = requests.get(url, params=params)
json_data = r.json()


print("★  タイトル")
pprint.pprint(json_data['list'][service][0]['title'])
print("★  サブタイトル")
pprint.pprint(json_data['list'][service][0]['subtitle'])
print("★  内容")
pprint.pprint(json_data['list'][service][0]['content'])
print("★  出演者")
pprint.pprint(json_data['list'][service][0]['act'])

df = pd.DataFrame(json_data)
pprint.pprint(df.to_json(force_ascii=False))
with open("D:/NHK_pandas.txt", "w") as target:
    target.write(df.to_json(force_ascii=False))
