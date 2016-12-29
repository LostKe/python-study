# coding=utf-8

'''
偏函数：

functools.partial就是帮助我们创建一个偏函数的

简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

'''

import functools

intforHexdex = functools.partial(int, base=2)
print(intforHexdex)

print(intforHexdex('10110'))

'''
小结

当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

'''


def foo(x, y, base=20):
    return x + y + base


print(foo(1, 1))

fun = functools.partial(foo, 5)

print(fun(6))
