import sqlite3
import datetime
import time

conn = sqlite3.connect("hashtag.db")

c = conn.cursor()

c.execute(
    """SELECT method, AVG(rate) FROM rates
GROUP BY method
"""
)
print(c.fetchall())
c.close()
