from __future__ import unicode_literals

import itchat
from bs4 import BeautifulSoup
from wxpy import *

import requests

from threading import Timer

# itchat = Bot(cache_path="botoo.pkl")


def getNews():
    url = "http://open.iciba.com/dsapi/"

    r = requests.get(url)

    content = r.json()['content']

    note = r.json()['note']

    return content, note


def sendNews():
    try:

        # 这里是备注

        friend = itchat.friends().search(name=u'乱世')

        content = getNews()

        print(content)

        message1 = str(content[0])

        message2 = str(content[1])

        message3 = "xxx"

        print(friend)

        for index, item in enumerate(friend):
            print("发送给 " + str(item) + " ing,index=" + str(index))

        item.send(message1)

        item.send(message2)

        item.send(message3)

        t = Timer(86400, sendNews)

        t.start()

    except:

        errorMessage = "xxx"

        for index, item in enumerate(friend):
            item.send(errorMessage)




import win32api, win32gui, win32con
import win32clipboard as clipboard
import time
from apscheduler.schedulers.blocking import BlockingScheduler


###############################
#  微信发送
###############################
def send_m(win):
    # 以下为“CTRL+V”组合键,回车发送，（方法一）
    win32api.keybd_event(17, 0, 0, 0)  # 有效，按下CTRL
    time.sleep(1)  # 需要延时
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, 86, 0)  # V
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开CTRL
    time.sleep(1)  # 缓冲时间
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 回车发送
    return


def txt_ctrl_v(txt_str):
    # 定义文本信息,将信息缓存入剪贴板
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(win32con.CF_UNICODETEXT, txt_str)
    clipboard.CloseClipboard()
    return


def day_english():
    # 获取金山词霸每日一句
    url = 'http://open.iciba.com/dsapi'
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    print(content + note)
    return note

def GetArtitle():
    """"获取文章"""
    url = 'http://www.59xihuan.cn/index_1.html'
    h = requests.get(url)
    html = h.text
    news_bf = BeautifulSoup(html, "html.parser")
    msg = news_bf.find('div', class_='pic_text1')
    news = msg.text
    return news


def get_window(className, titleName):
    title_name = className  # 单独打开，好友名称
    win = win32gui.FindWindow(className, titleName)
    # 窗体前端显示
    # win32gui.SetForegroundWindow(win)
    # 使窗体最小化
    win32gui.ShowWindow(win, win32con.SW_MAXIMIZE)
    win = win32gui.FindWindow(className, titleName)
    print("找到句柄：%x" % win)
    if win != 0:
        left, top, right, bottom = win32gui.GetWindowRect(win)
        print(left, top, right, bottom)  # 最小化为负数
        win32gui.SetForegroundWindow(win)  # 获取控制
        time.sleep(0.5)
    else:
        print('请注意：找不到【%s】这个人（或群），请激活窗口！' % title_name)
    return win

#######################发送过程=================
def sendTaskLog():
    # 查找微信小窗口
    # win = get_window('ChatWnd', '文件传输助手')
    win = get_window('ChatWnd', '乱世')
    str = GetArtitle()
    txt_ctrl_v(str)
    send_m(win)


# scheduler = BlockingScheduler()
# # scheduler.add_job(sendTaskLog, 'interval', seconds=3)
# # scheduler.add_job(sendTaskLog, 'cron',day_of_week='mon-fri', hour=7,minute=31,second='10',misfire_grace_time=30)
# scheduler.add_job(sendTaskLog, 'cron', day_of_week='mon-fri', hour=6, minute=55, second='10', misfire_grace_time=30)
# try:
#     scheduler.start()
# except (KeyboardInterrupt, SystemExit):
#     pass

if __name__ == '__main__':
    sendTaskLog()