# coding=utf-8

import math


# 定义一个方法给list 中的元素：若元素>5 则加上100
def _change_value(_array):
    for index, val in enumerate(_array):
        if val > 5:
            _array[index] = val + 100


_array = [2, 4, 6, 1, 9]

_change_value(_array)

print(_array)


# 定义一个多返回值的函数

def move_dx_dy(dx, dy, angle=0):
    nx = dx + math.cos(angle)
    ny = dy + math.cos(angle)
    return nx, ny


result = move_dx_dy(12, 24, 45)  # 返回的其实是一个 tuple
print(result)


# 定义带有默认参数的函数

def add_end(array=None):
    if array is None:
        array = []
    array.append("end")
    return array


print(add_end())
print(add_end([1, 2]))


# 定义可变参数的函数

def calc(*numbers):
    result = 0
    for x in numbers:
        result = result + x
    return result


print(calc(1, 2, 3))

numbers = [100, 0, 2]

print(calc(*numbers))  # 使用可变参数函数


# 定义关键字参数函数  接收的参数应该为键值对 或者定义的dict
# other 接收的参数必须是 String 类型

def person(name, age, **other):
    print("name", name, "age", age, "other", other)


person("zs", 20)

person("aa", 12, city="shenzhen")

location = {"prov": "gd", "street": "buji"}
person("bb", 13, **location)

# 参数组合
'''
在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，
这4种参数都可以一起使用，或者只用其中某些，但是请注意，
参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
'''


def func(a, b, c=0, *args, **kw):
    print("a=", a, "b=", b, "c=", c, "args=", args, "kw=", kw)


func(1, 2, 1, 3, city="sz")

kw = {"city": "beijing", "street": "luohu", "1": 100}

func(1, 2, **kw)

arg = (1, 2, 3, 4)
func(*arg, **kw)


# 定义 递归函数   计算 n!

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(50))



