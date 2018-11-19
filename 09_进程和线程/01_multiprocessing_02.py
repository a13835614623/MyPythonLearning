#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月19日

@author: zzk
'''
# Pool 进程池
from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('执行进程：[%s](%s)' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('[%s]执行时间:(%s)' %(name,end-start))
if __name__=='__main__':
    print('父进程:',os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有子进程执行完毕...')
    p.close()#调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()#对Pool对象调用join()方法会等待所有子进程执行完毕
    print('所有子进程执行完毕...')
# 请注意输出的结果，task 0，1，2，3是立刻执行的，
# 而task 4要等待前面某个task完成后才执行，
# 这是因为Pool的默认大小是CPU的核数，我的电脑为四核CPU，因此，最多同时执行4个进程。
# 第五个进程必须等待
# 这是Pool有意设计的限制，并不是操作系统的限制。

