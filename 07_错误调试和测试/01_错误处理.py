#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月9日

@author: zzk
'''
# 错误处理 try
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
print('---------------')
# 调用栈 记录错误
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('---------------')
# 抛出错误
class FooError(ValueError):
    pass
def throwerror(s):
    if int(s) == 0:
        raise FooError('s can not equal 0')
throwerror(0)
print('-----------------')
# raise语句如果不带参数，就会把当前错误原样抛出。
# 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：