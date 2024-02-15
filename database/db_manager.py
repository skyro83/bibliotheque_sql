import sqlite3

def connect_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, password TEXT)")
    cursor.execute("SELECT * FROM users WHERE id='root'")
    user = cursor.fetchone()
    if user is None:
        cursor.execute("INSERT INTO users (id, password) VALUES ('root','rouviere')")
        conn.commit()
    return conn