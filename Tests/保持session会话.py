"""
@Time    : 2021/5/24 9:07
@Author  : ZHC
@FileName: 保持session会话.py
@Software: PyCharm
"""

import requests
import time
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
session=requests.Session()  #会话   打开一个网页，直到关闭浏览器之前 都是会话
#params为flddler抓包的数据  抓包登录的 POST  尾部数据  在flddler的 TextView 显示
params={"username":"用户名","pwd":"密码","formhash":"FA0334B8A2"}
mysession=session.post("https://www.yaozh.com/login/",params)
print(mysession.cookies.get_dict())  #打印cookie   cookie转化为一个字典
time.sleep(3)
mysession=session.get("https://www.yaozh.com/member/")
print(mysession.text)