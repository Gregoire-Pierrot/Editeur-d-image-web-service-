import sqlite3
from fonctions import generate_token

def init_db():
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        token TEXT DEFAULT ''
    )
    ''')
    
    conn.commit()
    conn.close()