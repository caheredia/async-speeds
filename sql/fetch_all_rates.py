import sqlite3

conn = sqlite3.connect("hashtag.db")

c = conn.cursor()

c.execute(
    """SELECT * FROM rates
"""
)
print(c.fetchall())
c.close()
