# Projet : mouvement de masse

Comme indiqué dans le titre, l’objectif de ce mini-projet est de réaliser une simulation de mouvements de masse. 
Le type d’algorithme que vous allez coder est utilisé dans le cinéma, pour les mouvements d’oiseaux, d’armées etc. 
Historiquement la 1 ère utilisation au cinéma a été pour des nuées de chauve-souris dans un des Batman des années 90. 
Il y a des utilisations « non ludiques » de ce type d’algorithmes ceci dit.
Vous allez utiliser le paradigme de la programmation objet pour réaliser ce projet.

## 1. La classe Vecteur

Cette classe permet de faire plus simplement des opérations sur des vecteurs du plan. On l’utilisera
ensuite pour calculer positions et trajectoires des animaux.

On complétera le fichier `classe_vecteur.py` 

### Écrire les méthodes de la classe Vecteur
Enlever les instructions `pass` au fur et à mesure. Elles ne font rien, mais évitent une erreur lorsqu'une méthode est "vide".  

Sont à faire ou à compléter les méthodes suivantes :
*  est_nul()
* vect_nul()
* norme()
* diff(v)
* oppose()
* prodk(k)
* affectation(v)  

Vous disposez d’un exemple de tests,  que vous aurez à compléter. 

## 2. La classe Animal
Cette classe représente un seul animal.
Elle est à compléter dans le fichier classe_animal.py.
Vous remarquerez qu’on importe dans ce programme la classe Vecteur, sous la syntaxe 
`from classe_vecteur import *` du fichier classe_vecteur.py. 
Ce fichier doit être dans le même dossier que classe_nuee.py.

### a. Compléter le constructeur de la classe.

Lire les spécifications de la classe pour y voir les attributs déjà crées. 
Il en reste à compléter :
* La position initiale est un vecteur, dont les coordonnées aléatoires (en pixels) sont limitées par la taille de l’univers (en pixels également). Prévoyez une marge de 10 pixels au minimum, plus la taille de l’animal (également en pixels). Si l’animal est au point A, ce vecteur est égal à $\overrightarrow{OA}$.
* La vitesse est également un vecteur aléatoire, qui ne doit pas être nul. Chaque coordonnée de la vitesse est un nombre flottant compris entre -1 et 1, sachant que les deux coordonnées ne peuvent pas
être nulles en même temps. La vitesse générée initialement est transformée de manière à avoir la
norme de la vitesse initiale, on calcule
$\vec v = \vec v_{aléatoire} \times \frac{v\_{init}}{\|\| \vec v_{aléatoire} \|\|}$
  * On rappelle que random.random() renvoie un nombre flottant aléatoire entre 0 et 1.
  * Cette classe contient des attributs de classe. Ces attributs sont identiques pour toutes les instances de la classe, on ne les modifie pas. Ils sont déclarés avant le constructeur.

### b. Les méthodes : faire se déplacer un animal.
#### (1) L’explication théorique.
On raisonne de manière discrète, par modification de la position à chaque tick d’horloge.
Un animal va passer de la position $A_n$ , à l’instant n, à la position 
$A_{n+1}$  , à l’instant n + 1, grâce à
sa vitesse $\vec v_ n$ : 
on a : $\overrightarrow{OA_{n+1}} = \overrightarrow{OA_n} + \vec v_n$ .  

De même, la vitesse est modifiée à chaque tick par la force (assimilée avec l’accélération) qui lui est
appliquée. 
On a $\vec v_{n+1} = \vec v_n + \vec a_n$ .

#### (2) La programmation : mise à jour de la position.
Ecrire la méthode `maj_position()`, qui :
1. applique les règles expliquées ci-dessus au (1)
   * il est possible de tester le code en exécutant l'interface graphique fournie dans le fichier `gui_animal_aleatoire.py`
2. vérifie que la vitesse n’est pas supérieure à la vitesse maximale autorisée. Si c’est le cas, on
limitera cette vitesse en calculant 
$\vec v = \vec v \times \frac{v\_{max}}{\|\| \vec v \|\|}$
   * penser à tester le code
3. empêche l'animal de sortir de l'univers en programmant un "rebond" :
   * lorsque l'animal arrive à l'un des  bords, l'une des coordonnées de sa vitesse et de son accélération (ou force) doit changer de signe!
   * penser à tester le code
4. méthode `force_alea()`  
Cette méthode applique une force aléatoire sur l’animal, en modifiant l’attribut self.force.
Chaque composante de la force est comprise entre -1 et 1. La force est ensuite maximisée à la
force maximale autorisée, en utilisant le même principe que pour la vitesse (décommenter
les lignes comme précisées dans le code).
5. méthode `distance(autre)`  
Simple à programmer avec les coordonnées. Il est déconseillé d’utiliser la classe Vecteur qui ici rend les choses plus compliquées.

## 3. La classe Nuee

Cette classe représente un groupe d’animaux. 
Elle est définie dans `classe_nuee.py`, et une interface graphique permet de tester le code : `gui_nuee.py`.  

### a. Compléter le constructeur de la classe.
Il s'agit de compléter le constructeur, en remplissant l'attribut  `essaim` avec le `nombre` d'animaux passé en paramètre. 
### b. Compléter la méthode `mouvement`
* Cette méthode met à jour la position de tous les animaux d'un essaim.  
   * Elle fait appel à une méthode de la classe Animal. 
* Tester le code avec l'interface graphique.

### c. Compléter la méthode `voisins_update`
* Cette méthode permet de mettre à jour les attributs suivants d'un objet de la classe Nuee : 
   * voisins_proches :  tableau de tableaux tel que voisin_proches[i] contient
            la liste de tous les indices des animaux "proches" de l'animal d'indice 'i',
            c'est-à-dire à une distance inférieure à à l'attribut animal.perception[0] 
   * voisins_moyens : tableau de tableaux tel que voisin_moyens[i] contient
            la liste de tous les indices des animaux "moyennement proches" de l'animal d'indice 'i',
            c'est-à-dire à une distance inférieure à l'attribut animal.perception[1]
   * voisins_distants :  tableau de tableaux tel que voisin_distants[i] contient
            la liste de tous les indices des animaux "distants" de l'animal d'indice 'i',
            c'est-à-dire à une distance inférieure à l'attribut animal.perception[2]
* Pour chacun de ces tableaux, les animaux voisins de l'animal d'indice `i` ont leur indice stocké dans `voisins[i]`
   * l'animal d'indice  `i` n'est pas considéré comme son propre voisin.
   * le code fera appel à la méthode `distance` de la classe Animal.
* Tester le code avec l'interface graphique.
   * on peut visualiser les voisins de l'animal d'indice 0 en définissant le booléen `AFFICHE_VOISINS` à `True`




