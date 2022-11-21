import yfinance as yf

#not working
# msft = yf.Ticker("NSE:ITC")
msft = yf.Ticker("MSFT")

# get stock info
print(msft.info)

# get historical market data
hist = msft.history(period="5d")