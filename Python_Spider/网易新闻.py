# 创建时间: 2021/4/12 14:50

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
# 获取随机请求头
headers = {"user-Agent": ua.random}


def GetTitle(url, headers=headers):
    """获取新闻标题"""
    html = requests.get(url, headers=headers)
    html.encoding = "utf-8"
    bs = BeautifulSoup(html.content,features="lxml")
    return bs


def SaveTitle(url):
    """保存到Excel"""
    import  re
    print(GetTitle(url).title)
    titleList = GetTitle(url).find_all(name="a",href=re.compile("article"),text= re.compile("(\w+)"))
    print(len(titleList))
    return titleList


if __name__ == '__main__':
    url = 'https://news.163.com/'

    for i in  SaveTitle(url):
         print(i.text,i.get('href'))
         print()
