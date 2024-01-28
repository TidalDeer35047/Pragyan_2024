import requests
import json
import time
import pandas as pd


r = requests.get("http://api.waqi.info/feed/delhi/alipur/?token=85102c9374068ef510a83f02a2a39e483bf00b0b")
# r.json()
json_data = json.loads(r.text)


realtime_df = pd.read_csv('./realtime/alipur_realtime.csv')

date = json_data['data']['time']['s']
pm25 = json_data['data']['iaqi']['pm25']['v']
pm10 = json_data['data']['iaqi']['pm10']['v']
o3 = json_data['data']['iaqi']['o3']['v']
no2 = json_data['data']['iaqi']['no2']['v']
so2 = json_data['data']['iaqi']['so2']['v']
co = json_data['data']['iaqi']['co']['v']


new_data = {'date': date, 'pm25':pm25, 'pm10': pm10, 'o3':o3, 'no2':no2, 'so2':so2, 'co':co}
exist_flag = False
for i in realtime_df['date']:
    if (i == date):
        exist_flag = True
if(exist_flag == False):
    realtime_df.loc[len(realtime_df)] = new_data

if(len(realtime_df['date'])>=11):
   realtime_df= realtime_df.iloc[1:, :]

realtime_df.to_csv("./realtime/alipur_realtime.csv", index=False)
