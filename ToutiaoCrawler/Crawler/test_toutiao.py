import json

import requests
from selenium import webdriver
from bs4 import BeautifulSoup


url = 'http://www.toutiao.com/api/pc/feed/?category=__all__&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1B5F9F067E5D91&cp=590705CD29410E1'
wbdata = requests.get(url).text

data = json.loads(wbdata)
news = data['data']

for n in news:
    if "source" in n:
        print(n['title'])