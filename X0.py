import numpy as np
import random

rows = 3
cols = 3

array = np.empty((rows, cols), dtype=str)

for i in range(rows):

    for j in range(cols):
        array[i][j] = random.choice(['x','0'])

print(array)  
