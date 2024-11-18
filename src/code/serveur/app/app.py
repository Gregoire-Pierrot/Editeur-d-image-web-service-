from flask import Flask
from config import Configuration # importation de la classe de configuration
from fonctions import generate_token

app = Flask(__name__)
# __name__ indique la racine de l'application pour retrouver les ressources

app.config.from_object(Configuration)

# Route pour ajouter un utilisateur
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    login = data['login']
    password = data['password']
    hashed_password = generate_password_hash(password)
    token = generate_token()

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO users (login, password, token) 
        VALUES (?, ?, ?)
        ''', (login, hashed_password, token))
        
        conn.commit()
        return jsonify({'message': 'User added successfully'}), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Login already exists'}), 400

    finally:
        conn.close()