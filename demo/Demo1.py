#  study python first day
# coding=utf-8
cal = 0
for x in range(101):
    cal = cal + x
print("The result is %d", cal)

array = [1, 2, 9, 4, 6, 0]
print("##########=======>")
print(len(array))
print(array[-2])
array.sort()
print(array)
print(array[1])
'''
    多行注释这样写的
    这就是多行注释
'''

_dict = {1: 'a', 2: array, 3: 'd'}

print(_dict)

_dict.setdefault(100, "100")

# dict.setdefault(_dict, 5, "b")
copy_dict = _dict.copy()

print(copy_dict)

print(_dict)

# set
_s = set([1, 2, 3])  # 这里并不是说可以存list
print(_s)
_s.add(5)
print(_s)
_s.remove(5)
print(_s)
_s_1 = set([3, 4, 5, 6])

_s_result = _s & _s_1  # 求俩个set集合的交集
print(_s_result)

_s_result_1 = _s | _s_1

print(_s_result_1)  # 求两个集合的并集


# method

# 不带返回值的函数
def _get_lick_name(code):
    if code == 'a':
        print("小明")
    elif code == 'b':
        print("小花")
    else:
        print("other")


_get_lick_name('b')


# 带返回值的函数
def _get_name(code):
    if code == 1:
        return "min"
    elif code == 2:
        return "middle"
    else:
        return "other"


print(_get_name(2))




for i in range(2):
    print(i)


