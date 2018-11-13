#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月7日

@author: zzk
'''
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s: %s' %(self.__name,self.__score))
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')
    def get_score(self):
        return self.__score
s = Student('zzk',99)
# s.set_score(101)
s.set_score(100)
'''
需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
是特殊变量，特殊变量是可以直接访问的，不是private变量，
所以，不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，
“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
'''
s.print_score()
print(s)
'''
双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
所以，仍然可以通过_Student__name来访问__name变量：
'''
# print(s._Student__name)
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

# >>> bart = Student('Bart Simpson', 59)
# >>> bart.get_name()
# 'Bart Simpson'
# >>> bart.__name = 'New Name' # 设置__name变量！
# >>> bart.__name
# 'New Name'
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
# 内部的__name变量已经被Python解释器自动改成了_Student__name，
# 而外部代码给bart新增了一个__name变量。不信试试：