# Projet de Compression - INFO 413 - Codage et traitement de signal

Ce projet est un utilitaire simple en Python permettant de tester et comparer l'efficacité de trois algorithmes de compression de données qui sont mentionnés dans le sujet d'examen : BZIP2, LZMA et 7-ZIP (via ZIP).

## Structure du projet : le dossier principal du projet est INFO 413

- main.py : Le script principal qui contient tout le code (lecture du fichier, compression avec les 3 algorithmes, calcul des gains en pourcentage et affichage).
- README.md : Ce fichier de documentation.
- tests : c'est le dossier où l'on peut mettre tous les types 4 types de fichiers de test spuhaités (texte, image, audio et vidéo).
NB : il faut juste retirer le fichier à tester dans "tests" et le mettre dans le dossier principal du projet INFO 413. (C'est pour la bonne structure du projet que j'ai créé le dossier "tests" pour y mettre le fichiers de test dedans, pour qu'il n'y aura pas trop de fichiers).

## Comment l'utiliser ?

1. Assurez vous d'avoir "Python" installé sur votre ordinateur. Moi, j'ai travaillé sur l'environnment Visual Studio Code.
2. Placez le fichier que vous souhaitez tester (texte, image, audio ou vidéo) dans le dossier principal où se trouve "main.py", donc le dossier INFO 413.
3. Ouvrez un terminal dans le dossier et lancez la commande suivante :
bash : python main.py
4. Puis la commande affiche "Entre le nom du fichier à compresser"; puis vous entrez le nom du fichier que vous souhaiteriez compresser.
