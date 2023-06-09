'''Создать матрицу 8 на 10 из случайных целых (используя модуль 
numpy. random) чисел из диапазона от 0 до 10 и найти в ней строку (ее 
индекс и вести саму строку), в которой сумма значений минимальна.
'''
import numpy as np


mat = np.random.randint(0, 10, size=(8, 10))
rez = np.argmin(np.sum(mat, axis=1))

print(f"Индекс строки с минимальной суммой значений: {rez}")
print(f"Строка с минимальной суммой значений: {mat[rez]}")
