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
leur propose de faire un chifoumi revisité... mais ils n'ont pas de mains,
donc ils ne peuvent pas mimer les symboles ! Skeleton a besoin de ton aide !
Il te demande de créer un programme leur permettant de jouer sur des `micro:bit` !
Peux-tu aider notre ami ?

Skeleton souhaiterait choisir un élément parmi trois choix sur un
`micro:bit` à l'aide des boutons. De plus, l'ordinateur devra ensuite choisir
à son tour un élément. Enfin, il faudra afficher le résultat. Les choix
seront les suivants : Skeleton, Pacman et Bouh !

Skeleton, faisant peur à Pacman, l'emporte contre lui. Pacman, quant à lui,
mange des fantômes, il gagne en toute logique contre Bouh. Bouh le fantôme voudra attraper
Skeleton, il gagnera donc contre notre ami le squelette.

{{<figure src="resources/images/all3.png" height=80% width=100% alt="Variable en Python">}}

Pour faire cela, nous allons t'aider à créer le code étape par étape.
Si tu as des questions particulières, n'hésite pas à demander à un
organisateur autour de toi, ils sont là pour ça !

## Mais dis-moi Jamy, c'est quoi un `micro:bit` ?

Les `micro:bit` sont des cartes programmables qu'on te fournit tout
au long de l'atelier. Avec celles-ci, tu vas pouvoir interagir avec ses
composants. Les 25 LEDs au milieu ou les boutons en sont des exemples.

{{<figure src=resources/images/microbit.png height=50% width=50% alt="Micro:bit">}}

Nous verrons un peu plus tard comment manipuler les `micro:bit`.


# Programmer en Python

Pour pouvoir créer notre jeu pour Skeleton, il va te falloir quelques connaissances
en Python. En programmation, les intructions sont lues ligne par ligne.
Chaque instruction est décrite sur une ligne. On va alors t'aider à écrire ses lignes.
Si tu as la moindre question, n'hésite pas à la poser à un organisateur !

## Les variables en Python

La plupart du temps, nous avons besoin de stocker des informations dans notre code.
On parle alors de variables. Elles permettent de ranger des choses
et de pouvoir les ressortir quand on le souhaite. Ce sont des éléments qui
associent un nom à une valeur. C'est comme si on utilisait des boîtes pour
ranger des éléments !

{{<figure src="resources/images/variable.png" height=25% width=25% alt="Variable en Python">}}

Pour déclarer une variable en Python, on procède de la sorte :

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

*C'est quoi les lignes qui commencent par un `#` ?*

Les lignes commençant par des `#`, ce sont des commentaires. Cela te permet
d'expliquer ton code par des phrases pour toi ou même pour les personnes qui
t'entourent. Python ne prend pas en compte les commentaires dans son exécution.

## Les booléens en Python

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

## Les conditions en Python : si, sinon si, sinon

Prenons un exemple, si Skeleton mange, il n'aura plus faim pour une glace.
Le début de cette phrase est une condition, qu'on peut identifier à l'aide
du mot "si". La condition ici est : Skeleton mange. Elle peut être vraie ou fausse.

{{<figure src="resources/images/conditions.png" height=75% width=75% alt="Conditions en Python">}}

C'est la même chose en Python. On va pouvoir définir des conditions qui
s'évaluent à vrai ou faux et exécuter des lignes de code en conséquence.
Le mot-clé "si" va être remplacé par son équivalent en anglais, `if`.

```python
# Vérifie si 1 est égal à 1
if 1 == 1:
    # Affiche dans la console "Skeleton est trop fort !"
    print("Skeleton est trop fort !")

# Sinon
else:
    # Affiche dans la console "Pacman est trop fort !"
    print("Pacman est trop fort !")
```

Parfois, il va falloir que tu vérifies si deux conditions sont vérifiées en
même temps. On va alors parler du mot-clé `and` qui signifie "et" en français.

En voici un exemple :

```python
a = 5

# Vérifie si 42 est inférieur à 50 et si a est égal à 5
if 42 < 50 and a == 5:
    # Affiche dans la console "Pacman aime les chats !"
    print("Pacman aime les chats !")
```

De plus, tu pourras avoir l'occasion de chercher le contraire d'une expression.
Par exemple, si Skeleton ne travaille pas aujourd'hui, il aura du mal pour son
contrôle. Ici, on a une négation, et la négation en Python se traduit comme suit :

