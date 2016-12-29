# coding=utf-8

'''
定义类
'''


class Person(object):
    location = 'futian sz zh'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        return 100

    def print_info(self):
        print("name==>%s,age==>%s" % (self.name, self.age))


p = Person("zs", 20)

print(p.age)

p.print_info()

p.age = 50

p.print_info()

# Python允许对实例变量绑定任何数据  绑定变量 score
p.score = 200

print(p.score)

print(len(p))

print(dir(p))

# 判断对象是否拥有某种属性
print(hasattr(p, 'age'))
print(hasattr(p, 'address'))
setattr(p, "address", "sz futian")
print(hasattr(p, 'address'))
print(getattr(p, "address"))
print(p.address)

print(p.location)


