#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月12日
UDP服务器端
@author: zzk
'''
import socket
# SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9992))
print('Bind UDP on 9999...')
while True:
    # 接收数据:
    # recvfrom()方法返回数据和客户端的地址与端口
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)