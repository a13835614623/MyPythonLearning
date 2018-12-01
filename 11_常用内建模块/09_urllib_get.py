#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月1日

@author: zzk
'''
# urllib提供了一系列用于操作URL的功能。
# Get
# urllib的request模块可以非常方便地抓取URL内容，
# 也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
from urllib import request
with request.urlopen('http://www.baidu.com') as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:',data.decode('utf-8'))
# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，
# 我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
