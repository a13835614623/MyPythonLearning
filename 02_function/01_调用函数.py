'''
Created on 2018年11月2日

@author: zzk
'''
print(abs(-5))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
jdz = abs
print(jdz(-6))