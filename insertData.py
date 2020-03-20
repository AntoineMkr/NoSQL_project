import json,csv
import pandas as pd
from getData import fetchNewData 
from pymongo import MongoClient

def mongoimport(csv_path,coll):
    data = pd.read_csv(csv_path)
    data = data.sort_values(by=['date'], ascending = False)
    data.reset_index(inplace=True)
    del data['index']
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)
    return coll.count()

def insertNewData(newData, collection):

    return True

if __name__ == "__main__":
    #INIT DATABASE
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb =  myclient["myDB"]
    collection = mydb["pollution"]

    #INSERT HISTORICAL DATA IN DB
    # collection.drop()
    # collection = mydb["pollution"]
    # print('%d documents inserted in myDB.pollution' % (mongoimport("paris-air-quality.csv",collection)))
    x = collection.find_one()

    print(x)
    # see if there is new data every x days.
    # newData = fetchNewData()