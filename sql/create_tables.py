import sqlite3

conn = sqlite3.connect("hashtag.db")

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
