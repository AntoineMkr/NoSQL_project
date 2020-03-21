import os
import json,csv
import pandas as pd
from getData import fetchNewData 
from pymongo import MongoClient
import schedule
import time
from datetime import date


def printTodaysData(collection):
    today = date.today()
    today = str(today)
    today = today.replace('-','/')
    if today[5] == '0': 
        today = today[:5] + today[6:]
    for obj in collection.find({'date': today}):
        print(obj)

