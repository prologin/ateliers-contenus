---
title: Blog
date: 2022
subtitle: Coder ton propre blog
code_stub_url: "./blog.zip"
---


# Introduction

Pendant cet atelier tu vas apprendre à créer ta propre page Web.

L'objectif va être de réaliser ton blog, que tu pourras personnaliser selon tes goûts.

{{<figure src="images/complete.png" >}}

# Qu'est-ce que c'est qu'une page internet ?

Avant toute chose, qu'est-ce qui se cache derrière une page internet ?
De nos jours, beaucoup de choses, mais à la base seulement un langage informatique, le `HTML`. Inventé en 1991 par Tim Berners-Lee, c'est simplement du texte qui va être lu par ton navigateur, qui va ensuite le traduire en éléments visibles sur l'écran.

Comme il ne s'agit que de texte, tu peux créer par toi-même une page très simplement :

1. Crée le fichier `hello_world.html` et ouvre le avec ton navigateur
2. Ouvre le également dans `Visual Studio Code` s'il est disponible, `Bloc-note` sinon
3. Écris `Hello world!`
4. Sauvegarde le fichier
5. Retourne sur ton navigateur et rafraîchit la page (touche F5)

Et voilà ! Tu viens d'écrire une page très simple qui s'affichera dans n'importe quel navigateur !

# Balises

La particularité du `HTML` par rapport à du texte simple, c'est qu'il permet de structurer la page (titres, paragraphes, liens, images, ...) à l'aide de balises.
En quelques mots, il va te permettre de donner des instructions au navigateur sur l'affichage souhaité : ``"Ceci est du texte"``, ``"Ceci est une image"``, etc.

*Mais qu'est-ce qu'une balise ?*

Une balise est composée d'un texte entouré de chevrons (les symboles `<` et `>`). Elles viennent généralement par paires : une balise ouvrante (`<nom de la balise>`) et une balise fermante (`</nom de la balise>`), permettant d'encadrer du texte pour en définir la nature.

```
du texte <titre> Le titre </titre> du texte
```

Seul le texte `Le titre`, contenu entre les balises ouvrantes `<titre>` et fermantes `</titre>` est considéré comme un titre, le reste n'est que du texte.

Voilà à quoi ça ressemblerait sur ton site :

> du texte ***Le titre*** du texte

Comme les poupées russes, les balises peuvent en contenir d'autres. Toute balise ouverte doit être fermée, donc dans l'ordre inverse d'ouverture.

```html
<a><b></b></a> <!-- Correct -->
```

Ici on ouvre `a`, puis on ouvre `b`, puis on ferme `b`, et enfin on ferme `a` ; ce qui est correct.

```html
<a><b></a></b> <!-- Incorrect -->
```

Ici on ouvre `a` puis on ouvre `b`, puis on ferme `a`, et enfin on ferme `b` ; c'est incorrect puisque les balises s'entremêlent.

Les navigateurs connaissent un certain nombre de balises, qui vont leur permettre de comprendre ce que tu veux afficher.

Dans la suite de ce TP, tu vas rencontrer petit à petit différentes balises et comprendre leur rôle. Tu auras l'occasion de les utiliser, à chaque fois dans un fichier fourni. Tu devras écrire exclusivement entre les balises `<body>` et `</body>` (nous reviendrons plus tard sur leur utilité et celle des autres balises présentes dans ce fichier).

```html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title> Mon blog </title>
    </head>

    <body>
        <!-- Écrire à la place de cette ligne -->
    </body>
</html>
```

<!-- Faudrait écrire cette partie dans une partie Note (voir new front GCC!) -->
Voici quelques explications :
- le `lang = "fr"` est un attribut de la balise `html`. Il permet de préciser la langue d'origine d'une page web et détermine le langage pour l'ensemble du texte sur la page.
- La balise `<head>` permet d'ajouter des informations à la page sans ajouter de contenu visible, comme les 2 lignes expliquées ci-dessous.
- `<meta charset="UTF-8">` permet de spécifier l'encodage des caractères de la page. "UTF-8" nous permet d'avoir les accents ('é', 'è', 'à', etc). Anciennement, lorsque UTF-8 n'existait pas, les pages web utilisaient "ASCII" comme encodage, qui supporte uniquement les nombres, les lettres de l'alphabet en majuscule et minuscule, ainsi que les caractères spéciaux (' ', '!', '$', '+', '-', '(', ')', '@', '<', '>', ',', '.').
- la balise `<title>` définit le titre de la page web dans la liste des onglets de ton navigateur.

