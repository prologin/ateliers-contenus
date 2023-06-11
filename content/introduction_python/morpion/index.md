---
title: Introduction au Python - Morpion
date: 2022
authors: Dorian 'renji' Péron, Clarisse 'Nyota' Blanco
subtitle: Code ton jeu du Morpion 
tags:
    - Python
code_stub_url: ../resources/given_resources/morpion.py
---

# Introduction au Python - Morpion
Bonjour et bienvenue sur cet atelier d'introduction au Python !

## Objectifs
Au cours de cette initiation au langage Python, tu vas te familiariser avec les concepts suivants :
- Afficher du texte 
- Récupérer et utiliser le texte entré par l’utilisateur
- Utiliser des variables pour stocker des informations
- Faire des calculs et comparer des nombres avec les opérateurs
- Exécuter du code sous certaines conditions
- Exécuter du code en boucle

## Prerequis 
Avoir réalisé l'exercice `Introduction au Python - Juste Prix`.

## Les fonctions
Pour cet exercice, tu vas avoir besoin des notions vues dans l'exercice précédent, donc n'hésite pas à revenir dessus si besoin. Tu auras également besoin d'une nouvelle notion : les **fonctions**.

Une fonction est un **bloc de code** que l'on peut ré-utiliser à volonté sans avoir à copier / coller les instructions qui la composent. Une fonction prend des **paramètres** et peut renvoyer une valeur appelée **sortie**.

Une fonction possède un nom et se définit à l'aide du mot-clé `def` :
```py
def ajouter_4(x):
   return x + 4
```
Ici, nous avons déclaré une fonction que nous avons appelée `ajouter_4`. Ensuite, nous avons ouvert des parenthèses afin de spécifier ses paramètres : dans notre cas, `ajouter_4` prend un seul paramètre que nous avons nommé `x`. Un paramètre de fonction se comporte comme une variable : il possède un nom (qui doit être **unique**, tout comme celui de la fonction) et une valeur d'un certain type (entier, texte, booléen, etc. comme vu précédemment).

Ensuite, nous avons utilisé la touche TAB pour aligner le code du corps de notre fonction, pour indenter. Ici, le corps de la fonction est composé d'une seule instruction : `return x + 4`. Ce mot-clé `return` permet à la fonction d'avoir une **valeur de retour**, c'est-à-dire une sortie que nous pourrons utiliser. Dans notre cas, nous souhaitons que la fonction renvoie la valeur de x + 4. Maintenant, nous allons pouvoir **appeler** cette fonction et observer le résultat !

```codepython
def ajouter_4(x):
   return x + 4

x = 6
resultat = ajouter_4(x)
print(resultat) # on obtient 10 car 6 + 4 = 10, même logique pour la suite

resultat = ajouter_4(5)
print(resultat)

mon_entier = 10
resultat = ajouter_4(mon_entier)
print(resultat)
```

Résumons ce qu'il vient de se passer dans cet exemple :

- Pour appeler une fonction, nous écrivons son nom suivi des paramètres que nous voulons lui fournir entre parenthèses.
- Les valeurs fournies en paramètre à la fonction sont copiées dans le paramètre correspondant au sein de la fonction :
    - Dans le premier appel, notre x au sein de la fonction va copier la valeur de la variable du même nom qui est de 6.
    - Dans le deuxième appel, notre x au sein de la fonction va prendre la valeur 5.
    - Dans le troisième appel, notre x au sein de la fonction va copier la valeur de la variable mon_entier qui est de 10.

- Nous récupérons la valeur de retour de la fonction comme lorsque nous définissons une variable avec le =, ici la valeur de retour de la fonction est stockée dans la variable resultat.

**Remarque :** il est possible d'avoir des fonctions qui ne prennent aucun paramètre ! Il suffit pour ça de ne pas en spécifier entre les parenthèses : `def ma_fonction():`

**Remarque :** il est possible d'avoir des fonctions qui ne renvoient rien. Il suffit simplement de ne pas utiliser le mot-clé `return`.

## Les listes
Les listes sont un autre type de valeur présent dans Python. Il s'agit d'un type qui va pouvoir contenir un ensemble d'autres types vus précédemment.

