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
Le fichier testbed.py implémente les fonctions pour produire les commandes pour le testbed (simu, ECDIS, ...)
Le fichier app.py est le fichier principal de l'app

L'onglet "agents" permet de gérer les agents Caldera,e t de leur donner un rôle (simulation, ECDIS, etc..)
L'onglet "simulation" permet de choisir un contexte et une attaque, et de lancer le tout automatiquement.

## TODO

- [x] Sauvegarder les rôles des agents dans une session
- [x] Lancement d'une simulation simple
- [ ] Créer une description modulable de l'environnement (description des attaques et des agent). Par exemple, une attaque est constituée d'un script prenant tels arguments, de telle manière, etc. De cette manière, il sera possible de modifier les attaques, le contexte etc. sans changer le code
- [ ] Création d'attaques complexes (gnagnagna oN DiT pAs coMpLExe Ca vEUt RiEN DirE) avec des blocs et des délais
- [ ] Attaques compexes: noramlisationd e la représentation 
- [ ] Attaques compexes: sauvegarde 
- [ ] Attaques compexes: triggers (attendre un événement avant de déclencher une attaque, déclencher une attaque ou une autre selon un événement etc.) 
- [ ] Checker la sécu de l'appli (injections etc.)