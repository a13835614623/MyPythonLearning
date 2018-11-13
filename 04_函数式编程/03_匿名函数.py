'''
Created on 2018年11月5日

@author: zzk
'''
# 在Python中，对匿名函数提供了有限支持.
# 还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)
def build(x, y):
    return lambda: x * x + y * y
print(build.__name__)