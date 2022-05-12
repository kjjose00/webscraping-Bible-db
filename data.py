# This is a python file to create 

import sqlite3

conn=sqlite3.connect("bible.db")
cur=conn.cursor()
cur.execute('select count(*) from bible')
s=cur.fetchall()
print(s)
conn.commit()
conn.close()