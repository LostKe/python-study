# coding=utf-8

'''

协程
协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。



生成器 send
第一次调用时，请使用next()语句或是send(None)，
不能使用send发送一个非None的值，否则会出错的，
因为没有Python yield语句来接收这个值。
'''


def coustom():
    index = 0
    r = 'i am init str'
    print('c')
    while True:
        if index == 0:
            print('i am first enter loop')
            index += 1
        n = yield r
        print('e')
        if not n:
            return
        print('[coustom] coustoming  %s...' % n)
        r = '200 OK'


def produce(c):
    print('a')
    first_str = c.send(None)  # 这里是为了启动生成器
    print(first_str)
    print('b')
    n = 0
    while n < 5:
        n = n + 1
        print('[produce] producing %s ....' % n)
        r = c.send(n)  # send 发送过去  yield 可以接收到
        print('[produce] coustom return :%s' % r)
    c.close()


c = coustom()

produce(c)

'''
1.首先调用c.send(None)启动生成器；

2.然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

3.consumer通过yield拿到消息，处理，又通过yield把结果传回；

4.produce拿到consumer处理的结果，继续生产下一条消息；

5.produce决定不生产了，通过c.close()关闭consumer，整个过程结束。



'''
