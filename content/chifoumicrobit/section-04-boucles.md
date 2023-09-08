## Les boucles en Python, les boucles en Python, les boucles en Python

Les boucles nous permettent de répéter plusieurs tâches. En Python,
il y a deux types de boucles ; cependant, dans cet atelier, seul un type
nous suffira : les boucles `while`.

On peut traduire `while` par "tant que" en français. On va pouvoir utiliser
les conditions dans les boucles `while` pour pouvoir répéter des choses
tant qu'une condition est toujours vraie. Par exemple, tant que le bébé dort,
nous ne devons pas faire de bruit.

Un exemple serait celui-ci :

```codepython
i = 0
# Tant que i est inférieur à 3
while i < 3:
    # Afficher "Bonjour !"
    print("Bonjour !")

    # Ajouter 1 à i à chaque tour de boucle
    i = i + 1
```