# coding=utf-8

# 生成器



arry = (x * x for x in range(10))

print(arry)

print(arry.__next__())
print(arry.__next__())

print("########")


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, b + a
        n = n + 1
    return 'done'


for val in fib(5):
    print(val)

# 练习 杨辉三角的输出
print("##########")


def triangles(max):
    L = [1]
    step = 0
    while step < max:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))] # L[-1] 为List 的倒数第一个元素
        step = step + 1
    return "done"


for val in triangles(9):
    print(val)
