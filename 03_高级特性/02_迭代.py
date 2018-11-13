'''
Created on 2018年11月3日
@author: zzk
'''
# *- code:utf-8 -*
# 1.dict迭代
dicts = {'name':'zzk','age':18}
for key in dicts:# 默认迭代key
    print(key)
for value in dicts.values():#迭代value
    print(value)
for item in dicts.items():#迭代每一项
    print(item)
from collections.abc import Iterable
# 判断是否可迭代
print(isinstance([1,2,3], Iterable))#True
print(isinstance('zzk', Iterable))#True
print(isinstance((1,2,3), Iterable))#True
#把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x,y in [(1,2),(2,3),(3,4)]:
    print('x=',x,'y=',y)
# 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
