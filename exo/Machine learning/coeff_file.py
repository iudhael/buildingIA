import numpy as np
from io import StringIO

#deterùine les coefficient cette fois ci le nombre de cas est > au nombre totale de coefficient
# ceci va causer un réajustement des prix qui  seront moins précis que les prix reels
#on simule la recuperation des données depuis un fichiers csv 
#on a 5 caracteristiques et la derniere colonne constitue le prix reel

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
 
def fit_model(input_file):
    # Please write your code inside this function
    data = np.genfromtxt(input_file, skip_header=1)
    #print(data)
    data_carac = data[:, :-1] # recupere toutes les colonnes sauf la derniere
    price = data[:, -1:].reshape(-1) #recupere la derniere colonne et mets la liste sur la verticale à 1dimension

    #print(data_carac)
    #print(price)
    #c1 = np.linalg.lstsq(x, y)[0]
    #print(c1)

    # read the data in and fit it. the values below are placeholder values
    c = np.asarray([])  # coefficients of the linear regression
    
    x = np.asarray(data_carac)  # input data to the linear regression
    #print(x)
    c = np.linalg.lstsq(x, price, rcond=None)[0]

    print(c)
    print(x @ c)

# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)
