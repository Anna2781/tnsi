# Créé par thfruchart, le 19/09/2022 en Python 3.7
class Eleve:
    def __init__(self, n, p, a):
        self.nom = n
        self.prenom = p
        self.age = a

    def texte(self):
        """renvoie une chaîne de caractère
        qui décrit l'élève """
        return self.nom + ' ' + self.prenom + ' ' + str(self.age)

    def __str__(self):
        return self.texte() + ' ans'

bill = Eleve("GATES", 'Bill', 65)
bill.texte()

print(bill)
