---
show_toc: true
---

# <span style="font-family: Courier;">[Lancement Module Automatisation]</span>

Dans le cas de missions plus importantes, le robot se devra de réagir à la situation
sans instructions externes. Ce module donne donc les bases permettant d'automatiser
les déplacement du robot.

## <span style="font-family: Courier;">[Lancement Sous-Module Détection]</span>

Le robot peut suivre les commandes qui lui ont été données, mais il peut également
envoyer des informations sur son état au programme.

Il existe 2 commandes permettant d'indiquer l'état du robot : `bot.distance()`
et `bot.floor_sensor(capteur)`.

La commande `bot.distance()` va utiliser les capteurs frontaux du robot pour
déterminer la distances en centimètres des obstacles sur son chemin. Une fois
envoyée au robot, la commande va ensuite être remplacée dans le programme par
la valeur de cette distance.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Erreurs lors de l'exécution (ID: EWHTRUE)]</span>

{{% box type="error" title="ID: EDIST" %}}

En raison de limitations techniques, le capteur ne détecte uniquement les
obstacles entre 2cm et 400cm de distance. Tout objet plus proche ou plus loin
ne sera pas reconnu.

{{% /box %}}

<span style="font-family: Courier;">[Erreurs supprimées]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Voici où ils sont situés sur le robot :

{{<figure src="resources/images/distance_captors_location.png" width=50% >}}

La commande `bot.floor_sensor(capteur)` permet d'utiliser les capteurs en dessous
du robot. La valeur `capteur` doit être remplacée par `LEFT` ou `RIGHT` pour
déterminer quel capteur utiliser. Une fois envoyée au robot, la commande va être
remplacée par `True` si le robot se déplace sur une zone noire, `False` autrement.

Voici où ils sont situés sur le robot :

{{<figure src="resources/images/floor_captors_location.png" width=50% >}}

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Informations incomplètes (ID: ICOND)]</span>

{{% box type="info" title="ID: ICOND" %}}

Une condition est valeur qui peut être remplacée par `True` (vrai) ou `False` (faux).
Les conditions peuvent être utilisées pour déterminer l'action qui suit.
Il est également possible d'effectuer des opérations avec :

- Le mot clé `not` (pas) va remplacer la condition par son inverse. `not True`
    (pas vrai) devient donc `False` (faux) et inversement.

- Le mot clé `and` (et) permet d'associer 2 conditions différentes. L'instruction
    sera remplacée par `True` si les **2 conditions sont vraies**.

- Enfin, le mot clé `or` (ou) remplacera les 2 conditions par `True` si **au moins
    l'une des 2** est vraie.

Voici un exemple pour illustrer le comportement de ces différentes opérations :

```codepython
print("Mot clé not")
print("not True  ->", not True)
print("not False ->", not False)
print("\nMot clé and") # '\n' indique à l'ordinateur de revenir à la ligne
print("True and False  ->", True and False)
print("False and False ->", False and False)
print("True and True   ->", True and True)
print("\nMot clé or")
print("True or False  ->", True or False)
print("False or False ->", False or False)
print("True or True   ->", True or True)
```

Toute commande remplacée par une condition est également considérée comme tel,
et peut donc être utilisée pour effectuer des opérations.

{{% /box %}}

<span style="font-family: Courier;">[Informations à jour]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

## <span style="font-family: Courier;">[Lancement Sous-Module Analyse]</span>

Il est possible de déterminer une action en fonction d'une condition à l'aide
de la commande `if`.
Voici comment elle est utilisée :

```py
if condition:
    bloc
```

Un élément important à noter est la présence du caractère `:` après la condition
annonçant la création d'un bloc. En effet la commande `if` enverra les instructions
du bloc au robot uniquement si la `condition` est vraie.

En voici donc un exemple d'utilisation :

```py
from prolobot import *
bot = Prolobot()

if not bot.floor_sensor(LEFT) and not bot.floor_sensor(RIGHT):
    bot.turn_on_led(ALL, (0, 255, 0))
```

