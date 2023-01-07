from nsetools import Nse
import time
from nsepy import get_history
from nsepy import get_quote
from nsepy.live import get_option_chain_table
from datetime import date
import tkinter
from tkinter import messagebox
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
    data = get_quote("ITC")
    count = count + 1
    print(count)
    # print(type(data))
    # print(data)
    # print("going to sleep")
    # time.sleep(5000)
    # root = tkinter.Tk()
    # root.withdraw()

# Message Box
    # messagebox.showinfo("Title", "Message")


