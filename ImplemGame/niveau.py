class Niveau ():
    
    def __init__ (self, cubes, pieces, zones, portes, clefs, cassables):
        self.cubes = cubes
        self.pieces = pieces
        self.zones = zones
        self.portes = portes
        self.clefs = clefs
        self.cassables = cassables

    #renvoie une liste de rectangle provenant de la liste d'objets objs
    def get_rects(self,objs):
        return [o.rect for o in objs]

    #appel de la fonction get_rects pour toutes les tuiles bloquantes
    def bloquants_rects(self):
        return self.get_rects(self.cubes+self.portes+self.cassables)
    
    def cubes_rects(self):
        return self.get_rects(self.cubes)

    def portes_rects(self):
        return self.get_rects(self.portes)

    def cassables_rects(self):
        return self.get_rects(self.cassables)

    

    #permet de dessiner tout le niveau
    def dessine (self):
        for c in self.cubes:
            c.dessine()
        for p in self.pieces:
            p.dessine()
        for z in self.zones:
            z.dessine()
        for d in self.portes:
            d.dessine()
        for k in self.clefs: 
            k.dessine()
        for b in self.cassables: 
            b.dessine()
        
