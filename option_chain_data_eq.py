import requests
import time
# from db_config import get_db 
from pymongo import MongoClient


def get_db():
    try:
        conn = MongoClient()
        db = conn.dump2data
        print("Connected successfully!!!")
        return db.pageind_oc_2
    except Exception as e:
        print("Could not connect to MongoDB" , e)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
            'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

main_url = "https://www.nseindia.com/"
response = requests.get(main_url, headers=headers)
#print(response.status_code)
cookies = response.cookies

url = "https://www.nseindia.com/api/option-chain-indices?symbol=PAGEIND"
while(True):
    bank_nifty_oi_data = requests.get(url, headers=headers, cookies=cookies)
    get_db().insert_one(bank_nifty_oi_data.json())
    time.sleep(10)
# print(bank_nifty_oi_data.json())