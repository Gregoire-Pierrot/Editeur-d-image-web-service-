# Backlog Sprint 1

---

## Objectif principal : 
Commencer le projet, se mettre d'accord sur le fonctionnement du web service.

Choisir la technologie (langage) pour :
- [X] **[Le groupe]** Le **serveur** : java avec TCP-IP
- [X] **[Le groupe]** Le **client** : python

---

### Git
- [x] **Grégoire** Faire un répertoire git | **1 point**
- [x] **Grégoire** Gestion du dépot git | **1 point**

---

### Client (Python)

#### Fonctionnalités
- [X] **Hamza** : Se connecter au serveur TCP-IP | **2 points**
  - [ ] **Test** : Vérifier la connexion au serveur | **1 point**

- [X] **Hamza** : Prendre l'instruction de modification d'image | **1 point**

- [X] **Elias** Prendre l'image à modifier (image locale) + vérifier le format du fichier | **12 points**
  - [ ] **Test** : Vérifier les formats d'image acceptés | **1 point**

- [X] **Ahibou :** Voir comment faire (+ tester) une requête au serveur avec l'image, l'instruction et le token (JWT - JSON Web Token) | **2 points**

- [ ] **Ibrahim :** Faire une interface utilisateur | **12 points**

- [ ] Afficher l'image retournée du serveur | **4 points**

- [X] **Elias** Permettre l'enregistrement de l'image modifiée | **2 points**

---

### Serveur (Java)

#### Fonctionnalités
- [x] **Grégoire** : Créer un serveur TCP-IP | **1 point**

- [X] **Ahibou & Grégoire** : Accepter les nouvelles connexions et générer un token par client | **3 points**

- [X] **Ahibou** : Recevoir une requête de la forme : [token] [image] [instruction] | **1 point**

- [X] **Ahibou** : Vérifier la validité du token | **1 point**

- [X] **Ahibou & Grégoire** : Différencier l'instruction | **1 point**

- [ ] **Tiago** Modifier l'image | **15 points**
  - [ ] Rotation à gauche | **3 points**
  - [ ] Rotation à droite | **3 points**
  - [ ] Inversion horizontale | **3 points**
  - [ ] Inversion verticale | **3 points**
  - [ ] Noir & blanc | **3 points**

- [ ] Renvoyer au client l'image modifiée | **12 points**

---

### Sécurité
- [ ] Cryptage des requêtes | **12 points**
  - [ ] Vérifier le cryptage des requêtes | **1 point**

---

#### Total des points
- **Points terminés** : 14 / 86 points
- **Points non terminés** : 72 / 86 points

---
