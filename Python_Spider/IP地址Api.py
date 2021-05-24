# 创建时间: 2021/4/2 9:59

import socket

from fake_useragent import UserAgent

import requests


ua = UserAgent()
headers = {'User-Agent': ua.random}

def get_mac():
    import uuid
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:].upper()
    print(mac)
    print("%s:%s:%s:%s:%s:%s" % (mac[0:2], mac[2:4], mac[4:6], mac[6:8], mac[8:10], mac[10:]))

def GetOutIP():
    try:
        url = "https://sapi.k780.com"
        data = {'app': 'ip.local', 'appkey': '10003',
                'sign': 'b59bc3ef6191eb9f747dd4e83c99f2a4', 'format': 'json',
                }
        headers = {'User-Agent': ua.random}
        response = requests.post(url, headers=headers, data=data)
        return response.json().get("result")
    except Exception as  e:
        print(e)
    return e
print("in承诺",GetOutIP())

'''
测试查找IP地址'''
def SeachIPAdress():
    url = "https://sapi.k780.com"
    data = {
        'app': 'ip.local',
        'appkey': '10003',
        'sign': 'b59bc3ef6191eb9f747dd4e83c99f2a4',
        'format': 'json',
    }
    headers = {
        'User-Agent': ua.random,

    }
    #response = requests.get(url)
    response = requests.post(url, headers=headers,data=data)
    return response


print(SeachIPAdress().json().get("result"))



'''
测试查找IP地址'''
def GetIPAdress():
    url = "http://api.guajicun.com/GetIp/default.aspx?queryIp=39.144.38.49"
    response = requests.get(url)
    return response

print( GetIPAdress().json())
IP_Dict = GetIPAdress().json()["data"][0]
print(IP_Dict.get("ip"))
print(IP_Dict.get("country"))
print(IP_Dict.get("region"))
print(IP_Dict.get("city"))
print(IP_Dict.get("as"))

att = IP_Dict.get("country")+','+IP_Dict.get("region")+','+IP_Dict.get("city")

print(att)
chr

def GetIP():
    headers = {'User-Agent': ua.random}

    url = 'http://ip-api.com/json'

    formdata = {'lang': "zh-CN"}

    r = requests.get(url, headers=headers, params=formdata).json()






def GetlocalhostIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 8080))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


"""
import socket

# 查看当前主机名
print('当前主机名称为 : ' + socket.gethostname())

# 根据主机名称获取当前IP
print('当前主机的IP为: ' + socket.gethostbyname(socket.gethostname()))

# Mac下上述方法均返回127.0.0.1
# 通过使用socket中的getaddrinfo中的函数获取真真的IP

# 下方代码为获取当前主机IPV4 和IPV6的所有IP地址(所有系统均通用)
addrs = socket.getaddrinfo(socket.gethostname(), None)

for item in addrs:
    print(item)

# 仅获取当前IPV4地址
print('当前主机IPV4地址为:' + [item[4][0] for item in addrs if ':' not in item[4][0]][0])

# 同上仅获取当前IPV4地址
for item in addrs:
    if ':' not in item[4][0]:
        print('当前主机IPV4地址为:' + item[4][0])
        break
"""
