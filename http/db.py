#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/5/22 下午8:13
# @Author  : lost
# @Site    : 
# @File    : db.py
# @Software: PyCharm
'''
python 操作 mongodb
'''

from pymongo import MongoClient

def getDB_Collection(col):
    client=MongoClient('localhost',27017)
    db_collection=client["wuzhi"][col]
    return db_collection


def inserUser(userId,img_name):
    inser_arg={"user_id":userId,"image_name":img_name}
    user_collection=getDB_Collection("user")
    user_collection.insert(inser_arg)



