from cube import Cube, Piece, Victoire, Clef, Porte, Cassable
from joueur import Joueur
from niveau import Niveau


def chargeur_niveau (f_name, cube_size, ecran):
    cubes = []
    pieces = []
    victoires = []
    portes = []
    clefs = []
    cassables = []
    p = None
    f = open(f_name,"r")
    lignes = f.readlines()
    f.close()
    for y in range(len(lignes)):
        for x in range(len(lignes[y])):
            if lignes[y][x] == "x":
                cubes.append(Cube(x*cube_size,y*cube_size,cube_size,cube_size,ecran))
            elif lignes[y][x] == "c":
                pieces.append(Piece(x*cube_size,y*cube_size,cube_size,cube_size,ecran))
            elif lignes[y][x] == "w":
                victoires.append(Victoire(x*cube_size,y*cube_size,cube_size,cube_size,ecran))
            elif lignes[y][x] == "p":
                p = Joueur(x*cube_size,y*cube_size,cube_size,cube_size,ecran, None)
            elif lignes[y][x] == "d":
                portes.append(Porte(x*cube_size,y*cube_size,cube_size,cube_size,ecran))
            elif lignes[y][x] == "k":
                clefs.append(Clef(x*cube_size,y*cube_size,cube_size,cube_size,ecran))
            elif lignes[y][x] == "b":
                cassables.append(Cassable(x*cube_size,y*cube_size,cube_size,cube_size,ecran))
    return Niveau(cubes, pieces, victoires, portes, clefs, cassables),p
