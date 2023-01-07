from nsetools import Nse
import time
from nsepy import get_history
from nsepy import get_quote
from nsepy.live import get_option_chain_table
from datetime import date
import tkinter
from tkinter import messagebox

from pymongo import MongoClient


def get_db(str):
    try:
        conn = MongoClient()
        db = conn.dump2data
        print("Connected successfully!!!")
        return db.collection(str)
    except Exception as e:
        print("Could not connect to MongoDB" , e)


nse = Nse()
# print(get_option_chain_table('SBIN'))
# print nse
# q = nse.get_quote('infy fut oct') # it's ok to use both upper or lower case for codes.
# from pprint import pprint # just for neatness of display
# pprint(q)



# data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
# data[['Close']].plot()
# print(type(data))
# print(data)
count = 0;
while(True):
    symbol_list =["CIPLA", "ITC"]
    # data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
    # data[['Close']].plot()
    data = get_quote("CIPLA")
    count = count + 1
    print(count)
    print(type(get_db("CIPLA")))
    # get_db("CIPLA").insert_one(data)
    time.sleep(10)
    # print(type(data))
    # print(data)
    # print("going to sleep")
    # time.sleep(5000)
    # root = tkinter.Tk()
    # root.withdraw()

# Message Box
    # messagebox.showinfo("Title", "Message")


