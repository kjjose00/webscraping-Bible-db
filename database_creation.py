# this is the python code for database creation

import sqlite3
connection = sqlite3.connect('bible.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS bible
              (id INTEGER PRIMARY KEY NOT NULL,Testament INTEGER,Bookname TEXT,Bookno INTEGER,Chapter INTEGER,Verseno IINTEGER,Verse TEXT)''')

connection.commit()
connection.close()