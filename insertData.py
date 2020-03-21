import json,csv
import pandas as pd
from getData import fetchNewData 
from pymongo import MongoClient
import schedule
import time

def mongoimport(csv_path,coll, ville):
    data = pd.read_csv(csv_path)
    data = data.sort_values(by=['date'], ascending = False)
    data.reset_index(inplace=True)
    data['ville'] = ville
    del data['index']
    payload = json.loads(data.to_json(orient='records'))
    # coll.remove()
    coll.insert(payload)
    return coll.count()

def insertNewData(newData, collection,city):

    payload = json.loads(newData.to_json(orient='records'))
    print(type(payload))
    collection.insert(payload)
    print('%d documents inserted in myDB.pulltion' % (len(payload)))
    print(newData)

def foo(city):
    newData = fetchNewData(city= city)
    if collection.find({'date': newData['date'][0]}).count() == 0:
        insertNewData(newData,collection,city)
    else: print("Data for today already inserted.")
if __name__ == "__main__":
    #INIT DATABASE
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb =  myclient["myDB"]
    collection = mydb["pollution"]

    # #INSERT HISTORICAL DATA IN DB
    # collection.drop()
    # collection = mydb["pollution"]
    # nbr =  mongoimport("paris-air-quality.csv",collection,"Paris")
    # print('%d documents inserted in myDB.pollution' % (nbr))
    for x in collection.find({'ville': {'$regex' : 'Beijing'}}):
        print(x)
    # foo("beijing")
    
    # #INSERT NEW DAILY DATA ONLY IF NOT ALREADY EXISTS
    # schedule.every().hours.do(foo())
    
    
    
    # see if there is new data every x days.
    