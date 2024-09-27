"""
Простые Юнит-Тесты
Цель: приобрести навык создания простейших Юнит-тестов
"""

import unittest
from module_12.HumanMoveTest import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """
        test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод walk у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 50.
        """
        r_1 = runner.Runner('Test_runner_1')
        for i in range(10):
            r_1.walk()
        self.assertEqual(r_1.distance, 50)

    def test_run(self):
        """
        test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод run у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 100.
        """

        r_2 = runner.Runner('Test_runner_2')
        for i in range(10):
            r_2.run()
        self.assertEqual(r_2.distance, 1000)

    def test_challenge(self):
        """
        test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Далее 10 раз у объектов вызываются методы run и walk соответственно.
        Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
        чтобы убедится в неравенстве результатов.
        """

        r_3 = runner.Runner('Test_runner_3')
        r_4 = runner.Runner('Test_runner_4')

        for i in range(10):
            r_3.walk()
            r_4.run()

        self.assertNotEqual(r_3, r_4)


if __name__ == '__main__':
    unittest.main()




