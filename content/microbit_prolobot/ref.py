from microbit import *
import prolobot
'''
Avec ce programme le robot est censé avancer tout droit jusqu'à un obstacle.
S'il en croise un alors il tourne d'abord sur la gauche et ce tant qu'il en voit un.
Puis si apres avoir repris sa course il recroise un obstacle il tourne mais dans
le sens opposé à la direction prise précédement pour tourner.
'''

# Instancie un element de la classe prolobot de la librairie maqueen
bot = prolobot.Prolobot()
# Instancie la direction a 0 (gauche) et l'etat a 0 (entrain d'avancer)
dire = 0
state = 0
while True:
# Si la distance vu devant le robot est superieur a 12
    if bot.distance() >= 12:
# Si l'etat d'avant etait 1 (entrain de tourner), eteind les leds
        if state == 1:
            bot.turn_off_led()
# Fait avancer le robot a une vitesse mis par defaut a 0.2
        bot.forward()
# Met l'etat a 0 (entrain d'avancer)
        state = 0
# Sinon (si la distance vu devant le robot est inferieur a 12)
    else:
# Si l'etat d'avant etait 0 (entrain d'avancer), alors change la direction (pour pivoter) de droite vers gauche ou inversement
        if state == 0:
            dire = (dire+1)%2
# Fait pivoter le robot a une vitesse de 0.12 < 0.20 (valeur par defaut) dans la direction dire (modifier precedement)
        bot.rotate(dire,0.12)
# Allume les leds en dessous du robot en fonction de sa direction
        bot.turn_on_led(dire*2,(0,0,170))
        bot.turn_on_led(dire*2+1,(0,0,170))
# Met l'etat actuel a 1 (entrain de pivoter)
        state = 1
