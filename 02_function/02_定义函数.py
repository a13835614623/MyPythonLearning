'''
Created on 2018年11月2日

@author: zzk
在Python中，定义一个函数要使用def语句，
依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
'''
'''
@param x: 数
@return x的绝对值
'''
def my_abs(x):
    # 类型检查
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if(x>=0):
        return x
    else:
        return -x
'''
请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，
函数内部通过条件判断和循环可以实现非常复杂的逻辑。
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。
'''
print(my_abs(-6))

# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
# 返回多值
# 但其实这只是一种假象，Python函数返回的仍然是单一值：
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y = move(5, 5, 3, 45)
print(x,y)
'''
原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
'''