---
title: Introduction au Python - Morpion
date: 2022
authors: Dorian 'renji' Péron, Clarisse 'Nyota' Blanco
subtitle: Code ton jeu du Morpion 
code_stub_url: ./morpion.py
---

# Introduction au python - Morpion
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
Avoir realise l'exercice `Introduction au Python - Juste Prix`.

## Les fonctions
Pour cet exercice, tu vas avoir besoin des notions vues dans l'exercices precedent, donc n'hesite pas a revenir dessus si besoin. Tu auras egalement besoin d'une nouvelle notion : les **fonctions**.

Une fonction est un **bloc de code** que l'on peut ré-utiliser à volonté sans avoir à copier/coller les instructions qui la composent. Une fonction prend des **paramètres** et peut renvoyer une valeur appelée **sortie**.

Une fonction possède un nom et se définit à l'aide du mot-clé `def` :
```py
def ajouter_4(x):
   return x + 4
```
Ici, nous avons déclaré une fonction que nous avons appelée ajouter_4. Ensuite, nous avons ouvert des parenthèses afin de spécifier ses paramètres : dans notre cas, `ajouter_4` prend un seul paramètre que nous avons nommé `x`. Un paramètre se comporte comme une variable : elle possède un nom (qui doit être **unique** tout comme celui de la fonction) et une valeur d'un certain type (entier, texte, booléen, etc. comme vu précédemment).

Ensuite, nous avons utilisé la touche TAB pour aligner le code du corps de notre fonction, pour indenter. Ici, le corps de la fonction est composé d'une seule instruction : `return x + 4`. Ce mot-clé `return` permet à la fonction d'avoir une **valeur de retour**, c'est-à-dire une sortie que nous pourrons utiliser. Dans notre cas, nous souhaitons que la fonction renvoie la valeur de x + 4. Maintenant, nous allons pouvoir **appeler** cette fonction et observer le résultat !

```py
>>> x = 6
>>> resultat = ajouter_4(x)
>>> print(resultat)
10 # on obtient ce resultat car 6 + 4 = 10, meme logique pour la suite

>>> resultat = ajouter_4(5)
>>> print(resultat)
9

>>> mon_entier = 10
>>> resultat = ajouter_4(mon_entier)
>>> print(resultat)
14
```

Résumons ce qu'il vient de se passer dans cet exemple :

- Pour appeler une fonction, nous écrivons son nom suivi des paramètres que nous voulons lui fournir entre parenthèses.
- Les valeurs fournies en paramètre à la fonction sont copiées dans le paramètre correspondant au sein de la fonction :
    - Dans le premier appel, notre x au sein de la fonction va copier la valeur de la variable du même nom qui est de 6.
    - dans le deuxième appel, notre x au sein de la fonction va prendre la valeur 5.
    - dans le troisième appel, notre x au sein de la fonction va copier la valeur de la variable mon_entier qui est de 10.

- nous récupérons la valeur de retour de la fonction comme lorsque nous définissons une variable avec le =, ici la valeur de retour de la fonction est stocké dans la variable resultat.

**Remarque :** il est possible d'avoir des fonctions qui ne prennent aucun paramètre ! Il suffit pour ça de ne pas en spécifier entre les parenthèses : `def ma_fonction():`

**Remarque :** il est possible d'avoir des fonctions qui ne renvoient rien. Il suffit simplement de ne pas utiliser le mot-cle `return`.

## Les listes
Les listes sont un autre type de valeur present dans Python. Il s'agit d'un type qui va pouvoir contenir un ensemble d'autres types vus precedemment.

```py
liste = [] # pour creer une liste vide
liste = [1, 2, 3, 4] # pour creer une liste avec des elements, ici des nombres
liste = ["salut", 3, 5.4] # pour creer une liste avec des elements de differents types
liste = [[0, 0], [1, 0]] # pour creer une liste de listes
```

Il est egalement possible de modifier et d'acceder a un element en particulier dans une liste.

```py
>>> liste = [1, 2, 3, 4]
>>> print(liste[0]) # on accede ici a l'element en position 0
1
>>> print(liste[3])
4

>>> liste = [[1, 2], [3, 4]]
>>> print(liste[0][1]) # on accede a l'element en position 0 de liste, puis a l'element en position 1 de liste[0]
2

>>> liste = ["a", "b", "c", "fin"]
>>> liste[2] = "d" # on modifie l'element en position 2
>>> print(liste[2])
"d"
```

## Le jeu du Morpion

**But du jeu :** sur une grille 3x3, deux joueurs vont chacun leur tour, placer sur la grille un symbole qui leur est attribue (O ou X). Le but est de reussir a aligner 3 de ses symboles de maniere horizontale, verticale ou diagonale. 

Pour coder notre jeu du Morpion, nous pouvons decomposer notre programme en plusieurs etapes et fonctions. Tu vas pouvoir trouver ces differentes fonctions a completer dans le fichier `morpion.py`. 

### Creer une grille vierge : `nouvelleGrille()`
Dans cette fonction, il va falloir creer une grille vierge de Morpion, de dimension 3x3. Pour modeliser une grille de morpion, on va utiliser des listes des listes. 

Chaque case de la grille aura un status particulier : `" "`, `"O"` ou `"X"`.
- `" "` signifie que la case est vide
- `"O"` signifie que le joueur O a rempli la case
- `"X"` signifie que le joueur X a rempli la case
On remplira notre liste des listes avec ces symboles par la suite. Ici, une grille vierge ne contient que des `" "`.

Exemple de ce que tu vas devoir faire avec une grille en 2x2 :
```py
grille = [[" ", " "], [" ", " "]]
```
Cette liste de listes correspond a la grille suivante:
|`grille[0][0]`|`grille[0][1]`|
|---|---|
|`grille[1][0]`|`grille[1][1]`|

N'oublie de renvoyer ta nouvelle grille dans cette fonction !

### Verifier si la grille a un gagnant : `verifierGrille(grille)`
Apres chaque modification dans la grille, il va falloir verifier si un joueur est gagnant. C'est a dire, verifier s'il y a 3 symboles identiques alignes de maniere horizontale, verticale ou diagonale. Il y a donc 3 cas a gerer.


