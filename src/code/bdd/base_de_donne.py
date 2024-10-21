import sqlite3
from flask import Flask, request, jsonify

# Créer une application Flask
app = Flask(__name__)

# Fonction pour créer la base de données SQLite et une table simple
def init_db():
    conn = sqlite3.connect('example.db')  # Connexion à la base SQLite (ou création si elle n'existe pas)
    cursor = conn.cursor()
    
    # Créer une table si elle n'existe pas déjà
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')
    
    conn.commit()  # Sauvegarder les changements
    conn.close()  # Fermer la connexion

# Route pour ajouter un utilisateur
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    age = data['age']
    
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Insérer un nouvel utilisateur dans la table
    cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
    ''', (name, age))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'User added successfully'}), 201

# Route pour récupérer tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    
    conn.close()
    
    # Retourner la liste des utilisateurs sous forme JSON
    return jsonify(users)

if __name__ == '__main__':
    init_db()  # Initialiser la base de données
    app.run(debug=True)  # Lancer le serveur
