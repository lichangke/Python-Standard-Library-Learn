#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Format String Syntax.py
@Time    :   2019/04/17 22:49:02
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :  
python 3.7.3 标准库  string     常见的字符串操作  

本文件包含：Format examples  字符串格式化示例

其他方法参见
https://docs.python.org/3/library/string.html#format-examples
'''

# here put the import lib

# 包含str.format（）语法的示例以及与旧的％-formatting的比较。
# 在大多数情况下，语法类似于旧的％-formatting，添加了{}和with：而不是％。例如，'％03.2f'可以翻译为'{：03.2f}'。


# 按位置访问参数：Accessing arguments by position:
tupdata = ("This","is","a","test") # 元组
formatstr = '{0} {1} {2} {3}'.format("This","is","a","test") 
print(formatstr)    # This is a test
formatstr = '{} {} {} {}'.format(*tupdata) # *data 解包参数序列
print(formatstr)    # This is a test
formatstr = '{3} {2} {1} {0}'.format(*tupdata) # *data 解包参数序列
print(formatstr)    # test a is This
formatstr = '{2} {3} {1} {2} {3}'.format(*tupdata)  # 参数可以重复
print(formatstr)    # a test is a test
# 按位置访问参数：Accessing arguments by position: End


# 按关键字访问参数：Accessing arguments by name：
dicdata = {'Author':'leacoder','Time':'2019/04/17'}
formatstr = 'The author is {Author}，The time is {Time}'.format(Author='leacoder',Time='2019/04/17')
print(formatstr)    # The author is leacoder，The time is 2019/04/17
formatstr = 'The author is {Author}，The time is {Time}'.format(**dicdata)
print(formatstr)    # The author is leacoder，The time is 2019/04/17
# 按关键字访问参数：Accessing arguments by name： End


# 访问参数的属性：Accessing arguments’ attributes:
class Point:
    def __init__(self,x,y):
        self.x ,self.y = x, y
point = Point(4,2)
formatstr = 'Thie point is ({key.x},{key.y})'.format(key = point) # key 可为其他 
print(formatstr)  # Thie point is (4,2)
formatstr = 'Thie point is ({point.x},{point.y})'.format(point = point) # point 可为其他 
print(formatstr)  # Thie point is (4,2)
# 访问参数的属性：Accessing arguments’ attributes: End


# 访问参数的各项：Accessing arguments’ items:
tupdata = ("leacoder","2019/04/17") # 元组
formatstr = 'The author is {0[0]},The time is {0[1]}'.format(tupdata)
print(formatstr)    # The author is leacoder,The time is 2019/04/17
formatstr = 'The author is {0[0]},The time is {0[1]}'.format(*tupdata)  # 注意区别
print(formatstr)    # The author is l,The time is e
# 访问参数的各项：Accessing arguments’ items:End


# 替换％s和％r： Replacing %s and %r: 使用 !s !r
formatstr = "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
print(formatstr)    # repr() shows quotes: 'test1'; str() doesn't: test2
# 替换％s和％r： Replacing %s and %r: End

# 对齐文本并指定宽度：Aligning the text and specifying a width:
formatstr = '{:<30}'.format('left aligned') # 左对齐 30位
print(formatstr)    # ‘left aligned                  ’  为了体现位数加了‘’
formatstr = '{:>30}'.format('right aligned')    # 右对齐 30位
print(formatstr)    # ‘                 right aligned’
formatstr = '{:^30}'.format('centered')  # 中间对齐 30位
print(formatstr)    # ‘           centered           ’
formatstr =  '{:*^30}'.format('centered')  # 使用* 作为填充字符
print(formatstr)    # ‘***********centered***********’
# 对齐文本并指定宽度：Aligning the text and specifying a width: End

# 替换％+ f，％ - f和％f并指定符号 Replacing %+f, %-f, and % f and specifying a sign:
formatstr = '{:+f}; {:+f}'.format(3.14, -3.14)  # 总是显示它符号
print(formatstr)    # ‘+3.140000; -3.140000’
formatstr = '{: f}; {: f}'.format(3.14, -3.14)  # 正数前显示空格
print(formatstr)    # ‘ 3.140000; -3.140000’
formatstr = '{:-f}; {:-f}'.format(3.14, -3.14)  # 只显示负号 同 '{:f}; {:f}'
print(formatstr)    # ‘3.140000; -3.140000’
# 替换％+ f，％ - f和％f并指定符号 Replacing %+f, %-f, and % f and specifying a sign: End



# 替换％x和％o并将值转换为不同的进制：Replacing %x and %o and converting the value to different bases:
formatstr = "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(64)
print(formatstr)  # int: 64;  hex: 40;  oct: 100;  bin: 1000000
formatstr = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(64)
print(formatstr)  # int: 64;  hex: 0x40;  oct: 0o100;  bin: 0b1000000
formatstr = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(0b1000001) # 也支持其他进制
print(formatstr)  # int: 65;  hex: 0x41;  oct: 0o101;  bin: 0b1000001
# 替换％x和％o并将值转换为不同的进制：Replacing %x and %o and converting the value to different bases: End


# 使用逗号作为千位分隔符： Using the comma as a thousands separator:
formatstr = '{:,}'.format(1234567890)
print(formatstr)    # 1,234,567,890
# 使用逗号作为千位分隔符： Using the comma as a thousands separator: End



# 表达百分比：Expressing a percentage:
points = 1
total = 3
formatstr = 'points / total = {:.2%}'.format(points/total)
print(formatstr)    # points / total = 33.33%
# 表达百分比：Expressing a percentage: End



# 使用特定类型的格式：Using type-specific formatting:
import datetime
d = datetime.datetime(2019, 4, 17, 22, 49, 2) # 2019/04/17 22:49:02
formatstr = '{:%Y-%m-%d %H:%M:%S}'.format(d)
print(formatstr)    # 2019-04-17 22:49:02
# 使用特定类型的格式：Using type-specific formatting: End