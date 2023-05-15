import dask.dataframe as dd
import pandas as pd
import dask.bag as db
import json
import dask
import zipfile
import os
import dask.diagnostics
import matplotlib.pyplot as plt
from dask.diagnostics import visualize
from datetime import datetime
import glob
import shutil


# 1
""" # Путь к архиву recipes_full.zip
zip_path = 'recipes_full.zip'

# Имя папки внутри архива, содержащей файлы
folder_path = 'recipes_full'

# Шаблон имени файлов
file_pattern = 'recipes_full_*.csv'

with zipfile.ZipFile(zip_path, 'r') as zip:
    file_names = [f.filename for f in zip.filelist if f.filename.startswith(folder_path+'/')]
    zip.extractall(folder_path, members=file_names)

# Загрузка данных в Dask DataFrame
recipes = dd.read_csv(f'{folder_path}/{file_pattern}', parse_dates=['submitted'], assume_missing=True)

# Вывод первых нескольких строк
#print(recipes.head()) """



# 2

""" print("Number of partitions:", recipes.npartitions)
print("\nColumn types:")
print(recipes.dtypes)
# нужен пункт 1 """

# 3

""" # Вывод 5 первых строк
print("Первые 5 строк:")
print(recipes.head(5))

# Вывод 5 последних строк
print("Последние 5 строк:")
print(recipes.tail(5))
# нужен пункт 1 """

# 4 
""" # Подсчет количества строк в каждом блоке
block_counts = recipes.map_partitions(len)

# Выполнение вычислений и получение результатов
result = block_counts.compute()

# Вывод результатов
print(result)
# нужен пункт 1 """

# 5
""" # 5.1
# Нахождение максимума в столбце n_steps
max_n_steps = recipes['n_steps'].max()

# Визуализация графа вычислений
visualize(max_n_steps, filename='graph.png')
# 5.2
# Нахождение максимума в столбце n_steps
max_n_steps = dask.delayed(recipes['n_steps'].max)()

# Визуализация графа вычислений
visualize(max_n_steps, filename='graph.png')

# Вычисление максимума
result = max_n_steps.compute()
print("Максимальное значение n_steps:", result)

# 5.3 

# Нахождение максимума в столбце n_steps
max_n_steps = recipes['n_steps'].max()

# Визуализация графа вычислений
with dask.diagnostics.ProgressBar():
    visualize(max_n_steps, filename='graph.png')

# Вычисление максимума
result = max_n_steps.compute()
print("Максимальное значение n_steps:", result)

# не робит  AttributeError: 'Scalar' object has no attribute '_plot' 
# или  AttributeError: Attribute _plot not found """

# 6
""" # Преобразование столбца 'submitted' в тип даты
recipes['submitted'] = recipes['submitted'].map_partitions(pd.to_datetime)

# Установка столбца 'submitted' в качестве индекса
recipes = recipes.set_index('submitted')

# Группировка по месяцу и подсчет количества отзывов
reviews_by_month = recipes.groupby(recipes.index.dt.to_period('M')).size()
# для пунтка 8 reviews_by_month.to_csv('lab13reviews.csv', index=False)
# Вывод результатов
print(reviews_by_month.compute()) """

# 7


""" def main():
    folder_path = 'reviews_full'
    file_pattern = os.path.join(folder_path, 'reviews_*.json')
    file_list = sorted(glob.glob(file_pattern))

    bag = db.read_text(file_list)
    bag = bag.map(json.loads)

    df = bag.to_dataframe()
    df.to_csv('lab13reviews.csv', index=False)

if __name__ == '__main__':
    main() """

""" # Путь к папке с файлами CSV
folder_path = r'D:\git\3.2_labs\lab12(8)\lab13reviews.csv'

# Считывание файлов CSV в Dask DataFrame
df = dd.read_csv(folder_path + '/*.part')

# Рассчитываем среднее значение оценок с группировкой по месяцам
df['date'] = dd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')
average_ratings = df.groupby('month')['rating'].mean().compute()

# Преобразуем результат к pd.Series
average_ratings_series = average_ratings.to_series()
# для пункта 8 average_ratings_series.to_csv('reviews_count.csv', index=False)
# Выводим результат
print(average_ratings_series) 
#pandas.errors.ParserError: Error tokenizing data. C error: EOF inside string starting at row 214113 """

""" # Путь к папке с частями файлов
folder_path = r'D:\git\3.2_labs\lab12(8)\lab13reviews.csv\*.part'

# Список файлов в папке
file_list = sorted(glob.glob(folder_path))

# Считывание первых 5 строк из каждого файла
dfs_first_5 = []
for file in file_list:
    df = pd.read_csv(file)
    df_first_5 = df.head(5)
    dfs_first_5.append(df_first_5)

# Объединение результатов в один DataFrame
df_first_5_combined = pd.concat(dfs_first_5)

# Вывод первых 5 строк
print("Первые 5 строк:")
print(df_first_5_combined)

# Считывание последних 5 строк из каждого файла
dfs_last_5 = []
for file in file_list:
    df = pd.read_csv(file)
    df_last_5 = df.tail(5)
    dfs_last_5.append(df_last_5)

# Объединение результатов в один DataFrame
df_last_5_combined = pd.concat(dfs_last_5)

# Вывод последних 5 строк
print("Последние 5 строк:")
print(df_last_5_combined) """

# 8
""" # Чтение файла с количеством отзывов по месяцам
reviews_count = pd.read_csv('reviews_count.csv')

# Чтение файла с средними значениями оценок по месяцам
average_ratings = pd.read_csv('average_ratings.csv')

# Объединение данных в один DataFrame
df = pd.merge(reviews_count, average_ratings, on='month')

# Вывод полученного DataFrame
print(df) """