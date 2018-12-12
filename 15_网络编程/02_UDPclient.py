#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月12日
UDP客户端
@author: zzk
'''
import socket
from psutil._common import sconn
# 创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server = ('127.0.0.1',9992);
# 发送数据
s.sendto(b'UDP:I am zzk.',server)
# 接收数据:
print(s.recv(1024).decode('utf-8'))
# 关闭连接
s.close()