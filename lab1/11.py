""" Решить матричное уравнение A * X * B = -C найти матрицу X. 
Где А = [[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]], B=[[3, -1], [2, 1]], C=[[7, 21], [11, 
8], [8, 4]]. """

import numpy as np


A = np.array([[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]])
B = np.array([[3, -1], [2, 1]])
C = np.array([[7, 21], [11, 8], [8, 4]])
B_inv = np.linalg.inv(B)
A_inv = np.linalg.inv(A)
X = -np.dot(np.dot(A_inv, C), B_inv)
np.set_printoptions(precision=2, suppress=True)

print(X)
