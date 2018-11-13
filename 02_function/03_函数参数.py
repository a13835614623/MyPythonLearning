#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月3日

@author: zzk
'''
# def power(x):
#     return x*x
# print(power(2))
def power(x,n=2):
    count=0
    num=1
    while count<n:
        num*=x
        count+=1
    return num
print(power(2))#默认计算平方
print(power(2,3))
'''
设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
'''
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())#['END']
print(add_end())#['END', 'END']
print(add_end())#['END', 'END', 'END']
'''
很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。

原因解释如下：

Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，
它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

定义默认参数要牢记一点：默认参数必须指向不变对象！ 
要修改上面的例子，我们可以用None这个不变对象来实现：
'''
def add_end2(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
print(add_end2())#['END']
print(add_end2())#['END']
print(add_end2())#['END']
'''
为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，
这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
'''

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))
print(calc())
num = [1,2,3]
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
# print(calc(num))#会报错
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(calc(*num))# 14

# 关键参数
'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('zzk',18)

#写法1
person('zzk',18,city='天津',address='北辰')
#写法2
extra = {'city':'天津','address':'北辰'}
person('zzk',18,city=extra['city'],address=extra['address'])
#写法3 kw获得的dict是extra的一份拷贝
person('zzk',18,**extra)
'''
**extra 表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
'''

# 命名关键字参数
def person2(name, age,*,city,job):
    print('name:', name, 'age:', age, 'city:',city,'job:',job)
person2('Jack', 24, city='Beijing', job='Engineer')
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# person2('Jack', 24, 'Beijing', 'Engineer')#报错

# 命名关键字参数可以有缺省值，从而简化调用：
def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)
# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
person('Jack', 24, job='Engineer')

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person5(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

# 参数组合
# 在Python中定义函数，
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

