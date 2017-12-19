#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 18:48
# @Author  : zsq
# @Site    : 
# @File    : prossbar.py
# @Software: PyCharm
# @desc    : 简单进度条实现

import sys, math,time


def progressbar(cur, total):
    percent = '{:.2%}'.format(float(cur) / float(total))
    sys.stdout.write('\r')
    sys.stdout.write("[%-50s] %s" % ('=' * int(math.floor(cur * 50 / total)), percent))
    sys.stdout.flush()


for index in range(100):
    process = int(float(index) / float(100) * 100)
    progressbar(process, 100)
    time.sleep(1)

