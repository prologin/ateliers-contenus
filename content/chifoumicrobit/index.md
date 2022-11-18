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

En arrivant, il croise Pacman et le fantôme Bouh qui s'ennuyaient. Skeleton
leur propose de faire un chifoumi... mais ils n'ont pas de mains,
donc ils ne peuvent pas mimer les symboles ! Skeleton a besoin de ton aide !
Il te demande de créer un programme leur permettant de jouer sur des `micro:bit` !
Peux-tu aider notre ami ?

<!-- TODO: ajouter le but du jeu -->
<!-- TODO: ajouter l'image du but du jeu -->

Pour faire cela, nous allons t'aider à créer le code étapes par étapes.
Si tu as des questions particulières, n'hésite pas à demander à un
organisateur autour de toi, ils sont là pour ça !

## Mais dis-moi Jammy, c'est quoi un `micro:bit` ?

Les `micro:bit` sont des cartes programmables qu'on te fournit tout
au long de l'atelier. Avec celles-ci, tu vas pouvoir interagir avec ses
composants comme les 25 LEDs au milieu ou les boutons.

{{< figure src=resources/images/microbit.png height=50% width=50% alt="Micro:bit">}}

Nous verrons un peu plus tard comment manipuler les `micro:bit`.


# Programmer en Python

Pour pouvoir créer notre jeu pour Skeleton, il va te falloir quelques connaissances
en Python. Si tu as la moindre question, n'hésite pas à la poser à un organisateur !

## Les variables en Python

La plupart du temps, on va vouloir stocker des informations dans notre code.
On parle alors de variables. Elles vont nous permettre de ranger des choses
et de pouvoir les ressortir quand on le souhaite. Les variables sont des éléments
qui associent un nom à une valeur. C'est comme si on utilisait des boîtes pour
ranger des éléments !

<!-- TODO: ajouter les images -->

Pour déclarer une variable en Python, on va faire comme ça :

```python
# `ma_variable` stocke la valeur 42
ma_variable = 42
```

Tu vas pouvoir afficher les valeurs de tes variables ou du texte avec la fonction
`print()`.

```python
# `ma_variable` stocke la valeur 42
ma_variable = 42

# Affiche la valeur de `ma_variable` dans la console
print(ma_variable)

# Affiche le texte "Hello world!" dans la console
# N'oublie pas les `"` pour écrire du texte en Python,
# sinon, cela ne fonctionnera pas !
print("Hello world!")
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

*C'est quoi les lignes qui commencent par un `#` ?*

Les lignes commençant par des `#`, ce sont des commentaires. Cela te permet
d'expliquer ton code par des phrases pour toi ou même pour les personnes qui
t'entourent.

## Les conditions en Python : si, sinon si, sinon

Prenons un exemple, si Skeleton mange, il n'aura plus faim pour une glace.
Le début de cette phrase est une condition, qu'on peut identifier à l'aide
du mot "si". La condition ici est : Skeleton mange. Elle peut être vraie ou fausse.

<!-- TODO: rajouter les images -->

C'est la même chose en Python. On va pouvoir définir des conditions qui
s'évaluent à vrai ou faux et pouvoir exécuter des lignes de codes en conséquence.
Le mot clé "si" va être remplacé par son équivalent en anglais, `if`.

```python
# Vérifie si 1 est égal à 1
if 1 == 1:
    # Affiche dans la console "Skeleton est trop fort !"
    print("Skeleton est trop fort !")
```

Parfois, il va falloir que tu vérifies si deux conditions sont vérifiées en
même temps. On va alors parler du mot clé `and` qui signifie "et" en français.
Pour faire cela, voici un exemple en Python :

```python
a = 5

# Vérifie si 42 est inférieur à 50 et si a est égal à 5
if 42 == 50 and a == 5:
    # Affiche dans la console "Pacman aime les chats !"
    print("Pacman aime les chats !")
```

*Mais pourquoi on rajoute des espaces avant les lignes ?*

Python suit ligne par ligne ton programme, donc pour lui expliquer ce que tu veux
faire sous certaines conditions, il faut rajouter des espaces avant les lignes
pour créer des blocs. On parle alors d'indentation. Cela permet à Python de
savoir quand est-ce que s'arrêter. Pour faire ça, on va utiliser la
touche de tabulation (`Tab`) sur ton clavier, elle ressemble à ça :

{{< figure src=resources/images/tab.png height=20% width=20% alt="La touche tabulation">}}

On peut également utiliser les mots clés "sinon" et "sinon si". Un petit exemple
en français : Si je mange japonnais, je n'aurais plus faim. Sinon si je mange
italien, j'aurais encore un peu faim. Sinon, j'aurais trop faim. On peut alors
utiliser `else` pour "sinon" et `elif` pour "sinon si".

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

Pacman et le fantôme Bouh veulent tester tes capacités à écrire du code !
Pour cela, tu dois créer une variable `x`, et en fonction de sa valeur tu dois
afficher un texte dans la console, en suivant ces conditions :
- si x est inférieur à 10, tu dois afficher "Glace"
- sinon si x est inférieur à 20, tu dois afficher "Pizza"
- sinon si x est inférieur à 30, tu dois afficher "Crêpe"
- sinon, tu dois afficher "Gaufre"

## Les boucles en Python, les boucles en Python, les boucles en Python

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
    # Afficher "Bonjour !"
    print("Bonjour !")

    # Ajouter 1 à i à chaque tour de boucle
    i = i + 1
