---
title: Prolobot
date: 2022
authors: Julie 'DaiF' Fiadino
subtitle: Codez avec le Robot Microbit
code_stub_url: "./resources/given_resources/prolobot.py"
---

<span style="font-family: Courier;">[Initialisation Procédure Formation]</span>  
<span style="font-family: Courier;">[ID: PROLOBOT]</span>  
<span style="font-family: Courier;">[Chargement des modules]</span>  
<span style="font-family: Courier;">[Chargement terminé]</span>  

# <span style="font-family: Courier;">[Lancement Module Introduction]</span>

Bonjour et bienvenue à ProloLab, un labo spécialisé dans la création de robots !
Vous avez été assigné à l'un de nos récents projets secrets : le _Prolobot_.

Le _Prolobot_ est un robot qui fonctionne à l'aide d'une carte électronique appelée `micro:bit`.
Ce robot est contrôlé en envoyant une suite d'instructions sur la carte, qui
va ensuite transmettre les informations aux autres composants.

Cet ensemble d'instructions s'appelle un _"programme"_. En tant que nouveau technicien
de notre labo, vous vous devez d'apprendre à les écrire.
Tout au long de la mission, vous allez être accompagnés par des _techniciens de qualification supérieure_. N'hésitez pas à faire appel à eux en cas de problème. 

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Informations incomplètes (ID: IEDITOR)]</span>

{{% box type="info" title="ID: IEDITOR" %}}

Pour s'assurer d'une communication réussie avec le robot, nous vous avons fourni
un fichier permettant d'envoyer des commandes spécifiques. Veuillez donc le 
télécharger en cliquant [ici](./resources/given_resources/prolobot.py) ou sur le
bouton _Code à compléter_ en haut de cette page.

Pour l'édition des programmes, tous nos techniciens utilisent le site
[python.microbit.org](https://python.microbit.org/). Afin de charger les fichiers
utilitaires, veuillez cliquer sur le bouton `Ouvrir...` présenté ci-dessous.

{{<figure src="resources/images/open_button.png" >}}

Sélectionnez ensuite le fichier téléchargé `prolobot.py`. Avant de confirmer,
appuyez sur le bouton indiqué ci-dessous.

{{<figure src="resources/images/load_button.png" >}}

Changez ensuite pour l'option `Ajouter le fichier prolobot.py`. Vous pouvez
maintenant confirmer.

Afin d'envoyer le code au robot, veuillez brancher le haut de la carte électronique
à l'ordinateur et appuyer sur le bouton `Envoyer vers micro:bit` comme ci-dessous :

{{<figure src="resources/images/send_button.png" >}}

En cas de problème, veuillez appeler un technicien de qualification supérieure pour qu'il vous montre
la procédure.

{{% /box %}}

<span style="font-family: Courier;">[Informations à jour]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Tout programme contrôlant le prolobot est précédé de ces 2 lignes :

```py
from prolobot import *
bot = Prolobot()
```

La première ligne charge le fichier utilitaire dans le programme, la seconde
permet de créer un robot. Par convention du labo, le robot est nommé bot.

[SECTION-BREAK]

# <span style="font-family: Courier;">[Lancement Module Déplacement]</span>

Ce module a pour but de vous montrer comment fonctionne le déplacement du robot.
Toutes ces commandes permettent d'activer les roues du robots de manière
différentes. Il est important que vous en saisissiez la nuance.

## <span style="font-family: Courier;">[Lancement Sous-Module Avancée]</span>

Le robot avance après avoir reçu la commande `bot.forward()`.

Le nombre de tours de roue par secondes peut également être précisé comme ceci :
`bot.forward(0.6)`. Pour des raisons de clarté, nous appelerons _vitesse_ ce 
nombre de tours de roue. Lorsqu'elle n'est pas précisée, la vitesse utilisée
est `0.4`.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Erreurs lors de l'exécution (ID: ESPEED)]</span>

{{% box type="error" title="ID: ESPEED" %}}

En raison des moteurs utilisés, la vitesse ne peut aller au delà de 2.
Une mauvaise utilisation pourrait endommager le robot.

{{% /box %}}

<span style="font-family: Courier;">[Erreurs supprimées]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Le robot peut également reculer à l'aide de la commande `bot.backward()`.
Les précisions de vitesse fonctionnent de la même manière que la précédente.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Vulnérabilité détectée (ID: WSTOP)]</span>

