import numpy as np
#calcule les distances (ou différences) entre chaque paire de lignes de la comptine This Little Piggy et trouve la paire la plus similaire. Utilisez la distance de Manhattan 

#avec cette methode chaque mot à la meme importance 
#Mais si nous considérions, par exemple, le sentiment du texte (en analysant ce que ressent quelqu'un), « un » et « magnifique » n'ont évidemment pas la même importance.
#une solution est la methode du TF-IDF
#Term Frequency Inverse Document Frequency (tf-idf) accorde plus de poids aux occurrences de mots peu fréquents par rapport aux mots courants comme « a », « le », « est », etc.

# this data here is the bag of words representation of This Little Piggy
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    # fix this function so that it returns 
    # the sum of differences between the occurrences
    # of each word in row1 and row2.
    # you can assume that row1 and row2 are lists with equal length, containing numeric values.
    d = 0
    for w1, w2 in zip(row1, row2):
        d += abs(w1 - w2)
        
    return d

def find_nearest_pair(data):
    N = len(data)
    #print(N)
    dist = np.empty((N, N), dtype=float)
     
    for i, sent1 in enumerate(data):
        for j, sent2 in enumerate(data):
            if distance(sent1, sent2) == 0:
                dist[i, j] = np.inf
            else:
                dist[i, j] = distance(sent1, sent2)
    print(dist)
    #Un moyen rapide d'obtenir l'index de l'élément avec la valeur la plus basse dans un tableau 2D (ou en fait, n'importe quelle dimension) consiste à utiliser la fonction
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
