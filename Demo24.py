# coding=utf-8

'''
    python 中的序列化
    Python提供了pickle模块来实现序列化。
'''

import pickle

d = dict(name='zs', age=20, address='sz')

f = open('dump.dp', mode='wb')

pickle.dump(d, f)  # 序列化到文件中

f.close()

print("==============")
# 从文件中反序列化数据
with open('dump.dp', mode='rb') as f:
    d = pickle.load(f)
    print(d)
