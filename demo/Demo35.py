# coding=utf-8

class Query(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __enter__(self):
        print('method enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('method exit')
        return self

    def print_info(self):
        print('this is query print method')


with Query('zs', 12, 'shenzheng') as q:
    q.print_info()
