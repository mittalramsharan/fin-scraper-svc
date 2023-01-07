import requests

import pandas as pd
from bs4 import BeautifulSoup


# url = "https://www1.nseindia.com/products/content/derivatives/equities/fo_underlying_home.htm"

# response = requests.get(url)
# response.text[:100]
# html_string = response.text[:100]

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
            'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

main_url = "https://www1.nseindia.com/"
response = requests.get(main_url, headers=headers)
#print(response.status_code)
cookies = response.cookies

url = "https://www1.nseindia.com/products/content/derivatives/equities/fo_underlying_home.htm"
html_string = requests.get(url, headers=headers, cookies=cookies)

soup = BeautifulSoup(html_string.json(), 'lxml') # Parse the HTML as a string

table = soup.find_all('table')[0] # Grab the first table


row_marker = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        new_table.iat[row_marker,column_marker] = column.get_text()
        column_marker += 1

print(new_table)