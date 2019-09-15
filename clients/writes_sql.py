import sqlite3
import datetime
import time

DATABASE = "sql/hashtag.db"


def main():
    conn = sqlite3.connect(DATABASE)

    c = conn.cursor()

    # print initial row count
    c.execute("SELECT COUNT(*) FROM hashtags")
    print(c.fetchall())

    def add_tag(tag):
        c.execute(
            "INSERT INTO hashtags VALUES (:user,:category,:tag)",
            {"user": "xristian", "category": "leica", "tag": tag},
        )
        conn.commit()

    def save_rate(method, write_rate):
        """Save rates to rate table."""
        conn = sqlite3.connect("hashtag.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO rates VALUES (:method,:rate)",
            {"method": method, "rate": write_rate},
        )
        conn.commit()
        conn.close()

    def calculate_write_rate(rows):
        """Returns write rate to write integer number of rows."""
        start = time.time()
        for i in range(rows):
            time_now = datetime.datetime.now().isoformat()
            add_tag(time_now)
        end = time.time()
        delta = end - start
        print(f"toatl time: {delta}")
        write_rate = int(rows / delta)
        print(f"Rows/second: {write_rate}")
        return write_rate

    def multiple_runs(method, rows, runs):
        """"Run writes multiple times and save results to rates table."""
        for i in range(runs):
            write_rate = calculate_write_rate(rows)
            save_rate(method=method, write_rate=write_rate)

    multiple_runs(method="sql", rows=100, runs=100)

    # print final row count
    c.execute("SELECT COUNT(*) FROM hashtags")
    print(c.fetchall())

    conn.close()


if "__main__" == __name__:
    main()
