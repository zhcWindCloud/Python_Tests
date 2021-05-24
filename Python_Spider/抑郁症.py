#创建时间: 2021/3/7 17:54

from  bs4 import  BeautifulSoup
import re, requests,warnings
warnings.filterwarnings("ignore")

#url = 'http://minke8.cn/yyz.html'
url = 'http://minke8.cn/yyzcs.html'

html = requests.get(url)

#使用 apparent_encoding获取网页使用的编码
html.encoding = html.apparent_encoding
bs = BeautifulSoup(html.text, "html.parser")

#print(bs.prettify()) # 格式化html结构

soup = bs.find_all('fieldset')
soup = soup[1:len(soup)-1]

for fieldset in soup:
  #  print(fieldset)
    print(fieldset.div.text)
    bs1 = BeautifulSoup(str(fieldset))
    soup1 = bs1.find_all("input")
    for content in soup1:

        print(content)
