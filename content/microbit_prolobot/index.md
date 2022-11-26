---
title: Prolobot
date: 2022
authors: Julie 'DaiF' Fiadino, Hippolyte Pik
subtitle: Codez avec le Robot Microbit
code_stub_url: "./prolobot.py"
---

## Introduction
Bonjour à toi jeune programmeuse, programmeur. Je me présente, je suis Joseph Marchand, et c'est moi qui t'accompagnerais au travers de cette découverte du monde de l'informatique durant cet atelier.
Avant de commencer, laisse moi te présenter mes fidèles acolytes : les organisateurs. Ce sont eux qui t'accompagnent
aujourd'hui. Ils me remplacent car je suis très occupé en ce moment, mais si tu as une quelconque question, à n'importe quel moment, n'hésite surtout pas à leur demander de l'aide, ils sont là pour ça.
Je m'arrête là pour les présentations, et commençons cet atelier par les bases de la création d'un programme.

Mais d'abord, un ordinateur, c'est quoi ? Un ordinateur n'est rien d'autre qu'un ensemble de composants électroniques qui exécutent des instructions. Lorsque tu ouvres un navigateur internet, ton ordinateur exécute les instructions du logiciel utilisé, qu'on appelle aussi programme. Le but de cet atelier est de te faire découvrir comment nous pouvons créer nos propres programmes. 
Et pour cela il nous faut un moyen d'écrire ces instructions : un langage de programmation.

Il existe énormément de langages de programmation, tout comme il existe des milliers de langues dans le monde ! Certains sont plus connus que d'autres et nous allons, avec les organisateurs, te faire découvrir Python, un langage facile à prendre en main tout en étant puissant.

