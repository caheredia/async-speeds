import sqlite3


DATABASE = "sql/hashtag.db"


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
