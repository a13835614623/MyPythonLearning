'''
Created on 2018年11月2日
@author: zzk
'''
#类型转换int(),字符串转int
age = int(input('请输入您的年龄:'))
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')