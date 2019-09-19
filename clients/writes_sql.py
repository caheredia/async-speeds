import sqlite3
import datetime
import time
from clients.helpers import save_rate, get_row_count, find_rate

DATABASE = "sql/write-speeds.db"
conn = sqlite3.connect(DATABASE)
c = conn.cursor()


def add_tag(tag):
    c.execute(
        "INSERT INTO hashtags VALUES (:user,:category,:tag)",
        {"user": "xristian", "category": "leica", "tag": tag},
    )
    conn.commit()


def calculate_write_rate(rows):
    """Returns write rate to write integer number of rows."""
    start = time.time()
    for i in range(rows):
        time_now = datetime.datetime.now().isoformat()
        add_tag(time_now)
    end = time.time()
    delta = end - start
    write_rate = find_rate(delta, rows)
    return write_rate


def multiple_runs(method, rows, runs):
    """"Run writes multiple times and save results to rates table."""
    for i in range(runs):
        write_rate = calculate_write_rate(rows)
        save_rate(method=method, write_rate=write_rate)


def main():

    # print initial row count
    get_row_count("hashtags")

    multiple_runs(method="sql", rows=100, runs=100)

    # print final row count
    get_row_count("hashtags")


if "__main__" == __name__:
    main()

conn.close()
