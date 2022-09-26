class Date:
    def __init__(self, j,m,a):
        self.jour = j
        self.mois = m
        self.annee = a

    def texte(self):
        mois = {1:' janvier ', 2 : ' février ', 3:'mars',
                4:'avril', 5:'mai', 6:'juin', 7:'juillet',
                8:'août', 9:'septembre', 10:'octobre',
                11:'novembre', 12:'décembre'}
        return str(self.jour) + mois[self.mois] + str(self.annee)

    def egale(self,v):
        return self.texte() == v.texte()

    def anterieure(self,v):
        return (self.annee,self.mois,self.jour) < (v.annee,v.mois,v.jour)

    def __str__(self):
        return self.texte()

    def __eq__(self,v):
        return self.egale(v)
    def __lt__(self,v):
        return self.anterieure(v)

d1  = Date(1,1,2023)
d2 = Date (31,12,2022)
d3 = Date (31,12,2022)

assert d2.egale(d3)
assert not d1.egale(d2)
print(d1)
print(d3==d2)
print(d2<d1)
