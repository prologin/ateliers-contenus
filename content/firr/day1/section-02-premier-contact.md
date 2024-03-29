# Étape 1 : Premier contact avec Mars

{{% box type="error" title="Objectif" %}}

Établissez votre première connexion avec la base martienne en programmant le
`micro:bit` pour afficher "Hello Mars!" C'est un petit pas pour un micro:bit, un
bond de géant pour la colonisation de Mars.

{{% /box %}}

En Python, le code s'exécute ligne par ligne, de haut en bas. Chaque ligne
correspond à une instruction précise.

{{% box type="warning" title="Différence avec les blocs" %}}

Contrairement au code par bloc, la façon
dont on écrit le code est très importante. Si une ligne contient une erreur, la
suite du code ne sera pas exécutée.

{{% /box %}}

{{% box type="info" title="Afficher du texte" %}}

Pour afficher un texte sur notre `micro:bit`, il faut utiliser la commande
suivante :

```python
basic.showstring(“Le texte à afficher”)
```

{{% /box %}}

Ici, `basic.showstring` est ce qu’on appelle une fonction. Une fonction est
toujours suivie de parenthèses avec dedans, 0, 1 ou plusieurs paramètres. Dans
notre cas, il y a 1 seul paramètre : le texte que nous voulons afficher. C’est
important de le mettre entre guillemets.
