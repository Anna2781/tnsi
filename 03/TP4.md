# Contraintes garanties par le SGBD (système de gestion de la base de données)
## Contraintes de domaine
* A chaque colonne d'une table est associé un **domaine**, qui correspond à
   * un certain **type** : entier, texte, date
   * éventuellement une certaine **taille** : nombre de caractères d'un texte, nombre de bits d'un entier, signe d'un entier
* Lors de chaque insertion, et de chaque modification, ces **contraintes de domaines** sont testées
   * si les valeurs fournies sont "hors domaine", la requête n'est pas exécutée et une erreur est renvoyée
* lors de la conception d'une base de donnée, il est important de bien choisir le domaine défini pour chaque champ (ou colonne).

## Contrainte d'unicité : clé primaire
Essayer la requête : 
* `INSERT INTO auteur VALUES(19, 'Fruchart', 'Thomas');`

Remarquer l'erreur obtenue :  
**Error: UNIQUE constraint failed: auteur.a_id**

Quelques explications s'imposent : 
* il existe dans la table `auteur` une **clé primaire** (identifiée par  : 'PRIMARY')
* cette clé primaire correspond ici au champ (ou colonne):  `a_id`
* pour chaque ligne de la table, la clé primaire doit permettre d'identifier cette ligne de manière **unique**
* ici, la clé primaire  `a_id` permet de s'assurer que deux lignes différentes de la table ne peuvent pas avoir un `a_id` identique!
   * il est donc impossible d'insérer une nouvelle ligne dans la table s'il existe déjà une ligne avec le même isbn
   * il est également impossible de modifier une valeur du champ à_id` sans tenir compte de la contrainte d'unicité.

Une clé primaire peut être définie par **un ou plusieurs champs** d'une même table.  
**exécuter**  
`INSERT INTO auteur_de VALUES (113,"978-2253174561");`


Sur la table `auteur_de` la clé primaire est le **couple** de champs (a_id, isbn).  
- La valeur de ce couple de champs doit être unique dans toute la table.
- Cette clé est définie lors de la création de la table :  
  CREATE TABLE auteur_de (a_id INT, isbn CHAR(14) , **PRIMARY KEY (a_id, isbn)** , FOREIGN KEY (isbn) REFERENCES livre(isbn), FOREIGN KEY (a_id) REFERENCES auteur(a_id) )
-   Sur le schéma ci-dessous, le(s) champs dont le nom est souligné forme(nt) la clé primaire de la table.

![structure](BIBLI-tables.svg)

## Contrainte de référence :  clé étrangère
**essayer** les requêtes :

* `INSERT INTO emprunt(code_barre, isbn, retour) VALUES ('123456789012345', '978-0199555918', '2020-12-13');`
* `DELETE FROM usager WHERE code_barre='917547585216771';`

Remarquer les messages d'erreur : 

**`Error: FOREIGN KEY constraint failed`**



Explication :
* la présence d'une clé étrangère sur la table `emprunt` impose une restriction lorsqu'on souhaite ajouter, supprimer ou modifier certaines lignes :
   * si on ajoutait un `emprunt` pour le code-barre 123456789012345...on aurait une incohérence dans la base de données, car ce code-barre ne correspond à aucune ligne dans la table `usager` !
   * si on supprimait de la table `usager` la ligne dont le code-barre '917547585216771'
   * alors une ligne de la table `emprunt` contiendrait une **référence** sans correspondance dans la table `usager`
   * cela reviendrait à supprimer un usager qui n'a pas encore rendu tous les livres empruntés
* l'ajout d'une clé étrangère permet de sécuriser la suppression ou la modification des données, pour préserver la cohérence des données.
* on dit qu'une telle clé étrangère assure une **contrainte d'intégrité** de la base de données.
* lors de la conception d'une base de données, il convient de bien définir les contraintes portant les champs d'une table qui font **référence** à d'autres tables. 
* Sur le schéma ci-dessus, une flèche représente une contrainte de référence depuis un champ "clé étrangère" vers sa référence qui est un champ "clé primaire".
