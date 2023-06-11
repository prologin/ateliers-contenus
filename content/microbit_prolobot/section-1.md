---
show_toc: false
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


