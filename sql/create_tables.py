import sqlite3

filename = "sql/write-speeds.db"
conn = sqlite3.connect(filename)

c = conn.cursor()

c.execute(
    """CREATE TABLE timestamps (
   stamp text
   )"""
)

c.execute(
    """CREATE TABLE rates (
   method text,
   rate real
   )"""
)

conn.commit()
conn.close()
print("database created: ", filename)
