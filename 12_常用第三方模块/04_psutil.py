#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月4日

@author: zzk
'''
# psutil可以用来获取系统信息的。
import psutil
# CPU逻辑数量
print(psutil.cpu_count(logical=True))
# CPU物理核心
print(psutil.cpu_count(logical=False))
# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())
# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))
# 获取内存信息
print(psutil.virtual_memory(),'\n', psutil.swap_memory())
# 获取磁盘信息
print(psutil.disk_partitions(all=True)) # 磁盘分区信息
print(psutil.disk_usage('/'))# 磁盘使用情况
print(psutil.disk_io_counters())# 磁盘IO
# 获取网络信息
print(psutil.net_io_counters()) # 获取网络读写字节／包的个数
print(psutil.net_if_addrs())# 获取网络接口信息
print(psutil.net_if_stats())# 获取网络接口状态
print(psutil.net_connections())#获取当前网络连接信息
# 获取进程信息
print(psutil.pids())# 所有进程ID
p = psutil.Process(560)
print(p.name())# 进程名称
#...还有很多，自行学习