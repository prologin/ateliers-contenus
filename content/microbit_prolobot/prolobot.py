# Library for DFRobot's Micro:Maqueen
# Author: Julie Fiadino

import microbit
import machine
import time
import neopixel

GAUCHE = 0
DROITE = 1

class Wheel:
    def __init__(self, moteur):
        self.speed = 0
        self.mot = moteur

    def __activate_motor(self, dir, vit):
        """
        activate a given motor.
        param dir: motor direction. 0 to go forward and 1 to go backward
        param speed: motor speed
        """
        self.speed = vit
        buf = bytearray(3)
        buf[0] = self.mot
        buf[1] = dir
        buf[2] = self.speed
        microbit.i2c.write(0x10, buf)

    def move(self, speed):
        """
        Move wheel forward
        """
        if speed >= 0:
            self.__activate_motor(0, speed)
        else:
            self.__activate_motor(1, -speed)

    def stop(self):
        """
        Stops the wheel
        """
        self.__activate_motor(0, 0)


class Prolobot:
    def __init__(self, freq=100000):
        microbit.i2c.init(freq=freq, sda=microbit.pin20,
                scl=microbit.pin19)
        self.__rgbleds = neopixel.NeoPixel(microbit.pin15, 4)
        self.__left_wheel = Wheel(0x00)
        self.__right_wheel = Wheel(0x02)

        self.__max_speed = 255

    def deplacer(self, vl, vr):
        """
        Run wheels with given speed
        vl: left motor speed coeff
        vr: right motor speed coeff
        """
        vl = max(min(vl, 1), -1)
        vr = max(min(vr, 1), -1)
        self.__left_wheel.move(int(self.__max_speed * vl))
        self.__right_wheel.move(int(self.__max_speed * vr))

    def avancer(self, vitesse=0.2):
        """
        Fait avancer les 2 roues a une vitesse donnee
        vitesse: nombre entre 0 et 1
        """
        self.deplacer(vitesse, vitesse)

    def reculer(self, vitesse=0.2):
        """
        Fait reculer les 2 roues a une vitesse donnee
        vitesse: nombre entre 0 et 1
        """
        self.deplacer(-vitesse, -vitesse)

    def tourner(self, direction, vitesse=0.2):
        """
        Tourne le prolobot a une vitesse donnee
        direction: 0 pour aller a gauche et 1 pour aller a droite
        vitesse: vitesse des roues entre 0 et 1
        """
        if direction == 0:
            self.deplacer(0, vitesse)
        else:
            self.deplacer(vitesse, 0)

    def pivoter(self, direction, vitesse=0.2):
        """
        Pivote le prolobot sur lui meme a une vitesse donnee
        direction: 0 pour aller a gauche et 1 pour aller a droite
        vitesse: vitesse des roues entre 0 et 1
        """
        if direction == 0:
            self.deplacer(-vitesse, vitesse)
        else:
            self.deplacer(vitesse, -vitesse)

    def stop(self):
        """
        Arrete les 2 roues
        """
        self.__right_wheel.stop()
        self.__left_wheel.stop()

    def distance(self):
        """
        Renvoie la distance entre le prolobot et les obstacles en face
        """
        microbit.pin1.write_digital(1)
        time.sleep_ms(10)
        microbit.pin1.write_digital(0)
        microbit.pin2.read_digital()
        t = machine.time_pulse_us(microbit.pin2, 1)
        dist = 340 * t / 20000
        return dist

    def capteur_sol(self, capteur):
        """
        Renvoie True si le capteur detecte du blanc
        param capteur: 0 pour le capteur de gauche et 1 pour le capteur de droite
        """
        if capteur == 0:
            return microbit.pin13.read_digital()
        else:
            return microbit.pin14.read_digital()

    def allumer_phares(self, phare, statut):
        """
        Allumer la led avant correspondante
        param led: 0 pour la led de gauche et 1 pour la led de droite
        param statut: 0 pour eteindre et 1 pour allumer
        """
        if phare == 0:
            microbit.pin8.write_digital(statut)
        else:
            microbit.pin12.write_digital(statut)

    def allumer_led(self, led, couleur):
        """
        Allume la led correspondante
        led: va de 0 a 3
        couleur: un tuple (r, v, b)
        """
        self.__rgbleds[led] = couleur
        self.__rgbleds.show()

    def eteindre_led(self):
        """
        Eteint toutes les leds de couleur
        """
        self.__rgbleds.clear()