## Balises, balises everywhere

### Titres

Comme tout bon blog qui se respecte, le tien a besoin de titres ! Le titre principal, et un titre pour chaque article.

Toutefois, tous les titres n'ont pas la même importance. En effet, comme sur une page web classique, il existe généralement en grand format le titre principal du site, puis de plus en plus petit les autres titres.

Pour représenter cette hiérarchie, les navigateurs connaissent 6 niveaux de titres, identifiés par les balises suivantes :

```html
<h1> Le titre le plus important!! </h1>
<h2> Un titre un peu moins important! </h2>
<h3> Un titre encore moins important. </h3>
...
<h6> Un titre vraiment vraiment moins important </h6>
```

Commençons donc la création de ton blog :

1. Télécharge le fichier fourni `blog.html` via le bouton `Code à compléter` en haut de la page
2. Ouvre le dans `Visual Studio Code` s'il est disponible, `Bloc-note` sinon
3. Ajoute le titre principal de ton blog avec les balises `<h1> </h1>` dans la partie `<body>`
4. Ajoute les titres de deux articles avec les balises appropriées
5. Ouvre le fichier `blog.html` dans ton navigateur

{{<figure src="images/titres.png" width=500 >}}

### Paragraphes

Des titres, c'est bien, mais un blog c'est aussi et surtout du contenu, du texte !


On a déjà vu tout à l'heure qu'il était possible de mettre du texte partout dans un fichier `HTML`, mais il est aussi important de préciser au navigateur ce qu'il représente.

Pour cela, il existe la balise ``<p>``.

```html
<h1> Ceci est un titre </h1>
<p> Ceci est un paragraphe </p>
```

Tu peux modifier le fichier ``blog.html`` pour inclure différents articles en dessous des titres ajoutés précédemment.

1. Sous le premier titre d'article, écrit un paragraphe avec la balise appropriée.
2. Sous le deuxième titre d'article, écrit deux paragraphes.

{{<figure src="images/paragraphes.png" >}}

### Indentation

Tu as pu le remarquer dans le fichier `blog.html`, toutes les lignes ne sont pas collées à gauche de l'écran, certaines sont décalées vers la droite par des espaces.

On appelle cela l'**indentation**. Indenter permet d'obtenir un code plus propre, plus lisible et donc plus compréhensible. Il sera possible de discerner plus facilement les différents éléments ou parties de code.

Il n'y a pas en HTML de règle absolue concernant l'indentation. Généralement, quand le contenu de balises s'étend sur plus d'une ligne, on indentera ce contenu d'un rang de plus que les balises. Chaque rang d'indentation est construit à l'aide de 4 espaces, ou 1 tabulation.

```html
<html>
    <body>
        <h1> Titre sur une ligne </h1>
        <p> Hello World! </p>
    </body>
</html>
```

Ici, le contenu de la balise `html` est identé d'un rang. Ensuite, le contenu de la balise `body` est indenté d'un rang de plus, donc de deux rangs.


### Mise en valeur du texte

De temps en temps, tu auras envie de mettre en valeur une partie du texte pour le faire ressortir. Une citation par exemple. Tu vas voir 2 manières de le faire.

Tu peux mettre en gras avec la balise ``<strong>`` :

```html
<p> Ceci est un <strong> mot important </strong> dans un pragraphe </p>
```

Tu peux également mettre en italique avec la balise `<em>` :

```html
<p> Ceci est aussi un <em> mot important </em> dans un pragraphe </p>
```

Mets en valeur des mots dans tes articles

1. Mets en **gras** un mot dans ton premier article
2. Mets en *italique* un mot du dans ton deuxième article
3. Choisis un mot dans ton blog et mets le en gras et en italique

{{<figure src="images/mise_en_valeur.png" >}}

### Listes

Pour structurer ta page, tu peux également utiliser des listes. Il en existe deux types : les listes à puces (en utilisant la balise `<ul>`) et les listes numérotées (en utilisant la balise `<ol>`).

La première liste permet d'énumérer sans notion d'ordre, la seconde ajoute un numéro devant chaque élément de la liste.

Chaque élément de la liste doit être encadré des balises `<li>` `</li>`.

```html
<h1> Liste de courses </h1>
<ul>
    <li> Pain </li>
    <li> Lait </li>
    <li> Oeufs </li>
</ul>
```

```html
<h1> Classement </h1>
<ol>
    <li> Dominique </li>
    <li> Sacha </li>
    <li> Frédérique </li>
</ol>
```

Profitons des listes pour ajouter un sommaire à ton blog.

