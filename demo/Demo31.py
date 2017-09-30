# coding=utf-8

from datetime import datetime

now = datetime.now()

print(now)

t = 3343121212.23

print(datetime.fromtimestamp(t))

print(datetime.utcfromtimestamp(t))
