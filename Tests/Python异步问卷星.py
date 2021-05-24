import asyncio,random,time
from pyppeteer import launch
from pyppeteer_stealth import stealth  # 反爬虫第三方库

"""获取问卷题目数量"""

async def Select_Title(driver):
    #arel = ".field-label"
    arel = ".div_question"
    asknum = await driver.querySelectorAll(arel)
    print(len(asknum))
    await ForOptions(asknum,driver)




"""for循环执行SelectOption"""
"""asknum 问卷的题目"""
"""driver 浏览器驱动"""
async def ForOptions(asknum,driver):
    for item in range(len(asknum)):
        if(item== 5 or item == 31):
            print("454448498489juibiubh")
            await  SelectOption(item,driver)
            s_button = '#btnNext'
            submit = await driver.querySelector(s_button)
            await asyncio.sleep(2)  # 页面延迟2s看是否提交成功
            await submit.click()
        else:
            await SelectOption(item,driver)


"""获取每个题目的选项数量"""
"""number 题目的序号 例如：第几题"""
async def SelectOption(number, driver):
    number += 1
   # arel = "#div"+str(number)+" > div.ui-controlgroup .label"
    arel  = "#divquestion"+str(number)+" > ul > li a"
    anum = await driver.querySelectorAll(arel)
    print("第{0}题有{1}个选项".format(number, len(anum)))

    rand = await RandomSelect(len(anum))
    await  Click_Chioce(number,rand,driver)
   # await Click_Option(number,len(anum),driver)

"""最终选择点击选项"""
"""number 题目的序号 例如：第几题"""
"""num 题目选项的个数"""
async def Click_Option(number,num, driver):
    rand = await RandomSelect(num)
    opt = await Mutiple_Choice(number, driver)
    if opt:
        list = []
        for item in range(rand):
            MutipleNum = await RandomSelect(num)
            list.append(MutipleNum)
        for item in list:
           await Click_Chioce(number, item, driver)
    await Click_Chioce(number,rand,driver)



"""点击选择选项"""
"""number 题目的序号 例如：第几题"""
"""num 题目选中的选项序号"""
async def Click_Chioce(number,num,driver):
    print("第{0}题选第{1}个选项".format(number, num))
    if number>6:
        num+=1
    #arel = "#div"+str(number)+">div.ui-controlgroup>div:nth-child("+str(num)+")>span>a"
    arel = "#divquestion"+str(number)+" > ul > li:nth-child("+str(num)+") > a"
    Option_Click = await driver.querySelector(arel)
    await Option_Click.click()

#divquestion20 > ul > li:nth-child(6) > a
"""判断多选题"""
"""number 题目的序号 例如：第几题"""
async def Mutiple_Choice(number,driver):
    aselrel = "#div"+str(number)+"> div.field-label > span.qtypetip"
    element = await driver.querySelector(aselrel)
    if  element:
        return 1
    return 0


"""随机选择选项"""
"""optnum 题目的选项个数"""
async def RandomSelect(optnum):
    renum = random.randint(1, optnum)
    return renum

"""新建一个browser对象"""
async def Browser():
    # launch方法会新建一个browser对象,然后赋值给browser
    browser = await launch({
        # 路径就是你的谷歌浏览器的安装路径
        'executablePath': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        # Pyppeteer 默认使用的是无头浏览器,所以要显示需要给False
        'headless': True,
        # 设置Windows-size和Viewport大小来实现网页完整显示
        'args': ['--no-sandbox', '--window-size=1366,850']
    })
    # 调用 newPage 方法相当于浏览器中新建了一个选项卡,同时新建了一个Page对象
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 768})
    # 防止页面识别出脚本(反爬虫关键语句)
    await stealth(page)
    return  page


async def Submit(driver):
    #s_button = "#ctlNext"
    s_button = "#submit_button"
    submit = await driver.querySelector(s_button)
    await asyncio.sleep(2)  # 页面延迟2s看是否提交成功
    await submit.click()

"""主函数"""
async def main(url):
    driver = await Browser()
    # 调用了Page对象的goto方法就相当于在浏览器中输入问卷的网址,浏览器跳转到了对应的页面进行加载
    await driver.goto(url)
    await Select_Title(driver)
    await Submit(driver)
    await asyncio.sleep(3)  # 页面延迟2s看是否提交成功
    await driver.close()



if __name__ == '__main__':
    number =int(input("请填写你想要的问卷份数"))
    start_time = time.time()
    for data in range(number):
         url = 'https://www.wjx.cn/jq/104098331.aspx'
         #url = "https://www.wjx.cn/m/104204068.aspx"
         #url = "https://ks.wjx.top/m/104345429.aspx"
         asyncio.get_event_loop().run_until_complete(main(url))
         time.sleep(5)
    end_time = time.time()
    print("填写完成,一共花费{}秒".format(end_time-start_time))
