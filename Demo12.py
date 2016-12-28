# coding=utf-8

'''

装饰器   由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

'''

import functools

def output_now(county):
    print(county + ':2016-02-03')


val = output_now  # 函数对象赋值给变量

val('beijiing')

print(output_now.__name__)
print(val.__name__)

'''
    通过装饰模式，使方法执行前后打印自定义日志
'''
print("=======================")


def log(func):
    @functools.wraps(func)
    def warpper(*args, **kwargs):
        print('start call %s()' % func.__name__)
        next_step = func(*args, **kwargs)
        print('end call %s()' % func.__name__)
        return next_step

    return warpper


# @log  相当于  print_now=log(print_now)

def print_now(city):
    print(city + ":now is 2016")
    return True


method = log(print_now)
method('beijing')

# 使用@ 语法糖的效果
print("#####################")


@log
def print_now_a(city):
    print(city + ":now is 2016")
    return True


print_now_a("london")

#  带参数的装饰器

print("###################")


def log_level(level):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kwargs):
            print("%s ==> call %s" % (level, func.__name__))
            result = func(*args, **kwargs)
            print("%s ==> call %s" % (level, func.__name__))
            return result

        return wapper

    return decorator


# foo=log_level('debug')(bar) ;  foo()
@log_level(level='debug')
def bar():
    print("this is bar")


bar()
