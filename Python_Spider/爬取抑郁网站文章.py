"""
@Time    : 2021/5/15 12:08
@Author  : ZHC
@FileName: 爬取抑郁网站文章.py
@Software: PyCharm
"""
import re
import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def GetArticleTitle(headers):
    url = ''
    title_dict = {}
    imgData_list = []
    for x in range(9):
        if x == 0:
            url = 'http://www.yiyuzheng.com.cn/news/index.html'
        else:
            url = 'http://www.yiyuzheng.com.cn/news/index_{0}.html'.format(x + 1)
        ht = requests.get(url, headers=headers)
        ht.encoding = 'utf-8'
        bs = BeautifulSoup(ht.text, 'lxml')
        soup_list = bs.findAll("a", attrs={"title": re.compile('\w+')})
        for soup in soup_list:

            if soup.get("title") == 'Total record':
                pass
            else:
                img = soup.find("img", attrs={"alt": re.compile('\w+')})
                img_list = []
                img_list.append("http://www.yiyuzheng.com.cn" + soup.get("href"))
                if img:
                    if re.compile('http').search(img.get("src")):
                        imgData_list.append(img.get("src"))
                    else:
                        img_list.append("http://www.yiyuzheng.com.cn" + img.get("src"))

                    title_dict[soup.get("title")] = img_list

                    # print(soup.get("title"),"http://www.yiyuzheng.com.cn" + soup.get("href"),img.get("src"))

    print(title_dict)

    return imgData_list


def SaveImg(ArticleTitle, headers):
    from  datetime import datetime
    import random
    name_list =[]
    for url in ArticleTitle:
        dt = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(0, 9))
        name_list.append(dt)
        html = requests.get(url, headers)
        html.encoding ='utf-8'
        path =r"E:\Img\{0}.jpg".format(dt)
        with open(path,"wb+") as f:
            f.write(html.content)
        time.sleep(1)
    print(name_list)



def GetArticleDetail(ArticleTitle, headers):
    title_dict = {}
    for title, url in ArticleTitle.items():
        html = requests.get(url, headers)
        html.encoding = 'utf-8'
        bs = BeautifulSoup(html.text, 'lxml')
        soup = bs.find("div", attrs={"class": "htmlcontent"})
        title_dict[title] = soup.get_text().strip()


if __name__ == "__main__":
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    ArticleTitle = GetArticleTitle(headers)
    SaveImg(ArticleTitle, headers)
    print(ArticleTitle)
