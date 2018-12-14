#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月14日
使用SQLite3
@author: zzk
'''
import sqlite3
conn = sqlite3.connect('test.db')
#创建一个cursor
cursor = conn.cursor()
#执行一条SQL语句，创建一个users表
cursor.execute('''create table users(
    id varchar(20) primary key,
    name varchar(20)
)''')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into users values(\'1001\',\'zzk\')')
print('插入行数',cursor.rowcount)
#关闭cursor
cursor.close()
#提交事务
conn.commit()
# 关闭连接
conn.close()