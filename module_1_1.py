# module_1_1 - strings and string indexing
'''
Задача:
Выполните следующие действия в PyCharm:

    В переменную example запишите любую строку.
    Выведите на экран(в консоль) первый символ этой строки.
    Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
    Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
    Выведите на экран(в консоль) это слово наоборот.
    Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
'''

s = 'первостепеннo'
print(s[0])
print(s[-1])
print(s[(len(s) // 2):])
print(s[::-1])
print(s[1::2])
