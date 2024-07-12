# module_2_5 Функции в Python. Функция с параметром.

'''
Задача "Матрица воплоти":
Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.

Пункты задачи:

    Объявите функцию get_matrix и напишите в ней параметры n, m и value.
    Создайте пустой список matrix внутри функции get_matrix.
    Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
    В первом цикле добавляйте пустой список в список matrix.
    Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
    Во втором цикле пополняйте ранее добавленный пустой список значениями value.
    После всех циклов верните значение переменной matrix.
    Выведите на экран(консоль) результат работы функции get_matix.
'''

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

n = 3
m = 4
value = 5
result = get_matrix(n, m, value)
for row in result:
    print(row)

# or as shown in the example
print(result)