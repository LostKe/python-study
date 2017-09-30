# coding=utf-8
# 高级特性 切片 arry[a:b]  取list中的元素 从 index=a 元素开始 到index=b 元素结束 结果不包含b元素

'''
    array=[1,2,3,4,5]
    array[start,end,step]  start:开始位置   end:结束位置  step:步进参数

    当step > 0 时
    切片从 start(含start)处开始，到end（不含end）处结束，**从左往右**，每隔（step-1）
    （索引之间的差仍为step，但相隔的元素是step-1个）个元素进行一次截取。
    这时，start 指向的位置应该在end指向的位置的左边，否则返回值为空


    当step < 0 时
    切片从 start(含start)处开始，到end（不含end）处结束，**从右往左**，每隔（step-1）
   （索引之间的差仍为step，但相隔的元素是step-1个）个元素进行一次截取。
    这时，start 指向的位置应该在end指向的位置的右边，否则返回值为空

'''

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(array[2:4])  # [3,4]

print(list(range(100)[1::2]))  # 0-100 的奇数
print(list(range(101)[::2]))  # 0-100的偶数
# 求 0-100 偶数的和


from functools import reduce


def fun_add(x, y):
    return x + y


print(reduce(fun_add, list(range(101)[::2])))

print(reduce(lambda x, y: x + y, list(range(101)[::2])))
