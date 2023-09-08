# Passons à la pratique !

Il va falloir maintenant que tu écrives le programme pour Skeleton ! Ne
t'inquiète pas, nous allons te guider pour rédiger ton code ! Si tu as la
moindre question, n'hésite pas à la poser aux organisateurs présents !

Nous t'invitons d'abord à télécharger le code source à modifier en cliquant sur
le bouton `Code à compléter` en haut de la page ! Tu retrouveras dans le fichier
donné un code non complet que tu ne peux pas encore lancer. Il va falloir le
remplir avec tes nouvelles connaissances.

{{% box type="warning" title="Code incomplet !" %}}

Différentes parties du code sont manquantes ! Elles sont désignées par le
mot-clé `TODO` qui se traduit par "À faire" en français. Tout au long du sujet,
tu vas pouvoir compléter le code en écrivant juste en dessous des commentaires
(les lignes de code commençant par un `#`).

{{% /box %}}

## Les possibilités d'affichage

{{% box type="exercise" title="Mission 1 : Les différentes possibilités" %}}

Dans la variable `possibilites`, il faut que tu rajoutes une liste de toutes les
images possibles que tu devras afficher à l'écran. Les images qui doivent
apparaître sont `Image.SKULL`, `Image.PACMAN` et `Image.GHOST`.

<br/>

Tu vas devoir également trouver la longueur de ta liste `possibilites`. Pour
cela, sers-toi de la fonction `len`. Tu dois mettre ce nombre dans la variable
`NB_POSSIBILITES`.

{{% /box %}}

## La boucle du jeu pour la sélection du personnage

L'utilisateur du `micro:bit` doit choisir son personnage. Pour faire cela, on va
utiliser une boucle `while` (tant que). Il va falloir alors trouver une
condition pour rester dans la sélection. Pour valider, le joueur devra appuyer
sur les deux boutons du `micro:bit` en même temps.

{{% box type="exercise" title="Mission 2 : La sélection du personnage" %}}

Dans la condition de ta boucle, il faut vérifier si les boutons A et B ne sont
pas pressés. Tu vas devoir alors utiliser le `and` et le `not` que nous avons vu
précédemment.

{{% /box %}}

{{% box type="exercise" title="Mission 3 : Affichage du choix actuel" %}}

Tant qu'on reste dans notre boucle `while`, il va falloir afficher le choix qui
est actuellement sélectionné. Pour ce faire, tu peux utiliser la fonction
`display.show()` avec comme paramètre l'image dans la liste `possibilites` à
l'indice du choix du joueur défini par la variable `choix_joueur`.

{{% /box %}}

{{% box type="exercise" title="Mission 4 : Changement de choix" %}}

Si le bouton A a été appuyé, il faut enlever 1 au nombre désignant le choix du
joueur. Cependant, il se peut qu'à un moment donné, tu sors en dehors ta liste.
Pour éviter cela, tu peux utiliser des conditions ou des modulos (`%`).

Nous allons voir en détails les conditions, mais si tu souhaites utiliser Les
modulos, n'hésite pas à appeler un organisateur pour qu'il puisse t'aider !

<br/>

Il faut vérifier si `choix_joueur` n'est plus dans ta liste, c'est-à-dire si
l'index qu'il représente n'est pas possible dans la liste `possibilites`. Pour
rappel, les valeurs possibles sont `0`, `1` et `2` dans la liste.

<br/>

Maintenant, tu dois faire la même chose pour le bouton B, seulement,
cette fois-ci, si le bouton B a été appuyé, il faut rajouter 1 au nombre
désignant le choix du joueur. N'oublie pas le modulo !

{{% /box %}}

## Le choix de l'ordinateur

{{% box type="exercise" title="Mission 5 : Le choix de l'ordinateur" %}}

Le choix de l'ordinateur doit se faire de manière aléatoire. La variable
`choix_adversaire` doit correspondre à un indice dans la liste `possibilites`.
Sachant que les éléments d'une liste en Python sont numérotés de 0 à la longueur
de la liste moins 1, il te faudra générer un nombre dans l'intervalle en
question.

{{% /box %}}

## Aficher le choix du joueur

{{% box type="exercise" title="Mission 6 : Affichage des choix" %}}

Comme pour le début de la boucle, il faut que tu réaffiches le choix du joueur
après le `display.clear()` qui éteint tous les pixels.

<br/>

Après l'affichage du texte "VS", il faut que tu affiches maintenant le choix
de l'adversaire en prenant une image dans la liste `possibilites` à l'indice
`choix_adversaire`.

{{% /box %}}

## Gagnant et perdant

{{% box type="exercise" title="Mission 7 : Qui a gagné ? Qui a perdu ?" %}}

Il faut maintenant trouver qui a gagné et qui a perdu ! Pour ce faire, on
va d'abord vérifier s'il y a égalité entre les deux joueurs.

<br/>

Il y a égalité entre les deux joueurs dans notre jeu quand le choix de
notre adversaire et le même que le nôtre. Il faut alors vérifier l'égalité
entre `choix_joueur` et `choix_adversaire`. Il faut alors afficher sur le
`micro:bit` "Egalite !" avec une vitesse d'affichage de 50.

<br/>

Sinon, s'il n'y a pas égalité, il faut vérifier les conditions pour savoir
si on a gagné. Atention, il faudra alors afficher "Gagne !" avec une vitesse
d'affichage de 50. Les conditions sont les suivantes :

- Si `choix_joueur` est égal à 0 et `choix_adversaire` est égal à 1
(Skeleton fait peur à Pacman)

- Si `choix_joueur` est égal à 1 et `choix_adversaire` est égal à 2
(Pacman mange Bouh)

- Si `choix_joueur` est égal à 2 et `choix_adversaire` est égal à 0
(Bouh fait peur à Skeleton)

<br/>

Enfin, sinon, si toutes les conditions au-dessus ne sont pas remplies,
cela veut dire que tu as perdu et il faut que tu affiches "Perdu..." avec
une vitesse d'affichage de 50.

{{% /box %}}