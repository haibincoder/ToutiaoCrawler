import requests
from bs4 import BeautifulSoup

from ToutiaoCrawler.Model.news import News
from ToutiaoCrawler.Utils.Util import get_connect


def select_url():
    arrList = []
    try:
        connect = get_connect()
        cursor = connect.cursor()
        print("connection")
        sql = "SELECT id,source_url FROM news_api"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            # print(row[0])
            news = News()
            news.id = row[0]
            news.source_url = row[1]
            arrList.append(news)
    except Exception as e:
        print(e)
    finally:
        return arrList

def update_content(news):
    try:
        connect = get_connect()
        cursor = connect.cursor()
        sql = "UPDATE news_api SET content = %s WHERE id = %s"
        cursor.execute(sql,(news.content,news.id))
        connect.commit()
    except Exception as e:
        print(e)

def get_content(url):
    content = ' '
    try:
        data = requests.get(url).text
        content_data = BeautifulSoup(data, "lxml")
        content = content_data.select('div.article-content')[0].get_text()
        return content
    except Exception as ex:
        print()
    finally:
        return content
#get_content("http://www.toutiao.com/a6417384497750311169/")

urlList = select_url()
for n in urlList:
    print(n.source_url)
    n.content =  get_content(n.source_url)
    print(n.content)
    print(n.id)
    update_content(n)


