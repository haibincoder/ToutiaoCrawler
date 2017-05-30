import requests
from bs4 import BeautifulSoup

from ToutiaoCrawler.Model.news import News
from ToutiaoCrawler.Utils.Util import select_url, update_content


#获取今日头条content
def get_content(url):
    content = ' '
    try:
        data = requests.get(url).text
        content_data = BeautifulSoup(data, "lxml")
        content = content_data.select('div.article-content')[0].get_text()
    except Exception as ex:
        print()
    finally:
        return content
#get_content("http://www.toutiao.com/a6417384497750311169/")

#获取链接地址
urlList = select_url()
for n in urlList:
    print(n.source_url)
    n.content =  get_content(n.source_url)
    print(n.content)
    print(n.id)
    update_content(n)


