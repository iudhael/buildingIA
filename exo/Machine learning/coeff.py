import numpy as np
#on 5 cas
#si le nombre de cas est <= au nombre de coefficient on aura des coefficients qui donneront toujours des prix reels

x = np.array([
             [25, 2, 50, 1, 500], 
             [39, 3, 10, 1, 1000], 
             [13, 2, 13, 1, 1000], 
             [82, 5, 20, 2, 120], 
             [130, 6, 10, 2, 600]
            ])   
y = np.array([127900, 222100, 143750, 268000, 460700])

c = np.linalg.lstsq(x, y)[0]
print(c)
print(x @ c)