---
title: Prolobot
date: 2022
authors: Julie 'DaiF' Fiadino, Hippolyte Pik
subtitle: Codez avec le Robot Microbit
code_stub_url: "./prolobot.py"
---

# Prolobot

<!-- TODO: Introduction -->

## Utiliser avec l'éditeur

<!-- NOTE: tuto pour l'editeur python du site microbit -->

Pour utiliser le robot, commence par télécharger le fichier donné.

Appuie ensuite sur le bouton 'Open...' en bas de l'écran puis 
choisis le fichier que tu viens de télécharger.
![]("img/open_button.png")

Appuie enfin sur le bouton a côté du nom du fichier et sélectionne 'Ajouter le
fichier' avant de valider.
![]("img/load_button.png")

## Introduction
Bonjour à toi jeune programmeur ou programmeuse, je me présente, je suis Joseph Marchand, et c'est moi qui vais t'accompagner au travers de cette decouverte au monde de l'informatique a travers cette atelier. Avant de commencer, laisse moi aussi te présenter mes fidèles acolytes : les organisateurs. Ce sont eux qui vont t'accompagner en ce début de matinée. Ils me remplacent car je suis très occupé en ce moment, mais si tu as une quelconque question à n'importe quel moment, n'hésite surtout pas à leur demander de l'aide, ils sont là pour ça. Je m'arrête là pour les présentations, et je vais commencer dans cette atelier par te montrer les bases pour créer un programme.

Mais d'abord, un ordinateur, c'est quoi ? Un ordinateur n'est rien d'autre qu'un ensemble de composants électroniques qui exécutent des instructions. Lorsque tu ouvres un navigateur internet, ton ordinateur exécute les instructions du logiciel utilisé, qu'on appelle aussi programme. Le but de cet atelier est de te faire découvrir comment nous pouvons créer nos propres programmes, et pour cela il nous faut un moyen d'écrire ces instructions : un langage de programmation.

Il existe énormément de langages de programmation, tout comme il existe des milliers de langues dans le monde ! Certains sont plus connus que d'autres et nous allons, avec les organisateurs, te faire découvrir Python, un langage facile à prendre en main tout en étant puissant.

