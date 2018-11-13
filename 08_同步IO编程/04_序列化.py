#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月13日

@author: zzk
'''
import pickle
from email.policy import default
# 序列化
d=dict(name='Bob',age=20,score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes
bys = pickle.dumps(d)
print(bys)
with open('file/pickle.txt','wb') as f:
    pickle.dump(d,f)#序列化存入文件f
# 反序列化
with open('file/pickle.txt','rb') as f:
    dd = pickle.load(f)#从文件f反序列化
    # 这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已
    print(dd)#{'name': 'Bob', 'age': 20, 'score': 88}
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
# 并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
print('------------------------------------------------------')
# JSON
import json
d=dict(name='Bob',age=20,score=88)
# 序列化为json
json_str = json.dumps(d)
# 反序列化
dd = json.loads(json_str)
print('序列化后',json_str,'\n反序列化后:',dd)
print('------------------------------------------------------')
# JSON进阶
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def __str__(self, *args, **kwargs):
        return 'Student{name:%s,age:%d,score:%d}' %(self.name,self.age,self.score)
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，
# 我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2Dict(s):
    return {'name':s.name,'age':s.age,'score':s.score}
def dict2Student(d):
    return Student(d['name'],d['age'],d['score'])
s=Student('zzk',20,99)
# 序列化
# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
s_json_str = json.dumps(s,default=student2Dict)
s_json_str2 = json.dumps(s,default=lambda x:x.__dict__)
print(s_json_str,s_json_str2)
# 反序列化
ss = json.loads(s_json_str,object_hook=dict2Student)
print(ss)