Dans cet exemple, le robot va donc allumer toutes ses LEDs si le capteur de 
gauche **ne détecte pas** du noir **et** le capteur de droit **ne détecte pas**
du noir non plus.

Le robot peut également déterminer les actions à effectuer avec le mot clé `else`.
Celle-ci peut être indiquée uniquement après le bloc d'une commande `if`.

Les commandes du bloc `else` ne seront envoyées aux composants du robot uniquement
si la condition du `if` n'a pas été validée, et donc si les commandes de son bloc
n'ont pas été envoyées.

Ces 2 mot clés peuvent se traduire par 'si ...' et 'sinon'.

Voici une suite de l'exemple d'utilisation précédent :

```py
from prolobot import *
bot = Prolobot()

if not bot.floor_sensor(LEFT) and not bot.floor_sensor(RIGHT):
    bot.turn_on_led(ALL, (0, 255, 0))
else:
    bot.turn_off_led(ALL)
```

Il existe également un 3ème mot clé qui correspond à la contraction des 2 précédents :
le mot clé `elif` (sinon, si ...).

Pour illustrer cette contraction, voici un court programme avec plusieurs commandes
`if` et `else` :

```py
if condition1:
    bloc1
else:
    if condition2:
        bloc2
    else:
        bloc3
```

Comme vous pouvez le voir, si la `condition1` n'est pas vraie, le programme
va donc analyser le bloc `else` et vérifier la `condition2`.

Voici un autre programme utilisant `elif` et faisant exactement la même chose :

```py
if condition1:
    bloc1
elif condition2:
    bloc2
else:
    bloc3
```

Ce programme ce comportera de la même manière que le précédent :
si la `condition1` est fausse, le programme analysera la `condition2`.

Voici comment il est possible de modifier l'exemple d'utilisation précédent avec
ces informations :

```py
from prolobot import *
bot = Prolobot()

if not bot.floor_sensor(LEFT) and not bot.floor_sensor(RIGHT):
    bot.turn_on_led(ALL, (0, 255, 0))
elif not bot.floor_sensor(LEFT):
    bot.turn_on_led(FRONTLEFT, (0, 0, 255))
    bot.turn_on_led(BACKLEFT, (0, 0, 255))
elif not bot.floor_sensor(RIGHT):
    bot.turn_on_led(FRONTRIGHT, (0, 0, 255))
    bot.turn_on_led(BACKRIGHT, (0, 0, 255))
else:
    bot.turn_off_led(ALL)
```

Les mots clés `if`, `elif` et `else` sont également utilisables avec des
conditions provenant d'une transformation.
Essayez ce code sur votre robot pour tenter de comprendre ce qu'il fait ! Si vous avez des questions, n'hésitez pas à vous adresser à un technicien de qualification supérieure. 
<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Informations incomplètes (ID: ITRCOND)]</span>

{{% box type="info" title="ID: ITRCOND" %}}

Tout nombre peut être transformé en condition à l'aide de comparateurs. Voici
la liste des comparateurs reconnus par le robot :

- `==` permet d'indiquer l'égalité, et sera remplacé par `True` uniquement si
    les 2 nombres sont identiques, `False` dans le cas contraire ;
- `!=` permet d'indiquer la différence, et sera remplacé par `True` si les 2 nombres
    sont différents, `False` autrement.

Voici un exemple permettant d'afficher par quoi ces comparateurs sont remplacés :

```codepython
print("Comparateur ==")
print("1 == 1 ->", 1 == 1)
print("1 == 2 ->", 1 == 2)
print("\nComparateur !=")
print("1 != 1 ->", 1 != 1)
print("1 != 2 ->", 1 != 2)
```

Il existe également des comparateurs dit 'comparateurs d'ordre'. Ceci permettent
d'indiquer si 2 nombres sont ordonnées.

Prenons 2 nombres quelconques. Étant quelconques, il n'est pas possible de
connaître en avance de quel nombre il s'agit, nous les nommerons donc `a` et `b`.

