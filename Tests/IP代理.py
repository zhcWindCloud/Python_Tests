"""
@Time    : 2021/5/16 18:44
@Author  : ZHC
@FileName: IP代理.py
@Software: PyCharm
"""

# 用到的库

import requests


# 写入获取到的ip地址到proxy

proxy = {


    'http': "212.32.242.111:3128",

}

# 用百度检测ip代理是否成功

url = 'https://www.baidu.com/s?'

# 请求网页传的参数

params = {

    'wd': 'ip地址'

}

# 请求头

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}

# 发送get请求

response = requests.get(url=url, headers=headers, params=params, proxies=proxy,timeout=5)

# 获取返回页面保存到本地，便于查看

with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
