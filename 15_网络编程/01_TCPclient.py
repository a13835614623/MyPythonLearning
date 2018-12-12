#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月9日
    TCP客户端
@author: zzk
'''
import socket
from psutil._common import sconn
# 创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接服务器
s.connect(('127.0.0.1',9999))
# 接收数据

s.send('tcp:I am zzk.')
# 关闭连接
s.close()