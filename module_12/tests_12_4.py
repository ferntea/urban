# tests_12_4 Логирование.

'''
Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное
значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:

    Уровень - INFO
    Режим - чтение
    Название файла - runner_tests.log
    Кодировка - UTF-8
    Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.


Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:

    Оберните основной код конструкцией try-except.
    При создании объекта Runner передавайте отрицательное значение в speed.
    В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
    В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
    "Неверная скорость для Runner".

test_run:

    Оберните основной код конструкцией try-except.
    При создании объекта Runner передавайте что-то кроме строки в name.
    В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
    В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
    "Неверный тип данных для объекта Runner".
'''

import logging
import unittest
from rt_with_exceptions import Runner

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='tests_12_4.log',  # file name is changed
    filemode='w',  # in the task it is recommended 'r', which is not common
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'  # timestamp - importance - message
)


class RunnerTest(unittest.TestCase):
    logging.info('RunnerTest')

    def test_runner_exceptions(self):
        logging.info('test_runner_exceptions')

        # Test for ValueError when negative speed is provided
        try:
            runner = Runner('Runner1', -5)  # negative speed
        except ValueError as e:
            logging.info("'test_runner_exceptions' executed successfully - ValueError raised for negative speed.")
        else:
            self.fail("ValueError not raised for negative speed")  # Fail the test if no exception is raised

        # Test for TypeError when invalid name is provided
        try:
            runner = Runner(12, 5)  # invalid name
        except TypeError as e:
            logging.info("'test_runner_exceptions' executed successfully - TypeError raised for invalid name.")
        else:
            self.fail("TypeError not raised for invalid name")  # Fail the test if no exception is raised


if __name__ == '__main__':
    unittest.main()
