# coding=utf-8

'''

    python: json 转换
'''

import json

d = dict(name='zsq', age=20, adress='sz futian')

val = json.dumps(d)
print(val)

print("==========================")


class Student(object):
    def __init__(self, name, age, address, score):
        self.name = name
        self.age = age
        self.address = address
        self.score = score

    def to_json(self):
        return {'name': self.name, 'age': self.age, 'address': self.address, 'score': self.score}


s = Student('zsq', 25, 'sz longgang', 100)

json_str = json.dumps(s, default=Student.to_json)

print(json_str)
