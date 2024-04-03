# Étape 3 : Utilisation des boutons

{{% box type="error" title="Objectif" %}}

Programmer le micro:bit pour utiliser des boutons externes afin de contrôler
**manuellement** l'activation ou la désactivation de la pompe à eau. Cette
fonctionnalité permettra une intervention rapide en cas de besoin et une
flexibilité dans la gestion de l'arrosage.

{{% /box %}}

{{% box type="info" title="Fonctionnement des boutons" %}}

Avant toute chose, il faut définir le comportement des boutons. Pour cela, on
utilise par exemple :

```python
def on_button_pressed_a():
    basic.show_string("Hello Mars !")
```

{{% /box %}}

La partie importante est la première ligne. On indique à la machine que l’on
veut changer le comportement du bouton A. Ensuite, on ajoute le code qui doit
s'exécuter lorsqu’on appuie sur le bouton. Ici, afficher "Hello Mars !".

{{% box type="exercise" title="Interrupteur basique" %}}

En utilisant le même principe, essayez de reprogrammer les boutons pour que le
bouton de gauche allume la pompe et que celui de droite l’éteigne.

{{% /box %}}

Un jour sur mars fait à peu près 24 heures aussi. Pour l’exercice, nous allons
considérer que 1 heure correspond 1 seconde. 

{{% box type="exercise" title="Interrupteur basique" %}}

Votre code devra attendre que l’utilisateur appuie en tout 24 fois sur le
bouton gauche et droite. Ensuite, il affiche le cycle prévu. 

{{% /box %}}

*Exemple :* On appuie 4 fois sur le bouton gauche, 12 fois sur le bouton droit et
8 fois sur le bouton gauche. Ensuite, le cycle pompe se lance. La pompe s'allume
pendant 4 secondes, s'éteint pendant 12 secondes et se rallume pendant 8
secondes. 
