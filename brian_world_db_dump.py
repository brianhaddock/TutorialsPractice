import sqlite3 as lite

c = lite.connect("D:\\Users\\Brian\\OneDrive\\Projects\\Python\\brian_world.db")
cur = c.cursor()

cur.execute("Select * from actions")
print(cur.fetchall())

c.commit()