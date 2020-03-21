import os
import json,csv
import pandas as pd
from getData import fetchNewData 
from pymongo import MongoClient
import schedule
import time
from bson.objectid import ObjectId

from readData import *


    
def main_menu():
  os.system('clear')

  print("Que voulez-vous faire ?")
  print("1. Voir les données brutes")
  print("2. Regarder la pollution d'aujourd'hui")

  print()
  print ("0. Quit")

  choice = input(" >>  ")
  exec_menu(choice)

  return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Entrée invalide, veuillez réessayer.\n")
            menu_actions['main_menu']()
    return

def liste_currencies():
    print()
    print ("9. Back")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return



# Back to main menu
def back():
    menu_actions['main_menu']()
 
# Exit program
def exit():
    sys.exit()

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': liste_currencies,


    '9': back,
    '0': exit,
}

if __name__ == "__main__":
        # Création des threads
    # main_menu()
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb =  myclient["myDB"]
    collection = mydb["pollution"]

    
    
