import Levenshtein

from ToutiaoCrawler.Model.keyword import keyword
from ToutiaoCrawler.Utils.Util import select_toutiao_news, update_distance

#编辑距离算法
def distance(keyword):
    arrayList = select_toutiao_news(keyword)
    distance = {}
    for n in range(0, len(arrayList)):
        for item in arrayList:
            temp = Levenshtein.distance(arrayList[n].title, item.title)
            distance[item.id] = temp

        # result = sorted(distance.items(), key=lambda item: item[1], reverse=True)

        # #print(result)
        # idList = []
        #
        # length = n
        # if n > 50:
        #     length = 50
        #
        # for item in range(0, length):
        #     idList.append(str(result[item][0]))
        #     #update_distance(result[item][0])

        # for item in distance:
        #     print(item)
        #     print(distance[item])

        update_distance(distance)
        #print("完成更新：" + keyword + " " + str(n))


for k in keyword.keyword:
    distance(k)
    print("更新完成：" + k)
