'''
Created on 2018年11月3日

@author: zzk
'''
print(list(range(1,11)))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l = [x*x for x in range(10)]
print(l)#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#双重循环生成全排列
l2 = [m+n for m in 'ABC' for n in 'abc']
print(l2)

#当前目录所有的文件和文件名
import os
l3 = [d for d in os.listdir('.')]
print(l3)
#迭代dict
dicts = {'name':'zzk','age':'18'}
l4 = [k + '=' + v for k, v in dicts.items()]
print(l4)
