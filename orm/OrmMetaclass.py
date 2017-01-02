# coding=utf-8

# 添加 属性和列的映射关系，表名和类的映射关系


from orm.Field import Field


class OrmMetaclass(type):
    def __new__(cls, cls_name, cls_parents, cls_attrs):
        print("ormMetaclass run cls_name:%s,cls_attrs=[%s]" % (cls_name, str(cls_attrs)))

        cls_attrs['__table__'] = cls_name
        mapping = dict()
        for key, value in cls_attrs.items():
            if isinstance(value, Field):
                mapping[key] = value
        cls_attrs['__mapping__'] = mapping
        for k in mapping:  # 实例的属性会遮盖类的同名属性 所以需要从类中删除该属性
            cls_attrs.pop(k)
        return type.__new__(cls, cls_name, cls_parents, cls_attrs)
