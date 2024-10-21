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

# Route pour récupérer tous les utilisateurs (login et token uniquement, pas de mot de passe)
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT login, token FROM users')  # Ne pas retourner le mot de passe
    users = cursor.fetchall()
    
    conn.close()
    
    # Retourner la liste des utilisateurs sous forme JSON
    return jsonify(users)

# Route pour authentifier un utilisateur et générer un token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    login = data['login']
    password = data['password']
    
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    # Rechercher l'utilisateur par son login
    cursor.execute('SELECT id, password FROM users WHERE login = ?', (login,))
    user = cursor.fetchone()

    if user and check_password_hash(user[1], password):
        # Générer un token (pour l'exemple, on utilise juste un simple identifiant)
        token = f'token_{user[0]}'
        cursor.execute('UPDATE users SET token = ? WHERE id = ?', (token, user[0]))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Login successful', 'token': token})
    else:
        conn.close()
        return jsonify({'error': 'Invalid login or password'}), 401

if __name__ == '__main__':
    init_db()  # Initialiser la base de données
    app.run(debug=True)  # Lancer le serveur