# ToutiaoCrawler

1. python3.6版本，需要配置mysql连接
2. 首先安装需要的包，pycharm打开会自动安装

3. 创建数据库和数据表ToutiaoCrawler/toutiao.sql
4. 运行Crawler/get_toutiao_news_byapi.py 获取新闻列表
5. 运行Crawler/get_toutiao_content_byapi.py 获取新闻内容(到这一步数据库已经有内容了)

6. 运行Analysis/levenshtein.py 计算编辑距离
7. 运行svd/svd.py 奇异值分解
8. 运行svd/test_kmeans.py 进行聚类分析和绘图

  如果需要txt文件，执行Utils/list_to_txt.py
  

