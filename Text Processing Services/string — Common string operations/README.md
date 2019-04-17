这里介绍标准库中string --- 常见的字符串操作的相关内容 

Source code:  [Lib/string.py](https://github.com/python/cpython/blob/3.7/Lib/string.py)

Link: [https://docs.python.org/3/library/string.html#module-string](https://docs.python.org/3/library/string.html#module-string)

包含：

# [String constants.py](https://github.com/lichangke/Python-Standard-Library-Learn/blob/master/Text%20Processing%20Services/string%20%E2%80%94%20Common%20string%20operations/String%20constants.py)
介绍字符串常量 

# [Custom String Formatting.py](https://github.com/lichangke/Python-Standard-Library-Learn/blob/master/Text%20Processing%20Services/string%20%E2%80%94%20Common%20string%20operations/Custom%20String%20Formatting.py)
介绍自定义字符串格式 class string.Formatter中主要的3个函数

format(format_string, *args, **kwargs)

vformat(format_string, args, kwargs)

parse(format_string)

# [Format String Syntax.py](https://github.com/lichangke/Python-Standard-Library-Learn/blob/master/Text%20Processing%20Services/string%20%E2%80%94%20Common%20string%20operations/Format%20String%20Syntax.py)
格式字符串语法示例

# [Template strings.py](https://github.com/lichangke/Python-Standard-Library-Learn/blob/master/Text%20Processing%20Services/string%20%E2%80%94%20Common%20string%20operations/Template%20strings.py)
介绍了模板字符串的规则

介绍了class string.Template(template) 类中的 substitute(mapping, **kwds) 和 safe_substitute(mapping, **kwds) 方法 
