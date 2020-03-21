import requests
import json,csv
import pandas as pd

# https://api.waqi.info/feed/paris/?token=73a0e30c4dd718ed0c5a327f96f31f5db2d33b5d

def fetchNewData(city = 'paris', apiToken = "73a0e30c4dd718ed0c5a327f96f31f5db2d33b5d"):
    url = "https://api.waqi.info/feed/"+city+"/?token="+apiToken
    r = requests.get(url)
    r_json = json.loads(r.text)
    r_json_data = r_json['data']
    tab = []
    tab.append(r_json_data['time']['s'][0:10].replace("-","/"))
    if tab[0][5] == '0': 
        tab[0]=tab[0][:5] + tab[0][6:]
    tab.append(r_json_data['iaqi']['pm25']['v'])
    tab.append(r_json_data['iaqi']['pm10']['v'])
    tab.append(r_json_data['iaqi']['o3']['v'])
    tab.append(r_json_data['iaqi']['no2']['v'])
    tab.append(r_json_data['iaqi']['so2']['v'])
    tab.append(r_json_data['iaqi']['co']['v'])
    tab.append(r_json_data['city']['name'])

    df = pd.DataFrame(columns=['date', 'pm25','pm10', 'o3','no2', 'so2','co'])
    df = df.append(pd.Series([tab[0],tab[1],tab[2],tab[3],tab[4],tab[5],tab[6],tab[7]], index=['date', 'pm25','pm10', 'o3','no2', 'so2','co','ville']), ignore_index=True)
    return df
