# coding:utf-8

from numpy import *

from ToutiaoCrawler.Utils.svd_utils import select_keywords, select_news_id


def loadData():
    arrList = select_keywords()
    contentList = select_news_id()

    print("keywords list length:",len(arrList))
    print(arrList)
    print("news list length:",len(contentList))

    return [[1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [3, 3, 3, 0, 0],
            [5, 5, 3, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 6, 6]]


data = loadData()

u, sigma, vt = linalg.svd(data)

print(sigma)

sig3 = mat([[sigma[0], 0, 0],
            [0, sigma[1], 0],
            [0, 0, sigma[2]]])

print(u[:, :3] * sig3 * vt[:3, :])

