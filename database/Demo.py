# coding utf-8

import sqlite3

# 连接到sqlite数据库，数据库文件是test.db ,若文件不存在会自动在当前目录创建test.db文件
conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS user (id VARCHAR(20) PRIMARY KEY ,name VARCHAR(20))")

cursor.execute("INSERT INTO user (id,name) VALUES ('1','zsq')")

cursor.execute("INSERT INTO user (id,name) VALUES ('2','lyf')")

count = cursor.rowcount

cursor.close()
conn.commit()
conn.close()
print(count)
