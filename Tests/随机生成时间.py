"""
@Time    : 2021/5/11 14:02
@Author  : ZHC
@FileName: 随机生成时间.py
@Software: PyCharm
"""

import random
from datetime import datetime


def GetRandomTime():
    date = datetime.now()
    a = datetime(2015, 4, 19, 12, 20, 50)  # 用指定日期时间创建datetime
    print(a, type(a))
    dt = datetime(2015, 4, 19, 22, 20, 0)  # 用指定日期时间创建datetime
    print(dt, type(dt))
    print(dt.strftime('%Y-%m-%d'))  # 返回指定格式的日期字符串，与time模块的strftime(format, struct_time)功能相同


def GetRandomDateTime(year=None):
    if year:
        month = random.randint(1, 12)
        if month in [1, 3, 5, 7, 8, 9, 12]:
            date = datetime(year, month, random.randint(1, 31), random.randint(0, 23), random.randint(0, 59),
                            random.randint(0, 59))
            return date
        elif month == 2:
            return datetime(year, month, random.randint(1, 28), random.randint(0, 23),  random.randint(0, 59),
                            random.randint(0, 59))
        return datetime(year, random.randint(1, 12), random.randint(1, 30), random.randint(0, 23),  random.randint(0, 59),
                        random.randint(0, 59))


if __name__ == '__main__':
    date_list = []
    for x in range(10):
        print(GetRandomDateTime(2020).strftime('%Y-%m-%d'))
        date_list.append(GetRandomDateTime(2020))

    print(date_list)
