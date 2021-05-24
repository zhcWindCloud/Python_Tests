print()
print("*"*60+"time模块"+"*"*60)
import time

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)




# 格式化成xxxx-xx-xx xx:xx:xx形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y %j", time.localtime()))

day = time.strftime("%j"),time.localtime()

days = 365- int(day[0])

print(day,days)

print(time.strftime("%A %B %d %H:%M:%S %Y %X", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2020"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

print()
print(time.time())

print()

print("*"*60+"datetime模块"+"*"*60)


#datetime模块

import  datetime

date  =  datetime.datetime.now()

print(date,date.hour)

print(date.timetuple())  #返回日期对应的time.struct_time对象

print(date.toordinal())	 #返回日期是是自 0001-01-01 开始的第多少天)

print(date.weekday())

print(date.isoweekday())

print(date.isocalendar())  #返回一个元组，格式为：(year, weekday, isoweekday)

print(date.isoformat(),type(date.isoformat())) #返回‘YYYY-MM-DD'格式的日期字符串

print(date.strftime('%Y-%m-%d %H:%M:%S')) #返回指定格式的日期字符串，与time模块的strftime(format, struct_time)功能相同

print(datetime.MAXYEAR)

a = date.date()
b =date.date()
mlast = datetime.date(a.year,a.month,1) - datetime.timedelta(days=1)  #上个月的最后一天
mfirst = datetime.date(a.year,mlast.month,1)  #上个月的第一天
print(mlast,mfirst)



start_time = datetime.date(2017,9,14)   #开始计算时间
end_time = datetime.datetime.now()    #结束计算时间
end_time1 = datetime.date(2021,7,1)
print("距离17年入学至今已有{}天".format((end_time.date() - start_time).days))

print("距离毕业还有{}天".format((end_time1 - end_time.date()).days))


ltime = date + datetime.timedelta(hours=10)

print(ltime)





#
# 获取某月日历
# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：

print("*"*60+"Calendar模块"+"*"*60)
import calendar

cal = calendar.month(2020, 10)
print ("以下输出2016年1月份的日历:")
print (cal)
print (calendar.day_name)
for i in calendar.day_name:
    print(i)
print("星期的全称:{}".format(calendar.day_name))


for x in calendar.day_abbr:
    print(x)
print("星期的简称:{}".format(calendar.day_abbr))


for x in calendar.month_name:
    print(x)
print("月份全称：{}".format(calendar.month_name))





print("{1}是闰年是{0}".format(calendar.isleap(2020),2020))#判断是否是闰年：


print(calendar.calendar(2020))  #显示某一年的日历

print(calendar.leapdays(2000, 2020)) # 从某年到某年,一共有多少个闰年,[n,m)


