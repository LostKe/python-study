# coding=utf-8

'''

    排序：sorted 函数  是一个高阶函数
'''

#  L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]  按名称排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def sort_by_name(t):
    return t[0]


def sort_by_score(t):
    return t[1]


output = sorted(L, key=sort_by_name, reverse=True) # 按 姓名的首字母排序

output_sort_score = sorted(L, key=sort_by_score, reverse=True) # 按成绩排序

print(output)

print(output_sort_score)



