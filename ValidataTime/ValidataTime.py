import datetime


class ValidataTime(object):
    """获取日期"""

    def getDate(self, Datetime):
        return Datetime.date()

    """获取时间"""
    def getTime(self, Datetime):
        return Datetime.strftime("%H:%M:%S")


if __name__ == "__main__":
    s = ValidataTime()
    print(s.getDate("2019-15-48 48:48:48"))
    print(s.getTime(datetime.datetime.now()))
