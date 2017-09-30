# coding=utf-8

# 列表生成式  运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。

import os

dir = [d for d in os.listdir('.')]

print(dir)

array = ["Nokia", "Huawei", "Apple", 15, "Xiaomi"]


# 类似三元运算
last_array = [item.lower() if isinstance(item, str) else item for item in array]

print(last_array)



