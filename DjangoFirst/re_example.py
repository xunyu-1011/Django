# 正则:一种高级的字符串处理工具,通常用于字符匹配 re
# 正则是通过描述指定元素的类型和数量来进行匹配,
# 比如手机号: 匹配 以1开头的13位数数字可以实现很高精度的匹配
# 同样,编写正则的复杂程度也在提高

import re
# re.findall() 匹配所有满足正则的条件的字符
# 匹配内容
# strings = "hello world i am your friend_Tom"
# 原样匹配,通常结合其他匹配使用,匹配前边是字母的o
# result = re.findall(r"o",strings)
# print(result)

# .匹配非换行的任意字符
# strings = "hello world \n i am your friend_Tom \t"
# result = re.findall(r"...",strings)
# print(result)

# \d 匹配字符串当中的数字
# strings = "hello world \n i am your friend_Tom \t i am 180 years old"
# result = re.findall(r"\d\d",strings)
# print(result)

# \D 匹配字符串当中的非数字
# strings = "hello world \n i am your friend_Tom \t i am 180 years old"
# result = re.findall(r"\D",strings)
# print(result)

# \w匹配数字, 字母, 下划线
# \W匹配非数字, 非字母, 非下划线

# [] 匹配任意一个元素
strings = "hello world \n i am your friend_Tom \t i am 180 years old"
# result = re.findall(r"[ao]",strings) #
# result = re.findall(r"[^ao]",strings) #取反
# print(result)

# () 组匹配 会将组外的匹配条件,作为条件进行匹配,返回组内匹配到的内容

# ()命名组 ?P<名称>
# strings = "hello world \n i am your friend_Tom \t i am 180 years old"
# result = re.findall(r"",strings)
# # result = re.findall(r"",strings)
# print(result)

# 匹配数量
# *匹配任意多个 匹配0~多次为成功
# strings = "hello world i am your friend_Tom"
# print(re.findall(r".*", strings))

# +匹配1~多次为成功
# strings = "hello world \n i am your friend_Tom \t I am 180a ears old"
# print(re.findall(r".+", strings))

# ?匹配0~1次
strings = "hello world \n I  your friend_Tom \t I am 180a ears old"
print(re.findall(r".?",strings))
# {}匹配指定次
# 特殊的匹配
# ^ 开始
# $ 结尾
