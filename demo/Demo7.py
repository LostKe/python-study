# coding=utf-8

# 高阶函数  编写高阶函数就是为了函数的参数能够接受别的函数

def method(a, b):
    return a * b


# 这里 可以将函数作为参数 传递

def add(x, y, method):
    return x + y + method(x, y)


print(add(4, 6, method))
