from microbit import *
import radio

from random import randint

# Configurer la radio
radio.config(channel=3)
radio.on()

# Cree une liste d'emojis
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

# Indique l'�motic�ne s�l�ctionn� dans la liste
i = 0

# La fonction qui permet d'envoyer des messages
def send():
    # 'global' permet d'indiquer que la variable i est definie en dehors de la fonction
    global i

    # Permet d'eviter de depasser de la liste
    # L'operateur '%' se lit 'modulo', il permet de calculer le reste de la division entiere
    # exemples :
    #   1 % 10 = 1
    #   14 % 10 = 4
    # Cela fonctionne aussi avec des nombres negatifs :
    #   -7 % 10 = 3
    i %= len(emojis)

    # On recupere l'emoji et on l'affiche a l'ecran
    emoji = emojis[i]
    display.show(emoji)

    # Les boutons A et B permettent de selectionner l'emoji
    if button_a.was_pressed():
        i -= 1
    if button_b.was_pressed():
        i += 1

    # Secouer le microbit envoie l'emoji en utilisant la radio
    if accelerometer.was_gesture('shake'):
        radio.send(repr(emoji)[7:-3])
        # Efface l'ecran un court instant pour qu'on puisse voir que le message a ete envoye
        display.clear()
        sleep(500)
        display.show(emoji)

# La fonction qui permet de recevoir des messages
def receive():
    # On ecoute les messages
    message = radio.receive()
    # Si un message est recu, on l'affiche pendant 2 secondes
    if message:
        display.show(Image(message))
        sleep(2000)
        display.clear()

# Le mode d'execution (soit 'send' soit 'receive')
# Ici, la variable contient une ***fonction*** (eh oui, c'est possible)
mode = 'send'

# Boucle d'execution du microbit
while True:
    # On execute l'action selectionnee (on peut l'appeler comme une fonction car... c'est une fonction !)
    if mode == 'send':
        send()
    elif mode == 'receive':
        receive()

    # Si on retourne le microbit, on eteint l'ecran et on change de mode d'execution
    if accelerometer.was_gesture('face down'):
        display.clear()
        if mode == 'send':
            mode = 'receive'
        else:
            mode = 'send'
