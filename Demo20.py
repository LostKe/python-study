# coding=utf-8

"""

1)   拦截类的创建

2)   修改类

3)   返回修改之后的类


"""
class UpperMetaclass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppper_case_attr = dict((name.capitalize(), value) for name, value in attrs)
        return type.__new__(cls, future_class_name, future_class_parents, uppper_case_attr)





class Foo(metaclass=UpperMetaclass):
    # __metaclass__ = upper_attr
    bar = 'bip'
    pass


print(hasattr(Foo, 'bar'))

print(dir(Foo))
print(hasattr(Foo, 'Bar'))
print(Foo)
foo = Foo()
print(foo)
print(foo.Bar)


print("abc".capitalize())