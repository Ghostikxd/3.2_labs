import h5py
import dask.array as da
import numpy as np
import time


# 1
# Загрузка датасета в виде dask.array
filename = 'minutes_n_ingredients_full.hdf5'
dataset = 'recipe'

with h5py.File(filename, 'r') as f:
    print(f.keys())
    data = da.from_array(f[dataset], chunks=(100_000, 3))
    print(data)
    print(data.compute())

    # 2

# Вычисление среднего значения по каждому столбцу, кроме первого
    mean_values = da.mean(data[:, 1:], axis=0)
    # Вычисление среднего значения и получение результата в виде numpy.ndarray
    mean_values_computed = mean_values.compute()
    # Вывод средних значений
    print(mean_values_computed)

# 3
chunks_values = [(100_000, 3), (50_000, 3), (25_000, 3)]

for chunks in chunks_values:
    with h5py.File(filename, 'r') as f:
        data = da.from_array(f[dataset], chunks=chunks)

        # Измерение времени выполнения операции поиска среднего значения
        start_time = time.time()
        mean_values = da.mean(data[:, 1:], axis=0) 
        mean_values_computed = mean_values.compute()
        end_time = time.time()

        # Вывод результатов
        print(f"Chunks: {chunks}, Time: {end_time - start_time} seconds")

# 4
with h5py.File(filename, 'r') as f:
    data = da.from_array(f[dataset], chunks=(100_000, 3))
# Вычислить медиану для каждого чанка массива
    chunk_medians = da.median(data, axis=0)

    # Найти медиану медиан
    overall_median = da.median(chunk_medians, axis=0)

    # Выбрать рецепты, время выполнения которых меньше медианного значения
    selected_recipes = data[data[:, 1] < overall_median].compute()

    print("Selected Recipes:")
    print(selected_recipes)

# 5
with h5py.File(filename, 'r') as f:
    data = da.from_array(f[dataset], chunks=(100_000, 3))

    counts = da.unique(data[:, 2], return_counts=True)
    for count in zip(counts[0].compute(), counts[1].compute()):
        print(count[0], count[1])
    print(counts[1].sum().compute())

   
# 6

with h5py.File(filename, 'r') as f:
    data = da.from_array(f[dataset], chunks=(100_000, 3))

    # Найти максимальную продолжительность рецепта
    max_duration = da.max(data[:, 1])

    # Найти 75-процентный квантиль
    quantile_75 = da.percentile(data[:, 1], q=75)

    # Ограничить максимальную продолжительность рецептов сверху 75-процентным квантилем
    max_duration_limited = da.minimum(max_duration, quantile_75)

    print("Максимальная продолжительность рецепта:", max_duration_limited.compute())

# 7

with h5py.File(filename, 'r') as f:
    data = da.from_array(f[dataset], chunks=(100_000, 3))

    # Ваши предпочтения относительно времени выполнения рецепта и количества ингредиентов
    pref_time = 300
    pref_ingredients = 100

    # Создание массива из предпочтений
    preferences = da.array([pref_time, pref_ingredients])

    # Вычисление L1-расстояния между предпочтениями и каждым рецептом
    distances = da.abs(data[:, 0] - preferences[0]) + da.abs(data[:, 1] - preferences[1])

    # Нахождение индекса рецепта с наименьшим L1-расстоянием
    most_similar_recipe_index = da.argmin(distances).compute()

    # Получение самого похожего рецепта
    most_similar_recipe = data[most_similar_recipe_index].compute()

    print("Наиболее похожий рецепт:")
    print(most_similar_recipe)

# 8

# Параметры блочного алгоритма
blocksize = 100000  # Размер блока

with h5py.File(filename, 'r') as f:
    dataset_length = f[dataset].shape[0]  # Общая длина датасета
    total_sum = 0
    total_count = 0

    for start in range(0, dataset_length, blocksize):
        end = min(start + blocksize, dataset_length)
        data_block = f[dataset][start:end, :]  # Загрузка блока данных

        sum_block = data_block[:, 1].sum()  # Сумма второго столбца в блоке
        count_block = data_block.shape[0]  # Количество элементов в блоке

        total_sum += sum_block
        total_count += count_block

    # Вычисление среднего значения
    mean_value = total_sum / total_count

    print("Среднее значение второго столбца: ", mean_value)