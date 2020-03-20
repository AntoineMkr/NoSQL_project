import json,csv
import pandas as pd
from getData import fetchNewData 
from pymongo import MongoClient
import schedule
import time

def mongoimport(csv_path,coll):
    data = pd.read_csv(csv_path)
    data = data.sort_values(by=['date'], ascending = False)
    data.reset_index(inplace=True)
    del data['index']
    payload = json.loads(data.to_json(orient='records'))
    # coll.remove()
    coll.insert(payload)
    return coll.count()

def insertNewData(newData, collection):

    payload = json.loads(newData.to_json(orient='records'))
    print(type(payload))
    collection.insert(payload)
    print('%d documents inserted in myDB.pulltion' % (len(payload)))

def foo():
    newData = fetchNewData()
    if collection.find({'date': newData['date'][0]}).count() == 0:
        insertNewData(newData,collection)
if __name__ == "__main__":
    #INIT DATABASE
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb =  myclient["myDB"]
    collection = mydb["pollution"]

    #INSERT HISTORICAL DATA IN DB
    # collection.drop()
    # collection = mydb["pollution"]
    # nbr =  mongoimport("paris-air-quality.csv",collection))
    # print('%d documents inserted in myDB.pollution' % (nbr))

    #INSERT NEW DAILY DATA ONLY IF NOT ALREADY EXISTS
    schedule.every().hours.do(foo())
    
    
    
    # see if there is new data every x days.
    