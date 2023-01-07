import pandas as pd
import pandas_datareader.data as web
import numpy as np

FB = web.YahooOptions('TCS')
print(FB.head())