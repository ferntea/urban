# module_1_6 - Dictionaries and sets

'''
2. Работа со словарями:
  - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
Например: Имя(str)-Год рождения(int).
  - Выведите на экран словарь my_dict.
  - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
  - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
 - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
  - Выведите на экран словарь my_dict.
'''

my_dict = {"Abram": 1984, "David": 1991, "Solomom": 2004}
print('initial dict: ', my_dict)
print(my_dict["Abram"])     # 1st variant
print(my_dict.get("Abram")) # 2nd variant
print(my_dict.get("Isaac"), 'Key "Isaac" not found')
my_dict.update({"Ann": 1979, "Peter": 1989})
print('updatated dict: ', my_dict)
deleted_key = "Ann"
deleted_value = my_dict.pop("Ann")
print(f'deleted_item: {deleted_key}: {deleted_value}')
print('final dict: ', my_dict)
