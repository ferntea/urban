# print("Hello world")

'''
Задание:
Большинство программистов лентяи и все поставленные задачи им проще решить при помощи кода.
На этот раз задача состояла в следующем:
Были даны числа:

    23891471923807487.142352314353455
    23891471923807487.142352314356734
    23891471923843245.142352314334563
    23891471923843245.142352314334553

Нужно было проверить что сумма 1 и 3 числа больше суммы 2 и 4.
Результат должен получится False (Ложь).

В ответ прикрепите составленное выражение составленное по условию задачи, например: 124 > 123.
'''

# Данные числа
num1 = 23891471923807487.142352314353455
num2 = 23891471923807487.142352314356734
num3 = 23891471923843245.142352314334563
num4 = 23891471923843245.142352314334553

res1 = num1 + num3 > num2 + num4
res2 = num1 + num2 + num4 > num1 + num2 + num3

print('res1 ', res1)  #False
print('res2 ', res2)  #False