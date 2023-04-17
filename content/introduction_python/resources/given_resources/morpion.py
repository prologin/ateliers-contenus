def nouvelleGrille():
    """Renvoie une grille de morpion vierge."""
    pass

def afficherGrille(grille):
    """Affiche la grille de morpion donnee en parametre.
    @grille : un tableau de taille 3x3, liste de listes"""
    # Tout d'abord, on itere sur la grille dans cet ordre:
    # 1|2|3
    # ─┼─┼─
    # 4|5|6
    # ─┼─┼─
    # 7|8|9
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            # On affiche la valeur de l'element correspondant.
            # Ici, "end" permet de choisir la chaine de caractere affichee
            # apres grille[i][j] et de ne pas avoir de retour a la ligne.
            print(grille[i][j], end="")
            # Pour ne pas avoir de | a la fin de la ligne
            if j != 2:
                print("|", end="")
            else:
                print()
        # On affiche le motif apres chaque ligne contenant les valeurs 
        # de la grille
        if i != len(grille) - 1:
            print("─┼─┼─")


def verifierGrille(grille):
    """Verifie si dans la grille donnee en parametre,
    un joueur est gagnant.
    Si un joueur est gagnant, on renvoie son symbole associe, 
    sinon on renvoie un espace " ". 
    @grille : un tableau de taille 3x3, liste de listes"""
    # verification horizontale

    # verification verticale

    # verification diagonale

    # cas sans gagnant

    pass


def verifierCoordonnees(grille, coord):
    """Verifie si les coordonnees sont valides avec la grille
    donnee en parametre.
    Si les coordonnees sont invalides, on renvoie False, sinon True.
    @grille : un tableau de taille 3x3, liste de listes
    @coord : couple de coordonnees (horizontal, vertical)"""

    # si les coordonnees sont bien des nombres
    
    # si les coordonnees sont dans le tableau

    # si la case est deja occupee

    # si les coordonnees sont valides

    pass

def demanderCoordonnees(grille, joueur):
    """Demande au joueur d'entrer les coordonnees horizontales
    et verticales de l'endroit ou il souhaite jouer. Renvoie un
    couple de coordonnees (horizontal, vertical)
    @grille : un tableau de taille 3x3, liste de listes
    @joueur : chaine de caracteres representant le symbole du joueur,
    "O" ou "X" """
    pass

def morpion():
    """Fonction qui permet de jouer au morpion."""
    print(
        "Bienvenue sur le jeu du morpion !\n"
        "Les règles sont simples : chaque joueur choisit des coordonnées sur la grille\n"
        "où il souhaite que son symbole soit placé."
    )
    # variables du jeu
    gagnant = False
    verif = None
    grille = nouvelleGrille()
    while not gagnant:
        # enchainement d'instructions pour que les joueurs
        # placent leur symbole
        pass

    # annonce du joueur victorieux

morpion()