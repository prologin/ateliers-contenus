---
title: Chifoumicro:bit
authors: ["Grégoire 'greg' Lefaure", "Clément 'swarwerth' Nguyen"]
subtitle: "Apprenez à coder un chifoumi sur un micro:bit"
date: 2022
weight: 5
---

# Introduction au sujet...

Notre ami Skeleton le squelette était en train de jouer à son jeu préféré, [Pacman](https://fr.wikipedia.org/wiki/Pac-Man). Il a voulu mettre en pause le jeu, mais, en cliquant sur le bouton, il a été téléporté dans l'univers du jeu.

En arrivant, il croise Pacman et un fantôme qui s'ennuyaient. Skeleton leur propose de faire un chifoumi... mais ils n'ont pas de mains, donc il ne peuvent pas mimer les symboles !
Skeleton a besoin de t'aide ! Il te demande de créer un programme leur permettant de jouer sur des `micro:bit` !

Pour faire cela, nous allons t'aider et pour créer le code étapes par étapes.

Si tu as des questions particulières, n'hésite pas à demander à un organisateur autour de toi, ils sont là pour ça !

## Mais dis moi Jammy, un micro quoi ?

Les `micro:bit` sont des cartes programmables qu'on te fournit tout au long de l'atelier.
Avec celles-ci, tu vas pouvoir intéragir avec ses composants comme les LEDs ou les boutons.

Ne t'inquiète pas, on va t'expliquer comment les utiliser dans la suite du sujet !

# Programmons avec des `micro:bit` !

Pour pouvoir utiliser les `micro:bit` avec Python, on va devoir importer une bibliothèque.
Cela va nous permettre d'utiliser des fonctions déjà écrites dans la bibliothèque pour intéragir avec les `micro:bit`.

Pour utiliser cette bibliothèque, dans les premières lignes de ton code, tu vas devoir ajouter cette ligne :

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *
```
