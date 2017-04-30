import time
from selenium import webdriver
from bs4 import BeautifulSoup

def get_news(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollBy(0, 5000)", "")
    time.sleep(3)
    page = driver.page_source
    driver.close()

    link_head = "http://toutiao.com"
    soup = BeautifulSoup(page,"lxml")
    news = soup.select("div.wcommonFeed li")

    for n in news:
        print(n.text)
        link = n.select("a")
        if len(link) == 1:
            print(link_head + link[0]["href"])
        elif len(link) == 2:
            print(link_head + link[0]["href"])
            print(link[1]["href"])
        elif len(link) >= 3:
            print(link_head + link[0]["href"])
            print(link[1]["href"])
            print(link_head + link[2]["href"])

    print(len(news))

get_news('http://toutiao.com')
