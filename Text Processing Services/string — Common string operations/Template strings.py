#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Template strings.py
@Time    :   2019/04/18 00:01:38
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   
python 3.7.3 标准库  string     常见的字符串操作    本文件包含：模板字符串
python 3.7.3  https://docs.python.org/3/library/string.html#template-strings
'''

# here put the import lib
from string import Template

'''
模板字符串提供更简单的字符串替换，如PEP 292中所述 https://www.python.org/dev/peps/pep-0292/
模板字符串支持基于$的替换，使用以下规则：
    1、$$是转义; 它被替换为单个$。
    2、$identifier 一个替换占位符，用于匹配映射关键字“identifier”默认情况下，
    “标识符”仅限于以下划线或ASCII字母开头的任何不区分大小写的ASCII字母数字字符串（包括下划线）。$字符后面的第一个非标识符字符结束此占位符。
    3、$ {identifier}相当于$ identifier。当有效标识符字符跟随占位符但不是占位符的一部分时，例如“$ {noun} ification”，则需要它。
    4、字符串中$的任何其他形式都将导致引发ValueError。
字符串模块提供实现这些规则的Template类。class string.Template(template)
'''
# 类 class string.Template(template) 构造函数采用单个参数，即模板字符串。

'''
@Description: 执行模板替换，返回一个新字符串。
@Param: 
mapping：任何类似字典的对象，其键与模板中的占位符匹配。
**kewds: 关键字参数，其中关键字是占位符。
当给出mapping和kwds并且存在重复时，来自kwds的占位符优先。
@Return: 返回一个新字符串
'''
# substitute(mapping, **kwds)
s = Template('The Author is $Author, The Time is $Time')    # 使用Template类构造函数
kewds = {'Author':'leacoder', 'Time':'2019/04/18 00:01:38'}
templatestr = s.substitute(Author='leacoder', Time='2019/04/18 00:01:38')  # **kewds
print(templatestr)  # The Author is leacoder, The Time is 2019/04/18 00:01:38
templatestr = s.substitute(**kewds)  # **kewds
print(templatestr)  # The Author is leacoder, The Time is 2019/04/18 00:01:38
templatestr = s.substitute(kewds)  # mapping
print(templatestr)  # The Author is leacoder, The Time is 2019/04/18 00:01:38
templatestr = s.substitute(kewds,Author='250',Time = 'No Time')  # mapping  **kewds
print(templatestr)  # The Author is 250, The Time is No Time

kewds1 = {'Author':'leacoder'}
templatestr = s.substitute(kewds1)
print(templatestr)  # KeyError: 'Time'
# substitute(mapping, **kwds) End


'''
@Description:  
与substitute（）一样，如果map和kwds中缺少占位符，原始占位符将在结果字符串中完整显示，而不是引发KeyError异常
此外，与substitute（）不同，$的任何其他形式只会返回$而不是引发ValueError。
@Param: 
同 substitute（）
@Return: 
'''
# safe_substitute(mapping, **kwds)
kewds1 = {'Author':'leacoder'}
templatestr = s.safe_substitute(kewds1)
print(templatestr)  # The Author is leacoder, The Time is $Time
# safe_substitute(mapping, **kwds) End