import base64
import os
from flask import Flask, request
from fonctions import verify_token, rotate, inverse, bw, grayscale
from app import app

mods = ["rotate_left", "rotate_right", "inverse", "b&w", "grayscale"]

@app.route("/", methods=['GET'])
def homepage():
    return "Salut !"

@app.route("/modification", methods=['GET', 'POST'])
def modification():
    data = request.get_json()
    
    if 'token' in data:
        token = data['token']
        if verify_token(token):
            print("Token valide.")
            modifications = []
            if 'encoded_image' in data:
                encoded_image = data['encoded_image']
                encoded_string = "Rien ne s'est passé."
                try:
                    image_data = base64.b64decode(encoded_image)
                except base64.binascii.Error:
                    return {"status": "error", "message": "Image mal encodée"}, 400
        
                image_path = 'images/image_recue.png'
                with open(image_path, 'wb') as image_file:
                    image_file.write(image_data)
                
                print("Image recue.")


                if 'modifications' in data:
                    modifications = data['modifications']
                    for modification in modifications:
                        if modification == "rotate_left":
                            rotate(90)
                        elif modification == "rotate_right":
                            rotate(270)
                        elif modification == "inverse":
                            inverse()
                        elif modification == "b&w":
                            bw()
                        elif modification == "grayscale":
                            grayscale()
                        else:
                            return {"status": "error", "message": "Modification inconnue. Voici les modifications disponible : {mods}"}, 400
                        print(modification)
                    
                    with open(image_path, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())

                    try:
                        os.remove(image_path)
                        print(f"{image_path} a été supprimé.")
                    except FileNotFoundError:
                        print(f"Le fichier {image_path} n'existe pas.")
                    except PermissionError:
                        print(f"Permission refusée pour supprimer {image_path}.")
                    except Exception as e:
                        print(f"Une erreur s'est produite : {e}")

                    return encoded_string
                else:
                    return {"status": "error", "message": "Aucune modification donnée."}, 400
            else:
                return {"status": "error", "message": "Aucune image donnée."}, 400
        else:
            return {"status": "error", "message": "Token invalide."}, 400
    else:
        return {"status": "error", "message": "Aucun token donné."}, 400
