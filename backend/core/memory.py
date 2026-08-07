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


    # ---------------------------------
    # Permanent Memory Table
    # ---------------------------------

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


    # ---------------------------------
    # Conversation History Table
    # ---------------------------------

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



# ---------------------------------
# Save Permanent Memory
# ---------------------------------

def save_memory(
    user_id,
    key,
    value
):

    # Only allow real permanent facts

    allowed_keys = [

        "name",

        "city",

        "location",

        "profession",

        "education",

        "skill",

        "preference"

    ]


    # Ignore unnecessary extracted data

    if key not in allowed_keys:

        return



    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()



    # Remove previous value

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



    # Insert new value

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



# ---------------------------------
# Get Permanent Memory
# ---------------------------------

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
        (
            user_id,
        )
    )


    rows = cursor.fetchall()


    conn.close()


    memory = {}


    for key,value in rows:

        if key not in memory:

            memory[key] = value



    return memory



# ---------------------------------
# Clear Permanent Memory
# ---------------------------------

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
        (
            user_id,
        )
    )


    conn.commit()

    conn.close()



# ---------------------------------
# Save Conversation
# ---------------------------------

def save_conversation(
    user_id,
    role,
    content,
    chat_id="default_chat"
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO conversations
        (
            chat_id,
            user_id,
            role,
            content,
            created_at
        )

        VALUES (?,?,?,?,?)

        """,
        (
            chat_id,
            user_id,
            role,
            content,
            datetime.now().isoformat()
        )
    )


    conn.commit()

    conn.close()



# ---------------------------------
# Get Conversation
# ---------------------------------

def get_conversation(user_id):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT role,content

        FROM conversations

        WHERE user_id=?

        ORDER BY id ASC

        """,
        (
            user_id,
        )
    )


    rows = cursor.fetchall()


    conn.close()


    messages = []


    for role,content in rows:

        messages.append(
            {
                "role": role,
                "content": content
            }
        )


    return messages