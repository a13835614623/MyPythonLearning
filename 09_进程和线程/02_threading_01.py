#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月20日

@author: zzk
'''
# 多线程
# Python的线程是真正的Posix Thread
# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
# threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。
import threading,time
def loop():
    print('线程%s正在运行:...' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('线程%s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('线程 %s 执行结束...' % threading.current_thread().name)
print('线程%s正在运行:...' % threading.current_thread().name)
t=threading.Thread(target=loop,name='loopThread')
t.start()
t.join()
print('线程 %s 执行结束...' % threading.current_thread().name)
# 任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
# Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
# 主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。