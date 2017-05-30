import pymysql.cursors

from ToutiaoCrawler.Model.news import News

#获取数据库连接
def get_connect():
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='toutiao',
        charset='utf8'
    )
    return connect


#插入toutiao_news
def insert_data(news_list):
    try:
        connect = get_connect()
        cursor = connect.cursor()

        for news in news_list:
            sql = "INSERT INTO toutiao_news(title, tag, source, source_url, keyword, keywords) VALUES ( %s,%s,%s,%s,%s,%s)"
            # data = {news.title, news.tag, news.source, news.source_url, news.keyword, news.keywords}
            cursor.execute(sql, (news.title, news.tag, news.source, news.source_url, news.keyword, news.keywords))
        connect.commit()

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connect.close()

def insert_data_apinews(news_list):
    try:
        connect = get_connect()
        cursor = connect.cursor()

        for news in news_list:
            sql = "INSERT INTO news_api(title, tag, source, source_url) VALUES ( %s,%s,%s,%s)"
            # data = {news.title, news.tag, news.source, news.source_url, news.keyword, news.keywords}
            cursor.execute(sql, (news.title, news.tag, news.source, news.source_url))
        connect.commit()
        print('successful')

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connect.close()


def select_url():
    arrList = []
    try:
        connect = get_connect()
        cursor = connect.cursor()
        print("connection")
        sql = "SELECT id,source_url FROM toutiao_news"
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
        sql = "UPDATE toutiao_news SET content = %s WHERE id = %s"
        cursor.execute(sql, (news.content, news.id))
        connect.commit()
    except Exception as e:
        print(e)

#查询头条新闻，id,title,keywords，返回arraylist
def select_toutiao_news(keyword):
    arrList = []
    try:
        connect = get_connect()
        cursor = connect.cursor()
        sql = "SELECT id,title,keywords FROM toutiao_news where keyword = %s"
        cursor.execute(sql, keyword)
        result = cursor.fetchall()
        for row in result:
            # print(row[0])
            news = News()
            news.id = row[0]
            news.title = row[1]
            arrList.append(news)
    except Exception as e:
        print(e)
    finally:
        return arrList

#更新距离算法
def update_distance(distance):
    try:
        connect = get_connect()
        cursor = connect.cursor()

        for item in distance:
            sql = "UPDATE toutiao_news SET distance = distance + %s WHERE id = %s"
            cursor.execute(sql, (distance[item], item))
        connect.commit()

    except Exception as e:
        print(e)

#查询头条新闻链接，返回set
def select_source_url_returnset():
    arrList = set()
    try:
        connect = get_connect()
        cursor = connect.cursor()
        print("connection mysql successful")
        sql = "SELECT source_url FROM toutiao_news"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            # print(row[0])
            arrList.add(row[0])
    except Exception as e:
        print(e)
    finally:
        return arrList