"""
Домашнее задание по теме "Логирование"
Цель: получить опыт использования простейшего логирования совместно с тестами.
"""
import unittest
from rt_with_exceptions import Runner
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        try:
            r_1 = Runner('Вася', speed=-5)
            for i in range(10):
                r_1.walk()
            self.assertEqual(r_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        try:
            r_2 = Runner(('Test_runner_2', 'qwerty'))
            for i in range(10):
                r_2.run()
            self.assertEqual(r_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        r_3 = Runner('Test_runner_3')
        r_4 = Runner('Test_runner_4')

        for i in range(10):
            r_3.walk()
            r_4.run()

        self.assertNotEqual(r_3, r_4)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='runner_tests.log',
                        filemode='w', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

    unittest.main()



