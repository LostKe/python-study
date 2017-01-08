# coding=utf-8
import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
print(cur.rowcount)

cur.execute('select * from user')

values = cur.fetchall()
print(values)

cur.close()
con.close()
