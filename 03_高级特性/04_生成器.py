'''
Created on 2018年11月3日

@author: zzk
'''
L = [x * x for x in range(10)]
print(L)
# 要创建一个generator，有很多种方法。第一种方法很简单，
# 只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(10))
print(g)
'''
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
generator也是可迭代对象
'''
for item in range(10):
    print(next(g))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(5)
print('---------------')
def fib2(max):#加上yield之后变为generator类型
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for a in fib2(5):
    print(a)
print('--------------------')
#杨辉三角
def triangles(rowsCount):
    listOld=[1]
    listNew=[1]
    for len in range(1,rowsCount+1):
        if len==1:
            listNew=[1]
        elif len==2:
            listNew=[1,1]
        elif len>2:
            listNew=[]
            listNew.append(1)
            for i in range(1,len-1):
                listNew.append(listOld[i]+listOld[i-1])
            listNew.append(1)
        listOld=listNew
        yield listNew
for item in triangles(5):
    print(item)