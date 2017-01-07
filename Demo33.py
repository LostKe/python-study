# coding=utf-8

import hashlib

str = "i'am a good boy"
str1 = "i'am b good boy"
md5 = hashlib.md5()
md5.update(str.encode('utf-8'))

print(md5.hexdigest())

md5_str1 = hashlib.md5()
md5_str1.update(str1.encode('utf-8'))
print(md5_str1.hexdigest())
