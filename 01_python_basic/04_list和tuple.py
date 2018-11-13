'''
Created on 2018年11月2日
@note: 
@author: zzk
'''
fruits = ['bnana','apple','pear']
print(fruits)
print('fruits长度为 %s' % len(fruits))
# -1索引直接获取最后一个元素
print(fruits[-1])
# 以此类推，可以获取倒数第2个、倒数第3个：
print(fruits[-2])

fruits.append('purple')
fruits.insert(1, 'strawberry')
fruits.pop()#删除末尾元素
fruits.pop(1)
print(fruits)
# list里面的元素的数据类型也可以不同
lists = [123,True,['java','python','php'],None]
print(list,'\n长度为:',len(lists))

# tuple
# tuple 一旦初始化就不能修改,不可变
# 如果可能，能用tuple代替list就尽量用tuple。
tuples = ('bnana','pear','apple')
# ! 当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
# 如果要定义一个空的tuple
tuples2 = ()
# 定义只有一个元素的tuple
tuples3 = (1,)
print(tuples3)
tuples4 = (1)
print(tuples4)
'''
定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，
又可以表示数学公式中的小括号，这就产生了歧义，
因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
'''

