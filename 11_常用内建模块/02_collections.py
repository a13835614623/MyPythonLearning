#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月26日

@author: zzk
'''
# namedtuple
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，
# 又可以根据属性来引用，使用十分方便。
p=Point(1,2)
# p.x=5 不能改变值，会报错
print(p.x,p.y,isinstance(p, Point),type(p))
print('------------------------------------------')

# deque
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['z','z','k'])
q.append('A')
print(q)#deque(['z', 'z', 'k', 'A'])
q.pop()
print(q)#deque(['z', 'z', 'k'])
q.appendleft('hello')
print(q)
q.popleft()#deque(['hello', 'z', 'z', 'k'])
print(q)#deque(['z', 'z', 'k'])
print('------------------------------------------')

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['1']='zzk'
print(dd['1'],dd['2'])#zzk N/A
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
print('------------------------------------------')

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
print('------------------------------------------')
# ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。
# ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# 什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，
# 参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。
# 我们可以用ChainMap实现参数的优先级查找，
# 即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。
from collections import ChainMap
import os, argparse
# 默认参数
defaults = {
    'color':'red',
    'user':'guest'
}
# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)
# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
print('------------------------------------------')

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c=Counter()
for ch in 'helloworld':
    c[ch] = c[ch]+1
print(c)