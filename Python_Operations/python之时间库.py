import time
#
# # 格式化成2016-03-20 11:45:39形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print(type(time.localtime()))
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) )
#
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print( time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
import datetime

print(datetime.timedelta(365).total_seconds()) # 一年包含的总秒数

dt = datetime.datetime.now()
print(dt + datetime.timedelta(3)) # 3天后
print(datetime.datetime.now(),type(datetime.datetime.now()))

# print(datetime.strftime("%Y-%m-%d %H:%M:%S", datetime.datetime.now()))
# datetime.datetime(2017, 2, 8, 9, 39, 40, 102821)
# dt + datetime.timedelta(-3) # 3天前
# datetime.datetime(2017, 2, 2, 9, 39, 40, 102821)
# dt + datetime.timedelta(hours=3) # 3小时后
# datetime.datetime(2017, 2, 5, 12, 39, 40, 102821)
# dt + datetime.timedelta(hours=-3) # 3小时前
# datetime.datetime(2017, 2, 5, 6, 39, 40, 102821)
# dt + datetime.timedelta(hours=3, seconds=30) # 3小时30秒后
# datetime.datetime(2017, 2, 5, 12, 40, 10, 102821)


print()
import datetime
import time
# 获取当前时间
dtime = datetime.datetime.now()
un_time = time.mktime(dtime.timetuple())
print(un_time)
# 将unix时间戳转换为“当前时间”格式
times = datetime.datetime.fromtimestamp(time.mktime(dtime.timetuple()))
print(times)


print('--'*50)
a = '2015-04-07 04:30:03'
aaa =  datetime.datetime.strptime(str(a),"%Y-%m-%d %H:%M:%S")
print(aaa,type(aaa))
print('--'*50)
b = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(b,type(b))
print(type(datetime.datetime.now()))



import datetime
starttime = datetime.datetime(2005, 2, 16,1,0,0)
#long running
endtime = datetime.datetime.now()
print ((endtime - starttime).seconds)

print('*'*71)


import datetime
start = datetime.datetime.now()
#long running
end = datetime.datetime.now()
print ((end - start).seconds)

print()

def time2sec(y):
  '''
  时间类型时分秒转换成秒
  '''
  h = y.hour #直接用datetime.time模块内置的方法，得到时、分、秒
  m = y.minute
  s = y.second
  return int(h)*3600 + int(m)*60 + int(s) #int()函数转换成整数运算

print(time2sec(datetime.datetime.now()))









print()

date1 = '2018-11-26 09:30:45'
date2 = '16/Nov/2013:08:44:34'

# 定义的日期格式需与当前时间格式一致
d1 = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime(date2, '%d/%b/%Y:%H:%M:%S')

d = d1 - d2

s = int(d.days)*3600*24
print('相差的天数：{}'.format(d.days))
print('相差的秒数：{}'.format((int(d.seconds))+s))
