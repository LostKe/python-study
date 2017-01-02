# coding=utf-8

'''
    进程池

'''
from multiprocessing import Pool
import os, time


def run_process(name):
    print('run task [%s] ,pid=%s' % (name, os.getpid()))
    start = time.time();
    time.sleep(.5)
    end = time.time();
    print('task [%s] use %0.2f seconds ' % (name, (end - start)))


if __name__ == '__main__':
    print('parent pid=%s' % os.getpid())
    p = Pool(4)  # 设置同时跑4个进程
    for i in range(5):
        p.apply_async(run_process, args=(i,))
    print('waiting for all process done....')
    p.close()
    p.join()
    print('all process has done')
