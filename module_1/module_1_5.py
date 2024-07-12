# module_1_5 - Immutable and mutable objects. Tuples

'''
2. Задайте переменные разных типов данных:
  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
  - Выполните операции вывода кортежа immutable_var на экран.

3. Изменение значений переменных:
  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

4. Создание изменяемых структур данных:
  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
  - Измените элементы списка mutable_list.
  - Выведите на экран измененный список mutable_list.
'''

immutable_var = ("one", "two", "three", 1, 2, 3, True, False)
print(immutable_var)

# immutable_val[2] = "four"  #unssuccessfull!!!

mutable_list = list(immutable_var)
print(mutable_list)

mutable_list[2] = "four"  #successfull!!!
print(mutable_list)
