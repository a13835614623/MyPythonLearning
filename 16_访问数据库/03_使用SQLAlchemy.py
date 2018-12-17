#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月16日

@author: zzk
'''
# 导入SQLAlchemy:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
# 初始化数据库连接:
'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:@127.0.0.1:3306/python')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session,DBSession对象可视为当前数据库连接
session = DBSession()
def user_add(object):
    global session
    # 创建新User对象:
    new_user = User(id=6,name='zzk')
    # 添加到session
    session.add(new_user)
def user_query():
    global session
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，
    # 如果调用all()则返回所有行:
    user = session.query(User).filter(User.id=='5').all()
    return user
# 查询
users = user_query()
# 查看查询结果
for user in users:
    print(user.id,user.name)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，
# 相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
# class User(Base):
#     __tablename__ = 'user'
# 
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
#     books = relationship('Book')
# 
# class Book(Base):
#     __tablename__ = 'book'
# 
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))