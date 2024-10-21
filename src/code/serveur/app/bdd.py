import sqlite3
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# Créer une application Flask
app = Flask(__name__)

# Fonction pour créer la base de données SQLite et une table avec login, mot de passe et token
def init_db():
    conn = sqlite3.connect('user.db')  # Connexion à la base SQLite (ou création si elle n'existe pas)
    cursor = conn.cursor()
    
    # Créer une table si elle n'existe pas déjà
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        token TEXT DEFAULT ''
    )
    ''')
    
    conn.commit()  # Sauvegarder les changements
    conn.close()  # Fermer la connexion

# Route pour ajouter un utilisateur avec login, mot de passe et token vide
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    login = data['login']
    password = data['password']

    # Hachage du mot de passe pour le stocker de manière sécurisée
    hashed_password = generate_password_hash(password)

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    # Insérer un nouvel utilisateur dans la table avec login, mot de passe haché et token vide
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

# Route pour vérifier si un token existe dans la base de données
@app.route('/check_token', methods=['POST'])
def check_token():
    data = request.get_json()
    token = data['token']
    
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    # Rechercher si le token existe dans la base de données
    cursor.execute('SELECT * FROM users WHERE token = ?', (token,))
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        return jsonify({'message': 'Token is valid', 'user': user[1]}), 200  # user[1] contient le login
    else:
        return jsonify({'error': 'Token is invalid'}), 404

if __name__ == '__main__':
    init_db()  # Initialiser la base de données
    app.run(debug=True)  # Lancer le serveur
