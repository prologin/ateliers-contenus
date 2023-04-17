def nouvelleGrille():
    grille = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return grille


def afficherGrille(grille):
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            print(grille[i][j], end="")
            # Pour ne pas avoir de | à la fin de la ligne
            if j != 2:
                print("|", end="")
            else:
                print()
        if i != len(grille) - 1:
            print("─┼─┼─")


def verifierGrille(grille):
    # verification horizontale
    for ligne in grille:
        if ligne[0] == ligne[1] and ligne[1] == ligne[2] and ligne[0] != " ":
            return ligne[0]

    # verification verticale
    for i in range(len(grille)):
        if (
            grille[0][i] == grille[1][i]
            and grille[1][i] == grille[2][i]
            and grille[0][i] != " "
        ):
            return grille[0][i]

    # verification diagonale
    if (
        grille[0][0] == grille[1][1]
        and grille[1][1] == grille[2][2]
        and grille[0][0] != " "
    ):
        return grille[0][0]
    if (
        grille[0][2] == grille[1][1]
        and grille[1][1] == grille[2][0]
        and grille[0][2] != " "
    ):
        return grille[0][2]

    # cas sans gagnant
    return " "


def verifierCoordonnees(grille, coord):
    # si les coordonnees sont possibles
    if not coord[0].isnumeric() or not coord[1].isnumeric():
        print("Ces coordonnées ne sont pas des nombres !")
        return False

    (hori, verti) = (int(coord[0]), int(coord[1]))
    if hori < 0 or hori > 2 or verti < 0 or verti > 2:
        print("Ces coordonnées sont en dehors du tableau !")
        return False

    # si la case est deja occupee
    if grille[hori][verti] != " ":
        print("La case est déjà occupée!")
        return False

    return True


def demanderCoordonees(grille, joueur):
    print("Au tour du joueur", joueur, "!")
    validCoord = False
    hori = None
    verti = None
    while not validCoord:
        hori = input("Coordonnée horizontale: ")
        verti = input("Coordonnée verticale: ")
        validCoord = verifierCoordonnee(grille, (hori, verti))
    return (hori, verti)


def morpion():
    print(
        "Bienvenue sur le jeu du morpion !\n"
        "Les règles sont simples : chaque joueur choisit des coordonnées sur la grille\n"
        "où il souhaite que son symbole soit placé."
    )
    gagnant = False
    verif = None
    grille = nouvelleGrille()
    while not gagnant:
        afficherGrille(grille)
        (hori, verti) = demanderCoordonees(grille, "O")
        grille[int(hori)][int(verti)] = "O"

        verif = verifierGrille(grille)
        if verif != " ":
            break

        afficherGrille(grille)
        (hori, verti) = demanderCoordonees(grille, "X")
        grille[int(hori)][int(verti)] = "X"

        verif = verifierGrille(grille)
        if verif != " ":
            gagnant = True

    afficherGrille(grille)
    if verif == "X":
        print("Victoire du joueur X !")
    else:
        print("Victoire du joueur O !")


if __name__ == "__main__":
    morpion()
