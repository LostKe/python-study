# coding=utf-8

'''
使用mysql 需要导入依赖库
pip install mysql-connector


'''

import mysql.connector

conn = mysql.connector.connect(user='root', password='', database='school')

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS user (id VARCHAR(20) PRIMARY KEY ,name VARCHAR(20))")
cursor.execute("create table if not exists cup  (id INTEGER  primary key,name varchar(20))")

# cursor.execute("INSERT INTO user (id,name) VALUES ('1','zsq')")
# cursor.execute("INSERT INTO user (id,name) VALUES ('2','zsq')")

cursor.close()
conn.commit()
conn.close()

print('--' * 50)
conn.connect()
cur = conn.cursor()
cur.execute("select * from USER ")
values = cur.fetchall()
print(values)
cur.close()
conn.close()
