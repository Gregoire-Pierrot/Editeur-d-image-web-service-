import base64
import json
from datetime import datetime, timedelta
from io import BytesIO
from PIL import Image
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

import secrets
import base64
from datetime import datetime, timedelta

def generate_token(username):
    token = base64.b64encode(secrets.token_bytes(32)).decode('utf-8')
    
    while verify_token(token):
        token = base64.b64encode(secrets.token_bytes(32)).decode('utf-8')
        
    hashed_token = generate_password_hash(token)
        
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE users SET token = ? WHERE username = ?
    ''', (hashed_token, username))
    conn.commit()
    conn.close()
    
    print("new token : ", token)
    return token

def verify_token(token):
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT token FROM users")
    result = cursor.fetchall()
    
    conn.close()
    
    tokens = [row[0] for row in result]

    for hashed_token in tokens:
        if hashed_token is not None and check_password_hash(hashed_token, token) :
            return True
    return False

def rotate(angle):
    with Image.open("images/image_recue.png") as img:
        rotated_img = img.rotate(angle)
        buffer = BytesIO()
        rotated_img.save(buffer, format="PNG")
        image_data = base64.b64encode(buffer.getvalue())
        image_data = base64.b64decode(image_data)
    
        image_path = 'images/image_recue.png'
        with open(image_path, 'wb') as image_file:
            image_file.write(image_data)
        
        return 1
    
def inverse():
    return rotate(180)

def bw():
    with Image.open("images/image_recue.png") as img:
        rotated_img = img.convert('1')
        buffer = BytesIO()
        rotated_img.save(buffer, format="PNG")
        image_data = base64.b64encode(buffer.getvalue())
        image_data = base64.b64decode(image_data)
    
        image_path = 'images/image_recue.png'
        with open(image_path, 'wb') as image_file:
            image_file.write(image_data)
        
        return 1

def grayscale():
    with Image.open("images/image_recue.png") as img:
        rotated_img = img.convert('L')
        buffer = BytesIO()
        rotated_img.save(buffer, format="PNG")
        image_data = base64.b64encode(buffer.getvalue())
        image_data = base64.b64decode(image_data)
    
        image_path = 'images/image_recue.png'
        with open(image_path, 'wb') as image_file:
            image_file.write(image_data)
        
        return 1

def getBolByEmail(email):
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT username FROM users")
    result = cursor.fetchall()
    
    conn.close()

    emails = [row[0] for row in result]

    for user in emails:
        if user == email :
            print("Email already taken")
            return True
    return False

def getBolByUsername(username):
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT username FROM users")
    result = cursor.fetchall()
    
    conn.close()

    usernames = [row[0] for row in result]

    for user in usernames:
        if user == username :
            print("Username already taken")
            return True
    return False

def getUsernameByEmail(email):
    conn = sqlite3.connect('datab.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    row = cursor.execute("SELECT username FROM users WHERE email = ?", (email,)).fetchone()

    conn.close()

    if row :
        return row['username']
    return None

def getEmailByUsername(username):
    conn = sqlite3.connect('datab.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    row = cursor.execute("SELECT email FROM users WHERE username = ?", (username,)).fetchone()

    conn.close()

    if row :
        return row['email']
    return None

def CheckEmail(email):
    conn = sqlite3.connect('datab.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    e = cursor.execute("SELECT email FROM users WHERE email = ?", (email,)).fetchone()

    return (e is not None and e == email)

def CheckIfLoginRight(email, password):
    conn = sqlite3.connect('datab.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print("ici 1")
    user = cursor.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    print("ici 2")

    conn.close()

    if user is None:
        return False
    
    print("ici 3")
    return check_password_hash(user['password'], password)

def Register(email, username, password):
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    
    # At this point, the email and the username were alwready verified.

    hashed_password = generate_password_hash(password)
    cursor.execute('''
    INSERT INTO users (email, username, password, date_now, limit_count, minute_usage)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (email, username, hashed_password, json.dumps([]), 0, 0))
    conn.commit()
    conn.close()
    
    print("---------------------------")
    print("New user added !")
    print("Username : ", username)
    print("---------------------------")
    
    return True

def ajout_date(token):
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()

    cursor.execute("SELECT token FROM users")
    result = cursor.fetchall()

    tokens = [row[0] for row in result]

    for hashed_token in tokens:
        if hashed_token is not None and check_password_hash(hashed_token, token):

            cursor.execute('''SELECT date_now FROM users WHERE token = ?''', (hashed_token,))
            result = cursor.fetchone()
            current_dates = json.loads(result[0]) if result and result[0] else []

            new_date = datetime.now().isoformat()
            current_dates.append(new_date)

            updated_dates_json = json.dumps(current_dates)
            cursor.execute('UPDATE users SET date_now = ? WHERE token = ?', (updated_dates_json, hashed_token))
    conn.commit()
    conn.close()


def limit_user(token):
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()

    cursor.execute("SELECT token FROM users")
    result = cursor.fetchall()

    tokens = [row[0] for row in result]

    for hashed_token in tokens:
        if hashed_token is not None and check_password_hash(hashed_token, token):
            cursor.execute('SELECT date_now FROM users WHERE token = ?', (hashed_token,))
            result = cursor.fetchone()

            if not result or not result[0]:
                return 0  # Si aucune donnée n'est trouvée, retourner 0

            # Charger les dates en tant que liste Python
            date_list = json.loads(result[0])  # Charger la chaîne JSON en liste Python
            print("date_list ", date_list)

            # Calculer la limite de temps (il y a une minute)
            one_minute_ago = datetime.now() - timedelta(minutes=1)
            print("one minute ", one_minute_ago)

            # Filtrer les dates de la dernière minute
            recent_dates = [date for date in date_list if datetime.fromisoformat(date) >= one_minute_ago]

            count = len(recent_dates)
            print("count ", count)
            cursor.execute('''UPDATE users SET limit_count = ? WHERE token = ?''', (count, hashed_token))
    conn.commit()
    conn.close()
    return count



def increment_usage(token):
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()

    cursor.execute("SELECT token FROM users")
    result = cursor.fetchall()

    tokens = [row[0] for row in result]

    for hashed_token in tokens:
        if hashed_token is not None and check_password_hash(hashed_token, token):
            cursor.execute("SELECT minute_usage, date_now FROM users WHERE token=?", (hashed_token,))
            row = cursor.fetchone()
            

            if row:
                usage, last_update_json  = row
                print(" usage ", usage)
                if last_update_json:
                    last_update_list = json.loads(last_update_json)
                    # On prend le dernier élément de la liste
                    last_update = datetime.fromisoformat(last_update_list[-1]) if last_update_list else datetime.now()

                    now = datetime.now()

                    if (now - last_update) > timedelta(minutes=1):
                        usage = 1
                        cursor.execute("UPDATE users SET minute_usage=?, date_now=? WHERE token=?", (usage, json.dumps([now.isoformat()]), hashed_token))

                    else:
                        usage += 1
                        cursor.execute("UPDATE users SET minute_usage=? WHERE token=?", ( usage, hashed_token))
                

    conn.commit()
    conn.close()

