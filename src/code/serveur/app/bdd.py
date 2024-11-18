import sqlite3
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from fonctions import generate_token

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

def ajout_user(login, password):
    # conn = sqlite3.connect('user.db')
    # cursor = conn.cursor()
    # hashed_login = generate_password_hash(login)
    # hashed_password = generate_password_hash(password)
    # token = generate_token()
    # hashed_token = generate_password_hash(token)
    # cursor.execute('''
    # INSERT INTO users (login, password, token) 
    # VALUES (?, ?, ?)
    # ''', ( hashed_login, hashed_password, hashed_token))
    # conn.commit()
    # conn.close()

    # return jsonify({'message': 'User added successfully'}), 201

