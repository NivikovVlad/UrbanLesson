"""
Систематизация и пропуск тестов.
Цель: понять на практике как объединять тесты при помощи TestSuite.
Научиться пропускать тесты при помощи встроенных в unittest декораторов.
"""

import unittest
from module_12.m12_les3.RunnerTest import RunnerTest
from module_12.m12_les3.TournamentTest import TournamentTest


if __name__ == '__main__':

    suite_12_3 = unittest.TestSuite()

    suite_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    suite_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_12_3)

