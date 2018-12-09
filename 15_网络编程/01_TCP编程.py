#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月9日

@author: zzk
'''
# 创建一个基于TCP连接的Socket
import socket

#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接:
# 参数是一个tuple，包含地址和端口号
s.connect(('www.bilibili.com', 80))
s.send(b'GET / HTTP/2.0\r\nHost: www.bilibili.com\r\nConnection: close\r\n\r\n')
# 接收数据
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
print(data)
# 关闭连接
s.close()
# 网页内容保存到文件
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('bilibili.html', 'wb') as f:
    f.write(html)