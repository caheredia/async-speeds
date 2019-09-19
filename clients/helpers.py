import sqlite3


DATABASE = "sql/write-speeds.db"


def save_rate(method, write_rate):
    """Save rates to rate table."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO rates VALUES (:method,:rate)",
        {"method": method, "rate": write_rate},
    )
    conn.commit()
    conn.close()


def get_row_count(table):
    """Print row count in table."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(f"SELECT COUNT(*) FROM {table}")
    print(c.fetchall())


def find_rate(delta, rows):
    print(f"toatl time: {delta}")
    write_rate = int(rows / delta)
    print(f"Rows/second: {write_rate}")
    return write_rate
