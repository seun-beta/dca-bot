import sqlite3

connection = sqlite3.connect("dca.sqlite3")
cur = connection.cursor()

cur.execute()

connection.commit()
