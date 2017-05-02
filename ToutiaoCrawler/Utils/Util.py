import pymysql.cursors

# 连接数据库
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

def insert_data(news_list):
    try:
        connect = get_connect()
        cursor = connect.cursor()

        for news in news_list:
            sql = "INSERT INTO news(title, tag, source, source_url, keyword, keywords) VALUES ( %s,%s,%s,%s,%s,%s)"
            #data = {news.title, news.tag, news.source, news.source_url, news.keyword, news.keywords}
            cursor.execute(sql, (news.title, news.tag, news.source, news.source_url, news.keyword, news.keywords))
        connect.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connect.close()
