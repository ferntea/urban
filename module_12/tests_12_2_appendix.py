# tests_12_2 Методы Юнит-тестирования.

'''
Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:

    Появился атрибут speed для определения скорости бегуна.
    Метод __eq__ для сравнивания имён бегунов.
    Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.

Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список
участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех
тестов.
setUp - метод, где создаются 3 объекта:

    Бегун по имени Усэйн, со скоростью 10.
    Бегун по имени Андрей, со скоростью 9.
    Бегун по имени Ник, со скоростью 3.

tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament
запускается метод start, который возвращает словарь в переменную results. В конце вызывается метод assertTrue,
в котором сравниваются последний объект из result и предполагаемое имя последнего бегуна (индекс -1).
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):

    Усэйн и Ник
    Андрей и Ник
    Усэйн, Андрей и Ник.

Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун
с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.
Пример результата выполнения тестов:
Вывод на консоль:
{1: Усэйн, 2: Ник}
{1: Андрей, 2: Ник}
{1: Андрей, 2: Усэйн, 3: Ник}

Ran 3 tests in 0.001s
OK

Примечания:

    Ваш код может отличаться от строгой последовательности описанной в задании. Главное - схожая логика работы тестов и
    наличие всех перечисленных переопределённых методов из класса TestCase.
'''


import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]: # Iterate over a copy
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)  # Remove from original list

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            # Format the output to show names
            formatted_result = {k: v.name for k, v in value.items()}
            print(f"{key}: {formatted_result}")

    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.assertEqual(list(results.values())[-1].name, "Ник")
        self.all_results[1] = results

    def test_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.assertEqual(list(results.values())[-1].name, "Ник")
        self.all_results[2] = results

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertEqual(list(results.values())[-1].name, "Ник")
        self.all_results[3] = results

    def test_speed_logic(self):
        """Test to ensure runners finish in the correct order based on speed."""
        slow_runner = Runner("Slow", speed=1)
        fast_runner = Runner("Fast", speed=10)
        tournament = Tournament(20, slow_runner, fast_runner)
        results = tournament.start()
        self.assertEqual(results[1].name, "Fast")  # Fast runner should finish first
        self.assertEqual(results[2].name, "Slow")  # Slow runner should finish second

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
