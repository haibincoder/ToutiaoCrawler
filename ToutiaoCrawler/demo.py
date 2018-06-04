import requests
from kombu.utils import json


def toutiao_news_api(url):
    toutiao_data = requests.get(url).text

    data = json.loads(toutiao_data)
    items = data['data']

    link_head = 'http://toutiao.com'

    for n in items:
        print(n)
        if 'title' in n and n['tag'] != 'ad':
            print(n['title'])
            print(n['tag'])
            print(n['source'])
            print(link_head + n['source_url'])


keyword = '手机'
url = 'https://toutiao.com/search_content/?offset=0&format=json&keyword=' + keyword + '&autoload=true&count=20&cur_tab=1&from=search_tab'
print(url)
toutiao_news_api(url)