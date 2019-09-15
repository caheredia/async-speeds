import sqlite3

filename = "sql/hashtag.db"
conn = sqlite3.connect(filename)

c = conn.cursor()

c.execute(
    """CREATE TABLE hashtags (
   user text,
   category text,
   tag text
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