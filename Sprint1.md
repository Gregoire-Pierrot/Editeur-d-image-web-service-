# Sprint 1

---

**Objectif principal :**  
Commencer le projet, se mettre d'accord sur le fonctionnement du web service.

Choisir la technologie (langage) pour :
- [X] Le **serveur** : java avec TCP-IP
- [X] Le **client** : python

#### Git
- [x] **Grégoire** Faire un répertoire git | 1
- [x] **Grégoire** Gestion du dépot git | 1

### Client (Python)

#### Fonctionnalités
- [X] **Hamza :** : Se connecter au serveur TCP-IP | 2
  - [ ] **Test** : Vérifier la connexion au serveur | 1

- [X] Prendre l'instruction de modification d'image | 1

- [ ] Prendre l'image à modifier (image locale) + vérifier le format du fichier | 12
  - [ ] **Test** : Vérifier les formats d'image acceptés | 1

- [X] **Ahibou :** Voir comment faire (+ tester) une requête au serveur avec l'image, l'instruction et le token (JWT - JSON Web Token) | 2

- [ ] Faire une interface utilisateur | 12

- [ ] Afficher l'image retournée du serveur | 4

- [ ] Permettre l'enregistrement de l'image modifiée | 2

---

### Serveur (Java)

#### Fonctionnalités
- [x] **Grégoire** : Créer un serveur TCP-IP / 1

- [X] **Ahibou & Grégoire** : Accepter les nouvelles connexions et générer un token par client / 3

- [X] **Ahibou** : Recevoir une requête de la forme : [token] [image] [instruction] / 1

- [X] **Ahibou** : Vérifier la validité du token / 1

- [X] **Ahibou & Grégoire** : Différencier l'instruction / 1

- [ ] **Tiago** Modifier l'image / 12
  - [ ] **Rotation à gauche** / 3
  - [ ] **Rotation à droite** / 3
  - [ ] **Inversion horizontale** / 3
  - [ ] **Inversion verticale** / 3
  - [ ] **Noir & blanc** / 3

- [ ] Renvoyer au client l'image modifiée / 12

---

### Sécurité
- [ ] Cryptage des requêtes / 12
  - [ ] Vérifier le cryptage des requêtes / 1

---

#### Total des points
- **Points terminés** : 1 points
- **Points non terminés** : 34 points
- **Total des points pour Sprint 1** : **35 points**