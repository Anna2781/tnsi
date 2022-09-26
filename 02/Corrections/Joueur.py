class Joueur:
    def __init__(self, pseudo, identifiant, equipe):
        " Appelle le constructeur et initialise "
        self.pseudo = pseudo
        self.equipe = equipe
        self.id = identifiant
        self.nb_de_tirs_emis = 0
        self.liste_id_tirs_recus = []
        self.est_actif = True

    def tire(self):
        " Méthode déclenchée par l'appui sur la gâchette "
        if self.est_actif:
            self.nb_de_tirs_emis += 1

    def est_determine(self):
        " Le joueur réalise-t-il un grand nombre de tirs ? "
        return self.nb_de_tirs_emis > 500  # Un booléen est renvoyé.

    def subit_un_tir(self, id_recu):
        " Méthode déclenchée par les capteurs de la veste "
        if self.est_actif:
            self.est_actif = False
            self.liste_id_tirs_recus.append(id_recu)
