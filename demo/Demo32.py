# coding=utf-8
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(12, 3)

print(p.x)

print(p.y)

Cycle = namedtuple('Cycle', ['x', 'y', 'r'])

cycle = Cycle(12, 49, 5)

print(Cycle)
print(cycle)

print(Cycle.__doc__)