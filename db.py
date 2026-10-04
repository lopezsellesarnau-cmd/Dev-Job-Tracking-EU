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
