import sqlite3

filename = "sql/hashtag.db"
conn = sqlite3.connect(filename)

c = conn.cursor()

c.execute(
    """SELECT * FROM hashtags
"""
)
print(c.fetchall())
c.close()
