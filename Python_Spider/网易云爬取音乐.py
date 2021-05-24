import time

from pyquery import PyQuery as pq
import requests
import json
import csv
import re


class Wangyi_yun(object):
    def __init__(self, id):
        # 定义初始信息请求头和url

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
        self.id = id
        self.url = "https://music.163.com/m/discover/toplist?id=" + str(self.id)

    def get_page(self):
        # 获取网页源代码

        res = requests.get(self.url, headers=self.headers).text
        return res

    def get_data(self, html):
        # 利用pyquery库解析原网页

        doc = pq(html)
        result = doc("#song-list-pre-data").text()
        return json.loads(result)

    def get_download(self, ID, name):
        # 下载歌曲，并保存到本地工作路径
        # http://music.163.com/song/media/outer/url?id=为网易云的下载连接更换id即可

        r = requests.get("http://music.163.com/song/media/outer/url?id=" + str(ID))
        path = r'F:\SpiderMusic\{0}'.format(str(name))
        with open( path  + ".mp3", "wb") as file:
            file.write(r.content)

    def write_csv(self, data):
        # 利用csv库将json数据保存到csv中

        with open("wangyiyun.csv", "a", encoding="utf-8-sig", newline='') as file:
            fieldnames = ["name", "singer", "url", "ID"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)

    def main(self):
        data = self.get_page()
        json_data = self.get_data(data)
        for item in range(len(json_data)):
            yield {"name": json_data[item].get("name"),
                   "singer": json_data[item].get("artists")[0].get("name"),
                   "url": "https://music.163.com/#/song?id=" + str(json_data[item].get("id")),
                   "ID": json_data[item].get("id")
                   }


if __name__ == "__main__":
    rank_music = Wangyi_yun(3779629)
    # 参数为榜单相应url的id
    for items in rank_music.main():
        rank_music.write_csv(items)
    # 写入csv文件
    for items in rank_music.main():
        # 遍历生成器
        ID = items.get("ID")
        name = items.get("name")
        rank_music.get_download(ID, name)
        time.sleep(3)
