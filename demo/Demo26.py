# coding=utf-8

'''
    多进程
'''

import os

print('Process %s start ,my parent is==>%s' % (os.getpid(),os.getppid()))

# Return 0 to child process and PID of child to parent process.
pid = os.fork() # 当前后 会有两个进程执行之后的代码

print("pid====>%s" % pid)

if pid == 0:
    print('i am child Process pid=%s,my parent pid=%s' % (os.getpid(), os.getppid()))
else:
    print('i (%s) just create Process pid=%s' % (os.getpid(), pid))
