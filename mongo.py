'''
python 操作 mongodb
'''

from pymongo import MongoClient

def getDB_col(col):
    client=MongoClient('localhost',27017)
    db_collection=client.wuzhi.col
    return db_collection


def query(key,value):
    collection=getDB_col("col")
    result=collection.find({key:value})
    return result

if __name__ == '__main__':
    array=query("UserName","libing")
    for item in array:
        print(item)