```python
# `ma_condition` est évaluée à `False` car 42 n'est pas égal à 0
ma_condition = 42 == 0

# Si `ma_condition` n'est pas vraie (si `ma_condition` est fausse)
if not ma_condition:
    print("Bouh aime les carottes")
```

*Mais pourquoi on rajoute des espaces avant les lignes ?*

Python suit ligne par ligne ton programme, donc pour lui expliquer ce que tu veux
faire sous certaines conditions, il faut rajouter des espaces avant les lignes
pour créer des blocs. On parle alors d'indentation. Pour faire ça, on va utiliser
la touche de tabulation (`Tab`) sur ton clavier. Cela permet à Python de
savoir quand est-ce qu'il faut sortir du bloc pour s'arrêter.

On peut également utiliser les mots-clés "sinon" et "sinon si". Un petit exemple
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

# Si les conditions au-dessus ne sont pas vérifiées, je fais cette partie
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
il y a deux types de boucles ; cependant, dans cet atelier, seul un type
nous suffira : les boucles `while`.

On peut traduire `while` par "tant que" en français. On va pouvoir utiliser
les conditions dans les boucles `while` pour pouvoir répéter des choses
tant qu'une condition est toujours vraie. Par exemple, tant que le bébé dort,
nous ne devons pas faire de bruit.

Un exemple serait celui-ci :

```python
i = 0
# Tant que i est inférieur à 3
while i < 3:
    # Afficher "Bonjour !"
    print("Bonjour !")

    # Ajouter 1 à i à chaque tour de boucle
    i = i + 1
```

## Les listes en Python

Lorsqu'on veut stocker de nombreuses valeurs pour pouvoir les réutiliser
par la suite, on ne va pas créer par exemple 20 variables.
Ce qui sera plus pratique pour nous, ce sont les listes. Les listes vont
nous permettre de stocker plusieurs valeurs dans une seule variable.

{{<figure src="resources/images/liste.png" height=80% width=80% alt="Liste en Python">}}

Par exemple,

```python
# Liste de lettres
ma_liste_lettres = ["a", "b", "c", "d"]
```

Tu peux accéder aux éléments d'une liste à l'aide de l'indice. Ce sont des nombres
qui désignent l'emplacement de la case que tu veux regarder. Attention,
en programmation, les indices commencent à 0. Si on nomme la longueur de la liste `l`,
les indices peuvent prendre des valeurs entre `0` et `l - 1`.

En Python, pour accéder à un élément à l'indice 2, tu peux faire comme ceci :

```python
# Liste de lettres
ma_liste_lettres = ["a", "b", "c", "d"]

# `ma_variable` est l'élément à l'indice 2 de `liste` ("c")
ma_variable = ma_liste_lettres[2]

# Affiche `ma_variable` dans la console
print(ma_variable)
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
cela, il faut alors donner deux nombres, qui formeront l'intervalle dans lequel on
veut générer le nombre aléatoire. Par exemple, avec un dé, les valeurs que l'on 
peut obtenir sont sur l'intervalle [1; 6].

Afin de générer notre nombre aléatoire, il va d'abord falloir importer
une bibliothèque. Cela va nous permettre d'utiliser des fonctions déjà écrites
dans la bibliothèque. Ici, on va juste utiliser la fonction `randint` de la
bibliothèque `random`.

Si tu ne connais pas les fonctions, il faut les considérer comme des machines
dans lequelles on entre des valeurs et qui nous en ressortent d'autres. Elles vont
travailler sur nos entrées pour ressortir un élément.

```python
# Importe la bibliothèque pour générer des nombres aléatoires
from random import randint

# `ma_variable` va contenir une valeur aléatoire comprise entre 0 et 4 inclus
# Les valeurs possibles sont alors : 0, 1, 2, 3 et 4
ma_variable = randint(0, 4)

# Affiche `ma_variable` dans la console
print(ma_variable)
```

N'hésite pas à relancer plusieurs fois ton code pour avoir un autre nombre
généré.

### Exercice 3

Bouh, le fantôme, n'arrive pas à faire de choix de ce qu'il veut manger à midi.
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

Les LEDs d'un `micro:bit` peuvent soit s'allumer, soit s'éteindre de manière
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
la bibliothèque des `micro:bit`. Tu peux retrouver la liste des images
disponibles [ici](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html).

Pour afficher du texte ou des nombres, tu vas pouvoir utiliser la fonction
`display.scroll()`.

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *

# Affiche "Chifoumicro:bit" sur le micro:bit
display.scroll("Chifoumicro:bit")
```

