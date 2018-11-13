#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月8日

@author: zzk
'''
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__=('name','age')
s=Student()
# s.arr = 'zzz'
s.name='zzk'
print(s.name)
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：