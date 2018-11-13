# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，
# 就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
# 字符串是以Unicode编码的
print(ord('A'))# 65
print(chr(65))#A
print('\u4e2d\u6587')

x=b'ABC'#bytes类型
xx='ABC'
print(x,len(x))
print(xx,len(xx))

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('中文UTF-8编码之后：','中文'.encode('utf-8'))
# 解码
decodeStr = b'ABC'.decode('ascii')
print('解码之后:',decodeStr)
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
print('中'.encode('utf-8').__len__())
print('a'.encode('utf-8').__len__())

# 格式化 %%表示%
print('hello,%s %%' %'world')

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
