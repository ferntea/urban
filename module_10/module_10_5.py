# module_10_2 Многопроцессное программирование.

'''
Задание:
Моделирование программы для управления данными о движении товаров на складе и эффективной обработки запросов
на обновление информации в многопользовательской среде.

Представим, что у вас есть система управления складом, где каждую минуту поступают запросы на обновление информации
о поступлении товаров и отгрузке товаров.
Наша задача заключается в разработке программы, которая будет эффективно обрабатывать эти запросы в
многопользовательской среде, с использованием механизма мультипроцессорности для обеспечения быстрой реакции
на поступающие данные.

Создайте класс WarehouseManager - менеджера склада, который будет обладать следующими свойствами:

    Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
    Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.

Есть 2 действия: receipt - получение, shipment - отгрузка.
а) В случае получения данные должны поступить в data (добавить пару, если её не было и изменить значение ключа,
если позиция уже была в словаре)
б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).

3.Метод run - принимает запросы и создаёт для каждого свой параллельный процесс, запускает его(start) и
замораживает(join).


Пример работы:
# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)

Вывод на консоль:
{"product1": 70, "product2": 100, "product3": 200}
'''

import multiprocessing

class WarehouseManager:
    def __init__(self):
        self.data = multiprocessing.Manager().dict()

    def process_request(self, request):
        product, action, quantity = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == "shipment":
            if product in self.data and self.data[product] >= quantity:
                self.data[product] -= quantity

    def run(self, requests):
        processes = []
        for request in requests:
            process = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

if __name__ == '__main__':
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)

    print(dict(manager.data))

