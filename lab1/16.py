""" Задан двумерный массив art1 размерности (4,7) состоящий из 
случайных чисел в пределах от 0 до 1. Обнулить все значения в 
массиве, расположенные строго правее и ниже максимального 
элемента массива. """

import numpy as np


art1 = np.random.rand(4, 7)
idx_max = np.unravel_index(np.argmax(art1), art1.shape)
art1[idx_max[0]+1:, idx_max[1]+1:] = 0
np.set_printoptions(precision=2)


print(art1)
