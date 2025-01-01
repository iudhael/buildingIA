import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Please write your code inside this function
    train_file = StringIO(train_string)
    test_file = StringIO(test_string)

    train_data = np.genfromtxt(train_file, skip_header=1) #igonre la premiere ligne du fichier(l'entete)

    test_data = np.genfromtxt(test_file, skip_header=1) #igonre la premiere ligne du fichier(l'entete)

    x_train = train_data[:, :-1]
    x_test = test_data[:, :-1]
    y_train = train_data[:, -1:].reshape(-1) #mettre le tableau sur l horizontal


    # read in the training data and separate it to x_train and y_train
     
    # fit a linear regression model to the data and get the coefficients
    c = np.asarray([])

    c = np.linalg.lstsq(x_train, y_train, rcond=None)[0]

    # read in the test data and separate x_test from it
    x_test = np.asarray(x_test)

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


main()