{{% box type="warning" title="ID: WSTOP" %}}

Les commandes `forward` et `backward` activent les moteurs mais ne les désactivent
pas. Pour arrêter le robot, il est nécessaire d'utiliser la commande `bot.stop()`

{{% /box %}}

<span style="font-family: Courier;">[Vulnérabilité prise en charge avec succès]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Voici donc un programme illustrant les différents éléments abordés :

```py
from prolobot import *
bot = Prolobot()

bot.forward()
sleep(1)
bot.backward(1)
sleep(2)
bot.stop()
```

Nous vous conseillons fortement de tester ce programme afin d'en comprendre les
détails.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Informations incomplètes (ID: ISLEEP)]</span>

{{% box type="info" title="ID: ISLEEP" %}}
La commande `sleep(time)` permet de mettre en pause le programme pour une durée
de `time` secondes. 

Les commandes `forward` et `backward` n'arrêtant pas les moteurs, les succéder
d'un sleep permet d'indiquer la durée de celles-ci.

Le programme ci-dessous indique donc au robot d'avancer à une vitesse de 0.2
pour une durée de 2 secondes, puis reculer durant 1 seconde, avant de s'arrêter.

```py
from prolobot import *
bot = Prolobot()

bot.forward(0.2)
sleep(2)
bot.backward()
sleep(1)
bot.stop()
```

{{% /box %}}

<span style="font-family: Courier;">[Informations à jour]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

## <span style="font-family: Courier;">[Lancement Sous-Module Rotation]</span>

Le robot peut-être tourné à l'aide de 2 commandes différentes :
- `bot.turn(direction)`
- `bot.rotate(direction)`

La valeur `direction` doit être remplacée par les mots `LEFT` ou `RIGHT`, indiquant
au robot de tourner respectivement à gauche et à droite.

Une vitesse peut y être précisé comme ceci : `bot.turn(direction, 0.5)`.
Les spécifications de la vitesse sont les mêmes que les fonctions précédentes.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Informations incomplètes (ID: IROTATURN)]</span>

{{% box type="info" title="ID: IROTATURN" %}}

Les commandes `rotate` et `turn` sont similaires mais contiennent une différence cruciale :
la manière dont ils *pivotent*.

La commande `turn` va activer une des 2 roues pour faire tourner le robot. La commande
`rotate` va activer les 2 roues pour le faire pivoter sur lui même.

Voici 2 exemples visuels pour illustrer cette différence :

- `bot.turn(LEFT)`
{{<figure src="resources/images/maqueen_turn.gif" width=50% >}}
- `bot.rotate(LEFT)`
{{<figure src="resources/images/maqueen_rotate.gif" width=50% >}}

{{% /box %}}

<span style="font-family: Courier;">[Informations à jour]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Voici donc un programme illustrant les éléments du sous-module de rotation :

```py
import prolobot
from microbit import *
bot = Prolobot()

bot.turn(RIGHT)
sleep(1)

bot.rotate(LEFT)
sleep(1)

bot.turn(LEFT, 1.0)
sleep(1)

bot.rotate(RIGHT, 0.3)
sleep(1)

bot.stop()
```

Tout comme le précédent, il vous est fortement conseillé de tester ce programme
avec votre propre Prolobot.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Demande d'intervention (ID: MSECUPERI)]</span>  

{{% box type="exercise" title="ID: MSECUPERI" %}}

Une mission vous a été confiée.

Le Prolobot va être envoyé en territoire inconnu pour sécuriser le périmètre. 

Pour que cela fonctionne, le robot doit poser 4 balises aux coins d'un carré parfait. 
On considère qu'une balise est posée après une rotation complète du robot. 

Le ProloLab vous souhaite bonne chance. 

{{% /box %}}

<span style="font-family: Courier;">[Rapport de mission reçu]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>  

[SECTION-BREAK]

# <span style="font-family: Courier;">[Lancement Module Signalement]</span>

Le but de ce module est de vous montrer comment le robot signale ses intentions aux utilisateurs
externes. Il est important de le maîtriser avant d'envoyer le robot en mission.

## <span style="font-family: Courier;">[Lancement Sous-Module LEDs]</span>

Afin de signaler ses intentions, le robot est composé de 2 types différents de
LEDs : 2 à l'avant, nommée phares, et 4 en dessous que nous nommerons simplement LEDs.

