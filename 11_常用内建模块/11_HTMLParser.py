#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月2日

@author: zzk
'''
# Python提供了HTMLParser来非常方便地解析HTML
# 利用HTMLParser，可以把网页中的文本、图像等解析出来。
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):#开始标签
        print('<%s>' % tag)

    def handle_endtag(self, tag):#结束标签
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):#单标签
        print('<%s/>' % tag)

    def handle_data(self, data):#数据
        print(data)

    def handle_comment(self, data):#注释
        print('<!--', data, '-->')

    def handle_entityref(self, name):#特殊字符
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)
parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')