# coding=utf-8

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'demo.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)

cursor = conn.cursor()
cursor.execute('CREATE TABLE user(id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), score INT)')
cursor.execute(r"INSERT INTO user VALUES ('A-001', 'Adam', 95)")
cursor.execute(r"INSERT INTO user VALUES ('A-002', 'Bart', 62)")
cursor.execute(r"INSERT INTO user VALUES ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("select * from user where score>=? and score<=? order by score desc", (low, high))
    values = cur.fetchall()
    cur.close()
    conn.close()
    print(values)


get_score_in(70, 100)
