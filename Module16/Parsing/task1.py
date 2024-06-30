import csv
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def write_cmp_top():
    url = "https://coinmarketcap.com/"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to load page")

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='cmc-table')
    if not table:
        raise Exception("No table found on the page")

    print(table)


write_cmp_top()
