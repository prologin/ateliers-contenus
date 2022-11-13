---
title: Introduction au Python - juste prix
date: 2022
authors: Dorian 'renji' Péron, Gaetan 'Downvot_ED' Mouisset, Clarisse 'Nyota' Blanco
subtitle: Code ton jeu du juste prix 
code_stub_url: ./juste-prix.py
---

# Introduction au Python
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

Ces instructions sont écrites par un programmeur dans un fichier texte que l'on appelle le **code source**. Le code source consiste en une **succession d'instructions** (un **programme**) qui seront interprétées et exécutées par l'ordinateur. Pour un fichier Python, il faut un nommage specifique l'extension du fichier sera "py" : `fichier.py` par exemple.

Le Python est un des langages les plus populaires : aujourd'hui, il est utilisé dans pratiquement tous les domaines tels que le développement web, l'intelligence artificielle, ou encore la science des données.

## Quelques notions pratiques 
Cette section te montre les fonctionnalités de Python qui te seront utiles pour créer ton jeu ensuite. N’hésite pas à essayer par toi-même les exemples donnés pour voir comment ça fonctionne ! Si tu ne comprends pas une partie, demande de l’aide aux organisateurs.


### Afficher du texte
Un langage de programmation nous permet de faire beaucoup de choses, mais nous voulons que nos programmes puissent nous parler si nécessaire. Tu peux lancer le programme suivant et observer le résultat !

```py
print("Hello world!")
```

Ici, notre programme est constitué d'une seule instruction : il s'agit d'un print (“imprimer” en anglais). Cela permet d'afficher à l'écran le texte spécifié entre les guillemets. C’est très pratique pour informer l’utilisateur du programme de toutes sortes de choses.
Tu peux écrire ta propre instruction print sur la ligne suivante afin d'afficher le texte de ton choix. Il ne faut pas oublier les guillemets !

En lançant le programme, tu peux voir que les phrases sont affichées dans l'ordre dans lequel tu les as écrites. En effet, en Python, les instructions sont exécutées les unes à la suite des autres.

### Lire/recuperer du texte
Maintenant que tu sais écrire du texte à l'écran, il serait intéressant d'avoir un moyen d'intéragir avec l'utilisateur du programme.

Une manière de faire cela est d'utiliser l'instruction input (“entrée” en anglais). Celle-ci permet au programme de récupérer du texte entré par l'utilisateur.

```py
input("Comment t'appelles-tu ?")
```

Tout comme pour print, il est possible de spécifier du texte qui sera affiché à l'écran.

Tu peux lancer le programme et répondre à la question. Il faut ensuite appuyer sur la touche “Entrée” pour valider.
Pour l’instant, ton programme ne fait rien de la réponse qu’on lui donne. Afin de la sauvegarder, il est nécessaire de la **stocker** dans une **variable**.

### Variables
Une variable est un élément qui associe un nom à une valeur. Elle peut être de plusieurs types différents:
- Un nombre entier : `ma_variable = 5`
- Une chaine de caracteres : `ma_variable = "bonjour !"` (on reconnait une telle variable grâce aux guillemets)
- Un nombre à virgule : `ma_variable = 1.05` (on utilise un point et non une virgule)
- Un booléen : `ma_variable = True` (deux valeurs possibles : `True` ou `False`, vrai ou faux, bien penser a mettre la majuscule !)

**Attention :** Il ne faut pas mélanger les types : ma_variable = 5 est le nombre entier 5 tandis que ma_variable = "5" est une chaine de caracteres contenant le chiffre 5.

```py
prenom = input("Comment t'appelles-tu ?")
```

Ici, nous associons le texte rentré par l'utilisateur dans une variable que nous nommons `prenom`. Nous aurions très bien pu nommer cette variable autrement (à condition de ne pas mettre d’espace, ni de “-” dans le nom, ni de numéro en début du nom de la variable) . En revanche, il est une bonne pratique de donner un nom explicite qui facilite la comprehension du code.

Pour afficher le contenu de la variable `prenom` tu peux utiliser à nouveau l'instruction `print()`. Attention cette fois-ci à ne pas mettre de guillemets, comme ceci :
```py
print(prenom)
```
Le texte que tu as rentré s'affiche maintenant à l'écran.

À présent, reprenons notre exemple avec la météo :

```py
prenom = input("Comment t'appelles-tu?")
print("Tu t'appelles ", prenom)
```

