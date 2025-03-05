# Système Automatique de Détection des Déchets Urbains 🗑️🏙️

## Introduction

Le projet de **Détection Automatique des Déchets Urbains** est une solution innovante qui utilise l'intelligence artificielle pour identifier et classifier les déchets dans les environnements urbains. En exploitant la puissance du modèle YOLOv5, ce système offre une approche technologique moderne pour la surveillance et la gestion des déchets.

## Fonctionnalités Principales

### 🔍 Détection Intelligente
- Utilisation du modèle YOLOv5 (`turhancan97/yolov5-detect-trash-classification`)
- Détection précise et classification des différents types de déchets
- Identification avec scores de confiance

### 🌐 Interface Web Conviviale
- Application développée avec Flask
- Chargement facile d'images
- Visualisation intuitive des résultats de détection

### 📊 Analyse Détaillée
- Affichage côte à côte de l'image originale et traitée
- Rapport détaillé incluant :
  - Nombre total de déchets détectés
  - Étiquettes de chaque déchet
  - Scores de confiance

## Pile Technologique

| Catégorie | Technologies |
|-----------|--------------|
| **Backend** | Python, Flask |
| **Deep Learning** | PyTorch, YOLOv5 |
| **Traitement d'Images** | OpenCV, Pillow, NumPy |

## Prérequis

- Python 3.8+
- Connexion Internet (pour le téléchargement des dépendances)
- Navigateur web

## Installation

### 1. Clonage du Répertoire

```bash
git clone <url_du_répertoire>
cd <dossier_du_répertoire>
```

### 2. Configuration de l'Environnement Virtuel

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Unix/MacOS
source venv/bin/activate

# Sur Windows
venv\Scripts\activate
```

### 3. Installation des Dépendances

```bash
pip install -r requirements.txt
```

## Structure du Projet

```
project_folder/
├── app.py                 # Application principale
├── deeplearning.py        # Logique de détection
├── requirements.txt       # Dépendances du projet
├── templates/             # Modèles HTML
│   ├── index.html         # Page principale
│   └── layout.html        # Mise en page de base
└── static/                # Ressources statiques
    ├── upload/            # Images téléchargées
    └── predict/           # Images traitées
```

## Utilisation

### Lancement de l'Application

```bash
python app.py
```

### Accès à l'Interface

1. Ouvrez votre navigateur
2. Naviguez vers [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
3. Chargez une image contenant des déchets

### Interprétation des Résultats

- **Image Originale :** Image source
- **Image Traitée :** 
  - Boîtes englobantes autour des déchets
  - Étiquettes de classification
  - Scores de confiance

## Perspectives d'Amélioration

- Intégration de détection en temps réel
- Raffinement du modèle de détection
- Connexion avec des systèmes de gestion urbaine intelligents

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des problèmes
- Proposer des améliorations
- Soumettre des pull requests

## Licence

Ce projet est sous licence MIT.

```
MIT License

Copyright (c) [année] [nom complet]

Permission est accordée, gratuitement, à toute personne obtenant une copie
de ce logiciel et des fichiers de documentation associés (le "Logiciel"), de traiter
le Logiciel sans restriction, notamment les droits d'utilisation, de copie, de modification, 
de fusion, de publication, de distribution, de sous-licencier et/ou de vendre des copies du Logiciel, 
et de permettre aux personnes à qui le Logiciel est fourni de le faire, sous réserve des conditions suivantes :

Le texte ci-dessus et cet avis de permission doivent être inclus dans toutes
copies ou parties substantielles du Logiciel.

LE LOGICIEL EST FOURNI "TEL QUEL", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU
IMPLICITE, NOTAMMENT SANS GARANTIE DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE
PARTICULIER ET D'ABSENCE DE CONTREFAÇON. EN AUCUN CAS, LES AUTEURS OU DÉTENTEURS DU
COPYRIGHT NE SERONT RESPONSABLES DE TOUTE RÉCLAMATION, DOMMAGE OU AUTRE RESPONSABILITÉ,
QUE CE SOIT DANS LE CADRE D'UN CONTRAT, D'UN DÉLIT OU AUTREMENT, EN RELATION AVEC LE
LOGICIEL OU SON UTILISATION OU AUTRES INTERACTIONS AVEC CELUI-CI.
```

## Contact

Pour plus d'informations, contactez [Votre Nom/Email]

## Remerciements

- Modèle YOLOv5 par Ultralytics
- Contributeurs des bibliothèques open-source utilisées
