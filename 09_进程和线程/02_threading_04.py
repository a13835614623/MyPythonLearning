#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月20日

@author: zzk
'''
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()