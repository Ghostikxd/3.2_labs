import sqlite3


# 1
""" # создаем соединение с базой данных
conn = sqlite3.connect('Chinook_Sqlite.sqlite')

# создаем курсор
cur = conn.cursor()

# формируем запрос к базе данных
query = '''
    SELECT FirstName, LastName
    FROM Customer
    WHERE Country = 'Canada'
'''

# выполняем запрос и получаем результаты
cur.execute(query)
results = cur.fetchall()

# выводим результаты на экран
for row in results:
    print(row[0], row[1])

# закрываем соединение с базой данных
conn.close() """

# 2
""" conn = sqlite3.connect('Chinook_Sqlite.sqlite')

cur = conn.cursor()

query = '''
    SELECT Album.Title
    FROM Album
    JOIN Artist ON Album.ArtistId = Artist.ArtistId
    WHERE Artist.Name = 'Accept'
'''

cur.execute(query)
results = cur.fetchall()

# выводим результаты на экран
for row in results:
    print(row[0])

conn.close() """

# 3
""" conn = sqlite3.connect('Chinook_Sqlite.sqlite')

cur = conn.cursor()

# создаем таблицу Student
cur.execute('''
    CREATE TABLE Student (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

students = [
    (1, 'Иванов Иван'),
    (2, 'Петров Петр'),
    (3, 'Сидоров Сидор'),
    # и т.д.
]

# добавляем данные в таблицу
cur.executemany('INSERT INTO Student (id, name) VALUES (?, ?)', students)

conn.commit()

conn.close()
 """
