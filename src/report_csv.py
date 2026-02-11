import sqlite3
import csv
import os

DB_PATH = os.path.join("database", "attendance.db")
CSV_PATH = os.path.join("database", "attendance_report.csv")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM attendance").fetchall()

with open(CSV_PATH, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Roll No", "Date", "Time", "Status"])
    writer.writerows(rows)

conn.close()

print("CSV report generated:", CSV_PATH)
