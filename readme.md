
```markdown
# Système Automatique de Détection des Déchets Urbains 🗑️🏙️

## Introduction

Ce projet propose un système automatique de détection des déchets dans un environnement urbain. En utilisant un modèle pré-entraîné YOLOv5 spécialement configuré pour la détection des déchets, ce système identifie et classe les déchets présents dans les images. Grâce à une interface web simple développée avec Flask, l'utilisateur peut charger une image et visualiser les résultats de détection (boîtes englobantes et scores de confiance). Ce projet vise à fournir un outil pratique pour la surveillance et la gestion des déchets en milieu urbain.

## Développement

### Fonctionnalités

- **Détection des Déchets :**  
  Utilisation du modèle YOLOv5 (`turhancan97/yolov5-detect-trash-classification`) pour détecter et classifier les déchets dans une image.

- **Interface Web :**  
  Application web basée sur Flask permettant à l'utilisateur de charger une image et de visualiser le résultat de la détection.

- **Visualisation :**  
  Affichage côte à côte de l'image originale et de l'image traitée (avec boîtes englobantes et labels), facilitant la comparaison.

- **Rapport de Détection :**  
  Affichage du nombre total de déchets détectés ainsi que des informations détaillées pour chaque détection (label et score).

### Pile Technologique

- **Backend :** Python, Flask  
- **Deep Learning :** PyTorch, YOLOv5  
- **Traitement d'Images :** OpenCV, Pillow, NumPy  
- **Déploiement :** Environnement Python local ou serveur

### Installation

1. **Cloner le Répertoire :**

   ```bash
   git clone <url_du_répertoire>
   cd <dossier_du_répertoire>
   ```

2. **Créer et Activer un Environnement Virtuel (Optionnel mais Recommandé) :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Unix/MacOS
   # ou
   venv\Scripts\activate     # Sur Windows
   ```

3. **Installer les Dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

4. **Structure du Projet :**

   Votre projet doit être organisé comme suit :

   ```
   project_folder/
   ├── app.py
   ├── deeplearning.py
   ├── requirements.txt
   ├── templates/
   │   └── index.html
   └── static/
       ├── upload/
       └── predict/
   ```

### Utilisation

1. **Lancer l'Application :**

   ```bash
   python app.py
   ```

2. **Accéder à l'Interface Web :**

   Ouvrez votre navigateur et rendez-vous sur [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. **Charger une Image :**

   Utilisez le formulaire pour charger une image. Le système traitera l'image et effectuera la détection des déchets.

4. **Visualiser les Résultats :**

   - **Image Originale :** Affichée telle qu'elle a été chargée.
   - **Image Traitée :** Montre les boîtes englobantes autour des déchets ainsi que les labels et scores.
   - **Détails de Détection :** Un tableau récapitule le nombre de déchets détectés et présente les informations détaillées.

## Conclusion

Ce projet démontre l'efficacité d'un système de détection automatique des déchets urbains en combinant des techniques avancées de vision par ordinateur et de deep learning. L'utilisation de YOLOv5 pour la détection, associée à une interface web conviviale basée sur Flask, offre une solution pratique pour la surveillance et la gestion des déchets en milieu urbain. Des améliorations futures pourraient inclure le traitement en temps réel, le raffinement du modèle et l'intégration avec des systèmes de gestion urbaine intelligents.
