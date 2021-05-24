"""
@Time    : 2021/5/23 23:35
@Author  : ZHC
@FileName: SqlConn.py
@Software: PyCharm
"""
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

BaseModel = declarative_base()  # 相当于Django model

def SqlConnection():
    # 4.创建数据库连接
    url = r'mysql+pymysql://root:root@127.0.0.1:3306/Scores?charset=utf8'
    engine = create_engine(url)
    return  engine
def GetSession():
    DbSession = sessionmaker(bind=SqlConnection())
    session = DbSession()
    return session

class StudentScore(BaseModel):
    # 现在的表绑定类
    metadata = MetaData(bind=SqlConnection())
    # 直接就加载了原有数据库！
    # 获取指定数据库表对象
    tables = "studentscore"
    __table__ = Table(tables, metadata, autoload=True)

def GetDBData(username=None):
    """从数据库取出数据然后格式化数据"""
    title_list =[]
    score_list = []
    jidian_list = []
    xuefen_list = []
    sum_list = [title_list,score_list,jidian_list,xuefen_list]
    querys = GetSession().query(StudentScore).filter(StudentScore.username == username)
    for query in querys:
        title_list.append(query.xuenianxueqi+"\n"+query.kechengmingcheng)
        score_list.append(query.zuizhong)
        jidian_list.append(query.jidian)
        xuefen_list.append(query.xuefen)
    return  sum_list

if __name__ == '__main__':
    print(GetDBData("覃月"))