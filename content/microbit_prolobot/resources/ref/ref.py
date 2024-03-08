# title: Prolobot exercises ref
# Author: Julie 'DaiF' Fiadino

# NOT TESTED YET!!!

# This file provides solutions for all the exercises
# in the subject microbit_prolobot.
# Each ref is made only with informations available at
# that point of the subject
# To run a specific mission, uncomment the correct function
# call and flash the microbit

from prolobot import *
bot = Prolobot()

### Mission 1 (ID: MSECUPERI)
def mission1():
    # Go forward
    bot.forward()
    sleep(1)
    # Drop checkpoint (rotation of 360deg)
    bot.rotate(LEFT)
    sleep(2) # TODO: check if correct value
    # Turn back to continue square
    bot.rotate(RIGHT, 0.2)
    sleep(1)

    bot.forward()
    sleep(1)
    bot.rotate(LEFT)
    sleep(2) # TODO: check if correct value
    bot.rotate(RIGHT, 0.2)
    sleep(1)

    bot.forward()
    sleep(1)
    bot.rotate(LEFT)
    sleep(2) # TODO: check if correct value
    bot.rotate(RIGHT, 0.2)
    sleep(1)

    bot.forward()
    sleep(1)
    bot.rotate(LEFT)
    sleep(2) # TODO: check if correct value
    bot.rotate(RIGHT, 0.2)
    sleep(1)


### Mission 2 (ID: MPSGNL)
def mission2():
    for i in range(4):
        # Go forward
        bot.forward()
        bot.set_headlight(ALL, ON)
        bot.turn_on_led(ALL, (255, 122, 0))
        sleep(1)

        # Drop checkpoint (rotation of 360deg)
        bot.rotate(LEFT)
        bot.turn_on_led(ALL, (255, 0, 0))
        bot.set_headlight(RIGHT, OFF)
        sleep(2) # TODO: check if correct value

        # Turn back to continue square
        bot.rotate(RIGHT, 0.2)
        sleep(1)

    # Signal end of square
    for i in range(2):
        bot.turn_on_led(ALL, (0, 0, 255))
        sleep(0.5)
        bot.turn_off_led(ALL)
        sleep(0.5)


### Mission 3 (ID: MRECTDTC)
def mission3():
    for i in range(4):
        # Go forward while no obstacle
        while not bot.floor_sensor(LEFT) and not bot.floor_sensor(RIGHT) and bot.distance() >= 12: # TODO: check if correct value
            bot.forward()
            bot.set_headlight(ALL, ON)
            bot.turn_on_led(ALL, (255, 122, 0))

        # Drop checkpoint (rotation of 360deg)
        bot.rotate(LEFT)
        bot.turn_on_led(ALL, (255, 0, 0))
        bot.set_headlight(RIGHT, OFF)
        sleep(2) # TODO: check if correct value

        # Turn back to continue square
        bot.rotate(RIGHT, 0.2)
        sleep(1)

    # Signal end of square
    for i in range(2):
        bot.turn_on_led(ALL, (0, 0, 255))
        sleep(0.5)
        bot.turn_off_led(ALL)
        sleep(0.5)


# Uncomment only one at a time
#mission1()
#mission2()
#mission3()