- `a < b` est remplacé par `True` uniquement si le chiffre que représente `a` est
*plus petit* que `b` ;
- `a > b` en revanche, est remplacé par `True` si `a` est *plus grand* que `b`.

Voici un exemple affichant le comportement de ces comparateurs :

```codepython
print("Comparateur <")
print("1 < 1 ->", 1 < 1)
print("1 < 2 ->", 1 < 2)
print("3 < 1 ->", 3 < 1)
print("\nComparateur >")
print("1 > 1 ->", 1 > 1)
print("1 > 2 ->", 1 > 2)
print("3 > 1 ->", 3 > 1)
```

Les comparateurs peuvent également être combinés comme ceci :
- `a <= b` est remplacé par le programme par `True` si `a` est plus petit que `b`
    **ou** `a` est égal à `b` ;
- `a >= b` est remplacé par `True` si `a` est plus grand que `b` **ou** `a` est
    égal à `b`.

Voici un exemple permettant d'illustrer le fonctionnement de ces comparateurs :

```codepython
print("Comparateur <=")
print("1 <= 1 ->", 1 <= 1)
print("1 <= 2 ->", 1 <= 2)
print("3 <= 1 ->", 3 <= 1)
print("\nComparateur >=")
print("1 >= 1 ->", 1 >= 1)
print("1 >= 2 ->", 1 >= 2)
print("3 >= 1 ->", 3 >= 1)
```

Il est important de noter que toute commande remplacée par un nombre est considérée
comme tel, et peut donc également être transformé en condition.

{{% /box %}}

<span style="font-family: Courier;">[Informations à jour]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Il est également possible d'indiquer au robot de répéter des commandes *tant que*
la condition n'est pas égale à `True`, donnant naissance au mot clé `while`.
Voici comment il est utilisé :

```python
while condition:
    bloc
```

Le mot clé `while` va donc répéter les commandes du bloc *tant que* la condition
est vraie.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Erreurs lors de l'exécution (ID: EWHTRUE)]</span>

{{% box type="error" title="ID: EWHTRUE" %}}

Bien qu'il soit possible de remplacer la valeur condition par `True`, cette
pratique est prohibée au sein du labo car cela rendrait le robot incapable de
s'arrêter.

De la même manière, l'usage de la commande la commande `while False:` est déconseillée
car toute commande située dans le bloc ne seraient jamais envoyée au robot.

{{% /box %}}

<span style="font-family: Courier;">[Erreurs supprimées]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Voici un exemple mettant en scène les éléments du module :

```py
from prolobot import *
bot = Prolobot()

for i in range(3):
    if i == 0:
        bot.turn_on_led(ALL, (255, 0, 0))
    elif i == 1:
        bot.turn_on_led(ALL, (0, 255, 0))
    else:
        bot.turn_on_led(ALL, (0, 0, 255))

    sleep(1)

bot.turn_off_led(ALL)

while bot.distance() >= 10:
    bot.rotate(LEFT)

bot.stop()
```

Tout technicien du labo est vivement invité à envoyer cet exemple au Prolobot,
afin d'en étudier le comportement.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Demande d'intervention (ID: MRECTDTC)]</span>  

{{% box type="exercise" title="ID: MRECTDTC" %}}

Une mission vous a été confiée.

Suite à une mise à jour des balises, il n'est plus nécessaire de former un carré
parfait pour définir le périmètre. La zone doit tout de même rester rectangulaire.

Les robots doivent donc couvrir la plus grande zone possible. Celle-ci est
définie par une bande *noire* visible sur le sol, chaque robot se doit donc
de poser une balise à l'apparition de cette ligne.

En cas d'obstacle en face de lui, le robot se doit d'ignorer la recherche de la
bande noire et poser une balise immédiatement.

Le signalement reste inchangé malgré ces modifications.

Veuillez donc mettre à jour le programme des robots pour satisfaire ces nouvelles
conditions.

Le ProloLab vous souhaite bonne chance. 

{{% /box %}}

<span style="font-family: Courier;">[Rapport de mission reçu]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>  


