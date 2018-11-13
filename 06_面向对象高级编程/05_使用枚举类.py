#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月8日

@author: zzk
'''
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr',
                    'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
print('-----------------')

@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Sun,'=',Weekday['Sun'].value)
print(Weekday(0),Weekday(1))
