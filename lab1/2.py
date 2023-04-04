""" Средствами numpy рассчитать произведения четных чисел от 2 до 20 
на ближайшие к ним большие нечетные числа.
"""
import numpy as np


even_numbers = np.arange(2, 21, 2)
odd_numbers = even_numbers + 1
result = even_numbers * odd_numbers

print(result)
