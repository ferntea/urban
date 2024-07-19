# module_10_4 Очереди для обмена данными между потоками.

'''
Задание:
Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа пищи и уходящих
после завершения приема.

Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и уходят.
Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.

Создайте 3 класса:
Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола, is_busy(bool) -
занят стол или нет.

Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:

    Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
    Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
    Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов,
    в случае наличия стола - начинает обслуживание посетителя (запуск потока), в противном случае - посетитель
    поступает в очередь. Время обслуживания 5 секунд.

Customer - класс (поток) посетителя. Запускается, если есть свободные столы.

Так же должны выводиться текстовые сообщения соответствующие событиям:

    Посетитель номер <номер посетителя> прибыл.
    Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
    Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
    Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)


Пример работы:
# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

Вывод на консоль (20 посетителей [ограничение выставить в методе customer_arrival]):
Посетитель номер 1 прибыл
Посетитель номер 1 сел за стол 1
Посетитель номер 2 прибыл
Посетитель номер 2 сел за стол 2
Посетитель номер 3 прибыл
Посетитель номер 3 сел за стол 3
Посетитель номер 4 прибыл
Посетитель номер 4 ожидает свободный стол
Посетитель номер 5 прибыл
Посетитель номер 5 ожидает свободный стол
......
Посетитель номер 20 прибыл
Посетитель номер 20 ожидает свободный стол
Посетитель номер 17 покушал и ушёл.
Посетитель номер 20 сел за стол N.
Посетитель номер 18 покушал и ушёл.
Посетитель номер 19 покушал и ушёл.
Посетитель номер 20 покушал и ушёл.
'''

import threading
import time
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range(1, 21):  # 20 customers
            time.sleep(1)  # Simulate customer arrival every second
            print(f'Посетитель номер {i} прибыл')
            customer = Customer(i, self)
            customer.start()

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {customer.number} сел за стол {table.number}')
                time.sleep(5)  # Simulate customer eating for 5 seconds
                print(f'Посетитель номер {customer.number} покушал и ушёл')
                table.is_busy = False
                return
        print(f'Посетитель номер {customer.number} ожидает свободный стол.')
        self.queue.put(customer)

class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
