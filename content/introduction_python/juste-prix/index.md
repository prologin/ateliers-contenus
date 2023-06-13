---
title: Introduction au Python - Juste Prix
date: 2022
authors: Dorian 'renji' Péron, Gaëtan 'Downvot_ED' Mouisset, Clarisse 'Nyota' Blanco
subtitle: Code ton jeu du juste prix
tags:
    - Python
---
# Introduction au Python - Juste Prix

Bonjour et bienvenue sur cet atelier d'introduction au Python !

## Objectifs

Au cours de cette initiation au langage Python, tu vas te familiariser avec les concepts suivants :

- Afficher du texte
- Récupérer et utiliser le texte entré par l’utilisateur
- Utiliser des variables pour stocker des informations
- Faire des calculs et comparer des nombres avec les opérateurs
- Exécuter du code sous certaines conditions
- Exécuter du code en boucle

## Qu'est-ce que Python ?

Python est un langage de programmation créé en 1991 par Guido van Rossum. Il existe des centaines de langages de programmation, avec des vocabulaires différents, mais tous partagent un point commun : l’utilisation de phrases. En informatique, nous appelons ces phrases des **instructions**. Une instruction est tout simplement une consigne que l'on fait exécuter à l'ordinateur.

Ces instructions sont écrites par un programmeur dans un fichier texte que l'on appelle le **code source**. Le code source consiste en une **succession d'instructions** (un **programme**) qui sont interprétées et exécutées par l'ordinateur. Pour un fichier Python, il faut un nommage spécifique. L'extension du fichier sera "py" : `fichier.py` par exemple.

Le Python est un des langages les plus populaires aujourd'hui. Il est utilisé dans pratiquement tous les domaines tels que le développement web, l'intelligence artificielle, ou encore la science des données. On l'utilise aussi parfois pour faire des jeux, et c'est ce que tu vas faire aujourd'hui !

## Quelques notions pratiques
Cette section te montre les fonctionnalités de Python qui te seront utiles pour créer ton jeu par la suite. N’hésite pas à essayer par toi-même les exemples donnés pour voir comment ça fonctionne ! Si tu ne comprends pas une partie, demande de l’aide aux organisateurs.

### Afficher du texte

Un langage de programmation nous permet de faire beaucoup de choses, mais nous voulons que nos programmes puissent nous parler si nécessaire. Tu peux lancer le programme suivant en cliquant sur _"Run"_ et observer le résultat !

```codepython
print("Hello world!")
```

Ici, notre programme est constitué d'une seule instruction : il s'agit d'un *print* (“imprimer” en anglais). Cela permet d'afficher à l'écran le texte spécifié entre les guillemets. C’est très pratique pour informer l’utilisateur du programme de toute sorte de choses.
Tu peux écrire ta propre instruction `print` sur la ligne suivante afin d'afficher le texte de ton choix. Il ne faut pas oublier les guillemets !

En lançant le programme, tu peux voir que les phrases sont affichées dans l'ordre dans lequel tu les as écrites. En effet, en Python, les instructions sont exécutées les unes à la suite des autres.

### Lire / récupérer du texte

Maintenant que tu sais écrire du texte à l'écran, il serait intéressant d'avoir un moyen d'intéragir avec l'utilisateur du programme.

Une manière de faire cela est d'utiliser l'instruction *input* (“entrée” en anglais). Celle-ci permet au programme de récupérer du texte entré par l'utilisateur.

```codepython
input("Comment t'appelles-tu ?")
```

Tout comme pour *print*, il est possible de spécifier du texte qui sera affiché à l'écran.

Tu peux lancer le programme et répondre à la question. Il faut ensuite appuyer sur la touche “Entrée” pour valider.
Pour l’instant, ton programme ne fait rien de la réponse qu’on lui donne. Afin de la sauvegarder, il est nécessaire de la **stocker** dans une **variable**.

### Variables

Une **variable** est un élément qui associe un nom à une valeur. Elle peut prendre un type parmi cette liste :

- Un nombre entier : `ma_variable = 5`
- Une chaîne de caractères : `ma_variable = "bonjour !"` (on reconnait une telle variable grâce aux guillemets)
- Un nombre à virgule : `ma_variable = 1.05` (on utilise un point et non une virgule)
- Un booléen : `ma_variable = True` (deux valeurs possibles : `True` ou `False`, vrai ou faux, bien penser à mettre la majuscule !)

