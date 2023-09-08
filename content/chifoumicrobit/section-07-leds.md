# Programmons avec des `micro:bit` !

Pour pouvoir utiliser les `micro:bit` avec Python, on va devoir importer une
bibliothèque comme ce que l'on a fait pour les nombres aléatoires. Cela va nous
permettre d'intéragir avec les `micro:bit`.

Pour utiliser cette bibliothèque, dans les premières lignes de ton code, tu vas
devoir ajouter cette ligne :

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *
```

## J'ai envie de jouer avec les LEDs du `micro:bit`...

Les LEDs d'un `micro:bit` peuvent soit s'allumer, soit s'éteindre de manière
totalement indépendantes. Cependant, dans notre cas, on s'intéressera seulement
à afficher des images déjà fournies par la bibliothèque de `micro:bit`. Voici un
 exemple pour afficher un smiley content :

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *

# Affiche un sourire sur le micro:bit
display.show(Image.HAPPY)
```

La fonction `display.show()` nous permet d'afficher ce que l'on souhaite sur les
LEDs du `micro:bit`. `Image.HAPPY` est une image déjà définie par la
bibliothèque des `micro:bit`. Tu peux retrouver la liste des images disponibles
[ici](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html).

Pour afficher du texte ou des nombres, tu vas pouvoir utiliser la fonction
`display.scroll()`.

```python
# Importe la bibliothèque pour les micro:bit
from microbit import *

# Affiche "Chifoumicro:bit" sur le micro:bit
display.scroll("Chifoumicro:bit")
```

Avec la dernière fonction, `display.scroll()`, tu peux changer la vitesse
d'affichage avec l'argument `delay=nb` avec `nb` la vitesse. La valeur est
à l'origine à 150. Ainsi, si tu donnes un nombre plus petit que 150, ton
texte ira plus vite que par défaut.

```python
# Affiche "Je vais vite !" sur le micro:bit avec une vitesse de 50
display.scroll("Je vais vite !", delay=50)
```

<br/>

{{% box type="exercise" title="Entraînement 4 : Afficher une image !" %}}

Pour voir si tu as bien compris comment on manipule les images, Skeleton
souhaiterait que tu affiches un cœur (heart en anglais) sur ton `micro:bit`.

{{% /box %}}