# coding:utf-8

from numpy import *

from ToutiaoCrawler.Utils.list_to_txt import list_to_txt
from ToutiaoCrawler.Utils.svd_utils import select_keywords, select_news


def isStringLike(anobj):
    try:
        anobj.lower() + anobj + ' '
    except:
        return False
    else:
        return True


def loadData():
    # 获取关键词词典
    arrList = select_keywords()
    print("keywords:",len(arrList))
    # 去除空白字符
    #del arrList[""]
    # 获取新闻
    contentList = select_news()

    # 对关键词进行排序
    sortList = sorted(arrList.items(), key=lambda item: item[1], reverse=True)
    height = 0
    width = len(contentList)
    for item in sortList:
        if item[1] > 0:
            height += 1
    print("height:", height, ";width:", width)

    # 构建二维数组
    keywords = [[0 for col in range(width + 1)] for row in range(height + 1)]

    keywords[0][0] = "news_id"
    i = 1
    for item in sortList:
        if item[1] > 0:
            keywords[i][0] = item[0]
            i += 1

    # 删除空白字符关键词，如果报错则删除这行！！！
    # del keywords[2]

    # 填写news id
    i = 1
    for item in contentList:
        keywords[0][i] = item
        i += 1

    # 统计词频
    for i in range(height):
        if i == 0:
            continue
        key = keywords[i][0]
        for n in range(width):
            if n == 0:
                continue
            id = keywords[0][n]
            content = contentList[id]
            if not isStringLike(content):
                continue
            count = content.count(key)
            keywords[i][n] = count

    # 写入到txt文件
    list_to_txt(keywords,'keywords')

    # 遍历keywords，可能不能显示完全
    for item in keywords:
        print(item)

    # 去除第一行和第一列
    result = [[0 for col in range(width)] for row in range(height)]
    for i in range(height-1):
        if i == 0:
            continue
        for n in range(width-1):
            if n == 0:
                continue
            result[i-1][n-1] = keywords[i][n]

    for item in result:
        print(item)

    return result


data = loadData()

# 奇异值分解
u, sigma, vt = linalg.svd(data)

print(sigma)

# 简化矩阵
sig3 = mat([[sigma[0], 0, 0],
            [0, sigma[1], 0],
            [0, 0, sigma[2]]])

u3 = u[:, :3]

# 保存文件
#list_to_txt(sigma,'sigma')
list_to_txt(u,'u')
list_to_txt(vt,'vt')
list_to_txt(u3,'u3')
