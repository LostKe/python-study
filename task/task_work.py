# coding=utf-8

import time, os, sys, queue

from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_send_queue')
QueueManager.register('get_task_recevice_queue')
# 服务端地址 (主任务 运行所在的地址)
server_address = '115.159.91.135'
print('connect to server ....[%s]' % server_address)
# 端口 验证码得保持和 服务端设定的一致 才能通信
m = QueueManager(address=(server_address, 50000), authkey=b'abc')
# 连接
m.connect()
# 获取Queue 对象
task = m.get_task_send_queue()
result = m.get_task_recevice_queue()

# 从task 获取任务，把结果写入result中

for i in range(10):
    try:
        n = task.get(timeout=10)
        print('run task %d * %d ....' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty as e:
        print('task queue is empty', e)

# 处理结束

print('worker exit....')
