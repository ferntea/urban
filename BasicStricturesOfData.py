# Базовые структуры данных
# 1st program
'''
Задача 1 (просто) "Арифметика":
    Напишите в начале программы однострочный комментарий: "1st program".
    Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5, после умножение на 5.
    Предполагаемый результат: 15.0
'''
print('\n1st program')
print(5 * 9**0.5)

# 2nd program
'''
Задача 2 (просто) "Сравнение, or, and":

    Напишите в начале программы однострочный комментарий: "2nd program".
    Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
     Предполагаемый результат: True
'''

print('\n2nd program')
print(9.99 > 9.98 and 1000 != 1000.1)


# 3rd program
'''
Задача 3 (средне) "Сложная арифметика":

    Напишите в начале программы однострочный комментарий: "3rd program".
    Дано два целых четырёхзначных числа: 1234 и 5678.
    Выведите на экран(в консоль) сумму серединных чисел исходных данных (23 и 67).
    Предполагаемый результат: 90

ПОДСКАЗКА. Для взятия определённых частей числа понадобятся следующие арифметические действия: целочисленное деление //, остаточное деление %, а так же "круглые" числа: 10, 100 и т.д.
Например:
123 % 100 -> 23;
23 // 10 - > 2;
Так мы получили цифру 2 из числа 123.
'''

a = 1234
b = 5678

# Another trial
# a = 1234
# b = 567800

# One more trial
# a = 1234
# b = 56780

# It seems that condition should include '2 neighbour digits' but not simply 'neighbour digits'
if len(str(a)) % 2 == 0:
    a_mid = (a // 10**((len(str(a)) // 2) - 1)) % 100
else:
    print("length of 'a' is not even")

if len(str(b)) % 2 == 0:
    b_mid = (b // 10**((len(str(b)) // 2) - 1)) % 100
else:
    print("length of 'b' is not even")

# This is shortest solution!!!
# a_mid = int(str(a)[1:3])
# b_mid = int(str(b)[1:3])

print('\n3rd program')
print(a_mid+b_mid)

# More reneral solution. Here recommendation is not used
print('More general solution')

if len(str(a)) % 2 == 0:
    a_mid = str(a)[(len(str(a)) // 2) - 1: (len(str(a)) // 2) + 1]
else:
    print("length of 'a' is not even")

if len(str(b)) % 2 == 0:
    b_mid = str(b)[(len(str(b)) // 2) - 1: (len(str(b)) // 2) + 1]
else:
    print("length of 'b' is not even")

print(int(a_mid) + int(b_mid))


# 4th program
'''
Задача 4 (сложно) "Всё, везде и сразу":

    Напишите в начале программы однострочный комментарий: "4th program".
    Дано два дробных числа: 13.42 и 42.13.
    Необходимо убедиться в том, что целая часть хотя бы одного из чисел равна дробной части другого. 
    Например: 13 == 13 (13.42, 42.13) или 42 == 42 (13.42, 42.13).
    Предполагаемые результат: True

УТОЧНЕНИЕ. 54.39 и 37.54 в результате дают True, т.к. один из вариантов был верным (54 == 54).
ПОДСКАЗКА. Многие фишки можно взять из предыдущей задачи. Не забывайте про преобразование типов, or и and.
НАПОМИНАНИЕ. Не достаточно просто написать сравнение этих двух чисел - print(13 == 13), 
нужно написать выражение, которое изначально работает с этими дробными числами.
'''

a = 13.42
b = 42.13

# Another trial
# a = 13.45
# b = 42.15

print('\n4th program')
compare = int(a) == int(str(b).split('.')[1]) or int(b) == int(str(a).split('.')[1])
print(compare)
