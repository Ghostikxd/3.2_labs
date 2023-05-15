import dask.bag as db
import json
import re
import pandas as pd
import zipfile
import glob
import os


# 1
""" def main():
    # Загрузка файлов из архива в виде dask.bag
    bag = db.read_text(r'D:\git\3.2_labs\reviews_full\reviews_*.json')

    # Преобразование текстового содержимого в объекты Python с помощью модуля json
    bag = bag.map(json.loads)

    # Вывод первых 5 элементов из полученного bag
    print(bag.take(5))


if __name__ == '__main__':
    main() """

# 2
""" def parse_json_with_rating(json_str):
    # Компилируем регулярное выражение для извлечения рейтинга из имени файла
    path = re.compile(r'_(\d+)\.json$')
    
    # Преобразуем JSON-строку в объект Python
    data = json.loads(json_str[0])
    
    # Извлекаем рейтинг из имени файла и добавляем его в словарь
    data.update({'rating': int(re.findall(path, json_str[1])[0])})
    
    return data


def main():
    # Загрузка файлов из папки в виде dask.bag
    bag = db.read_text(r'D:\git\3.2_labs\reviews_full\reviews_*.json', include_path=True)

    # Преобразование текстового содержимого в объекты Python с помощью модуля json и добавление рейтинга
    bag = bag.map(parse_json_with_rating)

    # Вывод первых 5 элементов из полученного bag
    print(bag.take(5))


if __name__ == '__main__':
    main() """

# 3
""" def main():
    # Загрузка файлов из архива в виде dask.bag
    bag = db.read_text(r'D:\git\3.2_labs\reviews_full\reviews_*.json')
    # Подсчет количества отзывов в датасете
    count = bag.count().compute()

    print(f"Количество отзывов: {count}")


if __name__ == '__main__':
    main()  """

# 4
""" def filter_reviews_by_year(review):
    pattern = re.compile(r'2014|2015')
    if re.findall(pattern, review['date']):
        return review  

def main():
    bag = db.read_text(r'D:\git\3.2_labs\reviews_full\reviews_*.json')
    bag = bag.filter(filter_reviews_by_year)
    print(bag.take(5))

if __name__ == '__main__':
    main() """
# не работает 

#ТЯЖЕЛОООООООООООО передалал все в ipynb