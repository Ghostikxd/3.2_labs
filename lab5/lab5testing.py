import h5py
import csv
import numpy as np
import time

# 1
""" data = {'fas_id': [], 'name': [], 'address': [], 'postcode': [], 'easting': [],
        'northing': [], 'latitude': [], 'longitude': [], 'local_authority': []}

with open('open_pubs.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)  # пропускаем заголовок
    for row in reader:
        if '\\N' in row:  # пропускаем строки, содержащие '\\N'
            continue
        try:
            data['fas_id'].append(int(row[0]))
            data['name'].append(row[1])
            data['address'].append(row[2])
            data['postcode'].append(row[3])
            data['easting'].append(int(row[4]))
            data['northing'].append(int(row[5]))
            data['latitude'].append(float(row[6]))
            data['longitude'].append(float(row[7]))
            data['local_authority'].append(row[8])
        except ValueError:
            print(
                f"Невозможно преобразовать значение в тип 'int' или 'float': {row}")
            continue

for i in range(10):
    print(f"fas_id: {data['fas_id'][i]}, name: {data['name'][i]}, \
          address: {data['address'][i]}, postcode: {data['postcode'][i]}, \
          easting: {data['easting'][i]}, northing: {data['northing'][i]}, \
          latitude: {data['latitude'][i]}, longitude: {data['longitude'][i]}, \
          local_authority: {data['local_authority'][i]}") """

# 2
""" start_time = time.time()
a = np.random.rand(10000, 10000)
b = np.random.rand(10000, 10000)
c = np.dot(a, b)
end_time = time.time()
print(f"Время выполнения трех операций: {end_time - start_time} секунд")
np.savez("matrix_a.npz", data=a)
np.savez("matrix_b.npz", data=b)
np.savez("matrix_c.npz", data=c) """

# 3
""" # Создаем первую матрицу размера 1000x1000, заполненную случайными числами из нормального распределения с параметрами mean=0 и std=1
matrix1 = np.random.normal(loc=0, scale=1, size=(1000, 1000))

# Создаем вторую матрицу размера 1000x1000, заполненную случайными числами из равномерного распределения на интервале от 0 до 1
matrix2 = np.random.uniform(low=0, high=1, size=(1000, 1000))

# Создаем файл hdf5 и записываем в него два датасета, соответствующих двум созданным матрицам
with h5py.File("matrices.hdf5", "w") as f:
    # Создаем первый датасет для первой матрицы и указываем параметры распределения в описании
    dset1 = f.create_dataset("matrix1", data=matrix1)
    dset1.attrs["distribution"] = "normal"
    dset1.attrs["mean"] = 0
    dset1.attrs["std"] = 1

    # Создаем второй датасет для второй матрицы и указываем параметры распределения в описании
    dset2 = f.create_dataset("matrix2", data=matrix2)
    dset2.attrs["distribution"] = "uniform"
    dset2.attrs["low"] = 0
    dset2.attrs["high"] = 1 """
