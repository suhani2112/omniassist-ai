import sqlite3
from datetime import datetime


class ConversationMemory:

    def __init__(
        self,
        db_path="backend/database/memory.db",
        max_messages=10
    ):

        self.db_path = db_path
        self.max_messages = max_messages
        print("DATABASE PATH:", self.db_path)
        self.create_table()


    def create_table(self):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

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

        conn.commit()
        conn.close()



    def add_message(
        self,
        user_id,
        role,
        content
    ):
        print(
        "SAVING MEMORY:",
        user_id,
        role,
        content
    )


        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO memories
            (
                user_id,
                key,
                value,
                created_at
            )

            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                role,
                content,
                datetime.now().isoformat()
            )
        )


        conn.commit()
        conn.close()



    def get_messages(
        self,
        user_id
    ):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT key, value

            FROM memories

            WHERE user_id = ?

            ORDER BY id DESC

            LIMIT ?

            """,
            (
                user_id,
                self.max_messages
            )
        )


        rows = cursor.fetchall()

        conn.close()


        messages = []


        for role, content in reversed(rows):

            messages.append(
                {
                    "role": role,
                    "content": content
                }
            )


        return messages



    def clear(
        self,
        user_id
    ):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()


        cursor.execute(
            """
            DELETE FROM memories

            WHERE user_id = ?

            """,
            (
                user_id,
            )
        )


        conn.commit()
        conn.close()