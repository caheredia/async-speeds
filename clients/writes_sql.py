import sqlite3
import datetime
import time
from sql.helpers import save_rate, get_row_count, find_rate

DATABASE = "sql/write-speeds.db"
conn = sqlite3.connect(DATABASE)
c = conn.cursor()


def write(tag):
    c.execute("INSERT INTO timestamps VALUES (:stamp)", {"stamp": tag})
    conn.commit()


# print initial row count
get_row_count("timestamps")

runs = 100
rows = 100
for i in range(runs):
    start = time.time()
    for i in range(rows):
        time_now = datetime.datetime.now().isoformat()
        write(time_now)
    end = time.time()
    delta = end - start
    write_rate = find_rate(delta, rows)
    # save write speeds
    save_rate("sql", write_rate=write_rate)


# print final row count
get_row_count("timestamps")


conn.close()
