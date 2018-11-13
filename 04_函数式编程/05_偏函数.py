'''
Created on 2018年11月6日

@author: zzk
'''
# Python的functools模块提供了很多有用的功能，
# 其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
print(int('12345'))
# 2进制转换为10进制
def int2(x, base=2):
    return int(x, base)
print(int2('10110'))
'''
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
可以直接使用下面的代码创建一个新的函数int2：
所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单。
'''
import functools
int2 = functools.partial(int, base=2)

max2 = functools.partial(max, 10)
print(max2(5,6,7))
# 相当于max2(10,5,6,7)
