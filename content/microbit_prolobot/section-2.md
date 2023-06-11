---
show_toc: true
---

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


