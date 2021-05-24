"""
@Time    : 2021/5/23 10:49
@Author  : ZHC
@FileName: Spider_Score.py
@Software: PyCharm
"""

import requests
from fake_useragent import UserAgent
from lxml import etree


# "cookie":"
# JSESSIONID=ADC0245FD84EECDFA697B0E6BF3A7F68" #覃月

class GetScore():
    session = requests.Session()
    def __init__(self, url):
        self.url = url

    def GetCookie(self):
        url = "http://jxzx.ahtcm.edu.cn/eams/login.action"
        data = {

            "username": "2017205309026",
            "password": "2017205309026",
            "encodedPassword": "",
            "session_locale:": "zh_CN"
        }
        html = self.session.post(url, data=data, timeout=3)
        print("Cookie", html.cookies.values()[0])
        return html.cookies.values()[0]

    def GetHtmlData(self):

        ua = UserAgent(use_cache_server=False)
        headers = {"User-Agent": ua.random,
                   "cookie":
                   self.GetCookie()
                   }
        """请求获得html"""
        html =  self.session.get(url=self.url,headers=headers)
        if html.status_code == 200:
            ht = etree.HTML(html.text)
            title_list = []
            score_list = []
            getPersonID = ht.xpath(r'/html/body/div[3]/table')[0].get("id")
            tr = ht.xpath(r'//*[@id="{0}"]/thead/tr/th'.format(getPersonID))
            tb = ht.xpath(r'//*[@id="{0}_data"]/tr'.format(getPersonID))

            for i in range(1, len(tr) + 1):
                th = ht.xpath(r'//*[@id="{0}"]/thead/tr/th[{1}]/text()'.format(getPersonID, i))
                if not th:
                    th = ""
                else:
                    th = th[0].strip()
                title_list.append(th)

            for j in range(1, len(tb) + 1):
                l = []
                for x in range(1, len(tr) + 1):
                    td = ht.xpath(r'//*[@id="{0}_data"]/tr[{1}]/td[{2}]/text()'.format(getPersonID, str(j), str(x)))
                    if not td:
                        td = ""
                    else:
                        td = td[0].strip()
                    l.append(td)
                score_list.append(l)
            return title_list, score_list

    def GetLocalData(self):
        """从文本获取html"""
        with open(r"F:\爬取测试\person03!historyCourseGrade.htm", encoding="utf-8") as file:
            html = file.read()
        ht = etree.HTML(html)
        title_list = []
        score_list = []
        getPersonID = ht.xpath(r'/html/body/div[3]/table')[0].get("id")
        tr = ht.xpath(r'//*[@id="{0}"]/thead/tr/th'.format(getPersonID))
        tb = ht.xpath(r'//*[@id="{0}_data"]/tr'.format(getPersonID))

        for i in range(1, len(tr) + 1):
            th = ht.xpath(r'//*[@id="{0}"]/thead/tr/th[{1}]/text()'.format(getPersonID, i))
            if not th:
                th = ""
            else:
                th = th[0].strip()
            title_list.append(th)

        for j in range(1, len(tb) + 1):
            l = []
            for x in range(1, len(tr) + 1):
                td = ht.xpath(r'//*[@id="{0}_data"]/tr[{1}]/td[{2}]/text()'.format(getPersonID, str(j), str(x)))
                if not td:
                    td = ""
                else:
                    td = td[0].strip()
                l.append(td)
            score_list.append(l)
        return title_list, score_list


if __name__ == '__main__':
    url = "http://jxzx.ahtcm.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR"
    a = GetScore(url).GetHtmlData()
    print(a)