### Qu'est ce que c'est `microbit:macqueen` ?
Un `microbit` c'est un microcontrôleur de la taille d'une carte à jouer (indication: tu dois pouvoir voir le micro:bit à l'avant du robot). Et `maqueen` c'est le petit robot que vous avez devant vous. `maqueen` c'est un robot qui est entièrement configurable avec Python.

### Variables
Commençons dans le vif du sujet: les variables. Les variables sont essentielles en informatique elles permettent de stocker des valeurs et de les restituer plus tard mais aussi de les modifier au cours du temps. Voyons cela dans un exemple:
```py
#Debut du programme

a = 2
b = 5

a = b + a

print(a)
print(b)

#Fin du programme
```
Ce que python nous renvoit :
```
Sortie

7
5
```

Exécutons à la main ce petit programme:
    1. `a = 2 b = 5` Stocke la valeur 2 dans la variable `a` et la valeur 5 dans la variable `b`.
    2. Ensuite il y a une ligne vide, cette ligne n'influence en aucun cas ton code il permet simplement d'ajouter de l'espace pour en augmenter sa lisibilité. N'hésite pas à t'en servir il permet souvent de ne pas se perdre.
    3. `a = b + a` Ici la variable `a` va prendre la valeur de `b` c'est à dire 5 additionné à l'actuelle valeur de `a` c'est à dire 2 pour un total donc de 7.
    4. Encore une ligne vide ne servant qu'à rendre plus lisible le code.
    5. `print(a)` Cette instruction permet en Python d'afficher une valeur sur la sortie (ici 7 est affichés).
    6. `print(b)` Comme pour la ligne précédente affiche la valeur stockée dans `b` sur la sortie (ici 5 est affichés).
Si jamais tu n'as pas bien compris les explications n'hésite pas à questionner mes acolytes pour t'éclaircir.

### Conditions
Les conditions sont aussi une partie importante dans l'informatique car elles permettent de "séparer" le programme. C'est essentiel quand on cherche à traiter certaines choses. Voyons cela dans cet exemple:

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
    2. `if a == 1:` Ici le mot clé `if` demande au programme "si `a` est égal à 1". Si c'est vrai alors il va éxécuter l'ensemble des lignes se trouvant à l'intérieur de la condition c'est à dire sur toutes les lignes avec une INDENTATION de plus que lui (les indentations sont les espaces mis devant une instruction, nous reparlerons de leur importance dans la suite de cette introduction). 
    3. `print("Hello")` Ici on demande au programme d'afficher `Hello` si la condition est vraie (dans notre cas cette ligne ne sera pas lue car `a` différent de 1).
    4. `if a == 2:` Ici on retrouve le mot clé `if` qui demande au programme "si `a` est égal à 2". Si c'est vrai alors il va exécuter les lignes avec une INDENTATION de plus que lui.
    5. `print("World")` Ici on demande au programme d'afficher `World` si la condition est vraie (dans notre cas cette ligne sera exécutée et affichera `World`).
    6. La ligne `heure = 14` initialise la variable `heure` avec la valeur 14.
    7. `if heure == 12:` Ici le mot clé de condition `if` demande au programme "si `heure` est égale à 12". Si c'est vrai alors il éxécutera les instructions à l'intérieur de la condition.
    8. `print("A table!")` Ici on demande au programme d'afficher `A table!` si la condition est vraie (dans notre cas cette ligne ne sera pas lue car `heure` est différente de 12)
    9. `else:` Ici le mot clé impose au programme d'éxécuter ce qui suit si aucune des conditions précédentes, celle précédée d'un `if`, a été satisfaite (dans notre cas on entrera dans le `else`). 
       On peut par ailleurs traduire le mot clé `else` par "sinon" (`if`: si oui, `else`: si non).
    10. `print("Pas tout de suite")` Ici on demande au programme d'afficher `Pas tout de suite` si on n'est pas entré dans la condition `if`. Attention on ne peut pas mettre de `else` si il n'y a pas de `if`.

Cette partie peut être compliquée mais n'hésite pas à questionner mes acolytes afin de ne pas rester perdu.

Revenons rapidement sur les explications de l'INDENTATION. L'INDENTATION est très importante en Python. Elle permet de faire comprendre au programme quand aller dans une partie d'un programme ou non.
Quand vous ferez votre programme plus tard, il sera sûrement nécessaire d'en utiliser. Pour se faire, l'INDENTATION est représentée par les 2 flèches ayant des sens opposés. Cette touche ce nomme tabulation, abrégé tab.

## Le Prolobot

C'est ici que les choses commencent enfin. On va maintenant t'apprendre à utiliser les fonctionnalités des petits robots que tu as devant toi. Durant cette deuxième partie n'hésite pas à essayer ton code sur les robots c'est tout l'enjeu de cet atelier.
Commençons par forward.

### Utiliser avec l'éditeur

<!-- NOTE: tuto pour l'editeur python du site microbit -->

Pour utiliser le robot, commence par télécharger le fichier donné.

Appuie ensuite sur le bouton 'Open...' en bas de l'écran puis 
choisis le fichier que tu viens de télécharger.
![]("img/open_button.png")

Appuie enfin sur le bouton a côté du nom du fichier et sélectionne 'Ajouter le
fichier' avant de valider.
![]("img/load_button.png")

Toutes ces étapes permet à l'éditeur de reconnaitre le robot.
Pour enfin l'utiliser, écris ces 2 lignes au début de ton fichier.

```py
from prolobot import *
bot = Prolobot()
```

La première ligne va permettre d'indiquer au programme que tu veux utiliser le
robot. La deuxième dit au programme de créer un robot appelé bot.
C'est lui que tu vas faire bouger.

### Avancer

Pour faire forward le robot, tu peux écrire `bot.forward()`.

Cette ligne va permettre d'activer les moteurs du robot.
> Attention : Cette instruction ne le fait pas arrêter ! Pour cela, il faut
> écrire `bot.stop()`

Tu peux également préciser la vitesse du robot en mettant un nombre entre 0 et 1
entre les parenthèses. Si tu ne précise pas, le robot ira à la vitesse 0,2.

Voici par exemple comment tu peux le faire forward.

```py
bot.forward()
sleep(1000)
bot.forward(0.5)
sleep(2000)
bot.stop()
```

#### Le sleep
L'instruction `sleep(Temps)` est une instruction pour mettre en pause le 
programme pour une duree de `Temps` milisecondes. 

Dans le programme au dessus, la ligne `sleep(1000)` va donc indiquer au programme 
qu'il doit attendre pendant 1000 millisecondes, soit 1 seconde.
Le robot va donc activer les moteurs, puis attendre 1 seconde et activer les
moteurs à la vitesse 0.5, puis il attends 2 secondes avant de s'arrêter.

Le robot peut aussi backward en écrivant `bot.reculer()`. Tout comme pour forward,
on peut préciser la vitesse des roues entre les parenthèses.


### Ca tourne

Faire forward le robot c'est bien, le faire turn c'est encore mieux. Pour se faire plusieurs méthodes existent: 
    `bot.rotate(direction,vitesse)`
    `bot.turn(direction,vitesse)`

Ces deux instructions ont deux paramètres mais seule l'instruction direction est obligatoire. C'est à dire:
    `bot.rotate(direction)` fonctionne et aura une vitesse mise par défaut à 0.2
    `bot.turn(direction)` fonctionne et aura aussi une vitesse mise à 0.2

Faisons une distinction, l'instruction `bot.turn(GAUCHE)` allume seulement le moteur de droite pour faire tourner le robot. `bot.tourner(DROITE)` fait la même chose mais allume le moteur de gauche.

Maintenant, l'instruction `bot.rotate(GAUCHE)` allume le moteur droite comme pour `bot.turn(GAUCHE)` cependant il allume aussi le moteur gauche mais dans le sens opposé à celui du moteur de droite. L'instruction `bot.pivoter(DROITE)` fait la même chose dans le sens inverse.

Je te donne un court programme pour essayer ce que je viens de t'expliquer:

```py
import prolobot
from microbit import *
bot = Prolobot()

bot.turn(DROITE)
sleep(1000)

bot.rotate(GAUCHE)
sleep(1000)

bot.turn(DROITE)
sleep(1000)

bot.rotate(GAUCHE)
sleep(1000)

bot.stop()
```

## Les Bonus
Voici maintenant la partie la plus amusante de cet atelier et le moment où c'est votre créativité qui va devoir parler.

### Les Leds
Sur ce petit robot, plusieurs leds sont configurables et sont mises à votre disposition pour pouvoir s'amuser. 
Au total le robot possède 6 leds:
    2 positionnées à l'avant (qu'on appellera dans cet atelier "Phare") qu'on utilise avec la commande:
        `bot.set_headlight(Phare,État)`
            `Phare` : DROITE (led avant droite) / GAUCHE (led avant gauche).
            `État` : 1 (pour allumer) / 0 (pour éteindre).
    4 positionnées en dessous qu'on utilise avec la commande:
        `bot.turn_on_led(Led, Couleur)`
            `Led` : correspond à un chiffre entre 0 et 3.
                0 : en haut à gauche.
                1 : en bas à gauche.
                2 : en bas à droite.
                3 : en haut à droite.
            `Couleur` : c'est un paramètre de la forme (rouge, vert, bleu) (aussi appelé rgb).
                Les valeurs de `rouge`, `vert` et `bleu` sont entre 0 et 255.
                (0,0,0) correspond au noir.
                (255,255,255) correspond au blanc.
        `bot.turn_off_led()` permet d'éteindre toutes les leds du dessous.

