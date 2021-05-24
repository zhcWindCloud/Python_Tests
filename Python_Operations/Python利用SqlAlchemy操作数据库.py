# 创建时间: 2021/4/24 14:44


""""==============================使用sqlalchemy操作数据库======================================"""
import random
import time
from datetime import datetime, timedelta

import requests
from sqlalchemy import create_engine, ext, Column, Integer, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建一个模型基类


BaseModel = ext.declarative.declarative_base()

"""==================================封装连接数据库驱动=========================================="""


class SqlBuider(object):
    """封装ORM的一些管理"""

    def __init__(self):
        self.users = "root"
        self.password = "root"
        self.db = "depression"
        self.encoding = "utf-8"
        self.echo = False
        self.pool_size = 8
        self.pool_recycle = 60 * 30

    def SqlConnection(self):
        """
        数据库配置驱动 连接数据库，利用数据库字符串构造engine, echo为True将打印所有的sql语句
        pool_size: 连接池的大小，默认为5个，设置为0时表示连接无限制
        pool_recycle: 设置时间以限制数据库多久没连接自动断开
        create_engine("数据库类型+数据库驱动://数据库用户名:数据库密码@IP地址:端口/数据库"，其他参数)
        """
        # Mysql
        url = "mysql+pymysql://{0}:{1}@localhost/{2}?charset=utf8".format(self.users, self.password, self.db)
        # sqlite
        # url = r"create_engine('sqlite+sqlite3://foo.db')"
        engine = create_engine(url, encoding=self.encoding, echo=self.echo, pool_size=self.pool_size,
                               pool_recycle=self.pool_recycle)
        return engine

    def createDB(self):
        """根据类创建数据库表"""
        engine = self.SqlConnection()
        result = BaseModel.metadata.create_all(engine)  # 数据库引擎
        return result

    def DorpDB(self):
        """根据类删除数据库表"""
        engine = self.SqlConnection()
        result = BaseModel.metadata.drop_all(engine)  # 数据库引擎
        return result

    def SqlSession(self):
        """"
        创建session会话
        session的常见操作方法包括：
        flush：预提交，提交到数据库文件，还未写入数据库文件中
        commit：提交了一个事务
        rollback：回滚
        close：关闭
        """
        engine = self.SqlConnection()
        DbSession = sessionmaker(bind=engine)
        session = DbSession()
        return session


"""=====================================封装数据的增删改查========================================"""


class SqlManage(object):
    """增刪改查"""
    session = SqlBuider().SqlSession()

    def AddData(self, obj):
        """添加数据
         需要对象实例化
        """
        if isinstance(obj, list):
            res = self.session.add_all(obj)
        else:
            res = self.session.add(obj)
        try:
            self.session.commit()
        finally:
            self.session.close()
        return res

    def InsertData(self, obj, data):
        """非ORM 快速批量插入"""
        print(obj, data)
        try:
            res = self.session.execute(obj.__table__.insert(), data)
            self.session.commit()
        finally:
            self.session.close()
        return res

    def DeleteData(self, obj, ID):
        """刪除數據"""
        try:
            res = self.SelectData(obj).filter(obj.id == ID).delete()
            self.session.commit()
        finally:
            self.session.close()
        return res

    def UpdateData(self, obj, ID, query):
        """修改数据 """
        try:
            res = self.SelectData(obj).filter(obj.id == ID).update(query)
            self.session.commit()
        finally:
            self.session.close()
        return res

    def SelectData(self, obj):
        try:
            # 给个数据模型
            query = self.session.query(obj)
        finally:
            self.session.close()
        return query


""""================================Model类 对应数据库的表==================================="""


