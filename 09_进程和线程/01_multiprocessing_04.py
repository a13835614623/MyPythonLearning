#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月19日

@author: zzk
'''
# 进程间通信
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process,Queue
import os,time,random

def write(q,data='hello world'):
    print('写进程：',os.getpid())
    for value in data:
        print("    写 %s 到queue..." % value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    print('读进程：',os.getpid())
    while True:
        value = q.get(True)
        print('    从queue中读取的数据:',value)
if __name__=='__main__':
    queue = Queue()
    write(queue,'my name is zzk')
    read(queue)
# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。