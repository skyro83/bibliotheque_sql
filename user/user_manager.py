from database.db_manager import connect_db

def check_login(id, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=? AND password=?", (id, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None