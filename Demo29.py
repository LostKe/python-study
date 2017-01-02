# coding=utf-8
'''

进程间通信

进程间通信是通过Queue、Pipes等实现的。
'''

from multiprocessing import Process, Queue

import os, time, random


def write_msg(q):
    print('process to write %s' % os.getpid())
    for val in ['a', 'b', 'c', 'd']:
        print('put %s to queue ' % val)
        q.put(val)
        time.sleep(random.random())


def read_msg(q):
    print('process to read %s' % os.getpid())
    while True:
        value = q.get(True)
        print('get value[%s] from queue' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write_msg, args=(q,))
    pr = Process(target=read_msg, args=(q,))
    pr.start()
    pw.start()

    pw.join()
    pr.terminate()
