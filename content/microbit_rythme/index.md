---
title: Jeu de rythme
date: 2022
authors: Cyril Pujol
subtitle: Codez votre petit jeu de rythme sur micro:bit
code_stub_url: TODO
---

# Le jeu de rythme

Le but de cette exercice est de coder un jeu très simple et amusant sur `micro:bit`.

![Jeu de rythme](./images/todo)

## Principe du jeu

Dans ce jeu, des notes de musique avancent vers les boutons de plus en plsu vite et il faut appuyer pour les jouer au bon moment.

### Les notes

Les notes sont représentés par des traits qui apparaissent et se déplacent en haut et en bas de l'écran. En haut elles se dirigent vers la droite et en bas vers la gauche. 
Lorsqu'elles arrivent au bord de l'écran, il faut appuyer sur le boutons correspondant pour les jouer.

### Les vies

Pour faire durer un peu la partie, le joueur dispose initialement de trois vies visibles au centre de l'écran. 
Chaque fausse note lui fait perdre une vie et supprime toutes les notes à l'écran.

### Fin de la partie

La partie s'arrête lorsque le joueur n'a plus aucune vie. Le score du joueur, correspondant au nombre de notes jouées, est affiché.

Pour coder notre jeu, nous allons utiliser une carte `micro:bit`. Sur la carte, nous nous intéresserons aux 2 boutons (A et B) ainsi qu'à l'écran. Ce dernier est composé de 25 pixels rouges répartis sur 5 lignes et 5 colonnes. Les sections suivantes expliquent comment les utiliser.


## Fonctionnement de la carte `micro:bit`

### L'écran

Chaque pixel de l'écran est une LED rouge, que l'on peut allumer ou éteindre à un certain degré d'intensité allant de 0 à 9 (0 -> éteinte, 9 -> allumée au max). La ligne de code ci-dessous allumera le pixel de la première ligne et troisième colonne au niveau 6.

```py
# Attention, la numérotation des lignes et des colonnes commence à 0
display.set_pixel(0, 2, 6)
```

Il pourra vous être utile de réinitialiser l'écran et d'éteindre toutes les LEDs d'un coup. Pour cela, on utilise la fonction suivante.

```py
# Cette commande a le même effet que faire display.set_pixel(i, j, 0) 25 fois !
display.clear()
```

### Les boutons

Afin de pouvoir jouer les notes, nous allons utiliser les boutons A et B sur les côtés de l'écran. Quand on tient la carte `micro:bit` dans le bon sens, le bouton A est à gauche et le bouton B est à droite. 
On souhaite tester si et quand le joueur a appuyé sur un bouton. Il existe pour cela 2 fonctions principales :

```py
button_a.is_pressed()   # Ces fonctions renvoient True ou False si les boutons sont
button_b.is_pressed()   # appuyés quand la ligne est exécutée par le micro:bit

button_a.was_pressed()  # Ces fonctions renvoient True ou False si les boutons ont
button_b.was_pressed()  # été appuyés depuis la dernière fois qu'elles ont été appelées
```

Pour ce projet, `was_pressed()` est plutôt recommandé puisqu'il laisse une plus grande marge d'erreur à l'utilisateur.

## Le jeu

### Les notes

Ici, les notes sont représentées par deux pixels l'un au dessus de l'autre. 
Elles sont représentées informatiquement par un entier entre 0 et 4 qui représente leur avancée dans le temps : à 0 la note vient d'être créée, à 4 la note doit être jouée.
Les notes a jouer sont enregistrées dans des listes `notesA` et `notesB` qui contiennent l'ensemble des notes du haut et du bas respectivement.
Les opérations utiles sur les listes sont :
```py
liste = [1,2,3] # Créé une liste avec les valeurs 1, 2 et 3
liste.append(4) # Ajoute 4 à la fin de la liste
for x in liste: # On répète pour tout les elements x de la liste 
    print(x)    # Afficher x
```
Les notes apparaissent aléatoirement en début de ligne, pour effectuer une action avec une chance sur deux, on peut utiliser :
```py
if rd.random() < 0.5 :
    pass # ACTION
```

### Les vies

Les trois vies du joueur sont représentées par les trois pixels du milieu de l'écran, de coordonnées (1,2), (2,2) et (3,2). 
Elles sont perdues quand le joueur fait une fausse note : en appuyant sur un bouton alors qu'il ne devait pas ou en n'appuyant pas alors qu'il devrait le faire.
Lorsque qu'une vie est perdu, toutes les notes disparaissent de l'écran pour laisser au joueur le temps de se remettre dans le rythme.
Quand les trois vies sont perdues, le jeu s'arrête, on peut afficher un score final correspondant au nombre de notes jouées ou au temps de jeu. Pour cela on peut utiliser les fonctions :
```py
display.scroll("PERDU") # Affiche "perdu", lettre par lettre
display.scroll(123) # Affiche 123, chiffre par chiffre
# On peut aussi utiliser display.show() pour un style d'affichage différent
```
Une fois le score affiché, on peut recommencer le jeu.

### La pulsation

Pour rythmer le jeu, toutes les opérations se font sur une pulsation, c'est la vitesse de celle-ci qui va permettre d'ajuster la difficultée du jeu.

À chaque temps, il faut :
 - Afficher toute les notes et vies
 - Avancer les notes de un temps
 - Ajouter aléatoirement des notes
 - tester si le joueur appuie sur la bonne touche et agir en conséqunce
 - accélérer légèrement la pulsation

En première approximation, on peut supposer que tous les calculs faits par le microbits sont réalisés instantanéments, pour gérer la vitesse de la pulsation, il faut donc attendre un temps donné, pour cela on peut utiliser :
```py
sleep(500) #Ne fait rien pendant 500ms
```

### Conseils
Effectuer votre projet dans cet ordre : 
- affichage
- mouvement des notes
- test d'un appui sur un bouton
- gestion du temps
- gestion des vies

Faites bien attention à l'ordre dans lequel vous faites les choses, en particulier entre `sleep()` et `button_a.is_pressed()`.
Tester régulièrement votre jeu pour vérifier qu'il fonctionne correctement.
N'hésitez pas à varier les mécaniques et le design de votre jeu pour le rendre unique.


