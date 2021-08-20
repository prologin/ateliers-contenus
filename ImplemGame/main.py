import  pygame
import gestionnaire

# condition pour savoir si ce fichier .py 
# est le fichier de départ
if __name__ == '__main__':
    
    # on initialise le module pygame 
    pygame.init()

    # les variables qui seront toujours utilisé (elles pourraient être mise en global)
    largeur, hauteur = 1200 , 800
    ecran = pygame.display.set_mode((largeur, hauteur))
    
    # création de l'objet qui fait fonctionner le jeu complet
    handler = gestionnaire.Gestionnaire("stats.txt",ecran,largeur,hauteur)
    # lancement du jeu
    handler.boucle()
