from microbit import *
import radio

from random import randint

# Configurer la radio
radio.config(channel=34)
radio.on()

# Crée une liste d'emojis
emojis = [
    Image.ANGRY,
    Image.ASLEEP,
    Image.CONFUSED,
    Image.HAPPY,
    Image.HEART,
    Image.MEH,
    Image.SAD,
    Image.SILLY,
    Image.SURPRISED,
]

# Indique l'émoticône sélectionné dans la liste
i = 0

# La fonction qui permet d'envoyer des messages
def send():
    # 'global' permet d'indiquer que la variable i est définie en dehors de la fonction
    global i

    # Permet d'éviter de dépasser de la liste
    # L'operateur '%' se lit 'modulo', il permet de calculer le reste de la division entière
    # exemples :
    #   1 % 10 = 1
    #   14 % 10 = 4
    # Cela fonctionne aussi avec des nombres négatifs :
    #   -7 % 10 = 3
    i %= len(emojis)

    # On récupère l'émoticône et on l'affiche a l'écran
    emoji = emojis[i]
    display.show(emoji)

    # Les boutons A et B permettent de sélectionner l'émoticône
    if button_a.was_pressed():
        i -= 1
    if button_b.was_pressed():
        i += 1

    # Secouer le microbit envoie l'émoticône en utilisant la radio
    if accelerometer.was_gesture('shake'):
        radio.send(repr(emoji)[7:-3])
        # Efface l'écran un court instant pour qu'on puisse voir que le message a été envoyé
        display.clear()
        sleep(500)
        display.show(emoji)

# La fonction qui permet de recevoir des messages
def receive():
    # On ecoute les messages
    message = radio.receive()
    # Si un message est reçu, on l'affiche pendant 2 secondes
    if message:
        display.show(Image(message))
        sleep(2000)
        display.clear()

# Le mode d'execution (soit 'send' soit 'receive')
mode = 'send'

# Boucle d'execution du microbit
while True:
    # On exécute l'action selectionnee
    if mode == 'send':
        send()
    elif mode == 'receive':
        receive()

    # Si on retourne le microbit, on éteint l'écran et on change de mode d'exécution
    if accelerometer.was_gesture('face down'):
        display.clear()
        if mode == 'send':
            mode = 'receive'
        else:
            mode = 'send'
