# coding=utf-8

from orm.OrmMetaclass import OrmMetaclass


class Model(dict, metaclass=OrmMetaclass):
    def __init__(self, **kwargs):
        print("Model init")
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, item):
        print(">>>>>>>:%s" % item)
        try:
            return self[item]
        except KeyError:
            raise AttributeError("model has no attribute [%s]" % item)

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mapping__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print("sql===>%s" % sql)
        print("args===>%s" % str(args))
