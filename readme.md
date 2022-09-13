# Interface d'administration du banc de test

## Objectif

L'objectif de cette interface est de créer un wrapper autour de caldera pour facilement lancer une simulation d'attaque.

## Requierments
- python 3.10
- Caldera qui tourne sur le port 8888 en local (cf. documentation de caldera pour l'installation, utilisation de docker recommandée)

## Run

```console
sudo docker run -d -p 8888:8888 caldera:latest
cd admin-maritime
pip install -r requierments.txt
python app.py
```

## Fonctionnement

Le fichier caldera.py implémente les wrappers de l'API caldera. L'interface est présentée sous la forme d'une webapp Flask.

L'onglet "agents" permet de gérer les agents Caldera,e t de leur donner un rôle (simulation, ECDIS, etc..)
L'onglet "simulation" permet de choisir un contexte et une attaque, et de lancer le tout automatiquement.

## TODO

- [x] Sauvegarder les rôles des agents dans une session
- [ ] Lancement d'une simulation simple
- [ ] Possibilité d'enregistrer de laoder des simulations
- [ ] Système de configuration pour les simulation (au lieu de hardcoder). Par exemple au lieu de harcoder que le contexte prend une option fréquentation entre 0 et 3, et qu'il faut passer cette option au simulateur avec l'argument "--freq=n", faire un fichier type xml qui permet de modifier l'environnement sans toucher au code.
- [ ] Création d'attauqes complexes avec des blocs et des délais