class Users001(BaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    email = Column(String(64))

    def __init__(self, name, email):
        self.name = name
        self.email = email


"""==================================加载现有的表=========================================="""


class Curr_User(BaseModel):
    # 现在的表绑定类
    metadata = MetaData(bind=SqlBuider().SqlConnection())

    # 直接就加载了原有数据库！
    # 获取指定数据库表对象
    tables = "comprehensive_visitor"
    __table__ = Table(tables, metadata, autoload=True)


def FormatDate():
    """当前时间"""
    Now = datetime.now()
    return Now.strftime('%Y-%m-%d %H:%M:%S')


def GetNaMe():
    """获取姓名"""
    baijiaxing = """赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐"""
    name = ''
    for i in range(3):
        name += random.choice(baijiaxing)
    return name


def GetUsername():
    name = ''
    for i in range(6):
        name += chr(random.randrange(65, 123))
    return name


def getip(ip, count):
    count = int(count)
    ip2 = int(ip.split('.')[-2])
    ip1 = int(ip.split('.')[-1])
    ip_before = '%s.%s' % (ip.split('.')[0], ip.split('.')[1])
    IP_list = []
    for i in range(0, count):
        new_ip1 = ip1 + i
        if 11 <= new_ip1 <= 254:
            IP_list.append('{}.{}.{}'.format(ip_before, str(ip2), str(new_ip1)))
        else:
            new_ip2 = ip2 + int(new_ip1 / 254)
            new_ip1 = new_ip1 % 254 + 10
            IP_list.append('{}.{}.{}'.format(ip_before, str(new_ip2), str(new_ip1)))

    return IP_list


'''
测试查找IP地址'''


def GetIPAdress(IP):
    url = "http://api.guajicun.com/GetIp/default.aspx?queryIp=" + str(IP)
    response = requests.get(url)
    return response


def GetRandomDateTime(year=None):
    if year:
        month = random.randint(1, 12)
        if month in [1, 3, 5]:
            date = datetime(year, month, random.randint(1, 31), random.randint(0, 23), random.randint(0, 59),
                            random.randint(0, 59))
            return date
        elif month == 2:
            return datetime(year, month, random.randint(1, 28), random.randint(0, 23), random.randint(0, 59),
                            random.randint(0, 59))
        elif month == 4:
            return datetime(year, random.randint(1, 12), random.randint(1, 30), random.randint(0, 23),
                            random.randint(0, 59),
                            random.randint(0, 59))


def GetBroser():
    l = ["QQQBrowser 6.2", "QQQBrowser 10.7.4313.400", "Chrome 90.0.4430.93", "Edge 90.0.818.56", "safari 4.0"]
    new_list = ["Android 32位", "Android 64位", "Win10 64位", "Win7 64位", "Win7 32位", "Win8 64位", "Win8 32位"]
    return random.choice(l), random.choice(new_list)


def getip(ip, count):
    count = int(count)
    ip2 = int(ip.split('.')[-2])
    ip1 = int(ip.split('.')[-1])
    ip_before = '%s.%s' % (ip.split('.')[0], ip.split('.')[1])
    IP_list = []
    for i in range(0, count):
        new_ip1 = ip1 + i
        if 11 <= new_ip1 <= 254:
            IP_list.append('{}.{}.{}'.format(ip_before, str(ip2), str(new_ip1)))
        else:
            new_ip2 = ip2 + int(new_ip1 / 254)
            new_ip1 = new_ip1 % 254 + 10
            IP_list.append('{}.{}.{}'.format(ip_before, str(new_ip2), str(new_ip1)))

    return IP_list


'''
测试查找IP地址'''


def GetIPAdress(IP):
    url = "http://api.guajicun.com/GetIp/default.aspx?queryIp=" + str(IP)
    response = requests.get(url)
    return response


def GetRandomDateTime(year=None):
    if year:
        month = random.randint(1, 12)
        if month in [1, 3, 5]:
            date = datetime(year, month, random.randint(1, 31), random.randint(0, 23), random.randint(0, 59),
                            random.randint(0, 59))
            return date
        elif month == 2:
            return datetime(year, month, random.randint(1, 28), random.randint(0, 23), random.randint(0, 59),
                            random.randint(0, 59))
        elif month == 4:
            return datetime(year, month, random.randint(1, 30), random.randint(0, 23),
                            random.randint(0, 59),
                            random.randint(0, 59))


def GetBroser():
    l = ["QQQBrowser 6.2", "QQQBrowser 10.7.4313.400", "Chrome 90.0.4430.93", "Edge 90.0.818.56", "safari 4.0"]
    new_list = ["Android 32位", "Android 64位", "Win10 64位", "Win7 64位", "Win7 32位", "Win8 64位", "Win8 32位"]
    return random.choice(l), random.choice(new_list)


if __name__ == '__main__':
    lt = []
    IP_list = ["1.180.0.0", "1.188.0.0", "1.202.0.0", "14.0.0.0", "14.0.12.0",
               "14.1.0.0",
               "14.1.24.0",
               "14.1.96.0",
               "14.16.0.0",
               "14.102.124",
               "14.102.154",
               "14.102.184",
               "14.103.0.0",
               "14.192.60",
               "14.192.76",
               "14.196.0.0",
               "14.204.0.0",
               "14.208.0.0",
               "27.0.128.0",
               "27.0.160.0",
               "27.0.188.0",
               "27.8.0.0",
               "27.34.232",
               "27.36.0.0",
               "27.50.128",
               "27.54.192",
               "27.98.208",
               "27.99.128",
               "27.106.128.0",
               "27.109.32.0",
               "27.109.124.0",
               "27.112.0.0",
               "27.112.80.0",
               "27.112.112.0",
               "27.113.128.04",
               "27.115.0.0",
               "27.116.44.0",
               "27.121.72.0",
               "43.225.76.0"]
    start = time.time()
    for i in IP_list:
        for x in getip(i, 10):
            try:
                IP_Dict = GetIPAdress(x).json()["data"][0]
                IP = IP_Dict.get("ip")
                Country = IP_Dict.get("country") + "," + IP_Dict.get("region") + "," + IP_Dict.get("city")
                Operators = "中国" + IP_Dict.get("as")
                hostname = GetBroser()[0]
                OS = GetBroser()[1]
                Date = GetRandomDateTime(year=2021)
                # Date = datetime(2020,12,20,random.randint(0, 23), random.randint(0, 59),random.randint(0, 59))
                if Date:
                    Date = Date + timedelta(days=7)
                    a = Curr_User(OutIP=IP, country=Country, operators=Operators, hostname=hostname, MacAdress=OS,
                                  Viewtime=Date)
                    lt.append(a)
            except Exception as e:
                print(e)
    print(lt)
    session = SqlManage().AddData(lt)
    end = time.time()
    print("耗时{}秒".format(end - start))
#  session = SqlManage().InsertData(Curr_User, data_list)

# print(session)

# ad = SqlManage().UpdateData(Users001,1,query=data)
# print(ad)
