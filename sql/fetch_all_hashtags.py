import sqlite3

conn = sqlite3.connect("hashtag.db")

c = conn.cursor()

c.execute(
    """SELECT * FROM hashtags
"""
)
print(c.fetchall())
c.close()
