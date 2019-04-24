#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   String constants.py
@Time    :   2019/04/16 23:11:26
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   
python 3.7.3 标准库  string     常见的字符串操作    本文件包含：字符串常量
python 3.7.3  https://docs.python.org/3/library/string.html#string-constants
'''
# here put the import lib
import string

# this code block shows string constants start
'''
@Description: The concatenation of the ascii_lowercase and ascii_uppercase constants
@Param: 
@Return: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
'''
# ascii_letters     大小写字母常数
print(string.ascii_letters)	# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

'''
@Description: The lowercase letters 'abcdefghijklmnopqrstuvwxyz'.
@Param: 
@Return: abcdefghijklmnopqrstuvwxyz
'''
# ascii_lowercase   小写字母常数   
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz

'''
@Description: The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. 
@Param: 
@Return: ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''
# ascii_uppercase   大写字母常数
print(string.ascii_uppercase)	# ABCDEFGHIJKLMNOPQRSTUVWXYZ

'''
@Description: The string '0123456789'
@Param: 
@Return: 0123456789
'''
# digits    十进制数字常数
print(string.digits)	# 0123456789

'''
@Description: The string '0123456789abcdefABCDEF'.
@Param: 
@Return: 0123456789abcdefABCDEF
'''
# hexdigits     十六进制数字常数
print(string.hexdigits)	 # 0123456789abcdefABCDEF

'''
@Description: The string '01234567'.
@Param: 
@Return: 01234567
'''
# octdigits     八进制数字常数
print(string.octdigits)	# 01234567

'''
@Description: String of ASCII characters which are considered punctuation characters in the C locale.
@Param: 
@Return: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''
# punctuation   ASCII字符串，在C语言环境中被视为标点字符
print(string.punctuation)	# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

'''
@Description: String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.
@Param: 
@Return: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~  还要加上 字符空间，制表符，换行符，返回页面，换页符和垂直选项卡
'''
# printable     能够被打印的ASCII字符串
print(string.printable)

'''
@Description: A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
@Param: 
@Return: 字符空间，制表符，换行符，返回页面，换页符和垂直选项卡
'''
# whitespace    包含所有被视为空格的ASCII字符的字符串
print(string.whitespace) # 字符空间，制表符，换行符，返回页面，换页符和垂直选项卡
# this code block shows string constants end



