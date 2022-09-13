t = [ [4,1,1,3],
      [2,0,2,1],
      [3,1,5,1]]

def somme_max(t, i, j) :
    """renvoie la somme maximale, parmi tous les chemins
    depuis la case (0,0) jusqu'à la case (i,j) """
    # cas de base
    if (i,j) == (0,0):
        return t[0][0]
    # cas récursif
    elif i == 0:
        return t[i][j] + somme_max(t,i,j-1)
    elif j == 0:
        return t[i][j] + somme_max(t,i-1,j)
    else :
        return  t[i][j] + max (somme_max(t, i-1, j) , somme_max(t, i, j-1))

print(somme_max(t,2,3))