1. Crée une liste sous le titre principal
2. Ajoute autant d'éléments à la liste que tu as d'articles

{{<figure src="images/listes.png" >}}

## Les attributs

Les balises ont encore quelques secrets à nous livrer. On peut en effet leur ajouter des attributs.

Un attribut `HTML` est un composant de la balise utilisé pour ajuster le comportement ou l'affichage de l'élément de la balise. Par exemple, les attributs peuvent être utilisés pour modifier la couleur, la taille ou la fonctionnalité des éléments.

Pour ajouter un attribut, il suffit de l'inclure dans une balise `HTML` ouvrante :

```html
<p attribut="valeur"> Ceci est un paragraphe avec un attribut </p>
```

Un attribut comprend le nom de celui-ci suivi du signe égal ``=`` et d'une valeur placée entre guillemets ``""``.

### Liens

L'une des premières balises mettant à profit les attributs concerne une des fonctionnalités essentielles du web : les liens.

La balise de lien `<a>` utilise l'attribut `href` pour proposer un élément cliquable qui déplacera le visiteur vers un autre site, une autre page, ou simplement un endroit différent de la page.

```html
<p> Un lien vers <a href="www.prologin.org"> Prologin </a></p>
```

Et si tu voulais proposer une page de contact sur ton site et avoir un lien qui redirige vers cette page ? C'est possible, en indiquant dans l'attribut `href` le chemin vers la page :

```html
<a href="contact.html"> Me contacter </a>
```

Le chemin d'une page est le chemin qu'il faut parcourir dans ton explorateur de fichiers depuis le fichier d'origine vers le fichier cible.

<!-- TODO: on veut leur donner le fichier 'contact.html' ou on leur demande de le créer ? -->

1. Ouvre le fichier `contact.html`
2. Copie ce code dedans : 

```html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
        <link rel="icon" type="image/png" href="favicon.png"/>
    </head>

    <body>
        <h1>Me contacter</h1>
         <!-- Met le lien `Revenir en arrière` à la place de cette ligne -->
        <h2>Joseph Marchand</h2>
        <p><a href="mailto:joseph.marchand@prologin.org">josef.marchand@prologin,org</a></p>
        <p><em>06 12 34 56 78</em></p>
    </body>
</html>
```

3. Edite le avec les informations nécessaires pour te contacter
4. Ajoute un lien `Revenir en arrière` qui dirige vers la page `blog.html`
5. Ajoute dans le fichier `blog.html`, sous le titre principal, un lien `Me contacter` qui dirige vers la page `contact.html`




De plus, les liens permettent également de rejoindre un endroit spécifique de la page avec l'aide de points d'ancrage. Pour définir un point d'ancrage, il suffit d'ajouter un attribut `id`  à une balise ouvrante et spécifier une valeur. Il sera alors possible de créer un lien vers ce point d'ancrage en ajoutant à l'attribut `href` d'une balise `<a>` la valeur choisie, précédée d'un `#`. Attention tous les `id` doivent être uniques.

```html
<a href="#article2"> Direction le deuxième article </a>
<h2 id="article2"> Article 2 </h2>
```

Mets à jour ton sommaire pour qu'il soit possible de cliquer sur les éléments et atteindre les articles.

1. Commence par ajouter des ``id`` à tes titres d'article
2. Transforme ton sommaire en une liste de liens, afin que chaque élément de la liste dirige vers l'article correspondant

{{<figure src="images/liens_1.png" >}}

### Images

Du texte c'est bien, des images c'est encore mieux !

Pour afficher une image, il faut deux choses : la balise image `<img/>` et l'attribut `src`. L'attribut `src` prend comme valeur le chemin vers une image sur ton ordinateur.

```html
<img src="image.jpg" />
```

Tu remarqueras que la balise `<img/>` est à la fois ouvrante et fermante. Elle ne fonctionne pas par pair, mais se suffit à elle même, en ajoutant un `/` avant le chevron fermant `>`.

C'est maintenant l'heure d'utiliser un outil formidable : `Google Image`. 

Pour ce faire :
1. Recherche sur Google une image pour chacun de tes articles
2. Enregistre les dans le même dossier que les fichiers de ton site
3. Pour chaque article, ajoute une image entre le titre et le texte

On peut aussi associer un lien à une image, ce que nous allons faire de ce pas :
<!-- 'prologin.png' est censé être donné ? -->
1. En utilisant `prologin.png`, ajoute une image en dessous du titre principal
2. Transforme cette image en lien vers `prologin.org`

{{<figure src="images/images.png" width=750 >}}

