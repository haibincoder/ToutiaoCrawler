import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Program Files (x86)\Google\ChromeDriver\chromedriver.exe')
driver.get('https://www.toutiao.com/')
#print(driver.page_source)
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)

time.sleep(5)
ele = driver.find_element_by_class_name('feedBox')
print(ele.text)


def get_page(url):
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\ChromeDriver\chromedriver.exe")
    driver.get(url)
    driver.execute_script("window.scrollBy(0, 5000)", "")
    time.sleep(3)
    page = driver.page_source
    driver.close()
    return page

def get_news(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollBy(0, 5000)", "")
    time.sleep(3)
    page = driver.page_source
    driver.close()

    link_head = "http://toutiao.com"
    soup = BeautifulSoup(page,"lxml")
    item = soup.select("div.wcommonFeed li")

    for n in item:
        print(n.text)
        link = n.select("a")
        if len(link) >= 5:
            print(link_head + link[0]["href"])
            print(link_head + "/" + link[1]["href"])
            print(link_head + link[2]["href"])
            print(link_head + link[3]["href"])
            print(link_head + link[4]["href"])

    print(len(item))