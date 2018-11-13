#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月3日

@author: zzk
'''
#map/reduce

#map
from _functools import reduce
from test.test_binop import isint
from random import random
def f(x):
    return x*x
l = list(range(10))# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(f,l)))#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print('------------------------')

#reduce
def mult(x,y):
    return x*y
def add(x,y):
    return x+y
print(reduce(add,l))#45
print(reduce(mult,l[1:]))#362880
def str2Int(num1,num2):
    map ={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    if isint(num1):
        return num1*10+map[num2]
    else:
        return map[num1]*10+map[num2]
print(reduce(str2Int, '12345'))
# f(f(f(f('1','2'),'3'),'4'),'5')
print('------------------------')

#filter
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_Odd(x):#奇数
    return x%2==1
print(list(filter(is_Odd,range(10))))
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
#需要用list()函数获得所有结果并返回list。

#例子，产生质数
def _odd_iter():#奇数产生器
    n=1
    while True:
        n+=2
        yield n
#[3,5,7,9,...]
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
for p in primes():
    if p<10:
        print(p)
    else:
        break
# 筛选回文数
def is_palindrome(n):
    return str(n)==reduce(lambda x,y:y+x,str(n))
    #return str(n)==str(n)[::-1]
def reverse(s):#12345 f(f(f(1,2),3),4)
    return reduce(lambda x,y:str(y)+str(x),s)
a = filter(is_palindrome,range(1000))
print(list(a))
print('---------------')
#sorted
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
print(sorted([1,2,3,-1,6,4,9],key=lambda x:x*x))
#我们给sorted传入key函数，即可实现忽略大小写的排序：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))