## Rôle des protocoles de routage
Les protocoles de routage servent à calculer le chemin que doivent prendre les données pour arriver de l’expéditeur au destinataire. 

Chaque routeur sert à connecter plusieurs réseaux : il possède donc plusieurs cartes réseau, et plusieurs adresses IP (une sur chaque réseau).

Le *routage statique* consiste à **fixer la table de routage** de chaque routeur (au contraire du routage *dynamique* où les tables de routages sont périodiquement actualisées) en indiquant à quelle adresse faire suivre chaque paquet. 



|destination|passerelle|interface|
|:----------|:---------|:--------|
|IP de destination|IP où envoyer le paquet à l'étape suivante |depuis l'une des adresses du routeur|
|(éventuellement distante)|(adresse d'un des routeurs voisins)|(nom de l'interface ou adresse IP)|



### fonctionnement du routage
Lorsqu'un routeur reçoit un paquet IP :     
* Il calcule l’adresse de réseau R de destination (obtenue à partir de l'IP de destination avec le masque)
* Si  R est le réseau local :
   * Envoyer le paquet à cette adresse (sans passer par un autre routeur)
* Sinon si le routeur contient un chemin pour le réseau R :
   * Envoyer le paquet à l’étape suivante du chemin : « passerelle »
* Sinon si il existe un chemin par défaut :
   * Envoyer le paquet sur le chemin par défaut (ou « passerelle par défaut »)
* Sinon : 
   * Envoyer un message d’erreur à l’expéditeur


Le routage statique est utilisé dans certains cas, notamment lorsque l’on configure une table de routage à la main. 
Il a l’avantage d’être sécurisé, et aussi de ne pas consommer de bande passante, puisqu’aucune information sur la structure du réseau ne circule sur celui-ci.  
Dès que la taille du réseau  augmente, ou que sa configuration varie, ce type de routage et inadapté.