Avec la dernière fonction, `display.scroll()`, tu peux changer la vitesse
d'affichage avec l'argument `delay=nb` avec `nb` la vitesse. La valeur est
à l'origine à 150. Ainsi, si tu donnes un nombre plus petit que 150, ton
texte ira plus vite que par défaut.

```python
# Affiche "Je vais vite !" sur le micro:bit avec une vitesse de 50
display.scroll("Je vais vite !", delay=50)
```

### Exercice 4

Pour voir si tu as bien compris comment on manipule les images, Skeleton
souhaiterait que tu affiches un cœur (heart en anglais) sur ton `micro:bit`.

### Mais il y a des boutons à côté des LEDs !

À côté des 25 LEDs du `micro:bit`, tu peux retrouver à gauche, le bouton A,
et à droite, le bouton B. Pour connaître le nombre d'appuis sur les boutons,
tu peux utiliser les fonctions `button_a.is_pressed()` et `button_a.was_pressed()`.
Tu peux retrouver les mêmes fonctions pour le bouton B juste en remplaçant
`button_a` par `button_b`.

Essaye les codes suivants pour comprendre la différence entre les deux fonctions !
Si tu as une question, n'hésite pas à appeler un organisateur !

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

# Met en pause le programme pour laisser du temps à l'utilisateur
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

`sleep(200)`, permet de mettre en pause le programme pendant ici, 200 millisecondes.
Cela te laisse le temps d'appuyer sur les boutons. Il peut alors vérifier si
tu as appuyé sur les boutons pendant ce laps de temps.

### Exercice 5

Pour tester si le `micro:bit` fonctionne bien, Skeleton voudrait que lorsqu'on
appuie sur les deux boutons en même temps, l'image sourire s'affiche.
Aide-le en créant le programme !


# Passons à la pratique !

Il va falloir maintenant que tu écrives le programme pour Skeleton ! Ne t'inquiète
pas, nous allons te guider pour rédiger ton code ! Si tu as la moindre question,
n'hésite pas à la poser aux organisateurs présents !

Nous t'invitons d'abord à télécharger le code source à modifier en cliquant
sur le bouton `Code à compléter` en haut de la page ! Tu retrouveras dans
le fichier donné un code non complet que tu ne peux pas encore lancer. Il va
falloir le remplir avec tes nouvelles connaissances.

## Les possibilités d'affichage et le choix de l'ordinateur

Dans la variable `possibilites`, il faut que tu rajoutes une liste de toutes
les images possibles que tu devras afficher à l'écran. Les images qui doivent
apparaître sont `Image.SKULL` (pour Skeleton), `Image.PACMAN` (pour Pacman)
et `Image.GHOST` (pour Bouh).