```

## Les listes en Python

Lorsqu'on veut stocker de nombreuse valeurs pour pouvoir les réutiliser
par la suite, on ne va pas créer par exemple 20 variables.
Ce que l'on va utiliser sont les listes. Les listes vont nous permettre de stocker
plusieurs valeurs dans une seule variable.

<!-- TODO: rajouter des images -->

Par exemple, en Python :

```python
# Liste des nombres de 0 à 5
ma_liste_nombres = [0, 1, 2, 3, 4, 5]
```

La liste est numérotée de 0 à la longueur de la liste moins 1. Pour accéder
à un élément d'une liste en Python, tu peux utiliser les index ! Les index sont
compris entre 0 et la longueur de la liste moins 1.

En Python, pour accéder à un élément à l'index 2, tu peux faire comme ceci :

```python
# Liste de lettres
ma_liste_lettres = ["a", "b", "c", "d"]

# `ma_variable` est l'élément à l'index 2 de `liste` ("c")
ma_variable = liste[2]

# Affiche `ma_variable` dans la console
print(ma_valeur)
```

### Exercice 2

Pacman a stocké dans une liste ses derniers scores dans le jeu. Il voudrait
les afficher un à un, ligne par ligne. Pour faire cela, il te donne la liste et
sa longueur, et c'est à toi d'afficher les éléments de la liste avec une boucle !

```python
# Liste des scores
derniers_scores = [4242, 3942, 5832, 6048, 3891]

# Longueur de la liste `derniers_scores` (ici 5)
longueur = len(derniers_scores)
```

## L'aléAtOiRE eN PYthOn

En Python, on peut simuler de l'aléatoire, comme dans un lancé de dé. Pour faire
cela, il faut alors donner deux nombres, qui va être notre intevalle lequel on
veut générer le nombre aléatoire.

En Python, pour générer notre nombre aléatoire, il va d'abord falloir importer
une bibliothèque. Cela va nous permettre d'utiliser des fonctions déjà écrites
dans la bibliothèque. Ici, on va juste utiliser la fonction `randint`. Si tu ne
connais pas les fonctions, il faut les considérer comme des machines dans
lequelles on entre des valeurs et qui nous en ressortent d'autre. Elles vont
travailler sur nos entrées pour ressortir un élément.

```python
# Importe la bibliothèque pour générer des nombres aléatoires
from random import randint

# `ma_variable` va contenir une valeur entre 0 et 4 exclu
# Les valeurs possibles sont alors : 0, 1, 2 et 3
ma_variable = randint(0, 4)

# Affiche `ma_variable` dans la console
print(ma_variable)
```

N'hésite pas à relancer plusieurs fois ton code pour avoir un autre nombre
généré.

### Exercice 3

Bouh le fantôme n'arrive pas à faire de choix pour ce qu'il veut manger à midi.
Pour l'aider, Skeleton souhaiterait que tu lui fasses un programme permettant
de choisir aléatoirement un élément dans la liste des choix possibles et
d'afficher ce choix. On te donne alors la liste suivante :

```python
# Liste des choix
liste_choix = ["Frites", "Salade", "Riz"]
```

# Programmons avec des `micro:bit` !

Pour pouvoir utiliser les `micro:bit` avec Python, on va devoir importer
une bibliothèque comme ce que l'on a fait pour les nombres aléatoires.
Cela va nous permettre d'intéragir avec les `micro:bit`.

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
Voici un exemple pour afficher un sourire :

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *

# Affiche un sourire sur le micro:bit
display.show(Image.HAPPY)
```

La fonction `display.show()` nous permet d'afficher ce que l'on souhaite sur
les LEDs du `micro:bit`. `Image.HAPPY` est une image déjà définie par
la bibliothèque des `micro:bit`. Tu peux y retrouver la liste des images
disponibles [ici](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html).

Pour afficher du texte ou des nombres, tu vas pouvoir utiliser la fonction
`display.scroll()`.

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *

# Affiche "Chifoumicro:bit" sur le micro:bit
display.scroll("Chifoumicro:bit")
```

### Exercice 4

Pour voir si tu as bien compris comment on manipule les images, Skeleton
souhaiterait que tu affiches un coeur (heart en anglais) sur ton `micro:bit`.

### Mais il y a des boutons à côté des LEDs !

A côté des 25 LEDs du `micro:bit`, tu peux retrouver à gauche, le bouton `A`,
et à droite, le bouton B. Pour connaître le nombre d'appuis sur les boutons,
tu peux utiliser les fonctions `button_a.is_pressed()` et `button_a.was_pressed()`.
Tu peux retrouver les mêmes fonctions pour le bouton `b` juste en remplaçant
`button_a` par `button_b`.

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *

# Tant que `True` (vrai) est vrai :
# boucle infinie
while True:
    # Tant que le bouton A est appuyé
    while button_a.is_pressed():
        display.show(Image.GHOST)

    # Tant que le bouton B est appuyé
    while button_b.is_pressed():
        display.show(Image.PACMAN)

    # Eteint tous les pixels
    display.clear()
```

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *

# Affiche "Go !" sur le `micro:bit`
display.scroll("Go !")

# Met en pause le programme le temps que l'utilisateur
# appuie sur le bouton A
sleep(200)

# `a_presse` est une variable qui contient `True`
# si le bouton a été appuyé, `False` sinon
a_presse = button_a.was_pressed()

# Si `a_presse` est vrai
if a_presse:
    # Affiche une image avec une coche
    display.show(Image.YES)
else:
    # Affiche une image avec une croix
    display.show(Image.NO)

```

*Mais c'est quoi ça `sleep(200)` ?*

`sleep(100)`, permet de mettre en pause le programme le temps que tu puisses
appuyer sur les boutons. Il peut alors vérifier si tu appuies sur les boutons
pendant ce laps de temps.

<!-- TODO: explication de comment faire le TP -->

<!-- TODO: Bonus : radio -->
