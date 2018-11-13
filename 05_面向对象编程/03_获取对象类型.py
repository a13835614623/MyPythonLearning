#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月7日

@author: zzk
'''
# 获取对象类型
import types
print(type(123))# <class 'int'>
print(type(None))#<class 'NoneType'>
print(type(abs))#<class 'builtin_function_or_method'>
print(type(lambda x:x*x))#<class 'function'>
print(type(lambda x:x*x)==types.LambdaType)
print('===============================')
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky():
    pass
animal = Animal()
dog = Dog()
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))
#  总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
# 比如，获得一个str对象的所有属性和方法： 
print(dir('aaa'))
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是
# ，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
# 一个正确的用法的例子如下：
# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None
