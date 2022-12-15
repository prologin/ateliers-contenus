---
title: Prolobot
date: 2022
authors: Julie 'DaiF' Fiadino, Hippolyte Pik
subtitle: Codez avec le Robot Microbit
code_stub_url: "./prolobot.py"
---

## Introduction
Bonjour à toi jeune programmeuse, programmeur. Je me présente, je suis Joseph Marchand, et c'est moi qui t'accompagnerai au travers de cette découverte du monde de l'informatique durant cet atelier.
Avant de commencer, laisse-moi te présenter mes fidèles acolytes : les organisateurs. Ce sont eux qui t'accompagnent
aujourd'hui. Ils me remplacent car je suis très occupé en ce moment, mais si tu as une quelconque question, à n'importe quel moment, n'hésite surtout pas à leur demander de l'aide, ils sont là pour ça.
Je m'arrête là pour les présentations, et commençons cet atelier par une introduction du robot de cet atelier.

### Qu'est ce que c'est `microbit:maqueen` ?
Un `microbit` c'est un microcontrôleur de la taille d'une carte à jouer (indication: tu dois pouvoir voir le micro:bit à l'avant du robot). Et `maqueen` c'est le petit robot que tu as devant toi. `maqueen` c'est un robot qui est entièrement configurable avec avec un langage que l'on appelle le Python. Ce langage va être convertit en plein de petites instructions qui permettrons de diriger le robot.

## Le Prolobot

Entrons dans le vif du sujet. Dans cette partie, nous allons te montrer comment utiliser les petits robots maqueen.

### Utiliser avec l'éditeur

<!-- NOTE: tuto pour l'editeur python du site microbit -->

Pour utiliser le robot, commence par télécharger le fichier donné.

Appuie ensuite sur le bouton 'Open...' en bas de l'écran puis 
choisis le fichier que tu viens de télécharger.
{{<figure src="img/open_button.png" >}}

Appuie enfin sur le bouton à côté du nom du fichier et sélectionne 'Ajouter le
fichier' avant de valider.
{{<figure src="img/load_button.png" >}}

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

Pour faire avancer le robot, tu peux écrire `bot.forward()`.

Cette ligne va permettre d'activer les moteurs du robot.
> Attention : cette instruction ne le fait pas arrêter ! Pour cela, il faut
> écrire `bot.stop()`

Tu peux également préciser la vitesse du robot en mettant un nombre entre 0 et 2
entre les parenthèses, cette vitesse correspondant au nombre tours de roue par secondes.
Si tu ne précises pas, le robot ira à la vitesse 0.4.

Voici par exemple comment tu peux le faire avancer.

```py
bot.forward()
sleep(1)
bot.forward(1)
sleep(2)
bot.stop()
```

#### Le sleep
L'instruction `sleep(time)` est une instruction pour mettre en pause le 
programme pour une durée de `time` secondes. 

Dans le programme au-dessus, la ligne `sleep(1)` va donc indiquer au programme 
qu'il doit attendre pendant 1 seconde.  
Le robot va donc activer les moteurs, puis attendre 1 seconde et activer les
moteurs à la vitesse 100, puis il attend 2 secondes avant de s'arrêter.

Le robot peut aussi reculer en écrivant `bot.backward()`. Tout comme pour `bot.forward()`,
on peut préciser la vitesse des roues entre les parenthèses.


### Ca tourne

Faire avancer le robot c'est bien, le faire tourner c'est encore mieux. Pour se faire plusieurs méthodes existent: 
    `bot.rotate(direction, speed)`
    `bot.turn(direction, speed)`

Ces deux instructions ont deux paramètres mais seul `direction` est obligatoire. C'est-à-dire :
 - `bot.rotate(direction)` fonctionne et aura une vitesse mise par défaut à 0.4
 - `bot.turn(direction)` fonctionne et aura aussi une vitesse mise à 0.4

De plus deux variables te sont fournies: 
 - `LEFT` pour la direction gauche
 - `RIGHT` pour la direction droite

Faisons une distinction, l'instruction `bot.turn(LEFT)` allume seulement le moteur de droite pour faire tourner le robot.
Allumer le moteur de droite et éteindre le moteur de gauche va permettre au robot de tourner comme on le voit sur le schéma.
{{<figure src="img/maqueen_turn.png" >}}
`bot.turn(RIGHT)` fait la même chose mais allume le moteur de gauche.

Maintenant, l'instruction `bot.rotate(LEFT)` allume le moteur droite comme pour `bot.turn(LEFT)` cependant il allume aussi le moteur gauche mais dans le sens opposé à celui du moteur de droite. Les 2 roues avançant à la même vitesse, cela va permettre au robot
de tourner sur lui même.
{{<figure src="img/maqueen_rotate.png" >}}
L'instruction `bot.rotate(RIGHT)` fait la même chose dans le sens inverse.

Voici un court programme pour essayer ce que je viens de t'expliquer :

```py
import prolobot
from microbit import *
bot = Prolobot()

bot.turn(RIGHT)
sleep(1)

bot.rotate(LEFT)
sleep(1)

bot.turn(RIGHT)
sleep(1)

bot.rotate(LEFT)
sleep(1)

bot.stop()
```

## Les Bonus
Voici maintenant la partie la plus amusante de cet atelier et le moment où c'est votre créativité qui va devoir parler.

### Les Leds
Sur ce petit robot, plusieurs leds sont configurables et sont mises à votre disposition pour pouvoir s'amuser.  
Au total, le robot possède 6 leds :
   - 2 positionnées à l'avant (qu'on appellera dans cet atelier "Phare") qu'on utilise avec la commande : `bot.set_headlight(led, state)`
     - `led` : RIGHT (led avant droite) / LEFT (led avant gauche).
     - `state` : 1 (pour allumer) / 0 (pour éteindre).
   - 4 positionnées en dessous qu'on utilise avec la commande : `bot.turn_on_led(led, color)`
     - `led` : correspond à un chiffre entre 0 et 3.
        - 0 : en haut à gauche.
        - 1 : en bas à gauche.
        - 2 : en bas à droite.
        - 3 : en haut à droite.
     - `color` : c'est un paramètre de la forme (rouge, vert, bleu) (aussi appelé RVB).  
        Les valeurs de `rouge`, `vert` et `bleu` sont entre 0 et 255.  
        Le RVB est un systeme de couleur, qui permet à l'ordinateur de faire un mélange entre les couleurs pour obtenir la couleur voulu, comme en peinture avec les couleurs primaires !  
        Prenons l'exemple du Vert :  
        - En peinture on utilise du jaune et bleu.  
        - Et en systeme rvb on a simplement a mettre la valeur du vert à sa plus haute valeur : 255, et les autres valeurs à 0.  
        - Il faut voir le rvb comme une addition de couleur.  
        - Si on prend (r=0, v=0, b=0) l'addition d'aucune couleur, peut être identifié au noir.  
        - Si on prend (r=255, v=255, b=255) l'addition de toutes, peut être identifié au blanc.  
  - `bot.turn_off_led()` permet d'éteindre toutes les leds du dessous.

