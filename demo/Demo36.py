# coding=utf-8



'''

with 语句是在 Python 2.5 版本引入的，从 2.6 版本开始成为缺省的功能。
with 语句作为 try/finally 编码范式的一种替代，用于对资源访问进行控制的场合。


with看起来如此简单，但是其背后还有一些工作要做，因为你不能对Python的任意符号使用with语句，
它仅能工作于支持上下文管理协议（context management protocol）的对象。
也就是说，只有内建了“上下文管理”的对象可以和with一起工作，目前支持该协议的对象有：


file
decimal.Context
thread.LockType
threading.Lock
threading.RLock
threading.Condition
threading.Semaphore
threading.BoundedSemaphore




有了上下文管理器，with 语句才能工作。
下面是一组与上下文管理器和with 语句有关的概念。
上下文管理协议（Context Management Protocol）：包含方法 __enter__() 和 __exit__()，支持
该协议的对象要实现这两个方法。
上下文管理器（Context Manager）：支持上下文管理协议的对象，这种对象实现了
__enter__() 和 __exit__() 方法。上下文管理器定义执行 with 语句时要建立的运行时上下文，
负责执行 with 语句块上下文中的进入与退出操作。通常使用 with 语句调用上下文管理器，
也可以通过直接调用其方法来使用。

'''

from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('query by %s' % self.name)


@contextmanager
def create(name):
    print('start.....')
    q = Query(name)
    yield q
    print('end....')


with create('zsq') as q:
    q.query()
