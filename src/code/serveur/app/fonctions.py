import base64
from io import BytesIO
from PIL import Image
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

import secrets
import base64


def generate_token():
    token_bytes = secrets.token_bytes(32)
    return base64.b64encode(token_bytes).decode('utf-8')

def verify_token(token):
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT token FROM users")
    result = cursor.fetchall()
    
    conn.close()
    
    tokens = [row[0] for row in result]

    for hashed_token in tokens:
        if check_password_hash(hashed_token, token) :
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

    username = cursor.execute("SELECT username FROM users WHERE email = ?", (email,)).fetchone()

    conn.close()

    return username

def getEmailByUsername(username):
    conn = sqlite3.connect('datab.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    email = cursor.execute("SELECT email FROM users WHERE username = ?", (username,)).fetchone()

    conn.close()

    return email

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

    user = cursor.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

    conn.close()

    if user is None:
        return False
    
    return check_password_hash(user['password'], password)

def Register(email, username, password):
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    
    # At this point, the email and the username were alwready verified.

    hashed_password = generate_password_hash(password)
    token = generate_token()
    hashed_token = generate_password_hash(token)
    cursor.execute('''
    INSERT INTO users (email, username, password, token)
    VALUES (?, ?, ?, ?)
    ''', (email, username, hashed_password, hashed_token))
    conn.commit()
    conn.close()
    
    print("---------------------------")
    print("New user added !")
    print("Username : ", username)
    print("---------------------------")
    
    return True