**Attention :** Il ne faut pas mélanger les types : `ma_variable = 5` est le nombre entier 5 tandis que `ma_variable = "5"` est une chaîne de caractères contenant le chiffre 5. Par contre, c'est utile de pouvoir passer de l'un à l'autre, et très simple à faire :

```py
mon_nombre = 5
ma_chaine = str(5)

mon_autre_chaine = "4"
mon_autre_nombre = int(4)
```

Les instructions `int` et `str` permettent de transformer le type d'une variable en un autre.

Tu peux maintenant stocker la réponse à une instruction `input` dans une variable :

```py
prenom = input("Comment t'appelles-tu ?")
```

Ici, nous associons le texte rentré par l'utilisateur dans une variable que nous nommons `prenom`. Nous aurions très bien pu nommer cette variable autrement (à condition de ne pas mettre d’espace, ni de "-" dans le nom, ni de numéro au début du nom de la variable). En revanche, il est une bonne pratique d'utiliser un nom simple et explicite qui facilite la lecture du code pour les autres programmeurs.

Pour afficher le contenu de la variable `prenom` tu peux utiliser à nouveau l'instruction `print`. Attention cette fois-ci à ne pas mettre de guillemets, comme ceci :

```codepython
prenom = input("Comment t'appelles-tu ?")
print(prenom)
```

Le texte que tu as rentré s'affiche maintenant à l'écran.

À présent, reprenons notre exemple :

```codepython
prenom = input("Comment t'appelles-tu?")
print("Tu t'appelles", prenom)
```

Si tu lances ce programme et réponds à la question, tu verras que le contenu de la variable `prenom` s'est rajouté à la suite de la chaîne de caractères "Tu t'appelles".

**Info :** Dans une instruction `print`, la virgule permet d'afficher plusieurs éléments les uns à la suite des autres en les séparant par un espace.

### Les opérateurs

Les opérateurs sont une notion essentielle en informatique, on les retrouve dans tous les langages de programmation. Comme leur nom l'indique, les opérateurs permettent de réaliser des opérations, aussi bien mathématiques que logiques.

En Python, les principaux opérateurs dont tu auras besoin sont les suivants : `+`, `-`, `*`, `/`, `//`, `==`, `!=`, `>`, `<`, `<=`, `>=`, `and`, `or`, `not`. Leur fonctionnement est expliqué en-dessous.

#### **Les opérateurs mathématiques**

Ce sont les opérateurs les plus simples à comprendre. Il manipulent des nombres. Pour chacun des opérateurs dans le tableau, tu peux vérifier le fonctionnement en tapant :

```py
print(exemple)
```

puis en comparant le résultat de ton programme et celui du tableau.

|Opérateur|Exemple|Resultat|
|---|---|---|
|Addition :`+`|`5 + 5`|`10`|
|Soustraction : `-`|`10 - 5`|`5`|
|Multiplication : `*`|`5 * 5`|`25`|
|Division : `/`|`6 / 4` <br/> `9 / 3`| `1.5` <br/> `3`|
|Division euclidienne : `//`|`6 // 4` <br/> `9 // 3`|`1` <br/> `3`|

```codepython
# Addition
print(5 + 5)

# Soustraction
print(10 - 5)

# Multiplication
print(5 * 5)

# Division
print(6 / 4)

# Division euclidienne
print(6 // 4)
```

#### **Les opérateurs de comparaison**

Les opérateurs de comparaison permettent de comparer deux nombres, et renvoient une valeur booléenne (vrai ou faux). Comme pour les opérateurs mathématiques, tu peux expérimenter le fonctionnement de ces opérateurs directement dans ton programme.

|Opérateur|Exemple|Résultat|
|---|---|---|
|Égal : `==`| `5 == 5` <br/> `1 == 2`|`True` <br/> `False`|
|Inégal : `!=`|`1 != 2` <br/> `5 != 5`|`True` <br/> `False`|
|Supérieur :`>`|`2 > 1` <br/> `1 > 2`|`True` <br/> `False`|
|Inférieur :`<`|`1 < 2` <br/> `2 < 1`|`True` <br/> `False`|
|Supérieur ou égal :`>=`|`5 >= 5` <br/> `2 >= 5`|`True` <br/> `False`|
|Inférieur ou égal :`<=`|`4 <= 4` <br/> `4 <= 3`|`True` <br/> `False`|