Voici quelques exemples :
  - `bot.set_headlight(RIGHT,1)` allume le phare de droite
  - `bot.set_headlight(LEFT,0)` éteint le phare de gauche
  - `bot.turn_on_led(0,(255,0,0))` allume la led en haut à gauche avec la couleur rouge
  - `bot.turn_on_led(2,(135,206,235))` allume la led en bas à droite avec la couleur bleu ciel
  - `bot.turn_off_led()` éteint toutes les leds du dessous.

### Les boucles
Comme vous avez pu le remarquer, très souvent pour la même action, on copie la même ligne plusieurs fois. Ou alors votre robot avance mais quand le programme a fini d'exécuter les lignes, il s'arrête. Pour pallier ce problème, il y a en programmation ce qu'on appelle des boucles. Les boucles permettent d'exécuter un nombre de fois voulu une série d'instructions. Pour cela on utilise la boucle `for`.
Prenons cet exemple :
```py
#Debut du programme

for i in range(5):
    bot.forward()
    sleep(1)
    bot.stop()
    sleep(1)

#Fin du programme
```
Ce court programme permet à notre robot d'avancer pendant 1 seconde puis s'arrêter pendant 1 seconde et ce 5 fois avant de s'arrêter.

Une autre boucle existe c'est `while`. Celle-ci permet au programme de continuer la boucle tant que la condition qui lui est donné est vraie.
`while` peut être traduit par "tant que".

Prenons cet exemple :

```py
#Debut du programme

while True:
    bot.forward()
    sleep(1)
    bot.stop()
    sleep(1)

#Fin du programme
```
Ce programme ressemble beaucoup à celui d'avant hormis le fait qu'il ne sera pas répété 5 fois mais une infinité de fois.
`while True` peut se traduire pas "tant que vrai"

### Capteurs
Maintenant que tu sais manipuler les boucles, tu vas pouvoir t'amuser avec ton robot et ce grâce aux différents capteurs.
Les capteurs sont en bref des traductions du monde réel au monde numérique.
Il y 3 capteurs différents sur le robot :
  - 1 capteur de distance situé à l'avant qui permet de connaître la distance entre un objet et lui-même.  
        `bot.distance()` est l'instruction qui permet de renvoyer la distance entre le robot l'obstacle devant lui
  - 2 capteurs de ligne permettant de détecter les lignes sous le robot  
        `bot.floor_sensor(capteur)` est l'instruction qui permet de savoir si le capteur LEFT ou RIGHT détecte une ligne noire. S'il en détecte une, il renvoie True sinon il renvoie False (True se traduit par "Vrai" et False par "Faux")

Ces valeurs Vrai ou Faux vont servir à faire quelque chose de très utile que l'on appelle les conditions.

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

