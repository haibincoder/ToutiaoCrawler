# coding：utf-8
import random

import requests
import json

from ToutiaoCrawler.Model.keyword import keyword
from ToutiaoCrawler.Model.news import News

from ToutiaoCrawler.Utils.Util import insert_data, insert_data_apinews

def toutiao_news_api(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Referer': 'https://www.toutiao.com/'
    }
    toutiao_data = requests.get(url, headers=headers, allow_redirects=True).text

    data = json.loads(toutiao_data)
    global max_behot_time
    max_behot_time = data['next']['max_behot_time']
    items = data['data']

    news_list = []
    link_head = 'https://www.toutiao.com'

    for n in items:
        if 'title' in n and n['tag'] != 'ad':
            news = News()
            news.title = n['title']
            print(news.title)
            news.tag = n['tag']
            news.source = n['source']
            news.source_url = link_head + n['source_url']

            news_list.append(news)
            #print(news.title, news.source_url, news.source, news.keyword, news.keywords)

    return news_list

global max_behot_time
max_behot_time = 0
while(1):
    print(max_behot_time)
    url = 'https://www.toutiao.com/api/pc/feed/?category=news_feed&utm_source=toutiao&widen=1&max_behot_time={}&max_behot_time_tmp={}&tadrequire=true&as=A1B5D9F152FBC03&cp=59123B3CE0B3FE1'.format(max_behot_time, max_behot_time)
    news_list = toutiao_news_api(url)
    #print(len(news_list))
    #insert_data_apinews(news_list)