### Qu'est ce que c'est `microbit:macqueen` ?
Un `microbit` c'est un microcontrôleur de la taille d'une carte à jouer (indication: tu dois pouvoir voir le micro:bit à l'avant du robot). Et `maqueen` c'est le petit robot que vous avez devant vous. `maqueen` c'est un robot qui est entierement configurable avec Python.

### Variables
Commençons dans le vive du sujet, les variables. Les variables sont essentiel en informatique elles permettent de stocker des valeurs et de plus tard les restituer mais aussi de les modifier au cours du temps. Voyons ca dans un exemple:
```py
#Debut du programme

a = 2
b = 5

a = b + a

print(a)
print(b)

#Fin du programme
```
output
```
Sortie

7
5
```

Executons à la main ce petit programme:
    1. `a = 2 b = 5` Stocke la valeur 2 dans la variable `a` et la valeur 5 dans la variable `b`.
    2. Ensuite il y a une ligne vide cette ligne n'influence en aucun cas ton code il permet simplement d'ajouter de l'espace pour en augmenter sa lisibilité. N'hésite pas à t'en servir il permet souvent de ne pas se perdre.
    3. `a = b + a` Ici la variable `a` va prendre la valeur de `b` c'est à dire 5 additionné à l'actuel valeur de `a` c'est à dire 2 pour un total donc de 7.
    4. Encore une ligne vide ne servant qu'a rendre plus lisible le code.
    5. `print(a)` Cette instruction permet en Python d'afficher une valeur sur la sortie (ici 7 est afficher).
    6. `print(b)` Comme pour la ligne précédente affiche la valeur stocker dans `b` sur la sortie (ici 5 est afficher).
Si jamais tu n'as pas bien compris les expliquations n'hesite pas à questionner mes acolytes pour t'éclaircir.

### Conditions
Les conditions sont aussi une partie importante dans l'informatique car elle permet de "séparer" le programme c'est essentiel quand on cherche à traiter des certaines choses. Voyons ça dans cette exemple:

```py
#Debut du programme

a = 2

if a == 1:
    print("Hello")

if a == 2:
    print("World")

heure = 14

if heure == 12:
    print("A table!")

else:
    print("Pas tout de suite")

#Fin du programme
```

Executons ce programme a la main:
    1. La ligne `a = 2` initialise la variable `a` avec la valeur 2.
    2. `if a == 1:` Ici le mot clé de condition `if` demande au programme "si `a` est égale à 1" si c'est vrai alors il va aller à l'interieur de la condition c'est a dire sur la ligne d'apres et de maniere general sur toute les lignes avec une TABULATION de plus que lui (les tabulations sont les espaces mis devant une instruction, nous reparlerons de leur importance dans la suite de cette introduction). 
    3. `print("Hello")` Ici on demande au programme d'afficher `Hello` si la condition est vrai (dans notre cas cette ligne ne sera pas lu car `a` different de 1).
    4. `if a == 2:` Ici on retrouve le mot clé `if` qui demande au programme "si `a` est égale à 2" si c'est vrai alors il va executer les lignes avec une TABULATION de plus que lui.
    5. `print("World")` Ici on demande au programme d'afficher `World` si la condition est vrai (dans notre cas cette ligne sera executer et affichera "World").
    6. La ligne `heure = 14` initialise la variable `heure` avec la valeur 14.
    7. `if heure == 12:` Ici le mot clé de condition `if` demande au programme "si `heure` est égale à 12" si c'est vrai alors il entrera à l'interieur de la condition et affichera toutes les instructions possédant une indentation de plus que lui.
    8. `print("A table!")` Ici on demande au programme d'afficher `A table!` si la condition est vrai (dans notre cas cette ligne ne sera pas lu car `heure` different de 12)
    9. `else:` Ici le mot clé impose au programme d'aller dans la boucle s'il n'est pas entrer dans la condition (dans notre cas on entrera dans le `else`). On peut par ailleurs traduire le mot clé `else` par "sinon" (`if`: si oui, `else`: si non).
    10. `print("Pas tout de suite")` Ici on demande au programme d'afficher `Pas tout de suite` si on n'est pas entré dans la condition `if`. Attention on ne peut pas mettre de `else` si il n'y a pas de `if`.

Cette partie peut etre compliquer mais n'hesite pas à questionner mes acolytes afin de ne pas rester perdu.

Revenons rapidement sur les expliquations de la TABULATION. La TABULATION est une chose extremement important en Python elle permet de faire comprendre au programme quand aller dans une partie d'un programme ou non. Quand vous ferez votre programme plus bas il sera sûrement nécessaire d'en utiliser. Pour se faire, la TABULATION est representer par les 2 fleches ayant des sens opposés. Cette touche est situé à côté de la touche `A`.

## Le Prolobot

### Avancer

Pour faire avancer le robot, tu peux écrire `bot.avancer()`.

Cette ligne va permettre d'activer les moteurs du robot.
> Attention : Cette instruction ne le fait pas arrêter ! Pour cela, il faut
> écrire `bot.stop()`

Tu peux également préciser la vitesse du robot en mettant un nombre entre 0 et 1
entre les parenthèses. Si tu ne précise pas, le robot ira à la vitesse 0,2.

Voici par exemple comment tu peux le faire avancer.

```py
bot.avancer()
sleep(1000)
bot.avancer(0.5)
sleep(2000)
bot.stop()
```

Ici, la ligne `sleep(1000)` va indiquer au programme qu'il doit attendre pendant
1000 millisecondes, soit 1 seconde.
Le robot va donc activer les moteurs, puis attendre 1 seconde et activer les
moteurs à la vitesse 0.5, puis il attends 2 secondes avant de s'arrêter.

Le robot peut aussi reculer en écrivant `bot.reculer()`. Tout comme pour avancer,
on peut préciser la vitesse des roues entre les parenthèses.


### Ca tourne
#### Le sleep

## Les Bonus
### Les Leds
### Les boucles
### Capteurs

## La Doc

La doc répertorie toutes les fonctions qui permettent de contrôler le robot.

<!-- NOTE: La doc est temporaire, si elle reste ca sera juste a la fin pour
    en tant que recap -->

### Instantier le robot

```py
import prolobot

bot = Prolobot()
```

### Variables globales

`GAUCHE = 0`. A donner en parametre pour tourner a gauche.
`DROITE = 1`. A donner en parametre pour tourner a droite.

### Fonctions

#### Deplacement

`bot.avancer()`: avance le robot.
- La vitesse par defaut est 0.2

`bot.avancer(vitesse)`: avance a la vitesse donnee.
- La vitesse est un float entre 0 et 1.

`bot.reculer()`: recule le robot.
- La vitesse par defaut est 0.2.

`bot.reculer(vitesse)`: recule le robot a la vitesse donnee.
- La vitesse est un float entre 0 et 1.

`bot.tourner(direction)`: tourne le robot dans la direction donnee. 
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction.

`bot.tourner(direction, vitesse)`: tourne le robot dans la direction et a la vitesse donnee.
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction
- La vitesse est entre 0 et 1

`bot.pivoter(direction)`: tourne le robot sur lui même dans la direction donnee. 
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction.

`bot.pivoter(direction, vitesse)`: tourne le robot sur lui même dans la direction et a la vitesse donnee.
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction
- La vitesse est entre 0 et 1

`bot.stop()`: arrete le robot.

#### Capteurs

`bot.distance()`: renvoie la distance entre le robot et les obstacles en face de lui.

`bot.capteur_sol(capteur)`: renvoie 1 si le capteur detecte du noir.
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer quel capteur utiliser.

#### LEDs

`bot.set_phares(phare, statut)`: allume ou eteint un des phares avant,
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer quel capteur utiliser.
- Le statut est a 1 pour allumer et 0 pour eteindre la led

`bot.allumer_led(led, couleur)`: allume la led correspondante.
- La led est un entier de 0 a 3 servant a preciser la led a allumer
- La couleur est de la forme (rouge, vert, bleu), avec les couleurs allant de 0 a 255

`bot.eteindre_led()`: eteint toutes les leds
