import menu_principal
import menu_prochain_niveau
import jeux
import glob, os



class Gestionnaire ():
    def __init__ (self,stats,ecran, largeur, hauteur):
        self.stats = stats 
        self.niveau = 0
        self.sons = 1
        self.musique = 1
        self.running = True
        self.ecran = ecran
        self.largeur = largeur
        self.hauteur = hauteur
        self.niveaux = glob.glob(os.path.join("levels/","*.txt"))

        self.charge_stats()

    
    def charge_stats (self):
        """
        Récupère les information dans le fichier de stats
        et les charges comme attribut de l'objet
        """

        # ouverture du fichier stats en mode lecture
        f = open(self.stats,'r')
        # on récupère les lignes du fichier dans une liste
        lignes = f.readlines()
        #fermeture du fichier stats
        f.close()
        # chaque ligne corresultatpond à une information différente
        self.niveau = int(lignes[0])
        self.sons = bool(lignes[1])
        self.musique = bool(lignes[2])
        
    def enregistre_stats (self):
        """
        Enregistre les valeurs actualisé du fichier stats
        """
        # ouverture du fichier stats en mode écriture
        f = open(self.stats,'w')
        # écriture des informations
        f.write(f"{self.niveau}\n{self.sons}\n{self.musique}")
        #fermeture du fichier
        f.close()


    def boucle (self):
        """
        Méthode qui s'occupe de faire les bons appels pour le jeu
        """
        
        
        while True:
            # on lance le menu principale et on récupère l'action effectué
            resultat = menu_principal.MenuPrincipal(self.largeur,self.hauteur,self.ecran).run()
            # si 0 cela veut dire quitter
            if resultat == 0:
                self.running = False
                break
            # si 1 afficher les options
            elif resultat == 1:
                print('options')
                continue
            # sinon c'est jouer
            else:
                self.running = True
            # la boucle de jeu
            while self.running and self.niveau < len(self.niveaux) :

                # on lance le jeu et on récupère la valeur de fin de jeu 
                resultat = jeux.Jeu(self.largeur,self.hauteur,self.ecran,self.niveau).run()
                
                # 0 signifie que le niveau a été quitté avant d'être complété
                if resultat == 0:
                    self.running = False
                    break
                
                # le niveau est complété, on lance le menu de prochain niveau
                else:
                    # le nombre du niveau est incrémenté
                    self.niveau += 1
                    resultat = menu_prochain_niveau.MenuProchainNiveau(self.largeur,self.hauteur,self.ecran).run()

                    # si 0 on veut retourner au menu principale
                    if resultat == 0:
                        self.running = False
                        break

                    # si 1 on veut accéder aux options
                    elif resultat == 1:
                        print("option")
                        continue
                    # sinon, la boucle reviens sur le lancement d'un niveau

        # enregistre les valeurs modifié dans le fichier stats
        self.enregistre_stats()
        quit()
                    
        

