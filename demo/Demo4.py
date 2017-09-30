# coding=utf-8

# 迭代

'''

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的，例如：
'''

from collections import Iterable
from collections import Iterator

flag = isinstance([], Iterable)
print(flag)
print(isinstance([], Iterator))

print(isinstance(iter("abc"), Iterator))
print(isinstance("abc".__iter__(), Iterator))

print("==========")
array = ["a", "b", "c", "d", "e", "f"]

# 普通循环
for val in array:
    print(val)

# 带 index 的循环
for index, val in enumerate(array):
    print(index, val)

print("=========")
# 迭代 dict

my_dict = {1: "a", 2: "b", 3: "c"}

for key in my_dict:
    print(key, my_dict.get(key))

array = [1, 2, 3, 4, 5]

# print(next(array)) List 不是 Iterator 对象调用next 方法会出问题

print(isinstance(array.__iter__(), Iterator))
