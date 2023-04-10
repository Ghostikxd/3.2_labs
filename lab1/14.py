""" Задать два двумерных массива art1 и art2 размерности (5,10), 
состоящих из случайных целых чисел от 0 до 10. Удвоить все значения 
art1 которые совпадают со значениями art2, расположенными на 
аналогичных позициях. """

import numpy as np


art1 = np.random.randint(0, 10, size=(5, 10))
art2 = np.random.randint(0, 10, size=(5, 10))

for i in range(5):
    for j in range(10):
        if art1[i, j] == art2[i, j]:
            art1[i, j] = art1[i, j]*2


print(art1)