Si tu lances ce programme et réponds à la question, tu verras que le contenu de la variable `prenom` s'est rajouté à la suite de la chaine de caracteres "Tu t'appelles ".

**Info :** Dans une instruction print, la virgule permet d'afficher plusieurs éléments les uns à la suite des autres en les séparant par un espace.

### Les operateurs
Les opérateurs sont une notion essentielle en informatique, on les retrouve dans tous les langages de programmation.Comme leur nom l'indique, les opérateurs permettent de réaliser des opérations, aussi bien mathématiques que logiques.

En Python les principaux opérateurs dont tu aura besoin sont les suivants : `+`, `-`, `*`, `/`, `//`, `==`, `>`, `<`, `<=`, `>=`, `and`, `or`, `not`. Leur fonctionnement est expliqué en dessous.

**Les operateurs mathematiques**

Ce sont les opérateurs les plus simples à comprendre. Il manipulent des nombres. Pour chacun des opérateurs dans le tableau, tu peux vérifier le fonctionnement en tapant :
```py
print(exemple)
```
Et en vérifiant que tu as le bon résultat quand tu exécutes le programme.

|Operateur|Exemple|Resultat|
|---|---|---|
|Addition:`+`|`5 + 5`|`10`|
|Soustraction: `-`|`10-5`|`5`|
|Multiplication: `*`|`5*5`|`25`|
|Division: `/`|`6 / 4` <br/> `9 / 3`| `1.5` <br/> `3`|
|Division euclidienne: `//`|`6 // 4` <br/> `9 // 3`|`1` <br/> `3`|

**Les operateurs de comparaison**

Les opérateurs de comparaison permettent de comparer deux nombres, et créent une valeur booléenne (vrai ou faux). Comme pour les opérateurs mathématiques, tu peux expérimenter le fonctionnement de ces opérateurs directement dans ton programme.

|Operateur|Exemple|Resultat|
|---|---|---|
|Egal: `==`| `5 ==5` <br/> `1 == 2`|`True` <br/> `False`|
|Inegal: `!=`|`5 != 5` <br/> `1 != 2`|`False` <br/> `True`|
|Superieur:`>`|`1 > 2` <br/> `2 > 1`|`False` <br/> `True`|
|Inferieur:`<`|`1 < 2` <br/> `2 < 1`|`True` <br/> `False`|
|Superieur ou egal:`>=`|`5 >= 5` <br/> `2 >= 5`|`True` <br/> `False`|
|Inferieur ou egal:`<=`|`4 <= 4` <br/> `4 <= 3`|`True` <br/> `False`|

**Les operateurs logiques**

Les opérateurs permettent d’associer des valeurs booléennes (vrai ou faux), et de les transformer en autres valeurs booléennes (vrai ou faux). Voici les plus utiles :

|Operateur|Description|Exemple|Resultat|
|---|---|---|---|
|ET : `and`|Repond vrai si <br/> les valeurs a gauche et <br/> a droite sont vraies |`True and False` <br/> `False and True` <br/> `False and False` <br/> `True and True`| `False` <br/> `False` <br/> `False` <br/> `True`|
|OU : `or`|Repond vrai si <br/> au moins un des deux <br/> est vrai|`True or False` <br/> `False or True` <br/> `False or False` <br/> `True or True`|`True` <br/> `True` <br/> `False` <br/> `True`|
|NON : `not`|Repond l'inverse <br/> de ce qu'on lui donne|`not True` <br/> `not False`|`False` <br/> `True`|

**Utilisation des operateurs avec les conditions**

Grace a ces operateurs, il est possible de creer des **conditions** capables de verifier si un expression est vraie ou fausse. Voici un exemple :
```py
if 10 > 0:
    print("C'est vrai")
else:
    print("C'est faux")
```

Il est egalement possible de mettre plusieurs conditions a la suite avec le mot cle `elif`.
```py
if 14 < 13:
    print("14 < 13 est vrai")
elif 5 != 3:
    print("5 != 3 est vrai")
else:
    print("Les conditions precedentes sont fausses")
```

N'hesite pas a recopier les exemples et a les executer pour mieux comprendre. Tu peux aussi changer les conditions pour voir si le comportement est change.

Il est egalement possible de creer des expression mathematiques avec ces operateurs.
```py
nombre = 5
somme = (nombre - 2) * 3
```

Avec ces notions de base, tu vas pouvoir te lancer dans la realisation du jeu du juste prix !

