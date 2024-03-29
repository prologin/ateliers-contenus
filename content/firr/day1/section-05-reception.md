# Étape 4 : Réponse aux Changements de Lumière

{{% box type="error" title="Exercice" %}}

Les plantes doivent également s'adapter aux variations de température sur Mars. Utilisez le stick LED pour simuler comment les plantes perçoivent les changements de lumière.

{{% /box %}}

{{% box type="info" title="Capter les variations de lumières" %}}

Le micro:bit est équipé d'un capteur de lumière. La commande pour lire cette valeur est: 
```python
input.light_level()
```

Quand la commande est exécutée, elle va renvoyer un nombre. Il faut stocker ce nombre pour l’utiliser ensuite, on utilise pour cela une variable. Pour mettre une valeur dans une variable, on peut utiliser:
```python
niveau_de_lumiere = input.light_level()
```

Ici, le niveau de lumière va être stocké dans la variable qui s’appelle : `niveau_de_lumiere`. Pensez à une boîte sur laquelle il y a une étiquette avec écrit `niveau_de_lumiere`. Dans cette boite, on range notre valeur.

Le capteur de lumière va de la valeur 0 à 200.

{{% /box %}}

## Affichage de cette valeur

{{% box type="info" title="Afficher un nombre sur le micro:bit" %}}

Pour afficher un nombre sur le `micro:bit`, il faut utiliser:
```python
basic.show_number(nombre)
```

`nombre` est à remplacer par la valeur que l’on veut afficher.

{{% /box %}}

{{% box type="exercise" title="Niveau de luminosité" %}}

Essayez de créer une variable pour lire le niveau de lumière et ensuite, affichez-le sur le `micro:bit`.

{{% /box %}}

## Faible lumière

{{% box type="exercise" title="Seuil de luminosité minimum" %}}

Sur le `micro:bit`, affiche un texte si la lumière est faible.

{{% /box %}}

{{% box type="info" title="Gestion de Conditions" %}}

Il faut d’abord lire le niveau de lumière en le stockant dans une variable. Ensuite, il faut analyser le niveau de lumière. Pour cela, il faut utiliser des conditions:
```python
if “il pleut”:
    “je prends mon parapluie”
elif “il y a du vent”:
    “je prends ma veste”
elif “il faut beau”:
    “je sors en tee-shirt”
```

Ici, les mots clés importants sont: `if` et `elif`. Après ces mots clés, on met des conditions (ici “il pleut”, “il y a du vent” et “il fait beau”).
Ensuite, si la condition est remplie, un résultat se produit (ici “je prends mon parapluie”, “je prends ma veste” et “je sors en tee-shirt”).

{{% /box %}}

Dans notre cas, les conditions sont les valeurs du niveau de lumière et les résultats sont l’affichage ou non d’un texte. 

Un début de piste :
```python
niveau_de_lumiere = input.light_level()
if niveau_de_lumiere > 100:
    leds.show_color(NeoPixelColors.RED)
```

Ici, on stocke le niveau de lumière, dans une variable et si cette valeur est plus grande que 100, on allume les LEDs en rouge.

Essayez d’afficher le texte : “Faible lumière” si le niveau de lumière est plus petit que 50.

## Barre de lumière

{{% box type="exercise" title="Intensité Lumineuse" %}}

Essayez de créer une barre qui se remplit plus ou moins en fonction de la lumière (lumière en dessous de 20: une seule LED allumée, lumière en dessous de 40: 2 LEDs allumées, etc).

{{% /box %}}

Pour cette étape, il faut utiliser les conditions, le `while True` et le principe de la barre de chargement de l'étape 3.
