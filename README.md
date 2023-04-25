# Ateliers Contenu

Ce repo réunit toutes les ressources utilisées lors des Ateliers Prologin.
Le site est déployé à l'adresse [](https://ateliers.prologin.org).

# Faire tourner le site en local

Pour lancer le site en local, il suffit de taper ces commandes dans un terminal
à la racine du repo :

```
git submodule update --init themes/prologin
./build.sh
hugo server
```

Hugo affiche ensuite le port sur lequel trouver le site (en général le port 1313).

# Le thème

Pour avoir un détail des fonctionalités du site, vous pouvez vous rendre sur le
repo [hugo-base-theme]("https://gitlab.com/prologin/tech/packages/hugo-base-theme").

C'est également ici qu'il faut faire toute issue concernant le site : du CSS pas
très beau, un bouton qui marche pas, etc.

# Contribuer

Vous pouvez contribuer aux TPs en faisant une merge request sur le repo.

Un nouveau sujet est enregistré dans son propre sous-dossier dans `content`.
Le sujet est écrit en markdown dans le fichier `index.md`.

Vous pouvez créer une nouvelle architecture en tapant cette commande à la racine du repo : 
```bash
hugo new -k subject nom_du_sujet
```
Chaque sujet commence avec le header suivant :

```
title: Le titre
authors: Prénom1 'Pseudo' Nom1, Prénom2 'Pseudo' Nom2, ...
subtitle: Le sous-titre du tp
date: 20XX
code_stub_url: ./resources/given_resources/fichier_a_completer.py
```

Les ressources (images, refs, code à compléter) sont enregistrées dans dossier
`resources`. Dans le cas des ressources données aux participants, elles sont
enregistrées dans un dossier `given_resources` et indiquées dans le header sous
l'option `code_stub_url`. Dans le cas où il y aurait plusieurs fichiers fournis,
un fichier `zip` sera automatiquement créé (il ne faut pas push de `zip`). Le 
lien à mettre dans `code_stub_url` est alors `resources/given_resources/nom_du_sujet.zip`.
