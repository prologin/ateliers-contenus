---
show_toc: true
---

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


