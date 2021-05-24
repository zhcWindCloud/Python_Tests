"""
@Time    : 2021/5/22 14:35
@Author  : ZHC
@FileName: IP代理.py
@Software: PyCharm
"""

import requests

from lxml import etree  # lxml 是c语言的库，效率非常高

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}



def IS_ip(IP, Port):
    """判断IP代理是否有效"""
    import telnetlib

    try:
        telnetlib.Telnet(IP, port=Port, timeout=3)
    except:
        return False
    else:
        return True
if __name__ == '__main__':
    ip_list = []
    for x in range(1, 10):
        url = "https://www.kuaidaili.com/free/inha/{0}/".format(x)
        res = requests.get(url, headers=headers)
        html = etree.HTML(res.text)  # 初始化生成一个XPath解析对象
        result = etree.tostring(html, encoding='utf-8')  # 解析对象输出代码
        for i in range(1, 16):
            IP = html.xpath('//*[@id="list"]/table/tbody/tr[' + str(i) + ']/td[1]/text()')[0]
            # 一个列表
            port = html.xpath('//*[@id="list"]/table/tbody/tr[' + str(i) + ']/td[2]/text()')[0]
            if (IS_ip(IP, port)):
                ip_list.append(IP + ":" + port)


print(ip_list)

