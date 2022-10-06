# Créé par thfruchart, le 29/09/2022 en Python 3.7

class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10,
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    def remplir(self):
        """Remplit le paquet de cartes"""
        for c in range(1,5):
            for v in range(1,14):
                nouvelle_carte = Carte(c,v)
                self.contenu.append(nouvelle_carte)
                print(nouvelle_carte.getNom(), nouvelle_carte.getCouleur())

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        pass
        #A compléter