```py
liste = [] # pour créer une liste vide
liste = [1, 2, 3, 4] # pour créer une liste avec des éléments, ici des nombres
liste = ["salut", 3, 5.4] # pour créer une liste avec des éléments de différents types
liste = [[0, 0], [1, 0]] # pour créer une liste de listes
```

Il est également possible de modifier et d'accéder à un élément en particulier dans une liste.

```codepython
liste = [1, 2, 3, 4]
print(liste[0]) # on accède ici à l'élément en position 0
print(liste[3])

liste = [[1, 2], [3, 4]]
print(liste[0][1]) # on accède à l'élément en position 0 de liste, puis à l'élément en position 1 de liste[0]

liste = ["a", "b", "c", "fin"]
liste[2] = "d" # on modifie l'élément en position 2
print(liste[2])
```

## Les boucles `for`

Les boucles `for` sont un autre type de boucle, différents des boucles `while` vues dans l'exercice du Juste Prix. Dans le Morpion, elles vont nous être utiles pour **itérer** dans les listes, c'est-à-dire, parcourir les éléments. Voici un exemple d'utilisation :

```codepython
liste = [1, 2, 3]
for i in range(len(liste)):
    print(liste[i])

for element in liste:
    print(element)
```
Dans l'exemple précédent, on itère sur la liste de deux manières différentes. On obtient néanmoins le même affichage. Le choix de la manière d'itérer va dépendre des instructions que l'on va utiliser dans la boucle, si par exemple on a besoin de `i` ou non.

Il est possible d'imbriquer des boucles `for` comme ceci :
```codepython
liste = [[1, 2], [3, 4]]
for i in range(len(liste)):
    for j in range(len(liste[i])):
        print(element)

for l in liste:
    for element in l:
        print(element)
```

Avec ces notions supplémentaires, tu vas pouvoir te lancer dans la réalisation du jeu du Morpion !

## Le jeu du Morpion

**But du jeu :** sur une grille 3x3, deux joueurs vont chacun leur tour, placer sur la grille un symbole qui leur est attribué (O ou X). Le but est de réussir à aligner 3 de ces symboles de manière horizontale, verticale ou diagonale. 

Pour coder notre jeu du Morpion, nous pouvons décomposer notre programme en plusieurs étapes et fonctions. Tu vas pouvoir trouver ces différentes fonctions à compléter dans le fichier `morpion.py`. 

**A savoir avant de commencer l'exercice:** dans le fichier fourni, tu trouveras le mot-clé `pass` à la fin de chaque fonction à compléter. Ce mot-clé sert à faire en sorte que les fonctions qui ne sont pas encore complétées n'émettent pas de message d'erreur. Dès que tu commences à écrire une fonction, tu peux supprimer le mot-clé `pass` associé.  

N'hésite pas à appeler un orga si tu as la moindre question sur ce fichier.

### Créer une grille vierge : `nouvelleGrille()`
Dans cette fonction, il va falloir créer une grille vierge de Morpion, de dimension 3x3. Pour modéliser une grille de morpion, on va utiliser une liste de listes. 

Chaque case de la grille aura un statut particulier : `" "`, `"O"` ou `"X"`.
- `" "` signifie que la case est vide
- `"O"` signifie que le joueur O a rempli la case
- `"X"` signifie que le joueur X a rempli la case
On remplira notre liste de listes avec ces symboles par la suite. Ici, une grille vierge ne contient que des `" "`.

Exemple de ce que tu vas devoir faire avec une grille en 2x2 :
```py
grille = [[" ", " "], [" ", " "]]
```
Cette liste de listes correspond à la grille suivante :
|`grille[0][0]`|`grille[0][1]`|
|---|---|
|`grille[1][0]`|`grille[1][1]`|

N'oublie de renvoyer ta nouvelle grille dans cette fonction !

### Vérifier si la grille a un gagnant : `verifierGrille(grille)`
Après chaque modification dans la grille, il va falloir vérifier si un joueur est gagnant. C'est-à-dire, vérifier s'il y a 3 symboles identiques alignés de manière horizontale, verticale ou diagonale. Il y a donc 3 cas à gérer.

