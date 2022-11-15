---
title: Chifoumicro:bit
authors: ["Grégoire 'greg' Lefaure", "Clément 'swarwerth' Nguyen"]
subtitle: "Apprenez à coder un chifoumi sur un micro:bit"
date: 2022
weight: 5
code_stub_url: ./resources/given_resources/chifoumicrobit.py
---

# Introduction au sujet...

Notre ami Skeleton le squelette était en train de jouer à son jeu préféré,
[Pacman](https://fr.wikipedia.org/wiki/Pac-Man). Il a voulu mettre en pause
le jeu, mais, en cliquant sur le bouton, il a été téléporté dans l'univers du jeu.

En arrivant, il croise Pacman et un fantôme qui s'ennuyaient. Skeleton
leur propose de faire un chifoumi... mais ils n'ont pas de mains,
donc il ne peuvent pas mimer les symboles ! Skeleton a besoin de t'aide !
Il te demande de créer un programme leur permettant de jouer sur des `micro:bit` !

Pour faire cela, nous allons t'aider et pour créer le code étapes par étapes.
Si tu as des questions particulières, n'hésite pas à demander à un
organisateur autour de toi, ils sont là pour ça !

## Mais dis moi Jammy, c'est quoi un `micro:bit` ?

Les `micro:bit` sont des cartes programmables qu'on te fournit tout
au long de l'atelier. Avec celles-ci, tu vas pouvoir intéragir avec ses
composants comme les 25 LEDs au milieu ou les boutons.

{{< figure src=resources/images/microbit.png height=50% width=50% alt="Micro:bit">}}

Nous verrons un peu plus tard comment manipuler les `micro:bit`.


# Programmer en Python

Pour pouvoir créer notre jeu pour Skeleton, il va te falloir quelques connaissances
en Python. Si tu as la moindre question, n'hésite pas à la poser à un organisateur !

## Les variables en Python

La plupart du temps, on va vouloir stocker des informations dans notre code.
On parle alors de variables. Elles vont nous permettre de ranger des choses
et de pouvoir les resortir quand on le souhaite. C'est comme si on utilisait
des boîtes pour ranger des éléments !

Pour déclarer une variable en Python, on va faire comme ça :

```python
# `ma_variable` stocke la valeur 42
ma_variable = 42
```

En programmation, tu peux évaluer certaines phrases par vrai ou faux. Par exemple,
la préposition `1 < 2` (1 est inférieur à 2) est vraie ; et `42 > 42`
(42 est supérieur à 42) est faux. Tu peux essayer en Python avec le code suivant :

```python
preposition_une = 1 < 2
# Affiche dans la console le résultat de `1 < 2` (vrai)
print(preposition_une)

preposition_deux = 42 > 42
# Affiche dans la console le résultat de `42 > 42` (faux)
print(preposition_deux)
```

Tu remarqueras sûrement que Python te renvoie `True` et `False`. C'est les termes
en anglais pour dire vrai et faux.

## Les conditions en Python

Prenons un exemple, si Skeleton mange, il n'aura plus faim pour une glace.
Le début de cette phrase est une condition, qu'on peut identifier à l'aide
du mot `si`. La condition ici est : Skeleton mange. Elle peut être vraie ou fausse.

C'est la même chose en Python. On va pouvoir définir des conditions qui
s'évaluent à vrai ou faux et pouvoir exécuter des lignes de codes en conséquence.
Le mot clé `si` va être remplacé par son équivalent en anglais, `if`.

```python
# Vérifie si 1 est égal à 1
if 1 == 1:
    # Affiche dans la console "Skeleton est trop fort !"
    print("Skeleton est trop fort !")
```

*Mais pourquoi on rajoute des espaces ?*

Python suit ligne par ligne ton programme, donc pour lui expliquer ce que tu veux
faire sous certaines conditions, il faut rajouter des espaces avant les lignes
pour créer des blocs. Cela permet à Python de savoir quand est-ce que s'arrêter.
Pour faire ça, on va utiliser la touche de tabulation (Tab) sur ton clavier, elle
ressemble à ça :

{{< figure src=resources/images/tab.png height=30% width=30% alt="La touche tabulation">}}

On peut également utiliser les mots clés `sinon` et `sinon si`. Un petit exemple
en français : Si je mange japonnais, je n'aurais plus faim. Sinon si je mange
italien, j'aurais encore un peu faim. Sinon, j'aurais trop faim. On peut alors
utiliser `else` pour `sinon` et `elif` pour `sinon si`.

```python
ma_variable = 2

# Vérifie si `ma_variable` est égale à 1
if ma_variable == 1:
    # Affiche dans la console "Eau"
    print("Eau")

# Vérifie si `ma_variable` est égale à 2
elif ma_variable == 2:
    # Affiche dans la console "Soda"
    print("Soda")

# Si les conditions au dessus ne sont pas vérifiées, je fais cette partie
else:
    # Affiche dans la console "Lait"
    print("Lait")
```

### Exercice 1

Skeleton souhaite afficher dans la console 

## Les boucles en Python, les boucles en Python

Les boucles nous permettent de répéter plusieurs tâches. En Python,
il y a deux types de boucle ; cependant, dans cet atelier, seul un type
nous suffira : les boucles `while`.

On peut traduire `while` par `tant que` en français. On va pouvoir utiliser
les conditions dans les boucles `while` pour pouvoir répéter des choses
tant qu'une condition est toujours vraie. Par exemple, tant que le bébé dort,
nous ne devons pas faire de bruit.

Un exemple en Python serait celui ci :

```python
# Tant que i est inférieur à 3
while i < 3:
    # Afficher "Bonjour!"
    print("Bonjour!")

    # Ajouter 1 à i à chaque tour de boucle
    i = i + 1
```

<!-- TODO: Boucles, listes, random -->



<!-- TODO: Rajouter des exos -->

# Programmons avec des `micro:bit` !

Pour pouvoir utiliser les `micro:bit` avec Python, on va devoir importer
une bibliothèque. Cela va nous permettre d'utiliser des fonctions déjà écrites
dans la bibliothèque pour intéragir avec les `micro:bit`.

Pour utiliser cette bibliothèque, dans les premières lignes de ton code,
tu vas devoir ajouter cette ligne :

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *
```

## J'ai envie de jouer avec les LEDs du `micro:bit`...

Les LEDs d'un `micro:bit` peuvent soit s'allumer ou s'éteindre de manière
totalement indépendantes. Cependant, dans notre cas, on s'intéressera seulement
à afficher des images déjà fournies par la bibliothèque de `micro:bit`.
Voici un exemple pour afficher un coeur (n'oublie pas d'importer la bibliothèque
pour que cela fonctionne) :

```python
# Affiche un sourire sur le `micro:bit`
display.show(Image.HAPPY)
```

La fonction `display.show()` nous permet d'afficher ce que l'on souhaite sur
les LEDs du `micro:bit`. `Image.HAPPY` est une image déjà définie par
la bibliothèque des `micro:bit`. Tu peux y retrouver la liste des images
disponibles [ici](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html).

### Exercice 1

Pour voir si tu as bien compris comment on manipule les images, Skeleton
souhaiterait que tu affiches un coeur (heart en anglais) sur ton `micro:bit`.

### Mais il y a des boutons à côté des LEDs !

A côté des 25 LEDs du `micro:bit`, tu peux retrouver à gauche, le bouton `A`,
et à droite, le bouton `B`. Pour savoir, si un des boutons est appuyé, tu peux
utiliser les fonctions suivantes :

<!-- TODO: Boutons, Sleep -->

<!-- TODO: Bonus -->
