#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月1日

@author: zzk
'''
'''
操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，
因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，
缺点是我们需要自己处理事件。
正常情况下，优先考虑SAX，因为DOM实在太占内存。

当SAX解析器读到一个节点时：
<a href="/">python</a>
会产生3个事件：
    start_element事件，在读取<a href="/">时；
    char_data事件，在读取python时；
    end_element事件，在读取</a>时。
'''
from xml.parsers.expat import ParserCreate


class SaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
    
    def end_element(self,name):
        print('sax:end_element: %s' % name)
        
    def char_data(self,text):
        print('sax:char_data: %s' % text)
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">hello</a></li>
    <li><a href="/python">Python</a></li>
</ol>
''';
handler = SaxHandler();
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，
# 所以需要自己保存起来，在EndElementHandler里面再合并。