Pour cela, tu vas avoir besoin de boucles `for` que tu as pu voir dans une section au-dessus. Elles vont t'être utiles pour itérer dans la grille.

Si la grille n'a aucun joueur gagnant, alors il faut renvoyer `" "`, sinon il faut renvoyer le symbole associé au gagnant : `"O"` ou `"X"`.

**Important :** la variable `coord` passée en paramètre est un couple de variables. Dans notre cas : `coord = (coordonnee_horizontale, coordonne_verticale)`. Ainsi pour récupérer les coordonnées, il suffit de faire cela :
```codepython
coord = (4, 5)
# Méthode 1 : comme dans une liste !
coordonnee_horizontale = coord[0]
print(coordonnee_horizontale)
coordonnee_verticale = coord[1]
print(coordonne_verticale)

# Méthode 2 : à l'aide de variables
horizontal, vertical = coord
print(horizontal)
print(vertical)
```

### Vérifier si les coordonnées données par le joueur sont valides : `verifierCoordonnees(grille, coord)`
Dans cette fonction, tu vas devoir vérifier si les coordonnées passées en paramètre sont valides. Entre autres, tu vas devoir vérifier plusieurs choses :
1. Si les coordonnées sont bien des nombres
    - tu auras besoin de la fonction Python `isnumeric()` pour vérifier que la coordonnée donnée sous forme de chaîne de caractères est bien un nombre. Elle s'utilise de la manière suivante :

```codepython
texte = "42"
print(texte.isnumeric()) # Doit afficher 'True'

texte = "bonjour"
print(texte.isnumeric()) # Doit afficher 'False'
```

2. si les coordonnées sont bien dans la grille
    - pour cela, il faut vérifier si les nombres donnés par les coordonnées ne sont pas trop grands et permettent bien d'accéder à un élément de la grille
3. si la case dans la grille est déjà occupée
    - c'est-à-dire si le contenu de la case est différent de `" "`

### Demander des coordonnées au joueur : `demanderCoordonnees(grille, joueur)`
Dans cette fonction, on souhaite demander au joueur, les coordonnées de l'emplacement dans la grille où il souhaiterait placer son symbole. Les coordonnées doivent continuer à être demandées tant qu'elles ne sont pas valides par la fonction précédente, `verifierCoordonnees(grille, coord)`. Pour cela, tu vas pouvoir utiliser une boucle `while`.

Voici ce que la fonction va devoir faire :
1. Annoncer (afficher) que c'est au tour du joueur donné en paramètre
2. Demander les coordonnées en boucle, jusqu'à ce qu'elles soient valides
    - il faudra demander les coordonnées horizontales et verticales séparément
3. Renvoyer les coordonnées valides sous forme de couple de coordonnées : `(horizontal, vertical)`

### Faire la fonction pour joueur au morpion : `morpion()`
Dernière fonction de l'exercice, bravo pour être arrivé jusqu'ici ! Il ne reste plus qu'à assembler les fonctions que tu as codées plus tôt afin d'obtenir un jeu du morpion fonctionnel.

Dans la fonction `morpion()` tu vas devoir compléter la boucle donnée dans le fichier fourni, ainsi que la fin de la fonction qui annonce le joueur vainqueur. Voici ce que la boucle devra exécuter à chaque tour :
1. Afficher la grille
2. Demander les coordonnées au premier joueur
3. Mettre à jour la grille
4. Vérifier si la grille a un gagnant
    - Si la grille a un gagnant, on sort de la boucle avec le mot-clé `break`
    - Sinon, on continue
5. Demander les coordonnées au deuxième joueur
6. Mettre à jour la grille
7. Vérifier si la grille a un gagnant
    - Même chose qu'au-dessus

Voici ce qu'il doit se passer à la fin de cette fonction, après la boucle :
- Afficher la grille
- Annoncer (afficher) qui est le joueur gagnant

Une fois toutes ces étapes codées, tu devrais avoir un jeu du morpion fonctionnel, félicitations !