```codepython
# Egal
print(5 == 5)
print(1 == 2)

# Inegal
print(1 != 2)
print(5 != 5)

# Superieur
print(2 > 1)
print(1 > 2)

# Inferieur
print(1 < 2)
print(2 < 1)

# Superieur ou egal
print(5 >= 5)
print(2 >= 5)

# Inferieur ou egal
print(4 <= 4)
print(4 <= 3)
```

#### **Les opérateurs logiques**

Les opérateurs permettent de combiner des valeurs booléennes (vrai ou faux), et de renvoyer un autre booléen dont le résultat dépend de l'opération choisie. Voici les plus utiles :

|Opérateur|Description|Exemple|Résultat|
|---|---|---|---|
|ET : `and`|Renvoie vrai si <br/> les valeurs à gauche et <br/> à droite sont vraies |`True and False` <br/> `False and True` <br/> `False and False` <br/> `True and True`| `False` <br/> `False` <br/> `False` <br/> `True`|
|OU : `or`|Renvoie vrai si <br/> au moins un des deux <br/> est vrai|`True or False` <br/> `False or True` <br/> `False or False` <br/> `True or True`|`True` <br/> `True` <br/> `False` <br/> `True`|
|NON : `not`|Renvoie l'inverse <br/> de ce qu'on lui donne|`not True` <br/> `not False`|`False` <br/> `True`|

```codepython
# ET
print(True and False)
print(False and True)
print(False and False)
print(True and True)

# OU
print(True or False)
print(False or True)
print(False or False)
print(True or True)

# NON
print(not True)
print(not False)
```

#### **Utilisation des opérateurs avec les conditions**

Grâce à ces opérateurs, il est possible de créer des **conditions** capables de vérifier si une expression est vraie ou fausse. Voici un exemple :

```codepython
if 10 > 0:
    print("C'est vrai")
else:
    print("C'est faux")
```

Si l'affirmation écrite après `if` est vraie, alors Python va exécuter le code après le `if`. Sinon, il exécutera le code après le `else`.

Il est également possible de mettre plusieurs conditions à la suite avec le mot clé `elif`, qui est une contraction de "else if", et qu'on traduirait en français par "sinon, si ...".

```codepython
if 14 < 13:                         # Si 14 est inférieur à 13,
    print("14 < 13 est vrai")       # On fait ceci !
elif 5 != 3:                        # Sinon, si 5 est différent de 3,
    print("5 != 3 est vrai")        # On fait cela !
else:                               # Sinon,
    print("Les conditions précédentes sont fausses") # On fait ça
```

**Attention :** Quand tu utilises ces mots clés, il faut faire attention à bien *indenter* les instructions qui sont concernées ensuite. Cela veut dire qu'il faut les décaler à droite, en utilisant un symbole *tabulation*. Tu peux écrire ce symbole en appuyant sur la touche au dessus de *verrouillage majuscule* sur ton clavier.

N'hésite pas à exécuter les exemples pour mieux comprendre. Tu peux aussi changer les conditions pour voir si le comportement est différent.

Il est également possible de créer des expressions mathématiques avec ces opérateurs.

```codepython
nombre = 5
somme = (nombre - 2) * 3
```

Dans cet exemple, la variable `somme` contient le nombre `9`. Comprends-tu pourquoi ?

Avec ces notions de base, tu vas pouvoir te lancer dans la réalisation du jeu du juste prix !

## Le jeu du juste prix

**But du jeu :** le but du jeu du Juste Prix est de faire deviner un nombre entre 1 et 1000 au joueur. Le joueur commence en entrant un nombre dans le programme. Le programme doit répondre “Plus” si le nombre est plus petit que celui à deviner ou “Moins” s’il est plus grand. Le joueur peut alors continuer à entrer des nombres jusqu’à trouver le bon. Finalement, le score du joueur correspond au nombre de fois où il a rentré une réponse.

