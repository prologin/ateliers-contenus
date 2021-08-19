import pygame

from cube import Cube, Coin, WinningZone, Key, Door, Breakable
from player import Player
from level import Level





def generate_level (f_name, cube_size, screen):
    cubes = []
    coins = []
    wins = []
    doors = []
    keys = []
    breakables = []
    p = None
    f = open(f_name,"r")
    lines = f.readlines()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "x":
                cubes.append(Cube(x*cube_size,y*cube_size,cube_size,cube_size,screen))
            elif lines[y][x] == "c":
                coins.append(Coin(x*cube_size,y*cube_size,cube_size,cube_size,screen))
            elif lines[y][x] == "w":
                wins.append(WinningZone(x*cube_size,y*cube_size,cube_size,cube_size,screen))
            elif lines[y][x] == "p":
                p = Player(x*cube_size,y*cube_size,cube_size,cube_size,screen, None)
            elif lines[y][x] == "d":
                doors.append(Door(x*cube_size,y*cube_size,cube_size,cube_size,screen))
            elif lines[y][x] == "k":
                keys.append(Key(x*cube_size,y*cube_size,cube_size,cube_size,screen))
            elif lines[y][x] == "b":
                breakables.append(Breakable(x*cube_size,y*cube_size,cube_size,cube_size,screen))
    return Level(cubes,coins,wins, doors, keys, breakables, screen),p
