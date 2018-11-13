#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月13日

@author: zzk
'''
import os
print(os.name)#操作系统名称
# print(os.uname())
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 环境变量
print('-------------')
for path in os.environ.items():
    print(path)
print('-------------')
# 操作文件和目录
# 查看当前目录的绝对路径:
path = os.path.abspath('.')
print(path)
# 得到一个目录
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
newDir = os.path.join(path,'testDir')
print(newDir)
# 然后创建一个目录:
os.mkdir(newDir)
# 删除该目录
os.rmdir(newDir)

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('/Users/michael/testdir/file.txt'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('aaa.txt'))
# 重命名
# os.rename('file/test.txt','file/test2.txt')
# os.remove('file/test2.txt', dir_fd=None)

# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

# 列出当前目录下的目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出当前目录下的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])