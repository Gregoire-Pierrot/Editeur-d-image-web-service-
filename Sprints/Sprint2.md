# Backlog Sprint 2

---

## Objectif principal :  
Établir la connexion au serveur et commencer à développer l'interface client.

---

### **Schéma interaction Client-Serveur**
- [x] **Grégoire** : Créer un schéma illustrant le fonctionnement du Web-Service / **3 points**

---

### **Client (Python)**

#### **Fonctionnalités :**
- [x] **Hamza** : Se connecter au serveur | **2 points**
  - [ ] **Test** : Vérifier la connexion au serveur | **1 point**
- [X] **Elias** Gérer l'image à modifier (image locale) + vérifier le format du fichier | **12 points**
  - [ ] **Test** : Vérifier les formats d'image acceptés | **1 point**
- [x] **Ahibou** : Faire une requête au serveur avec l'image, l'instruction et le token (JWT) | **2 points**
- [x] **Ibrahim** : Créer l'interface utilisateur | **12 points**
- [ ] Afficher l'image retournée par le serveur | **4 points**
- [ ] Permettre l'enregistrement de l'image modifiée | **2 points**

---

### **Serveur (Java)**

#### **Fonctionnalités :**
- [x] **Grégoire** : Créer le serveur | **1 point**
- [ ] **Ahibou & Grégoire** : Accepter les nouvelles connexions et générer un token par client | **3 points**
- [ ] Recevoir une requête sous la forme : `[token] [image] [instruction]` | **1 point**
- [ ] Vérifier la validité du token | **1 point**
- [ ] **Grégoire** : Différencier les instructions | **1 point**
- [x] **Tiago** : Modifier l'image | **15 points**
  - [x] Rotation à gauche | **3 points**
  - [x] Rotation à droite | **3 points**
  - [x] Inversion horizontale | **3 points**
  - [x] Inversion verticale | **3 points**
  - [x] Noir et blanc | **3 points**
- [ ] Renvoyer l'image modifiée au client | **12 points**

---

### **Sécurité**
- [ ] Cryptage des requêtes | **12 points**
  - [ ] Vérifier le cryptage des requêtes | **1 point**

---

### **Total des points**
- **Points terminés** : 35 / 86 points
- **points non terminés** : 51 / 86 points

---