Pour cela, nous pouvons décomposer notre programme en plusieurs étapes.

### Choisir un nombre entre 1 et 1000

Pour générer un nombre aléatoire en Python, des programmes sont déjà existants. Ainsi, il faut ajouter le programme déjà existant à notre code. Cela se fait en rajoutant au début de notre fichier la ligne suivante :  `import random`.

Ensuite, pour générer un nombre aléatoire, il existe l'instruction :

```codepython
import random

x = 0
y = 5

nombre_aleatoire = random.randint(x, y)
# x et y sont des nombres entiers
# par exemple, si x est égal à 1 et y à 5,
# le nombre obtenu sera entre 1 et 5 compris ([1, 5])

print(nombre_aleatoire)
```

Comme nous voulons pouvoir facilement accéder ce nombre aléatoire, il va falloir le stocker dans une variable que tu vas pouvoir nommer `nombre_aleatoire`

### Créer un score

Pour garder l'avancement du joueur dans le jeu du juste prix, tu peux créer une nouvelle variable nommée `score`. Elle devra valoir `0` au début du jeu. À chaque fois que le joueur proposera une valeur, ce score devra être augmenté de 1.

### Récupérer une entrée du joueur

Maintenant que l'on a choisi un nombre entre 1 et 1000, le joueur va devoir le deviner en proposant des nombres.

Il ne faut pas oublier d'ajouter 1 au score.

**Conseil :** on a vu précédemment qu'il était possible de récupérer l'entrée d'un utilisateur avec l'instruction `input()` !

Tu peux stocker l'entrée du joueur dans une variable nommée `nombre`.

### Vérifier l'entrée du joueur

Une fois que l'entrée du joueur a été récupérée, il faut vérifier si elle correspond à notre nombre aléatoire définit précédemment. Si ce n'est pas le cas, il faut déterminer si l'entrée est supérieure ou inférieure à notre nombre. Nous avons donc 3 cas à prendre en compte.

- Dans le cas où le nombre du joueur est égal au nombre aléatoire, il faut afficher `"Gagné !"`, le nombre aléatoire, ainsi que le score du joueur.
- Si le nombre du joueur est supérieur au nombre aléatoire, il faut afficher `"Moins !"`
- Si le nombre du joueur est inférieur au nombre aléatoire, il faut afficher `"Plus !"`

**Conseil :** on a vu au début de l'atelier qu'il était possible de créer des conditions capables de vérifier si une expression est vraie ou fausse, cela avec l'aide d'opérateurs.

### Continuer le jeu tant que le joueur ne trouve pas le nombre aléatoire

En programmation, il existe un moyen d'exécuter un certain nombre de fois un même ensemble d'instructions. On appelle cela des **boucles**. Il en existe de deux types principalement : les boucles `for` et les boucles `while`. Ici, on va s'intéresser à la boucle `while`.

La boucle `while` va exécuter un ensemble d'instructions tant qu'une condition donnée est vraie. Voici un exemple :

```codepython
nombre = 0
while nombre < 12 :
    nombre = nombre + 2
    print(nombre)
print(nombre)
```

Dans cet exemple, Python va répéter l'instruction `nombre = nombre + 2` jusqu'à ce que `nombre` soit supérieure à 12.

Dans notre Juste Prix, on veut que les instructions suivantes soient répétées tant que le joueur n'a pas trouvé `nombre_aleatoire` :

- Récupérer l'entrée du joueur
- Mettre à jour le score
- Vérifier l'entrée du joueur

Tu vas donc devoir ajouter une boucle `while` à ton code de manière à ce que le comportement indiqué au dessus soit appliqué. Attention à ne pas créer de boucle qui exécute des instructions à l'infini !

### Dernière étape

Bravo pour avoir complété ces étapes ! Tu devrais à présent avoir un jeu du Juste Prix fonctionnel.

Si tu le souhaites, tu peux faire des améliorations à ton jeu et lui ajouter des fonctionnalités. Voici quelques idées :

- Faire en sorte que le joueur ait un nombre précis d'essais à jouer avant de perdre
- Faire en sorte que le joueur choisisse au début du jeu l'intervalle dans lequel le nombre aléatoire doit être compris