Voici quelques exemples:
    `bot.set_headlight(DROITE,1)` allume le phare de droite
    `bot.set_headlight(GAUCHE,0)` éteint le phare de gauche
    `bot.turn_on_led(0,(0,0,0))` allume la led en haut à gauche avec la couleur noire
    `bot.turn_on_led(2,(135,206,235))` allume la led en bas à droite avec la couleur bleue ciel
    `bot.turn_off_led()` éteint toutes les leds du dessous.

### Les boucles
Comme vous avez pu le remarquer, très souvent pour la même action on copie la même ligne plusieurs fois. Ou alors votre robot avance mais quand le programme a fini d'exécuter les lignes, il s'arrête. Pour pallier à ce probleme, il y a en programmation ce que on appelle des boucles. Les boucles permettent d'exécuter un nombre de fois précis une série instructions.
Prenons cet exemple:
```py
#Debut du programme

for i in range(5):
    bot.forward()
    sleep(1000)
    bot.stop()
    sleep(1000)

#Fin du programme
```
Ce court programme permet à notre robot d'forward pendant 1 seconde puis s'arrêter pendant 1 seconde et ce 5 fois avant de s'arrêter.

Une autre boucle existe mais celle-ci permet au programme de ne jamais s'arrêter c'est `while`
Prenons cet exemple:

