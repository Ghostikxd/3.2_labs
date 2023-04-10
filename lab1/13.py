""" Задать два двумерных массива art1 и art2 размерности (4,7) 
состоящих из случайных чисел в пределах от 0 до 10. Построить 
двумерный массив размерности (4,7), каждый элемент которого 
представляет собой максимум из двух значений, находящихся на 
аналогичной позиции в массивах art1 и art2. """

import numpy as np


art1 = np.random.randint(0, 10, size=(4, 7))
art2 = np.random.randint(0, 10, size=(4, 7))
max_arr = np.maximum(art1, art2)


print("art1:\n", art1)
print("art2:\n", art2)
print("max_arr:\n", max_arr)