## Le jeu du juste prix
**But du jeu :** le but du jeu du Juste Prix est de faire deviner un nombre entre 1 et 1000 au joueur. Le joueur commence en entrant un nombre dans le programme. Le programme doit répondre “Plus” si le nombre est plus petit que celui à deviner ou “Moins” s’il est plus grand. Le joueur peut alors continuer à entrer des nombres jusqu’à trouver le bon. Finalement, le score du joueur correspond au nombre de fois où il a rentré une réponse.

Pour cela, nous pouvons decomposer notre programme en plusieurs etapes.

### Choisir un nombre entre 1 et 1000
Pour generer un nombre aleatoire en python, des programmes sont deja existants. Ainsi, il faut ajouter le programme deja existant a notre code. Cela se fait en rajoutant au debut de notre fichier la ligne suivante :  `import random`. 

Ensuite, pour generer un nombre aleatoire, il existe l'instruction:

```py
nombre_aleatoire = random.randint(a, b)
# avec a et b des nombres entiers
# par exemple, si a est egal a 1 et b a 5,
# le nombre genere sera entre 1 et 5 compris ([1, 5])

print(nombre_aleatoire)
```
Comme nous voulons pouvoir facilement a ce nombre aleatoire, il va falloir le stocker dans une variable que tu vas pouvoir nommer `nombre_aleatoire`

### Creer un score
Pour garder l'avancement du joueur dans le jeu du juste prix, tu peux creer une nouvelle variable nommee `score`. Elle devra valoir 0 au debut du jeu. A chaque fois que le joueur proposera une valeur, ce score devra etre augmente de 1.

### Recuperer une entree du joueur
Maintenant que l'on a choisi un nombre entre 1 et 1000, le joueur va devoir le deviner en proposant des nombres. 

Il ne faut pas oublier d'ajouter 1 au score.

**Conseil :** on a vu precedemment qu'il etait possible de recuperer une entree d'un utilisateur avec l'instruction `input()` !

Tu peux stocker l'entree du joueur dans une variable nommee `nombre`.

### Verifier l'entree du joueur
Une fois que l'entree du joueur a ete recuperer, il faut verifier si elle correspond a notre nombre compris entre 1 et 1000. Si ce n'est pas le cas, il faut determiner si l'entree est superieure ou inferieure a notre nombre. Nous avons donc 3 cas a prendre en compte.

- Dans le cas ou le nombre du joueur est egal au nombre aleatoire, il faut afficher `Gagne !`, le nombre aleatoire, ainsi que le score du joueur.
- Si le nombre du joueur est superieur au nombre aleatoire, il faut afficher `Moins !`
- Si le nombre du joueur est inferieur au nombre aleatoire, il faut afficher `Plus !`

**Conseil :** on a vu au debut de l'atelier qu'il etait possible de creer des conditions capables de verifier si une expression est vraie ou fausse, cela avec l'aide d'operateurs.

### Continuer le jeu tant que le joueur ne trouve pas le nombre aleatoire
En programmation, il existe un moyen d'executer un certain nombre de fois un meme ensemble d'instructions. On appelle cela des **boucles**. Il en existe de deux types principalement: les boucles `for` et les boucles `while`. Ici, on va s'interesser a la boucle `while`. 

La boucle `while` va executer un meme ensemble d'instruction jusqu'a ce qu'une condition donnee devienne vraie. Voici un exemple :
```py
nombre = 0
while nombre < 12 :
    nombre = nombre + 2
print(nombre)
``` 

Dans notre juste prix, on veut que les instructions suivantes soient repetees jusqu'a ce que le joueur ait trouve `nombre_aleatoire`:
- Recuperer une entree du joueur
- Mettre a jour le score
- Verifier l'entree du joueur

Tu vas donc devoir ajouter une boucle `while` a ton code de maniere a ce que le comportement indique juste au dessus soit applique. Attention a ne pas creer de boucle qui execute des instructions a l'infini !

### Derniere etape

Bravo pour avoir complete les etapes precedentes ! Tu devrais a present avoir un jeu du juste prix fonctionnel. 

Si tu le souhaites, tu peux faire des ameliorations a ton jeu et lui ajouter des fonctionnalites. Voici quelques idees :
- Faire en sorte que le joueur ait un nombre precis de tours a jouer avant de perdre
- Faire en sorte que le joueur choisisse au debut du jeu l'intervalle dans lequel le nombre aleatoire etre compris