# coding=utf-8

'''

编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

'''

import os


def find_file(path, key):
    result = []

    def find_current_path(path):
        for val in os.listdir(path):
            next_path = os.path.join(path, val)
            if os.path.isfile(next_path) and os.path.splitext(val)[1] == key:
                # result.append(os.path.abspath(val))
                result.append(val)
            elif os.path.isdir(val):
                find_current_path(next_path)
        return result

    return find_current_path(path)


print(find_file('/Users/zhangshuqing/home/python-work/study', '.py'))
