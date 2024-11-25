import base64
import secrets
from io import BytesIO
from PIL import Image
import sqlite3
from werkzeug.security import check_password_hash


def generate_token():
    token_bytes = secrets.token_bytes(32)
    return base64.b64encode(token_bytes).decode('utf-8')
    
def verify_token(token):
    conn = sqlite3.connect('user.db')
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