Les phares peuvent être contrôlés à l'aide de la commande `bot.set_headlight(led, state)`.
La valeur led doit être remplacée par `LEFT` ou `RIGHT` pour indiquer quel phare contrôler.
La valeur state, quant à elle, indique l'état du phare. Elle doit être remplacée
par `ON` pour l'allumer et `OFF` pour l'éteindre.

Pour une communication plus avancée, il est nécessaire d'utiliser les leds en
raison de leur capacité à changer de couleur.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Informations incomplètes (ID: ICOLOR)]</span>

{{% box type="info" title="ID: ICOLOR" %}}

La couleur des LEDs est définie en suivant le format RGB (_Red Green Blue_, qui signifie _Rouge Vert Bleu_ en anglais).
Une couleur est donc représentée ainsi : `(rouge, vert, bleu)` avec les valeur
rouge, vert et bleu étant des entiers entre 0 et 255 (inclus).

Ces valeurs correspondent respectivement à la quantité de rouge, de vert et de bleu.
Elles vont ensuite être utilisées par le robot pour déterminer le mélange de
couleur final.

Voici quelques exemples de mélanges :
- rouge : (255, 0, 0)
- vert : (0, 255, 0)
- bleu : (0, 0, 255)
- cyan : (0, 255, 255)
- jaune : (255, 255, 0)

En raison de la difficulté de visualisation de ce système, il est vivement
conseillé aux techniciens du labo d'utiliser un [ColorPicker](https://www.colorspire.com/rgb-color-wheel/)
pour plus de simplicité lors du choix des couleur.

{{% /box %}}

<span style="font-family: Courier;">[Informations à jour]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Les LEDs peuvent être contrôlées à l'aide des commandes `bot.turn_on_led(led, color)`
et `bot.turn_off_led(led)`.

La valeur `led` doit être remplacée par `FRONTLEFT`, `FRONTRIGHT`, `BACKLEFT` ou
`BACKRIGHT` afin d'indiquer la led selectionnée. Voici un schéma indiquant où se trouvent
les leds :

{{<figure src="resources/images/leds_position.png" width=50% >}}

La valeur `color` est quant à elle remplacée par une couleur au format RGB.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Informations incomplètes (ID: ICSTALL)]</span>

{{% box type="info" title="ID: ICSTALL" %}}

Pour des raisons de simplicité, il est aussi possible de remplacer la valeur
`led` par la constante `ALL`, afin d'allumer ou d'éteindre **toutes** les LEDs simultanément.

Cette constante est aussi utilisable dans le cadre de la commande
`set_headlight(led, state)`.

{{% /box %}}

<span style="font-family: Courier;">[Informations à jour]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Voici un programme illustre tous les modules que nous avons abordés jusqu'ici :

```py
from prolobot import *
bot = Prolobot()

bot.turn_on_led(ALL, (0, 255, 0))
bot.rotate(LEFT)
bot.set_headlight(LEFT, ON)
sleep(2)

bot.set_headlight(ALL, OFF)
bot.backward()
bot.turn_on_led(BACKLEFT, (255, 0, 0))
bot.turn_on_led(BACKRIGHT, (255, 0, 0))
sleep(2)

bot.stop()
bot.turn_off_led(ALL)
```

Le labo vous invite à envoyer ce programme à votre Prolobot afin d'en comprendre
le fonctionnement.

## <span style="font-family: Courier;">[Lancement Sous-Module Répétition]</span>

Afin de diminuer le nombre de commandes du programme, il est possible de les
répéter plusieurs fois à l'aide d'une commande nommée la boucle `for`.

Voici un exemple d'utilisation (vous pouvez cliquer sur _Run_ pour afficher ce qu'il se passe) :

```codepython
for i in range(2):
    print("Ceci est la commande 1")
    print("Et ceci, la commande 2")
```

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Informations incomplètes (ID: IPRINT)]</span>

{{% box type="info" title="ID: IPRINT" %}}

La commande `print` permet d'afficher le texte compris entre les guillemets.
Elle n'est pas reconnue par le robot et est donc présentée ici uniquement à des
fins de démonstration.

{{% /box %}}

<span style="font-family: Courier;">[Informations à jour]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Il est important de noter plusieurs choses :
1. Le nombre à l'intérieur de la commande `range()` permet d'indiquer le nombre
    de répétitions ;
