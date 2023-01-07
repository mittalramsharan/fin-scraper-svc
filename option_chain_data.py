import requests
import time
from db_config import get_db 
from pymongo import MongoClient


# def get_db():
#     try:
#         conn = MongoClient()
#         db = conn.dump2data
#         print("Connected successfully!!!")
#         return db.pageind_oc_2
#     except Exception as e:
#         print("Could not connect to MongoDB" , e)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
            'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

main_url = "https://www.nseindia.com/"
response = requests.get(main_url, headers=headers)
#print(response.status_code)
cookies = response.cookies
symbol_list =["AARTIIND","ABB","ABBOTINDIA","ABCAPITAL","ABFRL","ACC","ADANIENT","ADANIPORTS","ALKEM","AMARAJABAT","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASIANPAINT","ASTRAL","ATUL","AUBANK","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BALKRISIND","BALRAMCHIN","BANDHANBNK","BANKBARODA","BATAINDIA","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD","BPCL","BRITANNIA","BSOFT","CANBK","CANFINHOME","CHAMBLFERT","CHOLAFIN","CIPLA","COALINDIA","COFORGE","COLPAL","CONCOR","COROMANDEL","CROMPTON","CUB","CUMMINSIND","DABUR","DALBHARAT","DEEPAKNTR","DELTACORP","DIVISLAB","DIXON","DLF","DRREDDY","EICHERMOT","ESCORTS","EXIDEIND","FEDERALBNK","FSL","GAIL","GLENMARK","GMRINFRA","GNFC","GODREJCP","GODREJPROP","GRANULES","GRASIM","GUJGASLTD","HAL","HAVELLS","HCLTECH","HDFC","HDFCAMC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDCOPPER","HINDPETRO","HINDUNILVR","HONAUT","IBULHSGFIN","ICICIBANK","ICICIGI","ICICIPRULI","IDEA","IDFC","IDFCFIRSTB","IEX","IGL","INDHOTEL","INDIACEM","INDIAMART","INDIGO","INDUSINDBK","INDUSTOWER","INFY","INTELLECT","IOC","IPCALAB","IRCTC","ITC","JINDALSTEL","JKCEMENT","JSWSTEEL","JUBLFOOD","KOTAKBANK","L&TFH","LALPATHLAB","LAURUSLABS","LICHSGFIN","LT","LTI","LTIM","LTTS","LUPIN","M&M","M&MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MCX","METROPOLIS","MFSL","MGL","MOTHERSON","MPHASIS","MRF","MUTHOOTFIN","NATIONALUM","NAUKRI","NAVINFLUOR","NESTLEIND","NMDC","NTPC","OBEROIRLTY","OFSS","ONGC","PAGEIND","PEL","PERSISTENT","PETRONET","PFC","PIDILITIND","PIIND","PNB","POLYCAB","POWERGRID","PVR","RAIN","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SBICARD","SBILIFE","SBIN","SHREECEM","SIEMENS","SRF","SRTRANSFIN","SUNPHARMA","SUNTV","SYNGENE","TATACHEM","TATACOMM","TATACONSUM","TATAMOTORS","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TVSMOTOR","UBL","ULTRACEMCO","UPL","VEDL","VOLTAS","WHIRLPOOL","WIPRO","ZEEL","ZYDUSLIFE"]
indecis_symbol_list =["NIFTY", "BANKNIFTY", "FINNIFTY", "MIDCPNIFTY"]
def get_option_chain_data(headers, cookies, symbol, url_without_symbol, db):
    no_error = True
    while(no_error):
        try:
            url = url_without_symbol + symbol
            bank_nifty_oi_data = requests.get(url, headers=headers, cookies=cookies)
            get_db(symbol, db).insert_one(bank_nifty_oi_data.json())
            print(symbol)
            # print(bank_nifty_oi_data.json())
            no_error = False
        except Exception as err:
            no_error = True
            time.sleep(5)
            try:
                cookies = requests.get(main_url, headers=headers)
            except:
                print("error in re cookies")
            print(err)
            print ("error in index_symbol " + symbol)

while(True):
    for symbol in symbol_list:
        get_option_chain_data( headers, cookies, symbol,"https://www.nseindia.com/api/option-chain-equities?symbol=",  "equties_op_8")
        # try:
        #     url = "https://www.nseindia.com/api/option-chain-equities?symbol=" + symbol
        #     bank_nifty_oi_data = requests.get(url, headers=headers, cookies=cookies)
        #     get_db(symbol, "equties_op_8").insert_one(bank_nifty_oi_data.json())
        #     print(symbol)
        # except Exception as err:
        #     print(err)
        #     print ("error in symbol " + symbol)
    for index_symbol in indecis_symbol_list:
        get_option_chain_data( headers, cookies, index_symbol,"https://www.nseindia.com/api/option-chain-indices?symbol=",  "indices_op_9")
    time.sleep(2)
# print(bank_nifty_oi_data.json())