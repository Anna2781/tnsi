# Récursivité

#### Exemples du cours sur PythonTutor
* [exemple1](http://www.pythontutor.com/visualize.html#code=def%20somme%28n%29%20%3A%20%0A%20%20%20%20if%20n%20%3D%3D%200%20%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20%23%20else%0A%20%20%20%20return%20n%20%2B%20somme%28n-1%29%0A%0Aprint%20%28somme%284%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
* [exemple2](https://pythontutor.com/visualize.html#code=def%20puissance%28x,n%29%3A%0A%20%20%20%20if%20n%3D%3D0%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20elif%20n%3D%3D1%20%3A%0A%20%20%20%20%20%20%20%20return%20x%0A%20%20%20%20else%20%3A%0A%20%20%20%20%20%20%20%20return%20x%20*%20puissance%28x,%20n-1%29%0A%0Aprint%28puissance%282,3%29%29&cumulative=false&curInstr=1&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
* [exemple3](https://pythontutor.com/visualize.html#code=def%20fibo%28n%29%3A%0A%20%20%20%20if%20n%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20elif%20n%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20else%20%3A%0A%20%20%20%20%20%20%20%20return%20fibo%28n-1%29%20%2B%20fibo%28n-2%29%0A%0Aprint%28fibo%284%29%29&cumulative=false&curInstr=1&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
* [exemple4](https://pythontutor.com/visualize.html#code=def%20a%28n%29%3A%0A%20%20%20%20if%20n%3D%3D0%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20return%202*a%28n-1%29%2B3*b%28n-1%29%0A%0A%0Adef%20b%28n%29%3A%0A%20%20%20%20if%20n%3D%3D0%3A%0A%20%20%20%20%20%20%20%20return%202%0A%20%20%20%20return%20a%28n-1%29-b%28n-1%29%0A%0Aprint%28b%282%29%29&cumulative=false&curInstr=2&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
* [exemple5](https://pythontutor.com/visualize.html#code=def%20puiss%28x,n%29%3A%0A%20%20%20%20if%20n%3D%3D0%20%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20if%20n%3D%3D1%20%3A%0A%20%20%20%20%20%20%20%20return%20x%0A%20%20%20%20r%20%3D%20puiss%28x,%20n//2%29%0A%20%20%20%20if%20n%252%3D%3D0%3A%20%0A%20%20%20%20%20%20%20%20return%20r*r%20%0A%20%20%20%20else%20%3A%0A%20%20%20%20%20%20%20%20return%20r%20*%20r%20*x%0A%0Aprint%28puiss%282,12%29%29&cumulative=false&curInstr=1&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
* [exemple6](https://pythontutor.com/visualize.html#code=def%20copy%28a%20%3Aint%20,b%20%3A%20str%29%3A%0A%20%20%20%20if%20a%3D%3D1%3A%0A%20%20%20%20%20%20%20%20return%20b%0A%20%20%20%20else%20%3A%0A%20%20%20%20%20%20%20%20return%20copy%28%20a-1%20,%20b%2Bb%29%0A%0Aprint%28copy%283,'%3F'%29%29&cumulative=false&curInstr=1&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

###[ COURS](RECURSIVITE_COURS1.ipynb)

#### [Notebook d'exercices](exercices_recursion.ipynb) => [correction](exercices_recursion.ipynb)

#### [travail personnel](RECURSIVITE_TRAVAIL_PERSO.ipynb)

#### QCM [entraînement](https://genumsi.inria.fr/qcm.php?h=cf4244c08fa38c7c0e611edfac246f7b)

#### retour sur le [problème du sac à dos](PbSacADos.ipynb) => [correction](PbSacADos_correction.ipynb)
