import sqlite3

conn=sqlite3.connect('database1.db')
print("OPened")

conn.execute('CREATE TABLE login1(username TEXT,pwd password)')
print("Table success")
conn.close()