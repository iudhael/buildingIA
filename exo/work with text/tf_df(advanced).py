#calcule du poids de chaque mot dans chaque document tf-idf
#ensuite recherche de la paire de ligne la plus similaire par calcule des distance avec les poids obtenues
import numpy as np
import math


text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    # docs = [line.lower().split() for line in text.split('\n')]

    # 2. go over each unique word and calculate its term frequency, and its document frequency

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.

    docs = [line.split() for line in text.splitlines()]
    #print(docs)

    N = len(docs)

    vocabulary = list(set(text.split()))
    #print(vocabulary)

    df = {}
    tf = {}

    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    # loop through documents to calculate the tf-idf values
    data = np.empty((N, len(vocabulary)))
    #print(data)
    for doc_index, doc in enumerate(docs):
        
        #print(doc_index)
        #print(tf[word][doc_index])
        for word_index, word in enumerate(vocabulary):
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)
        
            c = tf[word][doc_index] * math.log((1/df[word]), 10)
            #print(c)
            
            data[doc_index, word_index] = c

    #print(data)
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
        #print(dist)
        #Un moyen rapide d'obtenir l'index de l'élément avec la valeur la plus basse dans un tableau 2D (ou en fait, n'importe quelle dimension) consiste à utiliser la fonction
        print(np.unravel_index(np.argmin(dist), dist.shape))

    find_nearest_pair(data)



main(text)
