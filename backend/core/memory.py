import sqlite3
import os
from datetime import datetime

DB_PATH = "backend/database/memory.db"


def init_memory():

    # Create database folder if not exists
    os.makedirs(
        os.path.dirname(DB_PATH),
        exist_ok=True
    )

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    # -----------------------------
    # Permanent Memory Table
    # -----------------------------
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS memories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id TEXT NOT NULL,

            key TEXT NOT NULL,

            value TEXT NOT NULL,

            created_at TEXT NOT NULL

        )
        """
    )

    # -----------------------------
    # Conversation History Table
    # -----------------------------
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS conversations(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            chat_id TEXT NOT NULL,

            user_id TEXT NOT NULL,

            role TEXT NOT NULL,

            content TEXT NOT NULL,

            created_at TEXT NOT NULL

        )
        """
    )

    conn.commit()
    conn.close()


def save_memory(user_id, key, value):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    # Remove old value of same memory key
    cursor.execute(
        """
        DELETE FROM memories
        WHERE user_id=? AND key=?
        """,
        (
            user_id,
            key
        )
    )

    # Insert updated memory
    cursor.execute(
        """
        INSERT INTO memories
        (
            user_id,
            key,
            value,
            created_at
        )

        VALUES (?,?,?,?)
        """,
        (
            user_id,
            key,
            value,
            datetime.now().isoformat()
        )
    )

    conn.commit()
    conn.close()


def get_memory(user_id):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT key,value
        FROM memories
        WHERE user_id=?
        ORDER BY id DESC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    memory = {}

    for key, value in rows:

        # keep latest value only
        if key not in memory:
            memory[key] = value

    return memory


def clear_memory(user_id):

    """
    Delete all permanent memories of a user
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM memories
        WHERE user_id=?
        """,
        (user_id,)
    )

    conn.commit()
    conn.close()