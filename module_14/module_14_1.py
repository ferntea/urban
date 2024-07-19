# module_14_1 Дата и время.

'''
Задание:

Создайте класс SuperDate, наследованный от класса datetime модуля datetime, объекты которого будут дополнительно обладать следующими методами:

1. get_season - должен возвращать сезон года (Summer, Autumn, Winter, Spring)
2. get_time_of_day - должен возвращать  время суток
(Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6) (последнее число не включено в промежуток)


Пример работы класса:

a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())

Вывод на консоль:
Winter
Day

Примечание:
Для удобного хранения промежутков времени и номеров месяцев можно использовать словари.
'''

from datetime import datetime

class SuperDate(datetime):
    def get_season(self):
        month = self.month
        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Spring"
        elif month in [6, 7, 8]:
            return "Summer"
        elif month in [9, 10, 11]:
            return "Autumn"

    def get_time_of_day(self):
        hour = self.hour
        if 6 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 18:
            return "Day"
        elif 18 <= hour < 24:
            return "Evening"
        else:  # 0 <= hour < 6
            return "Night"


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())         # Вывод: Winter
print(a.get_time_of_day())    # Вывод: Day
