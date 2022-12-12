# OSPF : open shortest path first

Le protocole OSPF a été construit en 1987 pour répondre aux inconvénients de RIP.  
Il est plus complexe que RIP, seules les grandes lignes en seront données.

### métrique
* La métrique utilisée tient compte du **débit** des différentes liaisons. 
* Plus le débit est élevé, moindre est le coût de la métrique.  
* En pratique on prend comme métrique un quotient de la forme : $10^n / débit$

### échanges entre routeurs : "flooding"
* Un routeur E envoie des messages « Hello » à tous ses voisins. Ces messages contiennent son identificateur, ainsi que les identificateurs des voisins déjà connus. 
* Les voisins répondent par un message qui peut être de deux types. 
   * Si le routeur E est déjà connu, le message sera un simple accusé de réception. 
   * Si E n’est pas connu, le voisin V renvoie en envoyant les informations qu’il connaît sur la topologie du réseau (message LSA : linked state advertisement). 
   * Le **coût du lien à un voisin est mesuré expérimentalement**, et est également transmis. 

Après plusieurs messages LSA, tous les routeurs de la zone connaissent la topologie du réseau.  
Cette étape est la diffusion/« inondation » (flooding) de messages dans tout le réseau. 
