import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth  # 反爬虫第三方库


async def main():
    # launch方法会新建一个browser对象,然后赋值给browser
    browser = await launch({
        # 路径就是你的谷歌浏览器的安装路径
        'executablePath': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        # Pyppeteer 默认使用的是无头浏览器,所以要显示需要给False
        'headless': False,
        # 设置Windows-size和Viewport大小来实现网页完整显示
        'args': ['--no-sandbox', '--window-size=1366,850']
    })

    # 调用 newPage 方法相当于浏览器中新建了一个选项卡,同时新建了一个Page对象
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 768})
    # 防止页面识别出脚本(反爬虫关键语句)
    await stealth(page)

    # 调用了Page对象的goto方法就相当于在浏览器中输入问卷的网址,浏览器跳转到了对应的页面进行加载
    url = 'https://www.wjx.cn/m/104160686.aspx'
    #url = "https://www.wjx.cn/m/104204068.aspx"
    await page.goto(url)
    # 填空题：page.type(selector,text),在指定selector的元素上填写text
    # await page.type('#q1', '姓名')
    # await page.type('#q2', '学号')
    # await page.type('#divquestion5 > table > tbody > tr:nth-child(1) > td > div > textarea', '体温')
    # div19 > div.ui-controlgroup > div:nth-child(3) > span > a
    # 单选题：先用page.querySelector(selector)找到指定的元素,再调用元素的click()方法
    arel = ".field-label"
    asknum = await page.querySelectorAll(arel)
    print(asknum,len(asknum))

    for i in range(1,20):
        arel = "#div"+str(i)+">div.ui-controlgroup>div:nth-child(1)>span>a"
        button = await page.querySelector(arel)
        await button.click()
        # div1 > div.ui-controlgroup > div:nth-child(1) > span > a


    # div1 > div.ui-controlgroup > div:nth-child(1) > span > a
    # # 地址题：先点击手动填写地址,再在地址框内填写相应地址
    # address = await page.querySelector("#divquestion7 > ul > li:nth-child(1) > label")
    # await address.click()
    # await page.type('#q9', '地址')

    # # 日期选择题：先点击日期选择框,在出现的iframe寻找元素并调用click()方法
    # date1 = await page.querySelector("#q4")
    # await date1.click()
    #
    # frame = page.frames
    # date2 = await frame[1].querySelector('#selectTodayButton')
    # await date2.click()

    # 找到提交按钮提交
    #s_button ="#divSubmit > div.voteDiv > div > a"
    s_button = "#ctlNext"
    submit = await page.querySelector(s_button)
    print(submit)
    await asyncio.sleep(5)  # 页面延迟2s看是否提交成功
    await submit.click()

    print("dwadwadwadwadwa")
    await asyncio.sleep(6)  # 页面延迟2s看是否提交成功
    await browser.close()



asyncio.get_event_loop().run_until_complete(main())
