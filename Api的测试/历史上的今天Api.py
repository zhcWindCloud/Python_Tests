"""
@Time    : 2021/5/15 0:43
@Author  : ZHC
@FileName: 历史上的今天Api.py
@Software: PyCharm
"""
import requests
"""
历史上的今天API请求方式
GET
"""
def GetReslut():
    url = 'http://api.wpbom.com/api/today.php'
    content = requests.get(url)
    content.encoding ='utf-8'
    print(content.text)



if __name__ == '__main__':
    GetReslut()

