"""
Простые Юнит-Тесты
Цель: приобрести навык создания простейших Юнит-тестов
"""

import unittest
from pprint import pprint
from module_12.HumanMoveTest import runner_and_tournament as rt

"""
Класс Tournament(строка 35)
finishers[place] = participant заменена на
    finishers[place] = str(participant)
или вот так
    finishers[place] = participant.name
в противном случае в словарь попадает ссылка на объект в памяти
"""


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Словарь заменен на список
        """
        cls.all_results = list()

    def setUp(self):
        self.Useyn = rt.Runner('Усэйн', 10)
        self.Andrey = rt.Runner('Андрей', 9)
        self.Nick = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        pprint(cls.all_results)

    def test_Tour_1(self):
        Tour_1 = rt.Tournament(90, self.Useyn, self.Nick)
        result = Tour_1.start()
        self.assertTrue(result[max(result.keys())] == self.Nick.name)
        self.all_results.append(result)

    def test_Tour_2(self):
        Tour_2 = rt.Tournament(90, self.Andrey, self.Nick)
        result = Tour_2.start()
        self.assertTrue(result[max(result.keys())] == self.Nick.name)
        self.all_results.append(result)

    def test_Tour_3(self):
        Tour_3 = rt.Tournament(90, self.Useyn, self.Andrey, self.Nick)
        result = Tour_3.start()
        self.assertTrue(result[max(result.keys())] == self.Nick.name)
        self.all_results.append(result)


if __name__ == '__main__':
    unittest.main()






