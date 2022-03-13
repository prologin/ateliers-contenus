# Importer les fonctions pour pouvoir communiquer avec le micro:bit
from microbit import *
import radio

# Configurer la radio
radio.config(channel=3)
radio.on()

# Créer une liste d'emojis

# Indique l'émoticône sélectionné dans la liste
i = 0

# La fonction qui permet d'envoyer des messages
def send():
    # Vérifier si l'utilisateur a appuyé sur le bouton A ou le bouton B
    # Si c'est le cas, modifier la valeur de i

    # Afficher l'emoji à l'écran

    if """ utilisateur secoue le microbit """:
        # Envoyer le message par radio
        radio.send(repr(emoji)[7:-3])
        # Effacer l'écran un court instant pour qu'on puisse voir que le message a été envoyé

# La fonction qui permet de recevoir des messages
def receive():
    # Écouter les messages à la radio

    # Si un message est reçu, l'afficher à l'écran pendant un certain temps

# Le mode d'execution (soit 'send' soit 'receive')
mode = 'send'

while True:
    # Regarder le mode d'exécution ('send' ou 'receive') et exécuter la fonction correspondante

    if """ utilisateur retourne le microbit """:
        # Effacer l'écran et changer le mode d'exécution

    if """ en mode envoi """:
        # Appeler la fonction `send`
    elif """ en mode réception """:
        # Appeler la fonction `receive`
