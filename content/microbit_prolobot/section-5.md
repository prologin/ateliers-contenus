---
show_toc: false
---

<span style="font-family: Courier; color: #606060;">[Procédure Formation Terminée]</span>  
<span style="font-family: Courier; color: #606060;">[Analyse des modules...]</span>  
<span style="font-family: Courier; color: #606060;">[Analyse terminée]</span>  
# <span style="font-family: Courier;">[Rapport de modules]</span>  

### <span style="font-family: Courier;">[Prélude: Notations]</span>

Les spécifications de commandes sont inscrites comme ceci :

`commande(option1, option2 = valeurParDéfaut)`: description
- option1: descrition option1
- option2: description option2

Si une option est suivie d'un `=`, elle est donc facultative. Dans l'exemple
ci-dessous, `option2` sera donc remplacée par `valeurParDéfaut` si elle n'est
pas précisée.

### <span style="font-family: Courier;">[Informations additionnelles: Initialisation du Prolobot]</span>

Voici les commandes à écrire au début du fichier pour toute utilisation du robot :

```py
from prolobot import *
bot = Prolobot()
```

### <span style="font-family: Courier;">[Sous-Module Déplacement]</span>

`bot.forward(vitesse = 0.4)`: avance à la vitesse donnée.
- vitesse: nombre entre 0 et 2 (inclus). Correspond au nombre de tours de roue
    secondes.

`bot.backward(vitesse = 0.4)`: recule à la vitesse donnée.
- vitesse: nombre entre 0 et 2 (inclus). Correspond au nombre de tours de roue
    secondes.

`bot.stop()` : arrête le robot. À écrire après toute utilisation du robot, celui-ci
ne s'arrêtant pas de lui même

### <span style="font-family: Courier;">[Sous-Module Rotation]</span>

`LEFT` / `RIGHT` : variables de direction. À utiliser en paramètre.

`bot.turn(direction, vitesse = 0.4)`: tourne le robot dans la direction et à la vitesse donnée.
- direction: prend la valeur `LEFT` ou `RIGHT`.
- vitesse: nombre entre 0 et 2 (inclus). Correspond au nombre de tours de roue
    secondes.

`bot.rotate(direction, vitesse = 0.4)`: tourne le robot sur lui-même dans la direction
et à la vitesse donnée.
- direction: prend la valeur `LEFT` ou `RIGHT`.
- vitesse: nombre entre 0 et 2 (inclus). Correspond au nombre de tours de roue
    secondes.

### <span style="font-family: Courier;">[Informations additionnelles: Durée de déplacement]</span>

Pour indiquer la durée de la commande, il faut la succéder de `sleep(secondes)`,
avec `secondes` le temps en secondes de la commande.

```py
bot.forward() # Démarre les roues
sleep(1)      # Continue à avancer durant 1 seconde
bot.stop()    # Stop les roues
```

### <span style="font-family: Courier;">[Sous-Module LEDs]</span>

`LEFT` / `RIGHT` / `ALL` : variables pour le choix des phares. À utiliser en paramètre.
`FRONTLEFT` / `FRONTRIGHT` / `BACKLEFT` / `BACKRIGHT` / `ALL` : variable pour le choix des leds.
À utiliser en paramètre.

`bot.set_headlight(light, status)` : allume ou éteint un des phares avant,
- `light` : prend la valeur `LEFT`, `RIGHT` ou `ALL`
- `statut` : prend la valeur `ON` pour allumer, `OFF` pour éteindre

`bot.turn_on_led(led, couleur)` : allume la led correspondante avec la couleur donnée.
- `led` : prend la valeur `FRONTLEFT`, `FRONTRIGHT`, `BACKLEFT`, `BACKRIGHT` ou `ALL`
- `couleur : de la forme `(rouge, vert, bleu)`, les variables `rouge`, `vert` et `bleu`
    allant de 0 à 255 inclus.

`bot.turn_off_led(led)` : éteint la led correspondante.
- `led` : prend la valeur `FRONTLEFT`, `FRONTRIGHT`, `BACKLEFT`, `BACKRIGHT` ou `ALL`

### <span style="font-family: Courier;">[Sous-Module Répétition]</span>

```py
for i in range(repetition):
    bloc
    bloc
```

`range(repetition)` : indique à la boucle le nombre de répétition.
- `repetition` : remplacer par le nombre souhaité de répétitions.

`i` : remplacé par le nombre actuel de répétition, la première étant au numéro 0.
Ce nombre de répétitions étant un chiffre, il est donc possible de l'utiliser
pour effectuer des opérations.

### <span style="font-family: Courier;">[Informations additionnelles: Indentation]</span>

Une indentation sert à définir des blocs. Elle est composée de 4 espaces et peut
être ajoutée à l'aide de la touche `TAB`.

Ajouter une indentation crée un bloc, enlever une indentation le ferme et revient
au bloc précédent.

Un bloc doit être défini après toute apparition du caractère `:`.

### <span style="font-family: Courier;">[Informations additionnelles: Opérations]</span>

Il existe 4 types d'opérations sur les nombres :
- `+` (addition)
- `-` (soustraction)
- `*` (multiplication)
- `/` (division)

Il est possible de faire des opérations sur toute commande remplacée par un nombre.

### <span style="font-family: Courier;">[Sous-Module Détection]</span>

`LEFT` / `RIGHT` : variables pour le choix des capteurs. À utiliser en paramètre.

`bot.distance()` : donne la distance entre le robot et les obstacles en face de lui.

`bot.floor_sensor(capteur)` : renvoie True si le capteur détecte du blanc.
- `capteur` : prend la valeur `LEFT` ou `RIGHT`

### <span style="font-family: Courier;">[Sous-Module Analyse]</span>

```py
if condition1:
    bloc1
elif condition2:
    bloc2
else:
    bloc3
```

`if condition` : exécute les commandes du bloc si `condition` est vraie.

`elif condition` : exécute les commandes du bloc si `condition` est vraie, et
si la condition du bloc au dessus est fausse.

`else` : exécute les commandes du bloc si la condition du bloc au dessus est fausse.

### <span style="font-family: Courier;">[Informations additionnelles: Conditions]</span>

Une condition peut prendre la valeur `True` ou `False`. Il existe 3 mot clés
permettant de faire des opérations avec :

- `not` (pas) qui inverse la condition
- `and` (et) qui prend la valeur `True` si les 2 conditions sont vraies
- `or` (ou) qui prend la valeur `True` si seulement une des 2 conditions est vraie

Une condition peut également être créer à partir de nombres à l'aide de comparateurs.
Il en existe 6 :

- `==` (égalité)
- `!=` (différence)
- `<` (inférieur)
- `>` (supérieur)
- `<=` (inférieur ou égal)
- `>=` (supérieur ou égal)
