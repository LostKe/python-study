# coding=utf-8
'''

    枚举
'''

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(dir(Month))

for name, member in Month.__members__.items():
    print("name==%s,val==%s" % (name, member.value))


@unique
class Weekday(Enum):
    SUN = 0
    MON = 1
    TUE = 2
    WEN = 3
    THU = 4
    FIR = 5
    SAT = 6


day = Weekday.MON
print(day.value)

for name, member in Weekday.__members__.items():
    print("name==%s,val==%s" % (name, member.value))
