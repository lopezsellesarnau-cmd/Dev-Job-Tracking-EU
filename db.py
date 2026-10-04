import sqlite3

DB_FILE = "jobs.db"


def create_table():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS job_counts (
        id INTEGER PRIMARY KEY,
        date TEXT,
        country TEXT,
        role TEXT,
        count INTEGER
        )
    """)

    conn.commit()
    conn.close()


def save_count(date, country, role, count):
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "INSERT INTO job_counts (date, country, role, count) VALUES (?, ?, ?, ?)",
        (date, country, role, count)
    )
    conn.commit()
    conn.close()


def get_counts():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT date, country, role, count FROM job_counts"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]
