import menu_principal
import menu_prochain_niveau
import jeux



class Gestionnaire ():
    def __init__ (self,stats,ecran, largeur, hauteur):
        self.stats = stats 
        self.niveau = 1
        self.sons = 1
        self.musique = 1
        self.running = True
        self.ecran = ecran
        self.largeur = largeur
        self.hauteur = hauteur

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
            
            resultat = menu_principal.MenuPrincipal(self.largeur,self.hauteur,self.ecran).run()
            if resultat == 0:
                self.running = False
                break
            elif resultat == 1:
                print('options')
                continue
            else:
                self.running = True
            
            while self.running : 
                resultat = jeux.Jeu(self.largeur,self.hauteur,self.ecran,self.niveau).run()
                if resultat == 0:
                    self.running = False
                    break
                
                else:
                    self.niveau += 1
                    resultat = menu_prochain_niveau.MenuProchainNiveau(self.largeur,self.hauteur,self.ecran).run()

                    if resultat == 0:
                        self.running = False
                        break
                    elif resultat == 1:
                        print("option")
                        continue

        self.enregistre_stats()
                    
        

