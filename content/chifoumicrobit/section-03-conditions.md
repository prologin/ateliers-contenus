## Les booléens en Python

En programmation, tu peux évaluer certaines phrases par vrai ou faux. Par
exemple, la préposition `1 < 2` (1 est inférieur à 2) est vraie ; et `42 > 42`
(42 est supérieur à 42) est faux. Tu peux essayer en Python avec le code suivant :

```codepython
preposition_une = 1 < 2
# Affiche dans la console le résultat de `1 < 2` (vrai)
print(preposition_une)

preposition_deux = 42 > 42
# Affiche dans la console le résultat de `42 > 42` (faux)
print(preposition_deux)
```

Tu remarqueras sûrement que Python te renvoie `True` et `False`. C'est les
termes en anglais pour dire vrai et faux.

## Les conditions en Python : si, sinon si, sinon

Prenons un exemple, si Skeleton mange, il n'aura plus faim pour une glace. Le
début de cette phrase est une condition, qu'on peut identifier à l'aide du mot
"si". La condition ici est : Skeleton mange. Elle peut être vraie ou fausse.

{{<figure src="resources/images/conditions.png" height=75% width=75% alt="Conditions en Python">}}

C'est la même chose en Python. On va pouvoir définir des conditions qui
s'évaluent à vrai ou faux et exécuter des lignes de code en conséquence. Le
mot-clé "si" va être remplacé par son équivalent en anglais, `if`.

```codepython
# Vérifie si 1 est égal à 1
if 1 == 1:
    # Affiche dans la console "Skeleton est trop fort !"
    print("Skeleton est trop fort !")

# Sinon
else:
    # Affiche dans la console "Pacman est trop fort !"
    print("Pacman est trop fort !")
```

On peut également utiliser les mots-clés "sinon" et "sinon si". Un petit exemple
en français : Si je mange japonnais, je n'aurais plus faim. Sinon si je mange
italien, j'aurais encore un peu faim. Sinon, j'aurais trop faim. On peut alors
utiliser `else` pour "sinon" et `elif` pour "sinon si".

```codepython
# Essaye de modifier la valeur de `ma_variable` !
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

## Le mot clé `and`

Parfois, il va falloir que tu vérifies si deux conditions sont vérifiées en
même temps. On va alors parler du mot-clé `and` qui signifie "et" en français.

En voici un exemple :

```codepython
a = 5

# Vérifie si 42 est inférieur à 50 et si a est égal à 5
if 42 < 50 and a == 5:
    # Affiche dans la console "Pacman aime les chats !"
    print("Pacman aime les chats !")
```

## Le mot clé `not`

De plus, tu pourras avoir l'occasion de chercher le contraire d'une expression.
Par exemple, si Skeleton ne travaille pas aujourd'hui, il aura du mal pour son
contrôle. Ici, on a une négation, et la négation en Python se traduit comme suit :

```codepython
# `ma_condition` est évaluée à `False` car 42 n'est pas égal à 0
ma_condition = 42 == 0

# Si `ma_condition` n'est pas vraie (si `ma_condition` est fausse)
if not ma_condition:
    print("Bouh aime les carottes")
```

<br/>

{{% box type="info" title="Mais pourquoi on rajoute des espaces avant les lignes ?"%}}

Python suit ligne par ligne ton programme, donc pour lui expliquer ce que tu
veux faire sous certaines conditions, il faut rajouter des espaces avant les
lignes pour créer des blocs. On parle alors d'indentation. Pour faire ça, on va
utiliser la touche de tabulation (`Tab`) sur ton clavier. Cela permet à Python
de savoir quand est-ce qu'il faut sortir du bloc pour s'arrêter.

{{% /box %}}

{{% box type="exercise" title="Entraînement 1 : J'ai faim !" %}}

Pacman et le fantôme Bouh veulent tester tes capacités à écrire du code !
Pour cela, tu dois créer une variable `x`, et en fonction de sa valeur tu dois
afficher un texte dans la console, en suivant ces conditions :
- si x est inférieur à 10, tu dois afficher "Glace"
- sinon si x est inférieur à 20, tu dois afficher "Pizza"
- sinon si x est inférieur à 30, tu dois afficher "Crêpe"
- sinon, tu dois afficher "Gaufre"

```codepython
# Écris ton code ici !
```

{{% /box %}}
