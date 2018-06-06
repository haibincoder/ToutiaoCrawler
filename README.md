# ToutiaoCrawler
#### 接口示例：
2018.6.5更新 </br>
'https://toutiao.com/search_content/?offset=0&format=json&keyword='+keyword+'&autoload=true&count=20&cur_tab=1&from=search_tab'   </br>
keywordk:搜索的关键字  </br>
count:本页文章数量 </br>
cur_tab:当前页数 </br>

#### Demo：
ToutiaoCrawler\ToutiaoCrawler\demo.py
这里可以根据需求获取文章标题、标签、内容链接
#### Demo效果以及调试示例：
![](https://raw.githubusercontent.com/haibincoder/ToutiaoCrawler/master/ToutiaoCrawler/demo.png)
![](https://raw.githubusercontent.com/haibincoder/ToutiaoCrawler/master/ToutiaoCrawler/demo2.png)

***
--------------------以下为项目代码，部分接口已失效--------------------
* 需要python3.6版本</br>
* 首先安装需要的包，使用pycharm打开会自动安装 </br>

1. 创建数据库和数据表ToutiaoCrawler/toutiao.sql；配置mysql连接ToutiaoCrawler/ToutiaoCrawler/Utils/Util.py
2. 运行Crawler/get_toutiao_news_byapi.py 获取新闻列表
3. 运行Crawler/get_toutiao_content_byapi.py 获取新闻内容</br>
* (到这一步数据库已经有内容了) </br>

4. 运行Analysis/levenshtein.py 计算编辑距离
5. 运行svd/svd.py 奇异值分解
6. 运行svd/test_kmeans.py 进行聚类分析和绘图

* 如果需要txt文件，执行Utils/list_to_txt.py
  

