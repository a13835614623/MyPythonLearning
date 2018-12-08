#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月7日

@author: zzk
'''
from turtle import *
# # 设置笔刷宽度:
width(4)
 
# 前进:
forward(200)
# 右转90度:
right(90)
 
# 笔刷颜色:
pencolor('red')
forward(100)
right(90)
 
pencolor('green')
forward(200)
right(90)
 
pencolor('blue')
forward(100)
right(90)
 
# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:

# 调用width()函数可以设置笔刷宽度，调用pencolor()函数可以设置颜色。更多操作请参考turtle库的说明。
# 绘图完成后，记得调用done()函数，让窗口进入消息循环，等待被关闭。否则，由于Python进程会立刻结束，将导致窗口被立刻关闭。
def draw_star():
    for x in range(5):
        width(4)
        pencolor('red')
        forward(100)
        right(144)
#画五角星
draw_star()
done()

