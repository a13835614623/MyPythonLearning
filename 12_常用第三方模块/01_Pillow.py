#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年12月2日

@author: zzk
'''
# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。
# PIL功能非常强大，但API却非常简单易用。
from PIL import Image

# 操作图像
# 打开一个jpg图像文件
img = Image.open('img/test.jpg')
# 获取图片尺寸
w,h = img.size
print('Original image size: %sx%s' % (w, h))
# 缩放到20%:
img.thumbnail((w//5, h//5))
# 把处理后的图像用png格式保存:
img.save('img/test2.png', 'png')

from PIL import Image, ImageFilter
# 应用模糊滤镜
img2 = img.filter(ImageFilter.BLUR)
img2.save('img/test3.png', 'png')