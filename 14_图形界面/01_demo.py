#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月7日

@author: zzk
'''
from tkinter import *
import tkinter.messagebox as messagebox
class Appliaction(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'hello %s' % name)
    def createWidgets(self):
        #创建一个标签
        self.helloLabel = Label(self, text='Hello, world!')
        #将helloLabel加入父容器
        self.helloLabel.pack()
        #添加一个输入框
        self.nameInput = Entry(self)
        self.nameInput.pack()
        #添加一个输出对话框
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
#         #添加按钮quitButton
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         #将按钮加入父容器
#         self.quitButton.pack()
'''
在GUI中，每个Button、Label、输入框等，都是一个Widget。
Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，
grid()可以实现更复杂的布局。
在createWidgets()方法中，我们创建一个Label和一个Button，
当Button被点击时，触发self.quit()使程序退出。
'''
app=Appliaction()
app.master.title('myHello')
app.mainloop()     