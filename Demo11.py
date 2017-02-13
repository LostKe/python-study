# coding=utf-8

'''

函数作为返回值

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
'''


# TODO 复习闭包
def lazy_sum(*args):
    def sum():
        val = 0
        for i in args:
            val = val + i
        return val

    return sum


func_1 = lazy_sum(1, 2, 3)
fun_2 = lazy_sum(1, 2, 3)
print(func_1)  # 这里返回的不是求和结果而是 求和函数

print(func_1())  # 加上() 调用才会真正的返回结果

print(func_1 == fun_2)  # 每次都会返回一个新的函数，即使参数相同


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


result = count()

for fun in result:
    print(fun())


# lambda 表达式的编写

def build(x, y):
    return lambda: x * y


func_build = build(2, 5)

print(func_build())


def fun_a():
    #返回的是一个函数
    return lambda x, y: x * x + y * y


print(fun_a()(3, 4))
