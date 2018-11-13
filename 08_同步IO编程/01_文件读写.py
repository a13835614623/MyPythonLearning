#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月11日

@author: zzk
'''
# 文件读取和字符编码
try:
    f=open('file/a.txt','r',encoding='utf-8')
    fileData = f.read()
    print(fileData)
finally:
    if f:
        f.close()
print('-------------------')
# Python引入了with语句来自动帮我们调用close()方法
with open('file/a.txt','r') as f:
    print(f.read())
print('-------------------')
# 可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，
# 调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

# file-like Object

# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

# 二进制文件
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

# with open('file/test.jpg','rb') as f:
#     print(f.read())

# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，
# 传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
with open('file/a.txt','a',encoding='utf-8') as f:
    f.write('\nmy name is zzk')
# 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。