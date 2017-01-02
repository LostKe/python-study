# coding=utf-8

'''
跨平台 多进程编写  利用 Process 模块
'''

from multiprocessing import Process

import os


def run_process(name):
    print('process is run param[%s] pid=%s,parent pid is :%s' % (name, os.getpid(), os.getppid()))


if __name__ == '__main__':
    print('current pid=%s' % os.getpid())
    p = Process(target=run_process, args=('test',))
    print('child process will start')
    p.start()
    p.join()  # 等待子进程结束后 继续向下运行
    print("child process is end ")
