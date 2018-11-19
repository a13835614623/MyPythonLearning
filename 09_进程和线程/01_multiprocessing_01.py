#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月19日

@author: zzk
'''
'''
要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，
返回一次，但是fork()调用一次，返回两次，
因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
'''
# import os
# print('Process (%s) start...' % os.getpid())
# pid =os.fork()
# 由于Windows没有fork调用，上面的代码在Windows上无法运行。
# 由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的.
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
# if pid==0:
# print('我是子进程(%s),我的父进程是(%s)' % (os.getpid(),os.getpid()))
# print('----------------------------------')
# multiprocessing
from multiprocessing import Process
import os
# 子进程要执行的代码
def run_proc(name):
    print('执行子进程 【%s】 (%s)...' % (name,os.getpid()))
if __name__=='__main__':
    print('父进程：(%s)' % os.getpid())
    p=Process(target=run_proc('test'))
    print('子进程将要启动...')
    p.start()
    p.join()
    print('子进程运行结束...')

