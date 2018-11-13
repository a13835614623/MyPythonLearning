#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月13日
@author: zzk
'''
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
# StringIO顾名思义就是在内存中读写str。
from io import StringIO
from _io import BytesIO
f=StringIO('hello\nworld\n zzk')
f2=StringIO()
f2.write('my\nname\nis\nzzk')
print(f2.getvalue())
print('====================')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())
print('====================')

# BytesIO
fb = BytesIO()
fb.write('哈哈哈'.encode('utf-8'))
print(fb.getvalue())
fb2 = BytesIO(b'\xe5\x93\x88\xe5\x93\x88\xe5\x93\x88')
print(fb2.read().decode('utf-8'))