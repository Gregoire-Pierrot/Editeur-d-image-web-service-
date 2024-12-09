# Editeur d'image en web service
Web service de transformation d'images


## Description du projet et de l'utilisation client

Se projet permet à un client de modifier l'image de son choix avec un web service.
Pour cela il devra se créer un compte, enregistrer le token qui lui sera donné puis utilisé l'application client.
Une fois dedans, le client devra renseigner différents champs : son token, l'image à modifier et la liste des modifications à apporté.
Il aura ensuite la possiblité d'enregistrer cette nouvelle image.


## Pour utiliser le client
- Créez vous un compte sur le site
- Générez et récuperez un token
- Placez vous dans le répertoir src/code/client
- Créez un environnement python avec la commande :
   - ```bash
     python3 -m venv Client
     ```
- Activez l'environnement et installez les librairies :
   - ```bash
     source Client/bin/activate
     pip install requests PyQt5
     ```
- Installez les dépendences nécessaires :
   - ```bash
     sudo apt update
     sudo apt install --reinstall libxcb-xinerama0 libxcb-xinerama0-dev
     sudo apt install libxcb1 libx11-xcb1 libxrender1 libxext6
     sudo apt install python3-pyqt5 python3-pyqt5.qtsvg
     ```
- Lancez l'application : 
   - ```bash
     python3 client.py
     ```


## Pour pouvoir héberger un serveur veuillez suivre les instructions suivantes :
- Créer un dossier "images" dans src/code/serveur/app
- Télécharger Python 3.10.* ou plus
- Ouvrir un terminal à l'emplacement src/code/serveur
- Créer un environnement Python nommé "Flask" avec l'une des commandes suivantes : 

   ```python
   python -m venv Flask
   ```

   ```python
   python3 -m venv Flask
   ```

- Ouvrir ce nouvel environnement :
   Sous Windows :
   
   ```bash
   cd Flask
   ```

   ```bash
   ./Scripts/Activate.ps1
   ```

   Sous Linux :

   ```bash
   cd Flask
   ```

   ```bash
   source bin/activate
   ```

- Télécharger les différentes librairies : [flask, flask_wtf, pillow, email_validator] avec la commande :
    
   ```python
   pip install flask flask_wtf pillow email_validator
   ```

- Ce déplacer dans le dossier app et lancer le serveur : 
   
   ```bash
   cd ../app
   ```

   Lancer le serveur avec l'une des commandes suivantes :

   ```python
   python main.py
   ```

   ```python
   python3 main.py
   ```

---
---

# BackLog

---

La suite de ce fichier donne les liens vers les fichiers Markdown contenant les sprints de chaque scéance. Chacun de ces fichiers contien le but du sprint, toutes les tâches rajouté pour le prochain sprint ainsi que toutes les tâches qui n'ont pas encore été réalisé.
Devant chacunes des tâches, le nom de la personne affecté pour sa réalisation est noté ainsi que son état d'avancement.
Le chiffre qui suit chaque tâche annonce le temps estimé pour la dite tâche. Nous avons choisis l'unité : **1** --> **10mn** de recherche & développement.

**Exemple :**
- [X] **[Prénom]** Tâche fini. | 1
- [ ] **[Prénom]** Tâche non fini. | 5


Nous avons décider de choisir un but de scéance en debut de sprint, puis que chacun se positionne sur une tâche quand il à fini la prédédente tâche à laquelle il était affilié.
De cette manière nous avons pu assurer que chacun travail sur une tâche distincte tout en pouvant demander de l'aide à un autre membre du groupe et que chacun puisse faire les tâches qui lui plaise le plus. (Nous avions tout de même défini pour chacun un domaine d'action : développement serveur ou client).

## Liste des Sprint

---

## [Sprint 1](Sprints/Sprint1.md)

---

## [Sprint 2](Sprints/Sprint2.md)

---

## [Sprint 3](Sprints/Sprint3.md)

---

## [Sprint 4](Sprints/Sprint4.md)

---

## [Sprint 5](Sprints/Sprint5.md)

---

## [Sprint 6](Sprints/Sprint6.md)

---

