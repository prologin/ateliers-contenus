## L'aléAtOiRE eN PYthOn

En Python, on peut simuler de l'aléatoire, comme dans un lancé de dé. Pour faire
cela, il faut alors donner deux nombres, qui formeront l'intervalle dans lequel
on veut générer le nombre aléatoire. Par exemple, avec un dé, les valeurs que
l'on  peut obtenir sont sur l'intervalle [1; 6].

Afin de générer notre nombre aléatoire, il va d'abord falloir importer une
bibliothèque. Cela va nous permettre d'utiliser des fonctions déjà écrites dans
la bibliothèque. Ici, on va juste utiliser la fonction `randint` de la
bibliothèque `random`.

Si tu ne connais pas les fonctions, il faut les considérer comme des machines
dans lequelles on entre des valeurs et qui nous en ressortent d'autres. Elles
vont travailler sur nos entrées pour ressortir un élément.

```codepython
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

{{% box type="exercise" title="Entraînement 4 : Faire un choix" %}}

Bouh, le fantôme, n'arrive pas à faire de choix de ce qu'il veut manger à midi.
Pour l'aider, Skeleton souhaiterait que tu lui fasses un programme permettant
de choisir aléatoirement un élément dans la liste des choix possibles et
d'afficher ce choix. On te donne alors la liste suivante :

<br/>

```codepython
# Liste des choix
liste_choix = ["Frites", "Salade", "Riz"]

# Écris ton code ici !
```

{{% /box %}}
