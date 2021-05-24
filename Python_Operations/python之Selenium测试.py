from selenium import webdriver
import time
# 引入 Keys 模块
from selenium.webdriver.common.keys import Keys



def main():
    url = 'https://www.jianshu.com'
    browser = webdriver.Chrome()  # 调用Chrome浏览器
    browser.get(url)    #预设的浏览器网址
    print(browser.page_source) #打印网页源代码
    browser.quit()  #关闭浏览器

# close()	关闭单个窗口
# quit()	关闭所有窗口

# if __name__ == '__main__':
#     main()




browser = webdriver.Chrome()  # 调用Chrome浏览器

url = 'https:www.baidu.com'
browser.get(url)#打开浏览器预设网址


#3.刷新浏览器
browser.refresh()

#4.设置浏览器的大小
# browser.set_window_size(1400,800)
browser.forward()  #控制浏览器前进


#5.设置链接内容
# element = browser.find_element_by_link_text("新闻")
# element.click()
# print(element.text)

element_input = browser.find_element_by_id("kw").send_keys("风景")  #模拟按键输入


element_click = browser.find_element_by_id("su").submit() #单击元素



# 打印当前页面title
title = browser.title
print(title)

# 打印当前页面URL
now_url = browser.current_url
print(now_url)



#1.打印cookie信息
print('====================================='*20)
print("打印cookie信息为：")
print(browser.get_cookies)

# #2.添加cookie信息
# dict={'name':"name",'value':'Kaina'}
# browser.add_cookie(dict)
#
# print('=====================================')
# print('添加cookie信息为：')