""" Заданы три двумерных массива art1, art2, art3 размерности (4,7), 
состоящих из случайных целых чисел от 0 до 10. Обнулить все 
элементы art1 которые больше соответствующих (находящихся в 
соответствующих позициях) элементов art2 и меньше 
соответствующих элементов art3. """

import numpy as np


art1 = np.random.randint(0, 11, size=(4, 7))
art2 = np.random.randint(0, 11, size=(4, 7))
art3 = np.random.randint(0, 11, size=(4, 7))

for i in range(4):
    for j in range(7):
        if art2[i, j] < art1[i, j] < art3[i, j]:
            art1[i, j] = 0


print(art1)
