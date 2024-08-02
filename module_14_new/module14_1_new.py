#

'''
Задача "Первые пользователи":
Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:

    id - целое число, первичный ключ
    username - текст (не пустой)
    email - текст (не пустой)
    age - целое число
    balance - целое число (не пустой)

Заполните её 10 записями:
User1, example1@gmail.com, 10, 1000
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 1000
...
User10, example10@gmail.com, 100, 1000
Обновите balance у каждой 2ой записи начиная с 1ой на 500:
User1, example1@gmail.com, 10, 500
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 500
...
User10, example10@gmail.com, 100, 1000
Удалите каждую 3ую запись в таблице начиная с 1ой:
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 500
User5, example5@gmail.com, 50, 500
...
User9, example9@gmail.com, 90, 500

Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

Пример результата выполнения программы:
Вывод на консоль:
Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500
'''


import sqlite3

# Создание и подключение к базе данных
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')


users_data = []
for i in range(1, 11):
    users_data.append((f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

# users_data = [
#     ('User1', 'example1@gmail.com', 10, 1000),
#     ('User2', 'example2@gmail.com', 20, 1000),
#     ('User3', 'example3@gmail.com', 30, 1000),
#     ('User4', 'example4@gmail.com', 40, 1000),
#     ('User5', 'example5@gmail.com', 50, 1000),
#     ('User6', 'example6@gmail.com', 60, 1000),
#     ('User7', 'example7@gmail.com', 70, 1000),
#     ('User8', 'example8@gmail.com', 80, 1000),
#     ('User9', 'example9@gmail.com', 90, 1000),
#     ('User10', 'example10@gmail.com', 100, 1000)
# ]

cursor.executemany('''
INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
''', users_data)

# Обновление balance каждой 2-й записи начиная с 1-й на 500
cursor.execute('''
UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1
''')

# Удаление каждой 3-й записи начиная с 1-й
cursor.execute('''
DELETE FROM Users WHERE id % 3 = 1
''')

# Возраст не равен 60
cursor.execute('''
SELECT username, email, age, balance FROM Users WHERE age != 60
''')

# Вывод
results = cursor.fetchall()
for row in results:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')


conn.commit()
conn.close()