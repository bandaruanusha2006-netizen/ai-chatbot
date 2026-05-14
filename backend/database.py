import sqlite3

def connect_db():
    conn = sqlite3.connect("ai_project.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        ai_reply TEXT
    )
    """)

    conn.commit()
    conn.close()

print("Database Connected Successfully 🚀")