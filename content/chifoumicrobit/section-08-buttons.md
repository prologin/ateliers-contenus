## Mais il y a des boutons à côté des LEDs !

À côté des 25 LEDs du `micro:bit`, tu peux retrouver à gauche, le bouton A,
et à droite, le bouton B. Pour connaître le nombre d'appuis sur les boutons,
tu peux utiliser les fonctions `button_a.is_pressed()` et `button_a.was_pressed()`.
Tu peux retrouver les mêmes fonctions pour le bouton B juste en remplaçant
`button_a` par `button_b`.

Essaye les codes suivants pour comprendre la différence entre les deux fonctions !
Si tu as une question, n'hésite pas à appeler un organisateur !

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *

# Tant que `True` (vrai) est vrai :
# boucle infinie
while True:
    # Tant que le bouton A est appuyé
    while button_a.is_pressed():
        display.show(Image.GHOST)

    # Tant que le bouton B est appuyé
    while button_b.is_pressed():
        display.show(Image.PACMAN)

    # Eteint tous les pixels
    display.clear()
```

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *

# Affiche "Go !" sur le `micro:bit`
display.scroll("Go !")

# Met en pause le programme pour laisser du temps à l'utilisateur
sleep(200)

# `a_presse` est une variable qui contient `True`
# si le bouton a été appuyé, `False` sinon
a_presse = button_a.was_pressed()

# Si `a_presse` est vrai
if a_presse:
    # Affiche une image avec une coche
    display.show(Image.YES)
else:
    # Affiche une image avec une croix
    display.show(Image.NO)
```

<br/>

{{% box type="info" title="Mais c'est quoi ça `sleep(200)` ?" %}}

`sleep(200)`, permet de mettre en pause le programme pendant ici, 200 millisecondes.
Cela te laisse le temps d'appuyer sur les boutons. Il peut alors vérifier si
tu as appuyé sur les boutons pendant ce laps de temps.

{{% /box %}}

{{% box type="exercise" title="Entraînement 6 : Un grand sourire !" %}}

Pour tester si le `micro:bit` fonctionne bien, Skeleton voudrait que lorsqu'on
appuie sur les deux boutons en même temps, l'image sourire s'affiche.
Aide-le en créant le programme !

{{% /box %}}
