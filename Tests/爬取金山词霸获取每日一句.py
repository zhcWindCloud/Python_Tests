import requests
from bs4 import BeautifulSoup

"""获取金山词霸每日一句，英文和翻译"""
url = "http://open.iciba.com/dsapi/"
r = requests.get(url)
content = r.json()['content']
note = r.json()['note']
print(content, note)
def GetArtitle():
    url = 'http://www.59xihuan.cn/index_1.html'
    h = requests.get(url)
    html = h.text
    news_bf = BeautifulSoup(html, "html.parser")
    msg = news_bf.find('div', class_='pic_text1')
    news = msg.text
    return news
