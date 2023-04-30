import multiprocessing
import pandas as pd
import os
import csv
import csv
import glob
import time
from multiprocessing import Process
import queue


# 1
""" # Число файлов, на которые разбиваем исходный файл
n_files = 8

# Читаем исходный файл recipes_full.csv построчно и записываем его в n_files файлов
with open('recipes_full.csv', 'r', encoding='utf-8') as f:
    header = f.readline().strip()  # Считываем заголовок
    reader = csv.reader(f, delimiter=',', quotechar='"', escapechar='\\')
    for i in range(n_files):
        filename = f'id_tag_nsteps_{i}.csv'
        with open(filename, 'w', encoding='utf-8', newline='') as fout:
            writer = csv.writer(fout, delimiter=';')
            # Записываем заголовок в каждый файл
            writer.writerow(['id', 'tag', 'n_steps'])
            for j in range(int(2.3e6/n_files)):
                try:
                    row = next(reader)
                except StopIteration:
                    break
                id_ = row[1]
                tags = row[5].strip('[]').replace("'", "").split(', ')
                n_steps = row[6]
                for tag in tags:
                    writer.writerow([id_, tag, n_steps]) """


# 2


""" def calculate_avg_steps_by_tag(filename):
    # Определяем словарь для хранения средних значений количества шагов по каждому тегу
    tag_avg_steps = {}

    # Считываем данные из файла построчно
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader)  # Пропускаем заголовок

        # Обрабатываем каждую строку
        for row in reader:
            tag = row[1]
            n_steps = int(row[2])

            # Если тэг уже есть в словаре, обновляем среднее значение
            if tag in tag_avg_steps:
                count, total_steps = tag_avg_steps[tag]
                count += 1
                total_steps += n_steps
                tag_avg_steps[tag] = (count, total_steps)
            # Если тэга ещё нет в словаре, добавляем его
            else:
                tag_avg_steps[tag] = (1, n_steps)

    # Вычисляем среднее значение для каждого тега
    for tag, (count, total_steps) in tag_avg_steps.items():
        avg_steps = round(total_steps / count, 2)
        tag_avg_steps[tag] = avg_steps

    return tag_avg_steps


filename = 'id_tag_nsteps_0.csv'
avg_steps_by_tag = calculate_avg_steps_by_tag(filename)
print(avg_steps_by_tag) """

# 3


""" def read_file(filename):
    # Читает данные из CSV-файла и возвращает словарь со средними значениями количества шагов для каждой метки.
    tag_counts = {}
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            tags = row[1].strip("'").split("', '")
            n_steps = float(row[2])
            for tag in tags:
                if tag not in tag_counts:
                    tag_counts[tag] = {'count': 0, 'sum': 0}
                tag_counts[tag]['count'] += 1
                tag_counts[tag]['sum'] += n_steps
    tag_averages = {}
    for tag, count_sum in tag_counts.items():
        tag_averages[tag] = round(count_sum['sum'] / count_sum['count'], 2)
    return tag_averages


def merge_results(results):
    # Объединяет результаты обработки нескольких файлов в единый словарь\
    # со средними значениями количества шагов для каждой метки
    tag_counts = {}
    for result in results:
        for tag, count in result.items():
            if tag not in tag_counts:
                tag_counts[tag] = {'count': 0, 'sum': 0}
            tag_counts[tag]['count'] += 1
            tag_counts[tag]['sum'] += count
    tag_averages = {}
    for tag, count_sum in tag_counts.items():
        tag_averages[tag] = round(count_sum['sum'] / count_sum['count'], 2)
    return tag_averages


def process_files(file_list):
    # Обрабатывает список CSV-файлов и возвращает словарь со средними значениями количества шагов для каждой метки.
    results = []
    for filename in file_list:
        result = read_file(filename)
        results.append(result)
    return merge_results(results)


if __name__ == '__main__':
    start_time = time.time()

    file_list = [f'id_tag_nsteps_{i}.csv' for i in range(8)]
    result = process_files(file_list)
    print(result)

    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time:.2f} секунд") """

# 4


""" def read_file(filename):
    # Читает данные из CSV-файла и возвращает словарь со средними значениями количества шагов для каждой метки.
    tag_counts = {}
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            tags = row[1].strip("'").split("', '")
            n_steps = float(row[2])
            for tag in tags:
                if tag not in tag_counts:
                    tag_counts[tag] = {'count': 0, 'sum': 0}
                tag_counts[tag]['count'] += 1
                tag_counts[tag]['sum'] += n_steps
    tag_averages = {}
    for tag, count_sum in tag_counts.items():
        tag_averages[tag] = round(count_sum['sum'] / count_sum['count'], 2)
    return tag_averages


def process_file(filename):
    # Обрабатывает CSV-файл и сохраняет результаты в файл
    result = read_file(filename)
    with open(f'{filename}.result', 'w', encoding='utf-8') as f:
        for tag, value in result.items():
            f.write(f'{tag};{value}\n')


def merge_results(results):
    # Объединяет результаты обработки нескольких файлов в единый словарь\
    # со средними значениями количества шагов для каждой метки
    tag_counts = {}
    for result in results:
        for tag, count in result.items():
            if tag not in tag_counts:
                tag_counts[tag] = {'count': 0, 'sum': 0}
            tag_counts[tag]['count'] += 1
            tag_counts[tag]['sum'] += count
    tag_averages = {}
    for tag, count_sum in tag_counts.items():
        tag_averages[tag] = round(count_sum['sum'] / count_sum['count'], 2)
    return tag_averages


if __name__ == '__main__':
    start_time = time.time()

    file_list = [f'id_tag_nsteps_{i}.csv' for i in range(8)]
    pool = multiprocessing.Pool()
    results = pool.map(read_file, file_list)
    result = merge_results(results)

    print(result)
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time:.2f} секунд") """

# 5
