import sqlite3


filename = "sql/hashtag.db"
conn = sqlite3.connect(filename)

c = conn.cursor()

c.execute(
    """SELECT method, AVG(rate) FROM rates
GROUP BY method
"""
)
print(c.fetchall())
c.close()
