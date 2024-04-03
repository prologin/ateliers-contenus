# Étape 2 : Tests de la pompe

{{% box type="error" title="Objectif" %}}

Il faut s’assurer que la pompe à eau fonctionne correctement et est capable de distribuer l'eau de manière **efficace** dans tout le système. Cette étape est cruciale pour garantir que le mécanisme d'arrosage peut répondre aux besoins des plantes sans gaspiller de **précieuses** ressources en eau.

{{% /box %}}

{{% box type="info" title="Allumer la pompe" %}}

La fonction a utiliser est :

```python
pins.analog_write_pin(pin, valeur)
```

{{% /box %}}

Ici, notre fonction a 2 paramètres, pin et valeur.
Pour le premier paramètre, nous utiliserons toujours : AnalogPin.P2
Pour la valeur, il faut mettre 1023 pour allumer la pompe et 0 pour l'éteindre.

{{% box type="exercise" title="Premier test" %}}

Essayez d’allumer la pompe pendant deux secondes puis de l'éteindre.

{{% /box %}}

{{% box type="info" title="Rappel" %}}

```python
basic.pause(ms)
```

Cette fonction permet de faire patienter le programme pendant un certain temps.

{{% /box %}}
