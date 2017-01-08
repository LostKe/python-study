# coding=utf-8

from sqlalchemy import Column, String, INTEGER, create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'cup'

    id = Column(INTEGER, primary_key=True)
    name = Column(String(20))


def get_DBSession():
    engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/school', encoding='utf-8', echo=True)
    DBSession = sessionmaker(bind=engine)
    return DBSession()


# 插入
def insert_data(user):
    session = get_DBSession()
    session.add(user)
    session.commit()
    session.close()


# 查询
def query_data(arg):
    session = get_DBSession()
    print(session)
    user = session.query(User).filter(User.id == arg).one()
    print(type(user))
    print(type(user.name))
    print("id:%d,name:%s" % (user.id, str(user.name)))
    session.close


# new_user = User(id=1, name='jim')
# insert_data(new_user)


query_data('1')
