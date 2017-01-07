# coding=utf-8

import itertools

# group 挑选 相邻两个元素相等的
for key, group in itertools.groupby('ADDDccdDacBBadebd', lambda c: c.upper()):
    print(key, list(group))

for c in itertools.chain('abc', 'xyz'):
    print(c)
