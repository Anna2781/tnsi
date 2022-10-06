# 22-NSI-05
# EXO1

def RechercheMinMax(tab):
    if len(tab) == 0:
        return {'min':None, 'max':None}
    d = {'min':tab[0], 'max':tab[0]}
    for i in range(1,len(tab)):
        if tab[i] > d['max']:
            d['max'] = tab[i]
        if tab[i] < d['min']:
            d['min'] = tab[i]
    return d

t = [0,1,4,2,-2,9,3,1,7,1]
print('RechercheMinMax pour : ', t)
print(RechercheMinMax(t))
print('RechercheMinMax pour : ', [])
print(RechercheMinMax([]))