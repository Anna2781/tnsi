## Routage dynamique

Dans le routage dynamique :
* les algorithmes de mise à jour des tables sont exécutés par chaque routeur en permanence. 
* pour déterminer quelle route un paquet va suivre, le routeur se base sur une distance, aussi appelée coût ou **métrique**.
* dans le protocole RIP, la métrique utilisée est le nombre de sauts entre routeurs (*hop* en anglais)


### Protocole RIP

Le protocole  RIP est un protocole crée en 1983, par l’université de Californie, d'après des travaux de Bellman et Ford (1956-58). 
Dans ce protocole :  
* chaque routeur conserve l’adresse des routeurs voisins, et 
* il met à jour sa table de routage toutes les 30 secondes (avec une variabilité de +/- 5 secondes) en échangeant des messages avec ses voisins
    
 #### échanges entre routeurs
 * Lorsqu'un routeur émetteur E envoie des messages aux routeurs voisins.
 * Le voisin V répond en renvoyant sa table de routage (ou une partie éventuellement)
 * Le routeur E analyse le message de V.
     * S’il y a une nouvelle route, E l’inscrit dans sa table en ajoutant un saut à la métrique.  
     Le nombre maximal de sauts autorisés est de 15  
     (une route de plus de 15 sauts ne sera pas rajoutée dans la table).
     * Si la route existe déjà dans la table, trois possibilités se présentent.
          * Soit le coût de la nouvelle route est inférieur au coût en mémoire. L’ancienne route est remplacée par la nouvelle
          * Soit le coût est supérieur et l’ancienne route ne passait pas par V. L’information n’a pas d’intérêt et est ignorée.
          * Soit le coût est supérieur et l’ancienne route passait déjà par le routeur voisin V. Cela signifie que l’état du réseau a changé (une panne par exemple). Si le nouveau coût (+ 1 pour la mise à jour du nombre de sauts) est inférieur ou égal à 15, E met à jour le coût. Si ce nouveau coût est supérieur à 15, la route est supprimée.
#### Convergence
Une fois un nombre suffisant de messages échangés, chaque routeur a mis à jour sa table de routage de manière cohérente : on dit que les tables ont "convergé". Les tables de routage restent inchangées tant que le réseau n'est pas modifié (changement dans la structure du réseau, ou panne).

### Avantages du protocole RIP
* Simple et facile à mettre en place
* Efficace sur un petit réseau (10 routeurs ou moins)

### Inconvénients
* Surcharge du réseau, envoi de messages qui peuvent être lourds et fréquents (grosse consommation de bande passante).
* Temps de convergence assez lent. Un changement sur le réseau peut mettre longtemps à être connu. Par exemple, sur un réseau de diamètre 6, il faut 180 secondes pour qu’une information à une extrémité parvienne à l’autre.
* Métrique non optimale : certaines connexions sont plus rapides que d’autres, ce qui n’est pas pris en compte.
