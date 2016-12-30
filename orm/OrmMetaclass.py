# coding=utf-8

# 添加 属性和列的映射关系，表名和类的映射关系


from orm.Field import Field


class OrmMetaclass(type):
    def __new__(cls, cls_name, cls_parents, cls_attrs):
        cls_attrs['__table__'] = cls_name
        mapping = dict()
        for key, value in cls_attrs.items():
            if isinstance(value, Field):
                mapping[key] = value
        cls_attrs['__mapping__'] = mapping
        return type.__new__(cls, cls_name, cls_parents, cls_attrs)
