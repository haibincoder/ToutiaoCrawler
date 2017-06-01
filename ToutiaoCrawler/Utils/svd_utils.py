from ToutiaoCrawler.Model.news import News
from ToutiaoCrawler.Utils.Util import get_connect


# 查询头条新闻自带关键词
def select_keywords():
    arrList = {}
    try:
        connect = get_connect()
        cursor = connect.cursor()
        print("connection mysql successful")
        sql = "SELECT keywords FROM toutiao_news where keyword='反腐倡廉'"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            # print(row[0])
            keywords = row[0].split(',')
            for key in keywords:
                if key not in arrList:
                    arrList[key] = 1
                else:
                    arrList[key] += 1

    except Exception as e:
        print(e)
    finally:
        return arrList


# 查询头条id和content
def select_news():
    arrList = {}
    try:
        connect = get_connect()
        cursor = connect.cursor()
        print("connection mysql successful")
        sql = "SELECT id,content FROM toutiao_news where keyword='反腐倡廉'"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            # print(row[0])
            id = row[0]
            content = row[1]
            arrList[id] = content
    except Exception as e:
        print(e)
    finally:
        return arrList