```py
#Debut du programme

while True:
    bot.forward()
    sleep(1000)
    bot.stop()
    sleep(1000)

#Fin du programme
```
Ce programme ressemble beaucoup à celui d'avant hormis le fait que il ne sera pas répété 5 fois mais une infinité de fois.
`while True` peut se traduire pas "tant que vrai"

### Capteurs
Maintenant que tu sais manipuler les boucles, tu vas pouvoir t'amuser avec ton robot et ce grâce aux différents capteurs.
Les capteurs sont en bref des traductions du monde réel au monde numérique.
Il y 3 capteurs différents sur le robot:
    1 capteur de distance situé à l'avant qui permet de savoir la distance entre un objet et lui même.
        `bot.distance()` est l'instruction qui permet de renvoyer la distance entre le robot l'obstacle devant lui
    2 capteurs de ligne permettant de détecter les lignes sous le robot
        `bot.floor_sensor(capteur)` est l'instruction qui permet de savoir si le capteur GAUCHE ou DROITE détecte une ligne noire. Si il en détecte une, il renvoie True sinon il renvoie False (True se traduit par "Vrai" et False par "Faux")

### Conclusion
Voilà tu as maintenant toutes les cartes en main pour pouvoir t'amuser. Tu retrouveras en dessous un resumé de toutes les instructions qui sont mises à ta disposition.
Amuse toi bien !

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

`GAUCHE = 0`. A donner en parametre pour turn a gauche.
`DROITE = 1`. A donner en parametre pour turn a droite.

### Fonctions

#### Deplacement

`bot.forward()`: avance le robot.
- La vitesse par defaut est 0.2

`bot.forward(vitesse)`: avance a la vitesse donnee.
- La vitesse est un float entre 0 et 1.

`bot.backward()`: recule le robot.
- La vitesse par defaut est 0.2.

`bot.backward(vitesse)`: recule le robot a la vitesse donnee.
- La vitesse est un float entre 0 et 1.

`bot.turn(direction)`: tourne le robot dans la direction donnee. 
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction.

`bot.turn(direction, vitesse)`: tourne le robot dans la direction et a la vitesse donnee.
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction
- La vitesse est entre 0 et 1

`bot.rotate(direction)`: tourne le robot sur lui même dans la direction donnee. 
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction.

`bot.rotate(direction, vitesse)`: tourne le robot sur lui même dans la direction et a la vitesse donnee.
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction
- La vitesse est entre 0 et 1

`bot.stop()`: arrete le robot.

#### Capteurs

`bot.distance()`: renvoie la distance entre le robot et les obstacles en face de lui.

`bot.floor_sensor(sensor)`: renvoie 1 si le capteur detecte du noir.
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer quel capteur utiliser.

#### LEDs

`bot.set_headlight(led, status)`: allume ou eteint un des phares avant,
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer quel capteur utiliser.
- Le statut est a 1 pour allumer et 0 pour eteindre la led

`bot.turn_on_led(led, couleur)`: allume la led correspondante.
- La led est un entier de 0 a 3 servant a preciser la led a allumer
- La couleur est de la forme (rouge, vert, bleu), avec les couleurs allant de 0 a 255

`bot.turn_off_led()`: eteint toutes les leds