2. Le début de la liste des commandes à répéter est annoncée à l'aide d'un `:`.
    Ces `:` se doivent d'être sur la même ligne que la commande `for`. Par 
    convention du labo, ils seront également attachés au caractère précédent ;
3. Toutes les commandes à répéter sont reconnaissable car ayant la même **indentation**.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Vulnérabilité détectée (ID: WINDENT)]</span>

{{% box type="warning" title="ID: WINDENT" %}}

L'indentation correspond à une quantité d'espacement avant la commande. Par
convention du labo, une indentation correspond à 4 espaces. Celle-ci peut être
ajoutée rapidement à l'aide de la touche `TAB` (la touche juste au dessus de la touche _Verrouillage Majuscule_).

Bien que l'indentation puisse correspondre à 2 ou 6 espaces, il est important
que le nombre d'espaces par indentations soit le même sur l'entièreté du programme.
Cela est dû au fait que l'indentation permette de définir des blocs :

```py
bloc1
bloc1
    bloc2
    bloc2

    bloc2

bloc1

    bloc3
        bloc4
    bloc3
```

Comme vous pouvez le remarquer, augmenter d'une indentation permet de définir
un nouveau bloc. Revenir d'une indentation en arrière ferme le bloc et fait
revenir le programme au bloc précédent.

Tout programme démarre avec une indentation de 0 et celle-ci est augmentée de 1
à chaque apparition du caractère `:`. La boucle répètera alors les commandes
du bloc ainsi créé.

{{% /box %}}

<span style="font-family: Courier;">[Vulnérabilité prise en charge avec succès]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>

Le dernier élément qu'il vous faut comprendre est l'utilité de la valeur `i`.
Cette valeur va être automatiquement remplacée par le numéro de répétition de
la boucle. En voici un exemple :

```codepython
for i in range(4):
    print("Ceci est la répétition", i)
print("Ceci est la fin de la répétition")
```

Il est important de noter que cette numérotation démarre à 0. Ce `i` étant
remplacé par un chiffre, il est donc possible de l'utiliser pour faire
des calculs (addition avec `+`, soustraction avec `-`, multiplication avec `*`
et division avec `/`).

Voici donc un exemple d'utilisation avec le robot :

```py
from prolobot import *
bot = Prolobot()

for i in range(2):
    bot.forward(i + 1)
    sleep(1) # Attend 1 seconde avant de recommencer la boucle

bot.stop()
```

Il est recommandé de tester cet exemple avec votre propre robot, afin d'en
comprendre le fonctionnement.

<span style="font-family: Courier;">[Procédure mise en pause...]</span>  
<span style="font-family: Courier;">[Demande d'intervention (ID: MPSGNL)]</span>  

{{% box type="exercise" title="ID: MPSGNL" %}}

Une mission vous a été confiée.

Un rapport de mission récent indique que certains robots ont été interrompus lors
de la sécurisation du périmètre. Voici les annonces récentes à ce sujet :

> Les robots furent interrompus dans leur mission en raison d'un manque de
> communication quant au stade d'avancement de la sécurisation.
> Désormais les robots devront indiquer leur direction à l'aide des phares avant :
> *2 phares* allumés lors d'une avancée en ligne droite, *un seul phare* lors de 
> la rotation pour indiquer la direction de celle-ci. À la fin de la sécurisation,
> soit après la formation complète du carré, les phares doivent être éteints.
> Les robots devront également signaler l'étape en cours à l'aide du code couleur
> suivant : *rouge* lors de la pose d'une balise, *orange* lors du déplacement.
> À la fin de la sécurisation, le robot devra afficher 2 fois la lumière *bleue*.

Il vous faut donc mettre à jour les instructions du robot en fonction de ces
nouvelles règlementations.

Le ProloLab vous souhaite bonne chance. 

{{% /box %}}

<span style="font-family: Courier;">[Rapport de mission reçu]</span>  
<span style="font-family: Courier;">[Reprise de la procédure]</span>  

[SECTION-BREAK]

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

[SECTION-BREAK]

<span style="font-family: Courier;">[Procédure Formation Terminée]</span>  
<span style="font-family: Courier;">[Analyse des modules...]</span>  
<span style="font-family: Courier;">[Analyse terminée]</span>  
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