Exécutons ce programme à la main :
  - La ligne `a = 2` initialise la variable `a` avec la valeur 2.
  - `if a == 1:` Ici le mot clé `if` demande au programme "si `a` est égal à 1". Si c'est vrai alors il va éxécuter l'ensemble des lignes se trouvant à l'intérieur de la condition c'est à dire sur toutes les lignes avec une INDENTATION de plus que lui (les indentations sont les espaces mis devant une instruction, nous reparlerons de leur importance dans la suite de cette introduction). 
  - `print("Hello")` Ici on demande au programme d'afficher `Hello` si la condition est vraie (dans notre cas cette ligne ne sera pas lue car `a` différent de 1).
  - `if a == 2:` Ici on retrouve le mot clé `if` qui demande au programme "si `a` est égal à 2". Si c'est vrai alors il va exécuter les lignes avec une INDENTATION de plus que lui.
  - `print("World")` Ici on demande au programme d'afficher `World` si la condition est vraie (dans notre cas cette ligne sera exécutée et affichera `World`).
  - La ligne `heure = 14` initialise la variable `heure` avec la valeur 14.
  - `if heure == 12:` Ici le mot clé de condition `if` demande au programme "si `heure` est égale à 12". Si c'est vrai alors il éxécutera les instructions à l'intérieur de la condition.
  - `print("A table!")` Ici on demande au programme d'afficher `A table!` si la condition est vraie (dans notre cas cette ligne ne sera pas lue car `heure` est différente de 12)
  - `else:` Ici le mot clé impose au programme d'éxécuter ce qui suit si aucune des conditions précédentes, celle précédée d'un `if`, a été satisfaite (dans notre cas on entrera dans le `else`).   
       On peut par ailleurs traduire le mot clé `else` par "sinon" (`if`: si oui, `else`: si non).
  - `print("Pas tout de suite")` Ici on demande au programme d'afficher `Pas tout de suite` si on n'est pas entré dans la condition `if`. Attention on ne peut pas mettre de `else` si il n'y a pas de `if`.

Cette partie peut être compliquée mais n'hésite pas à questionner mes acolytes afin de ne pas rester perdu.

Revenons rapidement sur les explications de l'INDENTATION. L'INDENTATION est très importante en Python. Elle permet de faire comprendre au programme quand aller dans une partie d'un programme ou non.  
Quand vous ferez votre programme plus tard, il sera sûrement nécessaire d'en utiliser. Pour se faire, l'INDENTATION est représentée par les 2 flèches ayant des sens opposés. Cette touche ce nomme tabulation, abrégé tab.

### Conclusion
Voilà tu as maintenant toutes les cartes en main pour utiliser les fonctionnalités du robot. Tu retrouveras en dessous un résumé de toutes les instructions qui sont mises à ta disposition.
Amuse-toi bien !

## La Doc

La doc répertorie toutes les fonctions qui permettent de contrôler le robot.

<!-- NOTE: La doc est temporaire, si elle reste ca sera juste a la fin pour
    en tant que recap -->

### Instantier le robot

```py
from prolobot import *

bot = Prolobot()
```

### Variables globales

`LEFT = 0`. A donner en parametre pour tourner à gauche.  
`RIGHT = 1`. A donner en parametre pour tourner à droite.

### Fonctions

#### Déplacement

`bot.forward()`: avance le robot.
- La vitesse par défaut est 0.4.

`bot.forward(vitesse)`: avance à la vitesse donnée.
- La vitesse est un nombre entre 0 et 2.

`bot.backward()`: recule le robot.
- La vitesse par défaut est 0.4.

`bot.backward(vitesse)`: recule le robot à la vitesse donnée.
- La vitesse est un nombre entre 0 et 2.

`bot.turn(direction)`: tourne le robot dans la direction donnée. 
- On peut utiliser les constantes `RIGHT` et `LEFT` pour indiquer la direction.

`bot.turn(direction, vitesse)`: tourne le robot dans la direction et à la vitesse donnée.
- On peut utiliser les constantes `RIGHT` et `LEFT` pour indiquer la direction
- La vitesse est entre 0 et 2

`bot.rotate(direction)`: tourne le robot sur lui-même dans la direction donnée. 
- On peut utiliser les constantes `RIGHT` et `LEFT` pour indiquer la direction.

`bot.rotate(direction, vitesse)`: tourne le robot sur lui-même dans la direction et à la vitesse donnée.
- On peut utiliser les constantes `RIGHT` et `LEFT` pour indiquer la direction
- La vitesse est entre 0 et 2

`bot.stop()`: arrête le robot.

#### Capteurs

`bot.distance()`: renvoie la distance entre le robot et les obstacles en face de lui.

`bot.floor_sensor(capteur)`: renvoie True si le capteur détecte du blanc.
- On peut utiliser les constantes `RIGHT` et `LEFT` pour indiquer quel capteur utiliser.

#### LEDs

`bot.set_headlight(led, status)`: allume ou éteint un des phares avant,
- On peut utiliser les constantes `RIGHT` et `LEFT` pour indiquer quel capteur utiliser.
- Le statut est à 1 pour allumer et 0 pour éteindre la led

`bot.turn_on_led(led, couleur)`: allume la led correspondante.
- La led est un entier de 0 à 3 servant à préciser la led à allumer
- La couleur est de la forme (rouge, vert, bleu), avec les valeurs des couleurs allant de 0 a 255

`bot.turn_off_led()`: éteint toutes les leds de couleur (situé en dessous du robot)
