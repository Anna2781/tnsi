# OSPF : open shortest path first

Le protocole OSPF a été construit en 1987 pour répondre aux inconvénients de RIP.  
Il est plus complexe que RIP, seules les grandes lignes en seront données.  
#### découpage en zones
* OSPF est mis en place au sein d'une **zone** dans laquelle les routeurs s'échangent deux types de message : 
  *  HELLO
  *  LSA 
* chaque zone a un numéro unique
* la zone 0, appelée "*Backbone*", sert à connecter les autres zones.
* Des routeurs particuliers (ABR : *Area Border Router*) sont connectés à la fois à leur zone, et à la zone 0.

### métrique
* La métrique utilisée tient compte du **débit** des différentes liaisons. 
* Plus le débit est élevé, moindre est le coût de la métrique.  
* on prend comme métrique la **bande passante** c'est à dire la quantité d'information qui peut être transmise par unité de temps (en bit par seconde, ou bps).
* En pratique, elle est calculée sous la forme d'un quotient de la forme : $10^n / débit$. 
* En général, on prend n = 8, ce qui fait que
   *   une liaison de type FastEthernet (débit = 100 Mbit/s) aura un coût de 1 
   *   une liaison par câble Ethernet (débit = 10 Mbit/s) aura un coût de 10
   *   une liaision par Satellite	(débit= 50 Mbits/s) aura un coût de 2
   *   ...

#### échanges entre routeurs : "flooding"
* Un routeur E envoie des messages « Hello » à tous ses voisins. Ces messages contiennent son identificateur, ainsi que les identificateurs des voisins déjà connus. 
* Les voisins répondent par un message qui peut être de deux types. 
   * Si le routeur E est déjà connu, le message sera un simple accusé de réception. 
   * Si E n’est pas connu, le voisin V renvoie en envoyant les informations qu’il connaît sur la topologie du réseau (message LSA : linked state advertisement). 
   * Le **coût du lien à un voisin est mesuré expérimentalement**, et est également transmis. 

Après plusieurs messages LSA, tous les routeurs de la zone connaissent la topologie du réseau.  
Cette étape est la diffusion/« inondation » (flooding) de messages dans tout le réseau. 

#### calcul des routes
Une fois transmises les informations sur la topologie du réseau, chaque routeur exécute un algorithme de "plus court chemin" pour déterminer sa table de routage.  Cela renvient à minimiser la somme des coûts de toutes les liaisons empruntées jusqu'à une destination. 
L'algorithme utilisé est celui de Dijkstra.

### Avantages d'OSPF
* Diffusion moins fréquente des messages entre routeur qu'avec RIP
* Un changement sur le réseau est transmis rapidement
* Permet d'obtenir une route optimale en "temps de transmission", ce que ne fait pas RIP.

#### inconvénients
* Plus complexe à mettre en place que RIP.
* Nécessite des routeurs puissants pour le calcul et la mémorisation des chemins minimaux.
* Ne s’adapte pas à la charge des liens : une route "rapide" peut parfois être surchargée (penser aux bouchons sur autoroute).
