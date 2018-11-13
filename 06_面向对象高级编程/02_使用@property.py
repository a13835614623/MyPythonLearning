#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月8日

@author: zzk
'''


class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):  # 参数检查
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Student2(object):

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value


ss = Student2()
ss.score = 99
print(ss.score)
