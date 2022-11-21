from nsetools import Nse
import time
from nsepy import get_history
from nsepy import get_quote
from datetime import date
nse = Nse()
# print nse
# q = nse.get_quote('infy fut oct') # it's ok to use both upper or lower case for codes.
# from pprint import pprint # just for neatness of display
# pprint(q)



# data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
# data[['Close']].plot()
# print(type(data))
# print(data)

while(True):
    symbol_list =["CIPLA", "ITC"]
    data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
    # data[['Close']].plot()
    data = get_quote("ITC")
    print(type(data))
    print(data)
    print("going to sleep")
    time.sleep(5)
