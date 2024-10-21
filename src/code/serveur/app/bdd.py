import sqlite3
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        token TEXT DEFAULT ''
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    login = data['login']
    password = data['password']
    hashed_password = generate_password_hash(password)

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO users (login, password, token) 
        VALUES (?, ?, '')
        ''', (login, hashed_password))
        
        conn.commit()
        return jsonify({'message': 'User added successfully'}), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Login already exists'}), 400

    finally:
        conn.close()

@app.route('/check_token', methods=['POST'])
def check_token():
    data = request.get_json()
    token = data['token']
    
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE token = ?', (token,))
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        return jsonify({'message': 'Token is valid', 'user': user[1]}), 200
    else:
        return jsonify({'error': 'Token is invalid'}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
