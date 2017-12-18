# coding=utf-8

import os

import shutil  # 文件操作补充模块


# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

def create_dir(path):
    if (os.path.isdir(path)):
        return
    else:
        os.mkdir(path)


print(os.name)

print(os.uname())

print(os.environ)

# 查看当前路径
print(os.path.abspath('.'))
print(os.path.abspath('Demo1.py'))

test_path = os.path.join(os.path.abspath('.'), 'test')
print(test_path)

create_dir(test_path)

# os.path.splitext  得到文件名和文件拓展名

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


for val in os.listdir('.'):
    print(os.path.splitext(val))