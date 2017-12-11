# ToutiaoCrawler

python3.6版本，需要配置mysql连接
首先安装需要的包，pycharm打开会自动安装

1. 创建数据库和数据表ToutiaoCrawler/toutiao.sql
2. 运行Crawler/get_toutiao_news_byapi.py 获取新闻列表
3. 运行Crawler/get_toutiao_content_byapi.py 获取新闻内容
到这一步数据库已经有记录了

4. 运行Analysis/levenshtein.py 计算编辑距离
5. 运行svd/svd.py 奇异值分解
6. 运行svd/test_kmeans.py 进行聚类分析和绘图

  如果需要txt文件，执行Utils/list_to_txt.py
  

