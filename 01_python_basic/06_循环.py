'''
Created on 2018年11月2日
循环
@author: zzk
'''
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
# 计算1-100
# range()函数，生成一个整数序列
# range(5),生成的是[0,1,2,3,4]
sum=0
for x in range(101):
    sum+=x
print(sum)
'''
while循环
'''
n=0
sum=0
while n<=100:
    sum+=n
    n+=1
print(sum)