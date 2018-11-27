#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月27日

@author: zzk
'''
# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
# struct的pack函数把任意数据类型变成bytes：
import struct
bys = struct.pack('>I',10240099)
print(bys)
# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
print('-------------------')
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。

#该方法可以识别位图文件，如果是位图文件输出图片大小和颜色数
def bmp_info(data):
    bmp=struct.unpack('<ccIIIIIIHH', data)
    if not (bmp[0]==b'B' and bmp[1]==b'M'):
        print('不是.bmp文件!')
    else:
        return {
            'width':bmp[6],
            'height':bmp[7],
            'colorNum':bmp[-1]
        } 
import os
with open('img/aaa.bmp','rb') as f:
    print(bmp_info(f.read()[0:30]))
print('-------------------')