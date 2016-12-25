# coding=utf-8

'''

    筛选器：filter
'''


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数

def is_palindrome(n):
    reverse = str(n)[::-1]
    return str(n) == reverse # return True  的才会被筛选出来


output = filter(is_palindrome, range(10, 10000))
print(list(output))
