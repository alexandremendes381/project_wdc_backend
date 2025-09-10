import sqlite3
from datetime import datetime

DB_PATH = "emails.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    sent_at TEXT NOT NULL
)
''')
conn.commit()
conn.close()

def save_email(email: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now = datetime.now().isoformat(sep=' ', timespec='seconds')
    cursor.execute("INSERT INTO emails (email, sent_at) VALUES (?, ?)", (email, now))
    conn.commit()
    conn.close()

def get_all_emails():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, sent_at FROM emails ORDER BY sent_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return [
        {"id": row[0], "email": row[1], "sent_at": row[2]} for row in rows
    ]
