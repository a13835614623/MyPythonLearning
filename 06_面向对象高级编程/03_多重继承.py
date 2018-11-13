#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月8日

@author: zzk
'''
class Animal(object):
    pass
class FlyableMixIn(object):
    pass
class RunnableMixIn(object):
    pass
class Dog(Animal,RunnableMixIn):
    pass
class Bird(Animal,FlyableMixIn):
    pass
# 类似于java的接口实现和继承混合
