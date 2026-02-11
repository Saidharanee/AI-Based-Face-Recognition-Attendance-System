import sqlite3
import os
from datetime import datetime

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ensure database folder exists
DB_DIR = os.path.join(BASE_DIR, "database")
os.makedirs(DB_DIR, exist_ok=True)

DB_PATH = os.path.join(DB_DIR, "attendance.db")

# Prevent duplicate attendance in same day
marked_today = set()


def mark_attendance(roll_no):
    today = datetime.now().strftime("%Y-%m-%d")

    if (roll_no, today) in marked_today:
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    #  Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT,
            date TEXT,
            time TEXT,
            status TEXT
        )
    """)

    now = datetime.now()

    cursor.execute("""
        INSERT INTO attendance (roll_no, date, time, status)
        VALUES (?, ?, ?, ?)
    """, (roll_no, today, now.strftime("%H:%M:%S"), "Present"))

    conn.commit()
    conn.close()

    marked_today.add((roll_no, today))
    print(f"Attendance marked for {roll_no}")
