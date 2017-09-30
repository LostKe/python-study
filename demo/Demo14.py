#!/usr/bin/env
# coding=utf-8
'''
    编写模块 供其他文件调用

'''
'a test module'

__author__ = "zhangshuqing"


def _getname(name):
    return "my name is %s" % name


def show_name(name):
    return _getname(name)


def show_log():
    print("this py file is exec")


if __name__ == '__main__':
    show_log()
