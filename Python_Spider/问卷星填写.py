"""
@Time    : 2021/5/4 13:18
@Author  : ZHC
@FileName: 网易云爬取音乐.py
@Software: PyCharm
"""
import asyncio
import os
import random
import threading
import time

from pyppeteer import launch
from pyppeteer_stealth import stealth  # 反爬虫第三方库


async def ClickButton(page):
    """填写答案"""
    arel = ".field-label"
    allnum = await page.querySelectorAll(arel)

    for i in range(1, len(allnum) + 1):
        calss_arel = "#div" + str(i) + ">div.ui-controlgroup>div"
        asknum = await page.querySelectorAll(calss_arel)
        if i == 7 or i == 8:
            for arel in MutiChoose(i, len(asknum)):
                button = await page.querySelector(arel)

                await button.click()
        else:
            arel = SingleChoose(i, len(asknum))
            button = await page.querySelector(arel)

            await button.click()


async def SubmitClick(page,url):
    """提交答案"""

    # 找到提交按钮提交
    await  ClickButton(page)
    s_button = "#ctlNext"
    submit = await page.querySelector(s_button)
    print(submit)
    await asyncio.sleep(5)  # 页面延迟5s看是否提交成功
    await submit.click()




def SingleChoose(curr, number):
    """
    单选题选项
     @pamras: asknum 当前题目
     @pamras: number 当前题目 的答案数量
     """
    answer = random.randint(1, number)
    arel = "#div" + str(curr) + ">div.ui-controlgroup>div:nth-child(" + str(answer) + ")>span>a"

    return arel


def MutiChoose(curr, number):
    """
    多选题
    @pamras: asknum 当前题目
    @pamras: number 当前题目 的答案数量
     """
    answer_list = []
    number_list = list(set([random.randint(1, number) for x in range(random.randint(1, number))]))
    for answer in number_list:
        arel = "#div" + str(curr) + ">div.ui-controlgroup>div:nth-child(" + str(answer) + ")>span>a"
        answer_list.append(arel)
    return answer_list


async def Main(url):
    # launch方法会新建一个browser对象,然后赋值给browser
    browser = await launch({
        # 路径就是你的谷歌浏览器的安装路径
        'executablePath': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        # Pyppeteer 默认使用的是无头浏览器,所以要显示需要给False
        'headless': True,
        # 设置Windows-size和Viewport大小来实现网页完整显示
        'args': ['--no-sandbox', '--window-size=1366,850']
    })

    """获取page对象"""
    # 调用 newPage 方法相当于浏览器中新建了一个选项卡,同时新建了一个Page对象
    page = await browser.newPage()

    await page.setViewport({'width': 1366, 'height': 768})
    # 防止页面识别出脚本(反爬虫关键语句)
    await stealth(page)
    # 调用了Page对象的goto方法就相当于在浏览器中输入问卷的网址,浏览器跳转到了对应的页面进行加载
    await page.goto(url)

    await SubmitClick(page,url)

    """关闭浏览器"""
    await asyncio.sleep(6)  # 页面延迟6s关闭
    await browser.close()


def DoMain(url,number):
    fail, success = 0, 0
    for x in range(1, number + 1):
        try:
            asyncio.get_event_loop().run_until_complete(Main(url))
            print("填写第{0}份成功".format(x))
            success += 1
        except Exception as e:
            print("填写第{0}份失败,错误为{1}".format(x, e))
            fail += 1

    print("填写成功{0}份,填写失败{1}份".format(success, fail))

if __name__ == '__main__':
    # url = 'https://www.wjx.cn/m/104160686.aspx'
    number = int(input("请输入你要填写问卷的份数:"))
    url = "https://www.wjx.cn/vm/PEwjMFZ.aspx"
    strat_time = time.time()

    t = threading.Thread(target=DoMain(url,number))
        # 启动子线程
    t.start()
    end_time = time.time()
    print("本次填写问卷总共耗时{0}".format(end_time - strat_time))

