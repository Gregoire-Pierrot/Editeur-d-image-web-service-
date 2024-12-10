import base64
import os
from register import RegisterForm
from login import LoginForm
from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from fonctions import *
from bdd import init_db
from app import app

mods = ["rotate_left", "rotate_right", "inverse", "b&w", "grayscale"]

init_db()

@app.route("/", methods=['GET'])
def homepage():
    if 'username' in session :
        return render_template('home.html', username=session['username'])
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email_t = getBolByEmail(request.form['email'])
        username_t = getBolByUsername(request.form['username'])
        if email_t or username_t :
            return render_template('register.html', form=form, username_t=username_t, email_t=email_t)
        if Register(request.form['email'], request.form['username'], request.form['password']):
            return render_template('login.html', form=form)
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if CheckIfLoginRight(request.form['email'], request.form['password']):
            username = getUsernameByEmail(request.form['email'])
            session['username'] = username
            print("---------------------------")
            print("Nouvel utilisateur connecté !")
            print("Username : ", username)
            print("---------------------------")
            return redirect(url_for('account'))
        elif CheckEmail(request.form['email']):
            return render_template('login.html', form=form, wrong_password=True)
        return render_template('login.html', form=form, email_e=True)
    return render_template("login.html", form=form)

@app.route("/account", methods=['GET', 'POST'])
def account():
    if 'username' in session:
        print(session['username'])
        username = session['username']
        email = getEmailByUsername(username)
        # Si l'utilisateur à trafiqué son navigateur :
        if email is None :
            return redirect(url_for('login.html'))
        return render_template('account.html', email=email, username=username)
    form = LoginForm()
    return redirect(url_for('login'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    username = session['username']
    print("---------------------------")
    print("Un utilisateur s'en va ... ")
    print("Username : ", username)
    print("---------------------------")
    session.clear()
    return redirect('/')

@app.route("/get-token", methods=['GET', 'POST'])
def token():
    token = generate_token(session['username'])
    return jsonify({'token': token})

@app.route("/service", methods=['GET', 'POST'])
def service():
    return render_template('service.html', username=session['username'])



@app.route("/statistics", methods=['GET'])
def statistics():
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    if 'username' in session :
        cursor.execute("SELECT username, minute_usage FROM users WHERE username=?", (session['username'],))
        data = cursor.fetchall()
    conn.close()
    
    usage_data = {row[0]: row[1] for row in data}
    return render_template("statistics.html", usage_data=json.dumps(usage_data))
    


@app.route("/modification", methods=['GET', 'POST'])
def modification():
    data = request.get_json()
    limit = 100
    
    if 'token' in data:
        token = data['token']
        if verify_token(token):
            increment_usage(token)
            print("Token valide.")
            ajout_date(token)
            print("ajout fait")
            count = limit_user(token)
            if count <= limit:

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
                return {"status": "error", "message": "limite de requêtes dépassée."}, 400
        else:
            return {"status": "error", "message": "Token invalide."}, 400
    else:
        return {"status": "error", "message": "Aucun token donné."}, 400