#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月7日

@author: zzk
'''
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def jiao(self):
        print('wang wang wang ...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
dog = Dog()
dog.run()
dog.jiao()
cat = Cat()
cat.run()
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了：
def run_twice(animal):
    animal.run()
    animal.run()
print('=================')
run_twice(dog)
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running...')
tortoise = Tortoise()
run_twice(tortoise)
