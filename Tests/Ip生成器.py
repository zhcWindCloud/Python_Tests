"""
@Time    : 2021/5/11 13:42
@Author  : ZHC
@FileName: Ip生成器.py
@Software: PyCharm
"""

import os
import random
import time
from datetime import datetime
from fake_useragent import  UserAgent
import requests


def getip(ip, count):
    count = int(count)
    ip2 = int(ip.split('.')[-2])
    ip1 = int(ip.split('.')[-1])
    ip_before = '%s.%s' % (ip.split('.')[0], ip.split('.')[1])
    IP_list=[]
    for i in range(0, count):
        new_ip1 = ip1 + i
        if 11 <= new_ip1 <= 254:
            IP_list.append('{}.{}.{}'.format(ip_before, str(ip2), str(new_ip1)))
        else:
            new_ip2 = ip2 + int(new_ip1 / 254)
            new_ip1 = new_ip1 % 254 + 10
            IP_list.append('{}.{}.{}'.format(ip_before, str(new_ip2), str(new_ip1)))

    return  IP_list
'''
测试查找IP地址'''
def GetIPAdress(IP):
    UserAgent
    url = "http://api.guajicun.com/GetIp/default.aspx?queryIp="+str(IP)
    response = requests.get(url)
    return response

def GetRandomDateTime(year=None):
    if year:
        month = random.randint(1, 12)
        if month in [1, 3, 5]:
            date = datetime(year, month, random.randint(1, 31), random.randint(0, 23), random.randint(0, 59),
                            random.randint(0, 59))
            return date
        elif month == 2:
            return datetime(year, month, random.randint(1, 28), random.randint(0, 23),  random.randint(0, 59),
                            random.randint(0, 59))
        elif month == 4:
            return datetime(year, random.randint(1, 12), random.randint(1, 30), random.randint(0, 23),  random.randint(0, 59),
                        random.randint(0, 59))

def GetBroser():
    l = ["QQQBrowser 6.2","QQQBrowser 10.7.4313.400","Chrome 90.0.4430.93","Edge 90.0.818.56","safari 4.0"]
    new_list = ["Android 32位","Android 64位","Win10 64位","Win7 64位","Win7 32位","Win8 64位","Win8 32位"]
    return random.choice(l),random.choice(new_list)

if __name__ == '__main__':
    data_list=[]
    for x in  getip('101.26.31.147', 10):
        IP_Dict = GetIPAdress(x).json()["data"][0]
        data_list.append(IP_Dict.get("ip"))
        data_list.append(IP_Dict.get("country")+","+IP_Dict.get("region")+","+IP_Dict.get("city"))
        data_list.append("中国"+IP_Dict.get("as"))
        data_list.append(GetRandomDateTime(2021))

        time.sleep(2)
    print(data_list)