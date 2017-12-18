# coding utf-8

import threading

local_thread = threading.local()


def thread_student():
    std = local_thread.student
    print('helo %s is in %s ,====>%s,===>%s' % (
    std, threading.currentThread().name, local_thread.age, local_thread.address))


def test(name, **kwargs):
    local_thread.student = name
    local_thread.age = kwargs['age']
    local_thread.address = kwargs['address']
    thread_student()


t1_kw = {"age": 10, "address": "beijing"}
t2_kw = {"age": 18, "address": "shanghai"}

t1 = threading.Thread(target=test, args=('aaa',), name='i am Thread 1', kwargs=t1_kw)
t2 = threading.Thread(target=test, args=('bbb',), name='i am Thread 2', kwargs=t2_kw)

t1.start()
t2.start()

t1.join()
t2.join()
