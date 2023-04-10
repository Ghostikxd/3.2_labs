""" Задан произвольный массив numpy (например, массив из 100 
случайных чисел от 0 до 1). Необходимо найти в нем число 
наибольшее близкое к заданному. """

import numpy as np


arr = np.random.rand(100)
num = 0.5
rez = np.abs(arr - num)
index = np.argmin(rez)

print("Ближайший элемент:", arr[index])
