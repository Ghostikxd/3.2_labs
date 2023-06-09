""" Проверить, является ли система векторов а1 = (3; -3; 0; 7), а2 = (2; 
2; 4; 7), а3 = (1; 2; 3; 4), а4 = (5; -4; 1; 3) линейно зависимости? """

import numpy as np


A = np.array([[3, 2, 1, 5], [-3, 2, 2, -4], [0, 4, 3, 1], [7, 7, 4, 3]])
det_A = np.linalg.det(A)

if det_A != 0:
    print("Система векторов линейно независима.")
else:
    print("Система векторов линейно зависима.")
