import sqlite3

# Create a connection to the database
conn = sqlite3.connect('users.db')
curseur = conn.cursor()
curseur.execute("CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, password TEXT)")
# Ajouter un utilisateur par défaut (root, rouviere)

curseur.execute("SELECT * FROM users WHERE id='root'")
user = curseur.fetchone()
if user is None:
    curseur.execute("INSERT INTO users (id, password) VALUES ('root','rouviere')")
    conn.commit()
conn.close()


def check_login(id, password):
    conn = sqlite3.connect('users.db')
    curseur = conn.cursor()
    curseur.execute("SELECT * FROM users WHERE id=? AND password=?", (id, password))
    user = curseur.fetchone()
    conn.close()
    return user is not None