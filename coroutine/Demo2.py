# coding=utf-8

'''

asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

'''

import asyncio


@asyncio.coroutine
def hello():
    print('hello world')

    r = yield from asyncio.sleep(1)
    print(r)

    print('hello world again')


loop = asyncio.get_event_loop()

loop.run_until_complete(hello())
loop.close()
