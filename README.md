# Editeur d'image en web service
Web service de transformation d'images


## Description du projet et de l'utilisation client

Se projet permet à un client de modifier l'image de son choix avec un web service.
Pour cela il devra se créer un compte, enregistrer le token qui lui sera donné puis utilisé l'application client.
Une fois dedans, le client devra renseigner différents champs : son token, l'image à modifier et la liste des modifications à apporté.
Il aura ensuite la possiblité d'enregistrer cette nouvelle image.




## Pour pouvoir héberger un serveur veuillez suivre les instructions suivantes :
 - Créer un dossier "images" dans src/code/serveur/app
 - Télécharger Python 3.10.* ou plus
 - Ouvrir un terminal à l'emplacement src/code/serveur
 - Créer un environnement Python nommé "Flask" avec l'une des commandes suivantes : 
    - python -m venv Flask
    - python3 -m venv Flask
 - Ouvrir ce nouvel environnement :
    Sous Windows :
        - cd Flask
        - ./Scripts/Activate.ps1
    Sous Linux :
        - cd Flask
        - source bin/activate
 - Télécharger les différentes librairies : [flask, pillow] avec la commande :
    - pip install [librairie] // pour chacunes des librairies cité ci-dessus
 - Ce déplacer dans le dossier app et lancer le serveur : 
    - cd ../app
    Lancer le serveur avec l'une des commandes suivantes :
        - python main.py
        - python3 main.py