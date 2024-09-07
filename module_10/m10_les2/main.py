"""
Потоки на классах
Цель: научиться создавать классы наследованные от класса Thread
"""

from threading import Thread
from time import sleep


class Knight(Thread):
    COUNT_OF_ENEMY = 100

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies_left = Knight.COUNT_OF_ENEMY

    def run(self):
        count_day = 0
        print(f'{self.name}, на нас напали!')
        while self.enemies_left > 0:
            sleep(1)
            self.enemies_left -= self.power
            count_day += 1
            print(f'{self.name} сражается {count_day} день(дней), осталось {self.enemies_left} воинов')
        print(f'{self.name} одержал победу спустя {count_day} дней(дня)!')


if __name__ == '__main__':
    threads = []
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    # third_knight = Knight("Sir Cheburashka", 18)
    threads.append(first_knight)
    threads.append(second_knight)
    # threads.append(third_knight)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('Все битвы окончены')

"""
Sir Lancelot, на нас напали!
Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.
Sir Galahad, на нас напали!
Sir Galahad, сражается 1 день(дня)..., осталось 80 воинов.
Sir Galahad, сражается 2 день(дня)..., осталось 60 воинов.
Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.
Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.
Sir Galahad, сражается 3 день(дня)..., осталось 40 воинов.
Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.
Sir Galahad, сражается 4 день(дня)..., осталось 20 воинов.
Sir Galahad, сражается 5 день(дня)..., осталось 0 воинов.
Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.
Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.
Sir Galahad одержал победу спустя 5 дней(дня)!
Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.
Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.
Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.
Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.
Sir Lancelot одержал победу спустя 10 дней(дня)!
Все битвы закончились!
"""
