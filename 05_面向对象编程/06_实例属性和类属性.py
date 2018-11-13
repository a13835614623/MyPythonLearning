#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月7日

@author: zzk
'''
# 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，
# 这种属性是类属性，归Student类所有：
# 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，

# 实例属性优先级比类属性高
# 因为相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
class Student(object):
    class_name = 'Student'
    def study(self):
        print('学习')
print(Student.class_name)