Tu vas devoir également trouver la longueur de ta liste `possibilites`
(avec une fonction que l'on a vu précédemment). Tu dois mettre ce nombre
dans la variable `NB_POSSIBILITES`.

Le choix de l'ordinateur doit se faire de manière aléatoire. La valeur de la
variable `choix_adversaire` doit être un nombre compris entre 0 et la longueur
de ta liste `possibilites` moins 1.

## La boucle du jeu pour la sélection du personnage

### La condition de la boucle

L'utilisateur du `micro:bit` doit choisir son personnage. Pour faire cela,
on va utiliser une boucle `while` (tant que). Il va falloir alors trouver
une condition pour rester dans la sélection. Pour valider, le joueur devra
appuyer sur les deux boutons du `micro:bit` en même temps.

Dans la condition de ta boucle, il faut vérifier si les boutons A et B ne
sont pas pressés. Tu vas devoir alors utiliser le `and` et le `not` que
nous avons vu précédemment.

### Afficher le choix du joueur

Tant qu'on reste dans notre boucle `while`, il va falloir afficher le choix
qui est actuellement sélectionné. Pour ce faire, tu peux utiliser la fonction
`display.show()` avec comme paramètre l'image dans la liste `possibilites` à
l'indice du choix du joueur défini par la variable `choix_joueur`.

### Appuis sur les boutons

Si le bouton A a été appuyé, il faut enlever 1 au nombre désignant le choix du
joueur. Par la suite, sur ce nouveau nombre, il te faut rester dans l'intervalle
des indices de notre liste `possibilites`. Il va alors falloir rajouter un `%`
(modulo) !

*Un modu-quoi ?*

Le modulo, il faut le prendre comme le reste d'une division euclidienne.
Par exemple, quand tu souhaites diviser 5 par 2, tu auras le quotient qui est
égal à 2 et le reste qui est égal à 1.

On va utiliser le même procédé. On ne peut pas accéder au cinquième élément
d'une liste de longueur 3. On va donc revenir à 0 lorsqu'on dépasse la liste.

Par exemple, lorsque tu es à l'indice 3 dans une liste de longueur 3 : les indices
possibles sont 0, 1 et 2. On voudrait que revenir à l'indice 0. En Python,
tu peux le faire comme ceci :

```python
# Une liste de nombres
ma_liste = [42, 56, 98]

# On est à l'indice 3
mon_indice = 3

# Le nouvel indice est 3 modulo 3 = 0
# car le reste de la division euclidienne de 3 par 3 est égal à 0
mon_nouvel_indice = 3 % 3

# L'élément à l'indice 0 (3 % 3)
mon_element = ma_liste[mon_nouvel_indice]

# Affiche `mon_element`
print(mon_element)
```

Il faut maintenant que tu fasses la même chose pour le bouton B, seulement,
cette fois-ci, si le bouton B a été appuyé, il faut rajouter 1 au nombre
désignant le choix du joueur. N'oublie pas le modulo !

## Aficher le choix du joueur

Comme pour le début de la boucle, il faut que tu réaffiches le choix du joueur
après le `display.clear()` qui éteint tous les pixels.

Après l'affichage du texte "VS", il faut que tu affiches maintenant le choix
de l'adversaire en prenant une image dans la liste `possibilites` à l'indice
`choix_adversaire`.

## Gagnant et perdant

Il faut maintenant trouver qui a gagné et qui a perdu ! Pour ce faire, on
va d'abord vérifier s'il y a égalité entre les deux joueurs.

Il y a égalité entre les deux joueurs dans notre jeu quand le choix de
notre adversaire et le même que le nôtre. Il faut alors vérifier l'égalité
entre `choix_joueur` et `choix_adversaire`. Il faut alors afficher sur le
`micro:bit` "Egalite !" avec une vitesse d'affichage de 50.

Sinon, s'il n'y a pas égalité, il faut vérifier les conditions pour savoir
si on a gagné. Atention, il faudra alors afficher "Gagne !" avec une vitesse
d'affichage de 50. Les conditions sont les suivantes :

- Si `choix_joueur` est égal à 0 et `choix_adversaire` est égal à 1
(Skeleton fait peur à Pacman)

- Si `choix_joueur` est égal à 1 et `choix_adversaire` est égal à 2
(Pacman mange Bouh)

- Si `choix_joueur` est égal à 2 et `choix_adversaire` est égal à 0
(Bouh fait peur à Skeleton)

Enfin, sinon, si toutes les conditions au-dessus ne sont pas remplies,
cela veut dire que tu as perdu et il faut que tu affiches "Perdu..." avec
une vitesse d'affichage de 50.


# Un mode multijoueur ?

Bien joué, tu as terminé la partie principale de ce TP, et tu as maintenant un
chifoumi complètement fonctionnel pour aider notre ami Skeleton.
Comme c'est un très bon ami, nous nous sommes dit qu'il serait sympa de lui
ajouter une fonctionnalité surprise : un mode multijoueur.

Avant de commencer cette partie, il faut que ton programme fonctionne et que tu
aies compris tout ce que nous t'avons expliqué plus tôt.
Si tu as une quelconque question ou qu'il y a quelque chose que tu n'as pas
compris, n'hésite pas à demander de l'aide aux organisateurs.

## Un peu de théorie

Pour faire un jeu multijoueur, nous allons avoir besoin de faire communiquer les
`micro:bit` ensemble. Pour ce faire, nous allons utiliser la radio.

Avant tout, tout comme la première partie, il faut importer les fonctions
pré-écrites en ajoutant cette ligne au début de ton fichier :

```py
import radio
```

## Choix du mode de jeu

Pour commencer, nous voulons que Skeleton puisse s'entraîner contre
l'ordinateur, ou bien jouer en multijoueur avec ses amis.
Pour stocker le mode de jeu choisi, nous allons utiliser une variable,
que nous appelerons `multijoueur`.
Cette variable va prendre trois états différents :
- `-1` si le joueur n'a pas encore fait son choix
- `0` si le joueur veut jouer contre l'ordinateur (mode _local_)
- `1` si le joueur veut jouer avec ses amis (mode _multijoueur_)

Par ailleurs, le joueur veut aussi savoir quand est-ce qu'il doit choisir son
mode de jeu. Pour faire ça, il nous suffit d'afficher l'image `Image.SWORD`
(_épée_ en anglais). N'importe quelle image fonctionnerait, le principe est de
montrer au joueur que notre programme attend son choix.

Ensuite, il faut attendre que le joueur fasse son choix et enregistrer son
choix.
Tu peux utiliser une boucle qui s'arrête lorsque le joueur a fait son choix.
Par convention, on dira qu'un appui sur le bouton A activera le mode
_multijoueur_, et un appui sur B activera le mode _local_.

## Choix de l'ordinateur

Ici, une toute petite modification est nécessaire pour le choix de l'ordinateur.
En effet, le `micro:bit` doit faire un choix seulement si le programme est en
mode _local_.

## Ton choix

En ce qui concerne ton propre choix, tu n'as rien besoin de changer.

## Et l'adversaire ?

Si le mode choisi est _multijoueur_, juste après avoir fait notre choix,
nous allons devoir l'envoyer à l'adversaire, et recevoir le sien.

### Activons la radio

Avant de pouvoir envoyer ou recevoir des informations, nous devons allumer et
configurer la radio. Pour ce faire, nous devons l'allumer et choisir un canal
de communication. Un canal de communication, est un peu comme un tunnel. Si les
deux joueurs ont des canaux différents, alors ils ne pourront pas s'entendre.

```py
# Allume la radio
radio.on()

# Configure la radio pour communiquer sur le channel 42
# Tu peux changer 42 par une valeur entre 0 et 83 si besoin
radio.config(channel=42)
```

Pour montrer au joueur que tout s'est bien passé jusqu'ici, tu peux afficher une
image de ton choix (toutes les images sont disponibles
[ici](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html)).


### Envoi et réception du message

Avant de recevoir le message, nous avons besoin d'une variable pour le stocker.
Nous allons nommer cette variable `message_adversaire` par la suite pour s'y
retrouver. Nous allons aussi lui associer une valeur un peu particulière :
`None` (_rien_ en français). Cette valeur veut dire _"Il n'y a rien dans
cette variable"_, tout simplement.

Pour essayer de recevoir un message, il faut faire :

```py
# `message_adversaire` vaudra None si aucun message n'est reçu
message_adversaire = radio.receive()
```

Pour envoyer un message, il faut faire :

```py
radio.send(str(choix_joueur))
```

#### C'est quoi ça, `str()` ?

C'est quelque chose que nous n'avons pas abordé, mais toute de même important.
En effet, les variables sont _typées_. Cela veut dire qu'elles ne peuvent stocker
qu'un type de valeur : des nombres entiers, du texte, des nombres décimaux...
La fonction `str(entier)` permet simplement de convertir le nombre entier _`entier`_
en texte. Le texte peut être différencié des nombres entiers par la présence
de simple guillemets (`'`) ou double guillemets (`"`).

Par exemple :
```python
entier = 12
texte = str(entier)

# Affiche le texte "12"
print(texte)
```

Pour convertir un texte en nombre entier, il faut utiliser la fonction `int()`,
qui fonctionne de la même façon :

```python
texte = "12"
entier = int(texte)

# Affiche le nombre entier 12
print(entier)
```

Cette partie est un peu complexe, si jamais tu n'as pas compris quelque chose,
n'hésite pas à demander de l'aide aux organisateurs.

Nous voulons donc que tant qu'aucun message n'est reçu, on envoie notre choix
et on essaye de recevoir celui de l'adversaire.

### J'ai reçu son choix !

Une dernière étape pour ce qui concerne le multijoueur est de convertir le choix
de l'adversaire en nombre entier et le stocker dans la variable `choix_adversaire`
afin de pouvoir l'utiliser par la suite.

Une fois que l'utilisation de la radio est terminée, pense à l'éteindre avec la
fonction :

```py
radio.off()
```

## Afficher le résultat

Tu n'as normalement pas besoin de modifier la fin de ton code, il devrait
afficher correctement ton choix et celui de l'adversaire.

Si jamais tu as une question ou un problème, n'hésite pas à demander de l'aide
aux organisateurs.

# C'est la fin

Bien joué, tu as réussi à faire un mode _multijoueur_ dans ton programme !
