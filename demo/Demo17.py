# coding=utf-8


'''
把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
'''


# 使用 property 设置 get/setter 方法

class Student(object):
    score = 500

    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score


class Person(object):
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, val):
        self.__address = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val):
        self.__age = val


class Man(Person, Student):
    def __init__(self, name, age, address, score):
        Person.__init__(self, name, age, address)
        Student.__init__(self, score)

    def work(self):
        print("i'am man i must work")


p = Person("zs", 20, "futian sz cn")

p.address = '北京'

print(p.address)

m = Man("xiaoming", 30, "sz", 123)

print("%s==>%s===>%s" % (m.name, m.age, m.address))

print(m.get_score())
