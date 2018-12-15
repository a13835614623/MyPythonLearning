#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月15日
使用mysql
@author: zzk
'''
# 导入MySQL驱动:
import mysql.connector
conn = mysql.connector.connect(user='root',password='',database='python')
# 创建游标
cursor=conn.cursor()
def create_table_users():
    global cursor
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
#查询根据sql语句
def select_table_users(select_statement):
    global cursor
    cursor.execute(select_statement)
    values = cursor.fetchall()
    return values
print(select_table_users('select * from users'))

#     执行INSERT等操作后要调用commit()提交事务；
#     MySQL的SQL占位符是%s。
