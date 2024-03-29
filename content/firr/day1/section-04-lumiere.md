# Étape 3 : Variations lumineuses

{{% box type="error" title="Objectifs" %}}

Utiliser votre nouvelle installation pour créer les conditions lumineuses
optimales pour vos plantes, cette étape est cruciale pour leur adaptation à leur
nouvel environnement.

{{% /box %}}

Pour informer notre `micro:bit` que l'éclairage est branché, il faut ajouter la
ligne suivante au dessus de notre code :

```python
leds = neopixel.create(DigitalPin.P0, 10, NeoPixelMode.RGB)
```

Ici, nous utilisons la fonction `neopixel.create`. Les paramètres, dans l’ordre,
indiquent que notre éclairage est branché sur le pin 0, que nous avons 10 LEDs
et que ces LEDs peuvent faire différentes couleurs.

## Afficher les LEDs en rouge

{{% box type="info" title="Afficher des couleurs" %}}

La fonction à utiliser est :

```python
leds.show_color(neopixel.colors(couleur))
```

{{% /box %}}

Le paramètre `couleur` est à remplacer par la couleur que l’on veut.

{{% box type="warning" title="Le nom des couleurs" %}}

On ne peut pas mettre ce qu’on veut pour la couleur, il faut utiliser par
exemple : `NeoPixelColors.BLUE` ou `NeoPixelColors.GREEN`.

{{% /box %}}

{{% box type="exercise" title="Afficher les LEDs en rouge" %}}

Essaye d’afficher les LEDs en rouge

{{% /box %}}

## Différentes couleurs

{{% box type="info" title="Choisir les LEDs à allumer" %}}

Nous pouvons également choisir quelle LED doit changer de couleur. La commande
à utiliser est :

```python
r = leds.range(debut, fin)
r.show_color(neopixel.colors(couleur))
```

{{% /box %}}

Ici, nous avons 3 paramètres :
- `debut` doit être remplacé par le numéro de la première LED à changer de
couleur. Attention, en Python on commence à compter avec 0. (Pour commencer par
la première LED, il faut mettre 0, pour la deuxième, il faudra mettre 1, ainsi
de suite...)
- `fin` doit être remplacé par le numéro de la dernière LED à changer de couleur
- `couleur` fonctionne comme dans l’exercice précédent

{{% box type="exercise" title="Afficher des LEDs" %}}

Essaye d’afficher les 5 premières LEDs en bleu et les 5 dernières LEDs en vert.

{{% /box %}}

## Barre de chargement

En utilisant ce qu’on a vu avant, essaye de créer une barre de chargement.
D’abord la première LED doit s’allumer, ensuite les 2 premières etc...

{{% box type="info" title="Attendre un peu" %}}

L'exécution d’un code Python est très rapide. Dans notre cas, il faut dire à la
machine de laisser un peu de temps avant d'exécuter les lignes sinon, elle va
aller trop vite et on aura l’impression que toutes les LEDs s’allument en même
temps. 

La commande pour demander d’attendre est :

```python
basic.pause(ms)
```

{{% /box %}}

Ici, le paramètres `ms` est à remplacer par le temps que la machine doit
attendre. Cette valeur est en millisecondes, donc, pour attendre 1 seconde,
il faut remplacer ce paramètre par 1000.

{{% box type="exercise" title="Barre de chargement" %}}

Essaye de créer une barre de chargement.

{{% /box %}}

## Barre de chargement infinie

Le but est de créer la même barre de chargement qu’avant mais une fois qu’elle
est remplie, elle doit s'éteindre et recommencer.

{{% box type="info" title="Les boucles infinies" %}}

Pour qu’un code soit exécuté indéfiniment, il faut utiliser par exemple :

```python
while True:
    basic.showstring(“Hello Mars”)
```

La partie importante est le `while True`. En dessous, de cette ligne, tout ce
qui sera écrit s'exécutera indéfiniment. Remarquez aussi que la ligne du dessous
est décalée. C’est comme ça que la machine sait ce qu’il faut répéter
indéfiniment.

{{% /box %}}

{{% box type="info" title="Éteindre le stick" %}}

Pour éteindre complètement le stick LED, il faut utiliser :

```python
leds.clear()
leds.show()
```

{{% /box %}}

{{% box type="exercise" title="Barre de chargement infinie" %}}

Essaye de créer une barre de chargement infinie.

{{% /box %}}
