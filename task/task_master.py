# coding=utf-8


import random, os, time, queue

from multiprocessing.managers import BaseManager

# 发送队列
task_send_queue = queue.Queue()
# 接收队列
task_recevice_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_send_queue', callable=lambda: task_send_queue)
QueueManager.register('get_task_recevice_queue', callable=lambda: task_recevice_queue)

manager = QueueManager(address=('', 50000), authkey=b'abc')

# 启动Queue

manager.start()

# 获得通过网络访问的queue 对象
task = manager.get_task_send_queue()

result = manager.get_task_recevice_queue()

# 放任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('put task %s ......' % n)
    task.put(n)

# 获取结果
print("try get results....")

for i in range(10):
    r = result.get(timeout=10)
    print("get result:%s" % r)
# 关闭

manager.shutdown
print('master exit .....over!!!')
