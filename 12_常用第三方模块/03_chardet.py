#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月4日

@author: zzk
'''
# chardet用来检测编码
import chardet
print(chardet.detect(b'hello'))
# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。
data = '哈恍恍惚惚恍恍惚惚好'.encode('gbk')
print(chardet.detect(data))
#{'encoding': 'ISO-8859-1', 'confidence': 0.73, 'language': ''}
# 可见，用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理。
# 使用chardet检测编码非常容易，chardet支持检测中文、日文、韩文等多种语言。