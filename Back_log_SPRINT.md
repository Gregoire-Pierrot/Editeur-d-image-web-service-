# Backlog Sprint 1

---

**Objectif principal :**  
Commencer le projet, se mettre d'accord sur le fonctionnement du web service.

## Git
- [x] **Grégoire** : Faire un répertoire git / 1
- [x] **Grégoire** : Gestion du dépôt git / 1

## Client (Python)

### Fonctionnalités
- [x] **Hamza** : Se connecter au serveur / 2
  - [ ] **Test** : Vérifier la connexion au serveur / 1
- [x] Prendre l'instruction de modification d'image / 1
- [x] **Elias** Prendre l'image à modifier (image locale) + vérifier le format du fichier / 12
  - [ ] **Test** : Vérifier les formats d'image acceptés / 1
- [x] **Ahibou** : Faire une requête au serveur avec l'image, l'instruction et le token (JWT) / 2
- [ ] **Ibrahim** : Faire une interface utilisateur / 12
- [ ] Afficher l'image retournée du serveur / 4
- [ ] Permettre l'enregistrement de l'image modifiée / 2

## Serveur (Java)

### Fonctionnalités
- [x] **Grégoire** : Créer un serveur / 1
- [x] **Ahibou & Grégoire** : Accepter les nouvelles connexions et générer un token par client / 3
- [x] **Ahibou** : Recevoir une requête de la forme : `[token] [image] [instruction]` / 1
- [x] **Ahibou** : Vérifier la validité du token / 1
- [x] **Ahibou & Grégoire** : Différencier l'instruction / 1
- [ ] **Tiago** : Modifier l'image / 12
  - [ ] Rotation à gauche / 3
  - [ ] Rotation à droite / 3
  - [ ] Inversion horizontale / 3
  - [ ] Inversion verticale / 3
  - [ ] Noir & blanc / 3
- [ ] Renvoyer au client l'image modifiée / 12

## Sécurité
- [ ] Cryptage des requêtes / 12
  - [ ] Vérifier le cryptage des requêtes / 1

### Total des points
- **Points terminés** : 1 point
- **Points non terminés** : 34 points
- **Total des points pour Sprint 1** : **35 points**

---

# Backlog Sprint 2

---

**Objectif principal :**  
Commencer la connexion au serveur et commencer l'interface client.

## Schéma interaction Client-Serveur
- [x] **Grégoire** : Faire un schéma du fonctionnement du Web-Service

## Client (Python)

### Fonctionnalités
- [x] **Hamza** : Se connecter au serveur / 2
  - [ ] **Test** : Vérifier la connexion au serveur / 1
- [x] Prendre l'instruction de modification d'image / 1
- [x] **Elias** Prendre l'image à modifier (image locale) + vérifier le format du fichier / 12
  - [ ] **Test** : Vérifier les formats d'image acceptés / 1
- [x] **Ahibou** : Faire une requête au serveur avec l'image, l'instruction et le token (JWT) / 2
- [ ] **Ibrahim** : Faire une interface utilisateur / 12
- [ ] Afficher l'image retournée du serveur / 4
- [x] **Elias** Permettre l'enregistrement de l'image modifiée / 2

## Serveur (Java)

### Fonctionnalités
- [x] **Grégoire** : Créer un serveur / 1
- [ ] Accepter les nouvelles connexions et générer un token par client / 3
- [ ] Recevoir une requête de la forme : `[token] [image] [instruction]` / 1
- [ ] Vérifier la validité du token / 1
- [ ] Différencier l'instruction / 1
  - [x] **Tiago** : Modifier l'image / 12
    - [x] Rotation à gauche / 3
    - [x] Rotation à droite / 3
    - [x] Inversion horizontale / 3
    - [x] Inversion verticale / 3
    - [x] Noir & blanc / 3
- [ ] Renvoyer au client l'image modifiée / 12

## Sécurité
- [ ] Cryptage des requêtes / 12
  - [ ] Vérifier le cryptage des requêtes / 1

### Total des points
- **Points terminés** : 1 point
- **Points non terminés** : 34 points
- **Total des points pour Sprint 2** : **35 points**

---

# Backlog Sprint 3

---

**Objectif principal :**  
Reprendre le web service pour avoir des requêtes HTTP.

## Git
- [x] **Grégoire** : Modification du git pour chaque développeur

## Client (Python)
Modification client, passage d'une connexion TCP-IP en requêtes HTTP.
- [x] **Elias** Afficher l'image retournée du serveur / 4
### Fonctionnalités
- [x] **Hamza** : Modifier le client déjà existant pour faire des requêtes HTTP
- [ ] **Hamza** : Ajouter dans le client une zone de texte pour envoyer le token
- [x] **Hamza** : Tester la modification d'image avec le nouveau serveur
- [ ] **Hamza** : Enregistrer l'image modifiée

## Serveur (Python)
Modification du web service, passage en Python avec la librairie Flask.

### Fonctionnalités
- [x] **Grégoire** : Créer un serveur Flask / 2
- [x] **Grégoire** : Créer une route acceptant et renvoyant des données sous format JSON / 3
- [ ] Vérifier la validité du token / 1
- [x] **Grégoire** : Vérifier la validité de l'image / 1
- [x] **Grégoire** : Différencier l'instruction / 1
- [x] **Tiago** : Modifier l'image / 6
  - [x] Rotation à gauche / 1
  - [x] Rotation à droite / 1
  - [x] Inversion horizontale / 1
  - [x] Inversion verticale / 1
  - [x] Noir & blanc / 1
  - [x] Nuance de gris / 1
- [x] **Grégoire** : Renvoyer au client l'image modifiée / 12
- [x] Génération du token / 2

## Sécurité
- [ ] Cryptage des requêtes / 12
  - [ ] Vérifier le cryptage des requêtes / 1

### Total des points
- **Points terminés** : 0 points
- **Points non terminés** : 28 points
- **Total des points pour Sprint 3** : **28 points**

---

# Backlog Sprint 4

---

**Objectif principal :**  
Amélioration et ajout de nouvelles fonctionnalités.

## Git
- [x] **Grégoire** : Modification du git pour chaque développeur
- [x] **Grégoire** : Nettoyage dépôt git (merge des branches & suppression des branches inutiles)

## Client (Python)

### Fonctionnalités
- [x] **Hamza** : Modifier le client déjà existant pour faire des requêtes HTTP
- [ ] **Hamza** : Ajouter dans le client une zone de texte pour envoyer le token
- [x] **Hamza** : Tester la modification d'image avec le nouveau serveur
- [ ] **Hamza** : Enregistrer l'image modifiée

## Serveur (Python)

### Fonctionnalités
- [x] **Grégoire** : Créer un serveur Flask / 2
- [x] **Grégoire** : Créer une route acceptant et renvoyant des données sous format JSON / 3
- [ ] **Mouhamed** : Vérifier la validité du token / 1
- [x] **Grégoire** : Vérifier la validité de l'image / 1
- [x] **Grégoire** : Différencier l'instruction / 1
- [x] **Tiago** : Modifier l'image / 6
  - [x] Rotation à gauche / 1
  - [x] Rotation à droite / 1
  - [x] Inversion horizontale / 1
  - [x] Inversion verticale / 1
  - [x] Noir & blanc / 1
  - [x] Nuance de gris / 1
- [x] **Grégoire** : Renvoyer au client l'image modifiée / 12
- [x] **Mouhamed** : Génération du token / 2

## Sécurité
- [ ] Cryptage des requêtes / 12
  - [ ] Vérifier le cryptage des requêtes / 1

### Total des points
- **Points terminés**
