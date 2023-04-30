import sqlite3
import csv
from datetime import datetime


# 1
""" # создаем соединение с базой данных
conn = sqlite3.connect('recipes.db')

# создаем курсор
cur = conn.cursor()
 """

# 2
""" conn = sqlite3.connect('recipes.db')
cur = conn.cursor()

# создаем таблицу Recipe
cur.execute('''
    CREATE TABLE Recipe (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        minutes INTEGER,
        submitted DATE,
        description TEXT,
        n_ingredients INTEGER
    )
''')

# сохраняем изменения и закрываем соединение с базой данных
conn.commit()
conn.close() """


# 3
""" conn = sqlite3.connect('recipes.db')
cur = conn.cursor()

# создаем таблицу Review с использованием внешнего ключа recipe_id
cur.execute('''
    CREATE TABLE Review (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        recipe_id INTEGER,
        date DATE,
        rating INTEGER,
        review TEXT,
        FOREIGN KEY(recipe_id) REFERENCES Recipe(id)
    )
''')

conn.commit()
conn.close() """

# 4
""" with open('reviews_sample.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    conn = sqlite3.connect('recipes.db')
    cur = conn.cursor()

    # читаем каждую строку файла и записываем данные в таблицу Review
    for row in reader:
        id, user_id, recipe_id, date_str, rating, review = row
        # преобразуем строку с датой в формат yyyy-mm-dd
        date = datetime.strptime(date_str, '%Y-%m-%d')
        date_str = date.strftime('%Y-%m-%d')
        # добавляем данные в таблицу Review
        cur.execute('INSERT INTO Review (id, user_id, recipe_id, date, rating, review) VALUES (?, ?, ?, ?, ?, ?)',
                    (id, user_id, recipe_id, date_str, rating, review))

    conn.commit()
    conn.close()

with open('recipes_sample_with_tags_ingredients.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    conn = sqlite3.connect('recipes.db')
    cur = conn.cursor()

    # читаем каждую строку файла и записываем только нужные столбцы в таблицу Recipe
    for row in reader:
        id = row[1]
        name = row[0]
        minutes = row[2]
        submitted = row[4]
        description = row[6]
        n_ingredients = row[7]

        cur.execute('INSERT INTO Recipe (id, name, minutes, submitted, description, n_ingredients) VALUES (?, ?, ?, ?, ?, ?)',
                    (id, name, minutes, submitted, description, n_ingredients))

    conn.commit()
    conn.close() """

# 5
""" conn = sqlite3.connect('recipes.db')
cur = conn.cursor()

# выполняем запрос к базе данных
cur.execute('SELECT * FROM Recipe WHERE n_ingredients = 10 LIMIT 5')

# получаем результат запроса и выводим его на экран
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close() """

# 6
""" conn = sqlite3.connect('recipes.db')
cur = conn.cursor()

cur.execute("SELECT name FROM Recipe ORDER BY minutes DESC LIMIT 1;")
result = cur.fetchone()
print(result[0])

conn.close() """

# 7
""" recipe_id = input("Введите id рецепта: ")

conn = sqlite3.connect('recipes.db')
cur = conn.cursor()

cur.execute("SELECT * FROM Recipe WHERE id=?", (recipe_id,))
recipe = cur.fetchone()

# проверяем, что рецепт найден
if recipe:
    print("Название рецепта:", recipe[1])
    print("Количество минут:", recipe[2])
    print("Дата публикации:", recipe[3])
    print("Описание:", recipe[4])
    print("Количество ингредиентов:", recipe[5])
else:
    print("Рецепт с id", recipe_id, "не найден")

conn.close() """

# 8
""" conn = sqlite3.connect('recipes.db')
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM Review WHERE rating = 5")
result = cur.fetchone()
print(f"Количество отзывов с рейтингом 5: {result[0]}") """

# 9
""" conn = sqlite3.connect('recipes.db')
cur = conn.cursor()
cur.execute(
    'SELECT COUNT(DISTINCT recipe_id) FROM Review WHERE rating < 4 OR rating IS NULL')
result = cur.fetchone()
print(
    f"Количество уникальных рецептов, не имеющих отзывов с рейтингом меньше 4: {result[0]}") """

# 10
""" conn = sqlite3.connect('recipes.db')
cur = conn.cursor()
cur.execute('''SELECT COUNT(*)
               FROM Recipe
               WHERE submitted LIKE '2010%'
               AND minutes >= 15''')

result = cur.fetchone()
print(
    "Кол-во рецептов, опубликованных в 2010 году и имеющих длину не менее 15 минут:", result[0])

conn.close() """

# 11
""" conn = sqlite3.connect('recipes.db')
cur = conn.cursor()

cur.execute('''SELECT Recipe.id, Recipe.name, Review.user_id, Review.date, Review.rating
               FROM Recipe JOIN Review ON Recipe.id = Review.recipe_id
               WHERE Recipe.n_ingredients >= 3
               ORDER BY Recipe.id''')


result = cur.fetchall()

for row in result:
    print(row)

conn.close() """
