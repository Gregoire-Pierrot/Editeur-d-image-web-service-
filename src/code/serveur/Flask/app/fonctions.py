import base64
from io import BytesIO
from PIL import Image

def verify_token(str):
    return True

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