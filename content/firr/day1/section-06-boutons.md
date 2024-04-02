# Étape 5 : Utilisation des boutons

{{% box type="error" title="Objectif" %}}

L’utilisation de la télécommande est essentielle pour faciliter le contrôle de
nos serres.

{{% /box %}}

## Interrupteur basique

Avant toute chose, il faut définir le comportement des boutons. Pour cela, on
utilise par exemple :

```python
def on_button_pressed_a():
    basic.show_string(“Hello Mars !”)
input.on_button_pressed(Button.A, on_button_pressed_a)
```

La partie importante est la première ligne. On indique à la machine que l’on
veut changer le comportement du bouton A. Ensuite, on ajoute le code qui doit
s'exécuter lorsqu’on appuie sur le bouton. Ici, afficher “Hello Mars !”

{{% box type="exercise" title="Bouton A pour allumer les LEDs" %}}

En utilisant le même principe, essayez de reprogrammer les boutons pour que le
bouton de gauche allume les LEDs et que celui de droite les éteigne.

{{% /box %}}

## Cycle personnalisé

Un jour sur Mars fait à peu près 24 heures aussi. Pour l’exercice, nous allons
considérer que 1 heure = 1 seconde. Votre code devra attendre que l’utilisateur
appuie en tout 24 fois sur le bouton gauche et droite. Ensuite, il affiche le
cycle prévu. 

{{% box type="exercise" title="Exemple du comportement attendu" %}}

Exemple : On appuie 4 fois sur le bouton gauche, 12 fois sur le bouton droit et
8 fois sur le bouton gauche. Ensuite, le cycle de lumière se lance. La lumière
s'allume pendant 4 secondes, s'éteint pendant 12 secondes et s’allume pendant
8 secondes. 

{{% /box %}}
