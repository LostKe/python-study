# coding=utf-8

# map 和 reduce


'''
    map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

'''


# 实现 f(x)=x^2

def f(x):
    return x * x


array = [2, 4, 6, 8, 10]
result = map(f, array)

for val in result:
    print(val)

# print(list(result))

# str 函数可以把object 转换为string 类型数据
# print(str(123))
str_array = list(map(str, [1, 2, 3, 4, 5]))
print(str_array)

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，

'''

from functools import reduce


# 计算list 的和
def fun_add(x, y):
    return x + y


val = reduce(fun_add, [4, 5, 6, 7])
print(val)

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']：
'''


def format_input(array):
    def word_format(name):
        name = name.lower()  # 全部转换为小写字母
        return name[:1].upper() + name[1:]

    return map(word_format, array)


print(list(format_input(['adam', 'LISA', 'barT'])))


# list 求积

def fun(x, y):
    return x * y


def prod(array):
    return reduce(fun, array)


print(prod([1, 2, 3, 4, 5]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def char2int(c):
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}.get(c)


# 以 . 分割
def strcut(str):
    array = str.split(".")
    return array[0], array[1][::-1]


def str2float(val):
    start, end = strcut(val)
    return reduce(lambda x, y: x * 10 + y, map(char2int, start)) + reduce(lambda x, y: x / 10+y, map(char2int, end))/10


print(str2float("312.14151629"))
