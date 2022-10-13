3. `INSERT INTO Patientes VALUES (13862 ,"Bélanger" , "Ninette" , "La Rochelle");`
4. `UPDATE Naissances SET prenom = "Laurette" WHERE rang=1 and date='2022-03-01';` 
5. `SELECT nom, prenom FROM Patientes WHERE Commune="Aigrefeuille d'Aunis";`
6. `SELECT AVG(poids) FROM Naissances JOIN TypesAccouchement ON  TypesAccouchement.idAcc = Naissances.acc
    WHERE TypesAccouchement.libelleAcc='césarienne';` 
7. On obtient l'affichage suivant : 
```
nom    prenom
Berthlot  Michelle
Samson    Marine
Baugé     Gaëlle
Baugé     Gaëlle
```

