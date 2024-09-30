"""
Простые Юнит-Тесты
Цель: приобрести навык создания простейших Юнит-тестов
"""

import unittest
from pprint import pprint
from module_12.HumanMoveTest import runner_and_tournament as rt


class Corrected_Tournament(rt.Tournament):
    """
    Исправлен словарь finishers:
        в качестве ключа передается не объект <participant> в памяти,
        а <participant.name> объекта
    Исправлена ошибка, при которой менее быстрый спортсмен мог финишировать
    раньше более быстрого
    """

    def start(self):
        finishers = {}
        result_list = []
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    result_list.append(participant)
                    self.participants.remove(participant)
        result_list = sorted(result_list, key=lambda participant: participant.speed, reverse=True)
        for participant in result_list:
            finishers[place] = str(participant)
            place += 1

        return finishers


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        """
        Словарь заменен на список
        """
        cls.all_results = list()

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.Useyn = rt.Runner('Усэйн', 10)
        self.Andrey = rt.Runner('Андрей', 9)
        self.Nick = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        pprint(cls.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour_1(self):
        Tour_1 = Corrected_Tournament(90, self.Useyn, self.Nick)
        result = Tour_1.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == self.Nick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour_2(self):
        Tour_2 = Corrected_Tournament(90, self.Andrey, self.Nick)
        result = Tour_2.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == self.Nick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour_3(self):
        Tour_3 = Corrected_Tournament(90, self.Useyn, self.Andrey, self.Nick)
        result = Tour_3.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == self.Nick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour_4(self):
        Tour_4 = Corrected_Tournament(10, self.Useyn, self.Andrey, self.Nick)
        result = Tour_4.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == self.Nick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour_5(self):
        Tour_5 = Corrected_Tournament(5, self.Useyn, self.Andrey, self.Nick)
        result = Tour_5.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == self.Nick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour_6(self):
        Tour_6 = Corrected_Tournament(2, self.Useyn, self.Andrey, self.Nick)
        result = Tour_6.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == self.Nick.name)


if __name__ == '__main__':
    unittest.main()






