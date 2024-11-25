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
- [ ] Prendre l'image à modifier (image locale) + vérifier le format du fichier / 12
  - [ ] **Test** : Vérifier les formats d'image acceptés / 1
- [x] **Ahibou** : Faire une requête au serveur avec l'image, l'instruction et le token (JWT) / 2
- [ ] **Ibrahim** : Faire une interface utilisateur / 12
- [ ] Afficher l'image retournée du serveur / 4
- [ ] Permettre l'enregistrement de l'image modifiée / 2

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
