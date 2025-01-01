import math
import numpy as np

# le coefficient qui donne la regrssion logistic le plus élevé

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])


def sigmoid(z):
    # add your implementation of the sigmoid function here

    #calcule de la regrssion logistique
    logistic_r = 1 / (1 + math.exp(-z))
    print(logistic_r)

# calculate the output of the sigmoid for x with all three coefficients
#calcule de la regrssion lineaire
print("c1 ")
linear_r1 = sum(x*c1)
sigmoid(linear_r1)

print("c2 ")
linear_r2 = sum(x*c2)
sigmoid(linear_r2)

print("c3 ")
linear_r3 = sum(x*c3)
sigmoid(linear_r3)