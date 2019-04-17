#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Custom String Formatting.py
@Time    :   2019/04/16 23:49:13
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   
python 3.7.3 标准库  string     常见的字符串操作  

本文件包含：class string.Formatter

string.Formatter.format(format_string, *args, **kwargs)
string.Formatter.vformat(format_string, args, kwargs)
string.Formatter.parse(format_string)

其他方法参见
python 3.7.3  https://docs.python.org/3/library/string.html#custom-string-formatting
'''

# here put the import lib
import string

# class string.Formatter
# 字符串模块中的Formatter类允许您使用与内置format（）方法相同的实现来创建和自定义您自己的字符串格式化行为。

'''
@Description: 主要的API方法。它采用格式字符串和一组任意位置和关键字参数。它只是一个调用vformat（）的包装器。
@Param: 
format_string: 需要去格式化的目标字符串
*args: 任意位置 元组
**kwargs: 关键字参数 字典
@Return: 
'''
# string.Formatter.format(format_string, *args, **kwargs)
data = ("Pi = ",3.1415926)
strtmp = "This is a test:{}{:.4f}"
formatter  = string.Formatter()
strtmp = formatter.format(strtmp,*data) # 元组
print(strtmp)  # This is a test:Pi = 3.1416

data = {"Key1":3.1415926,"Key2":"Pi = "}
strtmp = "This is a test:{Key2}{Key1}"
formatter  = string.Formatter()
strtmp = formatter.format(strtmp,**data)  # 字典
print(strtmp)  # This is a test:Pi = 3.1415926

# string.Formatter.format(format_string, *args, **kwargs) End



'''
@Description: 此函数执行格式化的实际工作
@Param: 
format_string: 需要去格式化的目标字符串
args: 任意位置 元组
kwargs: 关键字参数 字典
@Return: 
'''
# string.Formatter.vformat(format_string, args, kwargs)
# 注意 Formatter.vformat的参数不是 (*args, **kwargs) 而是 (args, kwargs)
data = ("Pi = ",3.1415926)
strtmp = "This is a test:{}{:.4f}"
formatter  = string.Formatter()
strtmp = formatter.vformat(strtmp,data,{}) # 元组
print(strtmp)  # This is a test:Pi = 3.1416

data = {"Key1":3.1415926,"Key2":"Pi = "}
strtmp = "This is a test:{Key2}{Key1}"
formatter  = string.Formatter()
strtmp = formatter.vformat(strtmp,(),data)  # 字典
print(strtmp)  # This is a test:Pi = 3.1415926
# string.Formatter.vformat(format_string, args, kwargs) End


'''
@Description: 循环遍历format_string并返回一个可迭代的元组（literal_text，field_name，format_spec，conversion）。 vformat（）使用它将字符串分解为文字文本或替换字段。
@Param: 
format_string：需要去格式化的目标字符串
@Return: 
tuples  元组
'''
# string.Formatter.parse(format_string)
strtmp = "This is a test:{}{:.4f}"
formatter  = string.Formatter()
strtuple = formatter.parse(strtmp)

for i, v in enumerate(strtuple):
    print(i, v)
    '''
    0 ('This is a test:', '', '', None)
    1 ('', '', '.4f', None)
    '''
strtmp = "This is a test:{Key2}{Key1}"
formatter  = string.Formatter()
strtuple = formatter.parse(strtmp)

for i, v in enumerate(strtuple):
    print(i, v)
    '''
    0 ('This is a test:', 'Key2', '', None)
    1 ('', 'Key1', '', None)
    '''
# string.Formatter.parse(format_string) End


