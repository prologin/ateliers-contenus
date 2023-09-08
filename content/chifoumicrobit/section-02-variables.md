# Programmer en Python

Pour pouvoir créer notre jeu pour Skeleton, il va te falloir quelques
connaissances en Python. En programmation, les intructions sont lues ligne par
ligne. Chaque instruction est décrite sur une ligne. On va alors t'aider à
écrire ses lignes. Si tu as la moindre question, n'hésite pas à la poser à un
organisateur !

## Les variables en Python

La plupart du temps, nous avons besoin de stocker des informations dans notre
code. On parle alors de variables. Elles permettent de ranger des choses et de
pouvoir les ressortir quand on le souhaite. Ce sont des éléments qui associent
un nom à une valeur. C'est comme si on utilisait des boîtes pour ranger des
éléments !

{{<figure src="resources/images/variable.png" height=25% width=25% alt="Variable en Python">}}

Pour déclarer une variable en Python, on procède de la sorte :

```python
# `ma_variable` stocke la valeur 42
ma_variable = 42
```

Tu vas pouvoir afficher les valeurs de tes variables ou du texte avec la
fonction `print()`.

```codepython
# `ma_variable` stocke la valeur 42
ma_variable = 42

# Affiche la valeur de `ma_variable` dans la console
print(ma_variable)

# Affiche le texte "Hello world!" dans la console
# N'oublie pas les `"` pour écrire du texte en Python,
# sinon, cela ne fonctionnera pas !
print("Hello world!")
```

<br/>

{{% box type="info" title="C'est quoi les lignes qui commencent par un `#` ?" %}}

Les lignes commençant par des `#`, ce sont des commentaires. Cela te permet
d'expliquer ton code par des phrases pour toi ou même pour les personnes qui
t'entourent. Python ne prend pas en compte les commentaires dans son exécution.

{{% /box %}}