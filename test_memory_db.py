import sqlite3

conn = sqlite3.connect(
    "backend/database/memory.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM memories"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()