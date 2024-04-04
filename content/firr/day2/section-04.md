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
input.on_button_pressed(Button.A, on_button_pressed_a)
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

On va compter le nombre d'appuis sur le bouton A et le nombre d'appuis sur le
bouton B pour définir ces principes :

- le nombre d'appuis sur le bouton A correspond au temps pendant lequel la pompe
est allumée ;
- le nombre d'appuis sur le bouton B correspond au temps pendant lequel la pompe
est éteinte.

Au total, nous devons avoir 24 nombre d'appuis sur le bouton A et le bouton B.
Tant qu'on n'a pas atteint ces 24 appuis, vous devez vérifier les entrées sur
les boutons.

Par la suite, tu devras faire une itération du cycle de la pompe.

{{% /box %}}

Pour cette étape, tu dois utiliser les boucle `while` pour compter le nombre
d'appuis.
