""" Написать функцию, которая для целых значений n и m будет 
возвращать матрицу размера n и m, имеющую заполнение вида. 
Пример для 4 на 4:
0 1 0 1
2 3 2 3
0 1 0 1
2 3 2 3 
"""
import numpy as np


def generate_matrix(n, m):
    matrix = np.random.randint(0, 10, size=(n, m))
    matrix[::2, ::2] = 0
    matrix[::2, 1::2] = 1
    matrix[1::2, ::2] = 2
    matrix[1::2, 1::2] = 3

    return matrix


print(generate_matrix(6, 6))