<!-- lien des images avec une url -->
Tu peux aussi importer ton image depuis une URL en mettant cette URL en valeur de la balise `src` :
```html
<img src="URL" />
```
Qu'est-ce-que c'est qu'une URL ?

Une URL, c'est l'adresse d'un site, ce qui te permet de le retrouver. C'est comme l'adresse d'une maison, qui te permet de trouver ton chemin jusqu'à elle. 

Cette URL permet ensuite au navigateur de trouver le chemin menant à une page internet.
Par exemple, les URLs des sites tels que `Google` ou `Youtube` sont : `https://www.google.com` et `https://www.youtube.com`.
Donc si tu mets ces URLs dans la barre de recherche de ton navigateur internet, ils mèneront vers leurs sites respectifs.

D'ailleurs, ce système d'URL est unique à chaque page web, tout comme l'adresse d'une maison est elle aussi unique à chaque maison. 
Ces URLs peuvent aussi désigner l'adresse d'images, comme avec [https://prologin.org/static/img/logo_cube.png](https://prologin.org/static/img/logo_cube.png). 

<!-- resize une image -->

Il existe des arguments pour mettre l'image à la taille que tu veux !
Tu peux lui donner une hauteur (`height`) et une largeur (`width`).
Ces attributs prennent comme paramètre un nombre, la taille que tu veux en pixel.

Par exemple :

```html
<img src="image.jpg" width="128" height="128">
```

# Ajouter du style

Tu as maintenant un blog, mais il manque un peu de couleurs. Le style d'un site web ne se fait pas en `HTML`, mais dans un autre langage : le `CSS`.

Tu vas pouvoir modifier la couleur du fond, modifier la taille du texte, ajouter des bordures, et plein de choses encore.

Le CSS permet d'appliquer un style à un type d'élément (tous les titres, toutes les images, ...), ou à un élément en particulier grâce à son `id`.

Les règles CSS, qui permettent de déterminer le style à appliquer, sont composées de 2 éléments : le sélecteur, et les propriétés.

Une règle se présentera donc de la façon suivante :

```css
selecteur {
    propriete;
    ...
    propriete;
}
```

## Le sélecteur

Le selecteur indique l'élément qui est ciblé par cette règle. Il s'écrit simplement avec le nom de la balise.

Par exemple, pour les balises paragraphes, `<p>` :

```css
p {
    /* Ici je modifie le style de toutes les balises paragraphes de mon site */
}
```

Ou bien pour les balises de lien `<a>` :
```css
a {
    /* Ici je modifie le style de toutes les balises de lien de mon site */
}
```

Tu peux également cibler une balise précise grâce à son `id`. Il suffit de mettre '#' puis son id.
<!-- TODO: mettre un lien vers la partie 'id' du sujet -->
N'hésite pas à retourner à la partie `id` ou à appeler un organisateur si tu as un problème.

```css
#mon_id {
    /* Ici je modifie le style de la balise ayant l'id: 'mon_id' */
}
```

## Les propriétés

Les propritées sont composées comme suit :

```css
nom: valeur;
```

Il est possible de mettre autant de propriétés qu'on veut dans chaque règle. Tu verras par la suite quels sont les différents `nom` possibles.

## Feuille CSS

On appelle feuille CSS le fichier qui contient toutes les règles CSS d'une page. Ce fichier est communément nommé `style.css`.

Pour qu'une page `HTML` puisse utiliser une feuille CSS, il faut lui indiquer le nom de cette feuille dans une balise `<link/>`. Dans le fichier 'blog.html' fourni, cette balise est déja ajoutée en haut de la page.

```html
<link rel="stylesheet" href="style.css" />
```

La balise `<link/>` permet de spécifier une relation entre le document actuel et une ressource extérieure. Par exemple, ici, on annonce au document `HTML` qu'une feuille CSS est disponible dans le fichier `style.css`.

1. Crée le fichier `style.css` dans le même dossier que `blog.html`

## Le noir et blanc, c'est fini !

Pourquoi se contenter de deux couleurs quand il en existe des millions !
Sur ton blog tu vas pouvoir changer la couleur des arrière-plans (par exemple le fond de la page), ou même des textes.

Pour changer la couleur des fonds, tu vas utiliser la propriété `background-color`. Cette propriété prend pour valeur le nom d'une couleur en anglais (par exemple, red, blue, green). Tu peux retrouver la liste complète [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color_keywords#list_of_all_color_keywords).

Pour que tous tes paragraphes aient un fond rouge par exemple :
```css
p {
    background-color: red;
}
```

1. Change la couleur du fond de toute la page avec le selecteur `body`
2. Change la couleur du fond du titre principal

Maintenant que tu as changé la couleur des fonds, les textes ne sont peut-être plus très lisibles. Pour changer la couleur des textes, tu vas utiliser la propriété `color`. Cette propriété prend les mêmes valeurs que `background-color`.

Pour changer la couleur du titre principal en bleu :
```css
h1 {
    color: blue;
}
```

1. Change la couleur des titres de tes articles
2. Change la couleur des mots en gras

{{<figure src="images/couleur.png" width=750 >}}

## Des bordures

En `HTML`, chaque balise représente une boîte contenant des éléments comme du texte, une image, etc.


On peut ajouter une bordure à la boîte et la personnaliser en utilisant les trois propriétés suivantes : `border-style`, `border-width` et `border-color`.

La propriété `border-style` permet de choisir son style : un trait, un double trait, etc... La liste complète des valeurs possibles est disponible [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style#values).

La propriété `border-width` permet de contrôler son épaisseur. Elle peut prendre trois valeurs différentes : `thin`, `medium`, `thick`, respectivement pour une épaisseur fine, moyenne, ou épaisse.

Enfin la propriété `border-color` permet de choisir sa couleur. Elle utilise les mêmes valeurs de couleurs vues précédemment. Tu peux retrouver la liste des valeurs possibles [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color_keywords#list_of_all_color_keywords).


Pour ajouter une bordure aux titres des articles (définis en `h2`) :

```css
h2 {
    border-style: solid;
    border-width: medium;
    border-color: green;
}
```

1. Ajoute une bordure à tes images

{{<figure src="images/bordure.png" width=750 >}}

## Padding

Pour éviter que les éléments soient trop proches les uns des autres, on peut ajouter de l'espace autour d'un élément. On peut ajouter un espace différent sur chacun des côtés de l'élément en utilisant la propriété correspondante :

- En haut : `padding-top`
- A droite : `padding-right`
- En bas : `padding-bottom`
- A gauche : `padding-left`

Pour ajouter un espace autour des images :

```css
img {
  padding-top: 50px;
  padding-right: 30px;
  padding-bottom: 50px;
  padding-left: 80px;
}
```

1. Ajoute un padding à gauche de ton sommaire

{{<figure src="images/padding.png" width=750 >}}

# Tips & tricks

Prend le temps de manipuler les différents éléments vus au-dessus avant de te lancer dans cette partie.

## La touche magique

Sur tous les navigateurs, il existe une touche qui permet d'afficher le code HTML dans le navigateur et même de le modifier pour voir directement les changements. La modification n'est que temporaire, et ne modifie pas le fichier d'origine, c'est-à-dire qu'en rafraichissant la page, les modifications auront disparu.

Voici donc l'utilité de la touche **`F12`**.

En appuyant dessus, un menu s'ouvre sur la droite de la page. Dans ce menu se trouve l'onglet `Éléments`. En cliquant dessus, tu trouveras le code que tu as écrit. Tu peux effectuer cette manipulation sur n'importe quel site web, le code sera toutefois un peu plus complexe.

## Le template

Tu as depuis le début de ce TP utilisé un template déjà pré-rempli. Voyons à quoi servait chacune des lignes qui s'y trouve.

La balise `<html>` est la balise principale. Elle permet d'indiquer au navigateur que tout ce qui se trouve à l'intérieur est du code `HTML`.

La balise `<head>` sert à encadrer les informations complémentaires qui concernent le navigateur. On y retrouvera par exemple le nom de l'onglet et les différentes ressources externes (comme on a pu le voir avec la balise `<link>`). La balise `<title>` nous permet de donner un titre à la page, c'est le texte que l'on retrouve dans la liste des onglets ouverts du navigateur.

La balise `<body>` va contenir la partie principale du contenu de la page web. C'est à l'intérieur de celle-ci qu'on va retrouver les titres, le sommaire, les articles, les images, etc...

## Icône

Tu peux par ailleurs améliorer ton site avec une petite icône ! Cette icône s'affichera dans ton navigateur, à côté du nom de ton site web !

```html
<link rel="icon" type="image/png" href="prologin.png"/>
```

Et voilà ! Tu viens à présent de réaliser ta première page internet, bravo à toi !
Tu peux, si tu le souhaites, revenir sur certains points et les améliorer si tu en as envie.

N'oublie pas que les orgas sont là pour t'aider, et qu'il ne faut pas hésiter à les solliciter.
