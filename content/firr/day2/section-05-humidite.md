# Étape 4 : Arrosage automatique

{{% box type="error" title="Objectif" %}}

Créer un système d'arrosage automatique qui s'active en fonction des données
recueillies par le capteur d'humidité, assurant ainsi que les plantes reçoivent
la quantité d'eau optimale sans gaspillage.

{{% /box %}}

## Comment utiliser le capteur ?

### Où brancher le capteur ?

Pour commencer, il faut brancher le capteur d'humidité. Vous pouvez le brancher
sur le pin **1** du microbit.

### Comment connaître l'humidité de la terre ?

Pour connaître le taux d'humidité, il faut _lire la valeur sur le pin 1_. Pour
ce faire, vous pouvez utiliser la fonction suivante, qui va renvoyer une valeur
entre $0$ (pour une terre complètement sèche) à $1023$ (lorsque le capteur est
plongé dans l'eau.

En pratique, vous pourrez constater que le taux d'humidité d'une terre
complètement sèche est situé entre $10$ et $20$, et le taux d'humidité d'une
terre saturée en eau est situé entre $340$ et $360$.

{{% box type="exercise" title="Prenons le capteur en main" %}}

La première étape est de brancher le capteur d'humidité sur le **pin 1**.

Ensuite, vous pouvez télécharger le code suivant sur le microbit (ce dernier
affiche le taux d'humidité actuellement récupéré par le capteur).

```python
while True:
    basic.show_number(pins.analog_read(AnalogPin.1))
```

Vous pouvez désormais tester votre capteur d'humidité pour voir la valeur qui
s'affiche sur l'écran du microbit changer en fonction de l'environnement (vous
pouvez le tenir dans votre main, le plonger dans l'eau ou dans la terre sèche
par exemple).

{{% /box %}}

## Mise en application

{{% box type="exercise" title="Système anti-sécheresse" %}}

Votre code doit faire en sorte que si le capteur d'humidité passe en dessous
d'un certain seuil, alors il faut allumer la pompe pour arroser votre serre.

Pour définir une valeur seuil, vous devez vous baser sur vos expérimentations
précédentes. N'hésitez pas à demander de l'aide si vous en avez besoin !

{{% /box %}}

{{% box type="exercise" title="BONUS : Estimation de la consommation d’eau" %}}

Si vous le souhaitez, vous pouvez faire vos propres expérimentations pour
estimer la quantité d'eau consommée lorsque la pompe est allumée, et afficher
cette quantité sur le microbit.

<details>
<summary>Des pistes</summary>

Vous pouvez commencer par allumer la pompe pendant 10 secondes, estimer la
quantité d'eau que vous avez consommé, puis faire une division pour connaître la
quantité d'eau consommée par seconde.

</details>

{{% /box %}}
