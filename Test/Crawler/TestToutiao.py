# coding：utf-8
import requests
import json

url = 'http://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E5%B0%8F%E5%BA%B7%E7%A4%BE%E4%BC%9A&autoload=true&count=20&cur_tab=1'
wbdata = requests.get(url).text

data = json.loads(wbdata)
news = data['data']

for n in news:
    if 'title' in n:
      title = n['title']
      source = n['source']
      url = n['article_url']
      keyword = n['keywords']
      print(title,url,keyword,source)