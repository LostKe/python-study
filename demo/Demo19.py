# coding=utf-8

"""
metaclass，直译为元类
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

"""


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, base, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, base, attrs)


class Mylist(list, metaclass=ListMetaclass):
    pass


L = Mylist()
L.add("ccc")

print(L)

age = 35

print(type(age))

print(age.__class__.__class__)
