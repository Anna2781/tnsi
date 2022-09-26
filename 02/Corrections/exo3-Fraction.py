# Créé par thfruchart, le 26/09/2022 en Python 3.7
from math import gcd

class Fraction:
    def __init__(self, n, d):
        assert d>0, "le dénominateur doit être positif"
        self.num = n
        self.denom = d
    def multiplie(self,v):
        return Fraction(self.num * v.num , self.denom * v.denom)
    def __mul__(self,v):
        return self.multiplie(v).reduire()
    def additionne(self,v):
        return Fraction(self.num*v.denom + v.num*self.denom , self.denom * v.denom)
    def __add__(self,v):
        return self.additionne(v).reduire()
    def reduire(self):
        d = gcd(self.num, self.denom)
        a = self.num // d
        b = self.denom // d
        return Fraction(a,b)
    def __str__(self):
        if self.denom==1:
            return str(self.num)
        return str(self.num) + '/' + str(self.denom)
    def __repr__(self):
        return "Fraction(" + str(self.num) + ',' + str(self.denom) + ')'

a = Fraction(1,3)
b = Fraction(6,5)
print(a*b)
print(a+b)
print(Fraction(5,6) + Fraction(7,6))