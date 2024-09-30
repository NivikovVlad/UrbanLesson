"""
Простые Юнит-Тесты
Цель: приобрести навык создания простейших Юнит-тестов
"""

import unittest
from module_12.HumanMoveTest import runner


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        r_1 = runner.Runner('Test_runner_1')
        for i in range(10):
            r_1.walk()
        self.assertEqual(r_1.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        r_2 = runner.Runner('Test_runner_2')
        for i in range(10):
            r_2.run()
        self.assertEqual(r_2.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        r_3 = runner.Runner('Test_runner_3')
        r_4 = runner.Runner('Test_runner_4')

        for i in range(10):
            r_3.walk()
            r_4.run()

        self.assertNotEqual(r_3, r_4)


if __name__ == '__main__':
    unittest.main()




