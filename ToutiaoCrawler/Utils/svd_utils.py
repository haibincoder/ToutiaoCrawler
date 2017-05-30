from ToutiaoCrawler.Model.news import News
from ToutiaoCrawler.Utils.Util import get_connect

#查询头条新闻自带关键词
def select_keywords():
    arrList = set()
    try:
        connect = get_connect()
        cursor = connect.cursor()
        print("connection mysql successful")
        sql = "SELECT keywords FROM toutiao_news"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            # print(row[0])
            keywords = row[0].split(',')
            for key in keywords:
                arrList.add(key)
    except Exception as e:
        print(e)
    finally:
        return arrList

#查询头条id和content
def select_news_id():
    arrList = set()
    try:
        connect = get_connect()
        cursor = connect.cursor()
        print("connection mysql successful")
        sql = "SELECT id,content FROM toutiao_news"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            # print(row[0])
            news = News()
            news.id = row[0]
            news.content = row[1]
            arrList.add(news)
    except Exception as e:
        print(e)
    finally:
        return arrList