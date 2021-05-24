"""
@Time    : 2021/5/16 19:36
@Author  : ZHC
@FileName: GetIP.py
@Software: PyCharm
"""

# python3
# 国内高匿代理IP网站：http://www.xicidaili.com/nn/
# 爬取首页代理IP地址

from bs4 import BeautifulSoup
import requests
import random

# 获取首页IP列表
def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    # 提取ip列表
    # range()的用法：range(1,5) #代表从1到5(不包含5)
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[5].text.lower() + '://' + tds[1].text + ':' + tds[2].text)
    print(ip_list)
    return ip_list

# 随机获取一个ip
def get_random_ip(ip_list):
    # 随机获取一个ip（从返回的ip列表里面）
    proxy_ip = random.choice(ip_list)
    return proxy_ip

# 测试
if __name__ == '__main__':
    # 国内高匿代理IP
    url = 'http://x.fanqieip.com/index.php?s=/Api/IpManager/adminFetchFreeIpRegionInfoList&uid=16362&ukey=52bb98e447e7a27ac8b7046c86750410&limit=10&format=0&page=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    # 获取首页ip列表
    ip_list = get_ip_list(url, headers=headers)
    # 随机提取一个ip
    ip = get_random_ip(ip_list)
    print('代理ip地址：' + ip)