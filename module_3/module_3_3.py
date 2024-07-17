# module_3_3 Распаковка позиционных параметров.

'''
Задача "Распаковка":
1.Функция с параметрами по умолчанию:
    Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями
    по умолчанию (например сейчас это: 1, 'строка', True).
    Функция должна выводить эти параметры.
    Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
    Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])

2.Распаковка параметров:
    Создайте список values_list с тремя элементами разных типов.
    Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями
    разных типов.
    Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и **
    для словаря).

3.Распаковка + отдельные параметры:
    Создайте список values_list_2 с двумя элементами разных типов
    Проверьте, работает ли print_params(*values_list_2, 42)
'''

# 1: Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(f"a = {a}, b = {b}, c = {c}")

print('---1---')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# 2: Распаковка параметров
print('\n---2---')
values_list = [10, 'test', False]
values_dict = {'a': 10, 'b': 'test', 'c': True}
print_params(values_list)
print_params(*values_list)
print_params(values_dict)
print_params(*values_dict)
print_params(**values_dict)

# 3: Распаковка + отдельные параметры
print('\n---3---')
values_list_2 = ['test', 99]
print_params(*values_list_2, 42)