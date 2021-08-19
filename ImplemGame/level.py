import pygame
from cube import Cube, Coin, WinningZone

class Level ():
    
    def __init__ (self, cubes, pieces, zones, doors, keys, breakables, screen):
        self.cubes = cubes
        self.pieces = pieces
        self.zones = zones
        self.doors = doors
        self.keys = keys
        self.breakables = breakables

    def get_rects(self,objs):
        return [o.rect for o in objs]

    def all_blocking_rects(self):
        return self.get_rects(self.cubes+self.doors+self.breakables)
    
    def cubes_rects(self):
        return self.get_rects(self.cubes)

    def doors_rects(self):
        return self.get_rects(self.doors)

    def breakables_rects(self):
        return self.get_rects(self.breakables)


    def draw (self):
        for c in self.cubes:
            c.draw()
        for p in self.pieces:
            p.draw()
        for z in self.zones:
            z.draw()
        for d in self.doors:
            d.draw()
        for k in self.keys:
            k.draw()
        for b in self.breakables:
            b.draw()
        
