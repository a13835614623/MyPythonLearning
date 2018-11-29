#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月29日

@author: zzk
'''
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
import itertools
# 首先，我们看看itertools提供的几个“无限”迭代器：
# count()
wuxian = itertools.count(1)
for n in wuxian:
    print(n)  # 1,2,3,4.....,999,1000
    if(n > 1000):
        break
print('---------------------------------------')
# cycle()
cs = itertools.cycle('ABCABC')
# for c in cs:
#     print(c)#ABCABCABC....
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
ns = itertools.takewhile(lambda x:x<=10,wuxian)
print(list(ns))
print('---------------------------------------')

# repeat()
rp = itertools.repeat('A',3)
for r in rp:
    print(r)
#  无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
# 它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
print('---------------------------------------')
# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for chain in itertools.chain('ABC','EFG'):
    print(chain)
print('---------------------------------------')

# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
# 而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key,group in itertools.groupby('AABCCBACSSS',lambda c:c.lower()):
    print(key,list(group))