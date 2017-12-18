# coding=utf-8

array = ["a", "b", "c"]

# join 函数 将Iterable 对象连接起来
message = ",".join(array)

print(message)

mapping = {'aaa': 11, 'cc': 12}
mapping["ddddd"] = 999
print(mapping)

from  collections import Iterable

print(isinstance("adsd", Iterable))


print(":".join("abcdefg"))