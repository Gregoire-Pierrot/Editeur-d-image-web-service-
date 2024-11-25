import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from fonctions import generate_token

def init_db():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        token TEXT DEFAULT ''
    )
    ''')
    
    conn.commit()
    conn.close()
    
def is_username_taken(username):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT username FROM users")
    result = cursor.fetchall()
    
    conn.close()
    
    usernames = [row[0] for row in result]

    for user in usernames:
        if user == username :
            return True
    return False


def ajout_user(username, password):
    if is_username_taken(username):
        print("Username already taken")
        return {"status": "error", "message": "Username already taken."}, 400
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    token = generate_token()
    hashed_token = generate_password_hash(token)
    cursor.execute('''
    INSERT INTO users (username, password, token)
    VALUES (?, ?, ?)
    ''', (username, hashed_password, hashed_token))
    conn.commit()
    conn.close()
    
    print("---------------------------")
    print("New user added !")
    print("Username : ", username)
    print("---------------------------")
    
    print("Token : " + token)
    return "You have been added\nYour token : " + token