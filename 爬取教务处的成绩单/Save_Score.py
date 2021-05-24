"""
@Time    : 2021/5/23 10:50
@Author  : ZHC
@FileName: Save_Score.py
@Software: PyCharm
"""
import openpyxl
import pypinyin
from sqlalchemy import Column, Integer, String
# 1. 导入SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# 2.ORM 模型基类
from sqlalchemy.orm import sessionmaker

from 爬取教务处的成绩单.Spider_Score import GetScore

BaseModel = declarative_base()  # 相当于Django model


# 3. 创建ORM对象
class StudentScore(BaseModel):
    __tablename__ = "StudentScore"
    id = Column(Integer, primary_key=True)
    xuenianxueqi = Column(String(100))
    kechengdaima = Column(String(100))
    kechengxuhao = Column(String(100))
    kechengmingcheng = Column(String(100))
    kechengleibie = Column(String(100))
    xuefen = Column(String(100))
    bukaochengji = Column(String(100))
    zongpingchengji = Column(String(100))
    zuizhong = Column(String(100))
    jidian = Column(String(100))
    username = Column(String(100))


# 4.创建数据库连接

from sqlalchemy import create_engine

url = r'mysql+pymysql://root:root@127.0.0.1:3306/Scores?charset=utf8'
engine = create_engine(url)
DbSession = sessionmaker(bind=engine)
session = DbSession()

# 5.
# 去engine数据库中创建所有继承Base类的ORM对象
BaseModel.metadata.create_all(engine)


def Save_Excel(data):
    work_book = openpyxl.Workbook()
    work_sheet = work_book.create_sheet(title="成绩单")
    work_sheet.append(['期末成绩'])
    work_sheet.append(data[0])
    for x in data[1]:
        work_sheet.append(x)
    work_book.save(r"F:\大学成绩单.xlsx")


def FormatData():
    new_list = []
    datalist = GetScore("url").GetLocalData()
    newdatalist = [pypinyin.slug(x, separator="") for x in datalist[0]]
    for datas in datalist[1]:
        new_list.append(dict(zip(newdatalist, datas)))
    return new_list


if __name__ == '__main__':
    data_list =[]
    for datas in FormatData():
       sc =  StudentScore(xuenianxueqi=datas["xuenianxueqi"],
                     kechengdaima=datas["kechengdaima"],
                     kechengxuhao=datas["kechengxuhao"],
                     kechengmingcheng=datas["kechengmingcheng"],
                     kechengleibie=datas["kechengleibie"],
                     xuefen=datas["xuefen"],
                     bukaochengji=datas.get("bukaochengji",None),
                     zongpingchengji=datas["zongpingchengji"],
                     zuizhong=datas["zuizhong"],
                     jidian=datas["jidian"],username="张思伟")
       data_list.append(sc)

    session.add_all(data_list)
    session.commit()
# url  = ""
# start = time.time()
# data = GetScore(url).GetLocalData()
# Save_Excel(data)
# end =time.time()
# print("总共耗时{}秒".format(end-start))
