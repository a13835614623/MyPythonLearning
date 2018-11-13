'''
Created on 2018年11月2日
@author: zzk
'''
# dict 类似于Map，键值对
dicts = {'name':'zzk','age':18}
print(dicts)
print(dicts['name'])

dicts['address']='天津'
dicts['address']='tjcu'
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
print(dicts['address'])
print(dicts)
#判断key是否存在
#方法1
print('name' in dicts)
#方法2
print(dicts.get('uid', 'None'))

# 删除key
dicts.pop('address')
print(dicts)
print('----------------------------------------')
'''
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。

而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。

dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，
如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
'''

# set 无序，无重复，类似于数学的集合
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3])
s2 = set([2,3,4,5])
print(s)
# 重复元素在set中自动被过滤：
s.add(4)
print(s)
s.remove(4)
print(s)
print(s&s2)
print(s|s2)
'''
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
'''






