'''
Задача "Заморозка кейсов":
Подготовка:
В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.
Часть 1. TestSuit.

    Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
    Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
    Создайте объект класса TextTestRunner, с аргументом verbosity=2.

Часть 2. Пропуск тестов.

    Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
    Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.

Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
Пример результата выполнения тестов:
Вывод на консоль:
test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
test_run (tests_12_3.RunnerTest.test_run) ... ok
test_walk (tests_12_3.RunnerTest.test_walk) ... ok
test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'
test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'
test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'
----------------------------------------------------------------------
Ran 6 tests in 0.000s OK (skipped=3)
'''


# tests_12_3.py
import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_challenge(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        runner = Runner("Иван", speed=3)
        runner.run()
        self.assertEqual(runner.distance, 6)

    def test_run(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        runner = Runner("Иван", speed=3)
        runner.run()
        self.assertEqual(runner.distance, 6)

    def test_walk(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        runner = Runner("Иван", speed=3)
        runner.walk()
        self.assertEqual(runner.distance, 3)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        slow_runner = Runner("Slow", speed=1)
        fast_runner = Runner("Fast", speed=10)
        tournament = Tournament(20, slow_runner, fast_runner)
        results = tournament.start()
        self.assertEqual(results[1].name, "Fast")
        self.assertEqual(results[2].name, "Slow")