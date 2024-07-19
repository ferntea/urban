# module_11_3 Интроспекция

'''
адание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
   - Тип объекта.
   - Атрибуты объекта.
   - Методы объекта.
   - Модуль, к которому объект принадлежит.
   - Другие интересные свойства объекта, учитывая его тип (по желанию).


Пример работы:
number_info = introspection_info(42)
print(number_info)

Вывод на консоль:
{'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}

Рекомендуется создавать свой класс и объект для лучшего понимания
'''

import inspect

class IntrospectionAnalyser:
    def introspection_info(self, obj):
        obj_type = str(type(obj).__name__)
        attributes = dir(obj)
        truncated_attributes = attributes[:4] + ['...'] if len(attributes) > 4 else attributes
        methods = [method for method in attributes if inspect.ismethod(getattr(obj, method))]
        module = inspect.getmodule(obj).name if inspect.getmodule(obj) else 'None'

        info_str = (f"{{'type': '{obj_type}', 'attributes': {truncated_attributes}, 'methods': {methods}, "
                    f"'module': '{module}'}}")

        return info_str


introspector = IntrospectionAnalyser()
number_info = introspector.introspection_info(42)
print(number_info)