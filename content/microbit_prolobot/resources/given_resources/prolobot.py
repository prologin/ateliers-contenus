# Library for DFRobot's Micro:Maqueen
# Author: Julie Fiadino

import microbit
import machine
from time import sleep, sleep_ms
import neopixel

# Const for wheels
LEFT = 0
RIGHT = 1

# Const for lights
ON = 0
OFF = 1
ALL = 10

# Const for leds
FRONTLEFT = 0
FRONTRIGHT = 3
BACKLEFT = 1
BACKRIGHT = 2

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
        Moves the wheel forward
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

    def run(self, vl, vr):
        """
        Activates wheels with the given speed.
        vl: left motor speed between -2 and 2.
            Revolutions per seconds of the left wheel
        vr: right motor speed between -2 and 2
            Revolutions per seconds of the right wheel
        """
        vl = max(min(vl * 127, self.__max_speed), -self.__max_speed)
        vr = max(min(vr * 127, self.__max_speed), -self.__max_speed)
        self.__left_wheel.move(int(vl))
        self.__right_wheel.move(int(vr))

    def forward(self, speed=0.4):
        """
        Moves the robot forward with the given speed
        speed: number between 0 and 2
        """
        self.run(speed, speed)

    def backward(self, speed=0.4):
        """
        Moves the robot backward with the given speed
        speed: number between 0 and 2
        """
        self.run(-speed, -speed)

    def turn(self, direction, speed=0.4):
        """
        Turn the prolobot with the given speed
        direction: 0 to go to the left | 1 to go to the right
        speed: wheel speed between 0 and 2
        """
        if direction == 0:
            self.run(0, speed)
        else:
            self.run(speed, 0)

    def rotate(self, direction, speed=0.4):
        """
        Rotate the prolobot on itself with the given speed
        direction: 0 to go to the left | 1 to go to the right
        speed: wheel speed between 0 and 2
        """
        if direction == 0:
            self.run(-speed, speed)
        else:
            self.run(speed, -speed)

    def stop(self):
        """
        Stop the 2 wheels
        """
        self.__right_wheel.stop()
        self.__left_wheel.stop()

    def distance(self):
        """
        Return the distance between the prolobot and the obstacle in front of it
        """
        microbit.pin1.write_digital(1)
        sleep_ms(10)
        microbit.pin1.write_digital(0)
        microbit.pin2.read_digital()
        t = machine.time_pulse_us(microbit.pin2, 1)
        dist = 340 * t / 20000
        return dist

    def floor_sensor(self, sensor):
        """
        Return True if sensor detect white color
        sensor: 0 for the left sensor | 1 for the right sensor
        """
        if sensor == 0:
            return microbit.pin13.read_digital()
        else:
            return microbit.pin14.read_digital()

    def set_headlight(self, led, statut):
        """
        Switch on or off the front led 'led'
        led: LEFT, RIGHT or ALL consts for the left, right or all leds
        statut: ON or OFF consts to set state
        """
        if led == LEFT or led == ALL:
            microbit.pin8.write_digital(statut)
        if led == RIGHT or led == ALL:
            microbit.pin12.write_digital(statut)

    def turn_on_led(self, led, color):
        """
        Turn on the led 'led'
        led: take FRONTLEFT, FRONTRIGHT, BACKLEFT, BACKRIGHT or ALL const
        color: tuple (r,g,b)
        """
        if led == ALL:
            self.__rgbleds.fill(color)
            self.__rgbleds.show()
            return

        self.__rgbleds[led] = color
        self.__rgbleds.show()

    def turn_off_led(self, led):
        """
        Turn off the led 'led'
        led: take FRONTLEFT, FRONTRIGHT, BACKLEFT, BACKRIGHT or ALL const
        """
        if led == ALL:
            self.__rgbleds.clear()
            self.__rgbleds.show()
            return

        self.__rgbleds[led] = (0, 0, 0)
        self.__rgbleds.show()
