# Выбор элементов и функции в SQL запросах.

'''
Задача "Средний баланс пользователя":
Для решения этой задачи вам понадобится решение предыдущей.
Для решения необходимо дополнить существующий код:

    Удалите из базы данных not_telegram.db запись с id = 6.
    Подсчитать общее количество записей.
    Посчитать сумму всех балансов.
    Вывести в консоль средний баланс всех пользователя.

Пример результата выполнения программы:
Выполняемый код:
# Код из предыдущего задания
# Удаление пользователя с id=6
# Подсчёт кол-ва всех пользователей
# Подсчёт суммы всех балансов
print(all_balances / total_users)
connection.close()

Вывод на консоль:
700.0
'''


import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Удаление пользователя с id=6, в конце база данных сохранена
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# Подсчёт кол-ва всех пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Проверка
if total_users > 0:
    average_balance = all_balances / total_users
else:
    average_balance = 0

print(average_balance)


conn.commit()
conn.close()
