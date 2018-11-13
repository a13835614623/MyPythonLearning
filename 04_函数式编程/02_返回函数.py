#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月4日
@author: zzk
'''
from _functools import reduce
from builtins import str
def calc_sum(*args):
    return reduce(lambda x,y:x+y,args)
print(calc_sum(1,2,3,4))
def lazy_sum(*args):
    def sum():
        return reduce(lambda x,y:x+y,args)
    return sum
print(lazy_sum(1,2,3,4)())
print('-------------')
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
'''

#闭包
#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。 
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
def createCount():
    i=0
    def counter():
        nonlocal i
        i=i+1
        return i
    return counter
count = createCount()
print(count(),count(),count(),count())