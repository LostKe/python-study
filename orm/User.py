# coding=utf-8


from orm.Model import Model
from orm.Field import IntegerField
from orm.Field import StringField


class User(Model):
    id = IntegerField('id')
    name = StringField("username")
    email = StringField("email")


u = User(id=1, name='zs', email='a123@qq.com')

u.save()
