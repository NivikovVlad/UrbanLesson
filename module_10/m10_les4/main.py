"""
Очереди для обмена данными между потоками
Цель: Применить очереди в работе с потоками, используя класс Queue
"""
from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    """
    number - номер стола
    guest - объект класса Guest
    """
    def __init__(self, number, quest=None):
        self.number = number
        self.guest = quest


class Guest(Thread):
    """
    Класс создает поток для name - имя гостя
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    tables = []

    def __init__(self, *args):
        self.queue = Queue()
        for arg in args:
            self.tables.append(arg)

    def guest_arrival(self, *guests):
        """
        Прибытие гостей
        """
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                print(f'{guest.name} в очереди')
                self.queue.put(guest)

    def discuss_guests(self):
        """
        Обслуживание гостей
        """
        while not self.queue.empty() or [table.guest for table in self.tables if table.guest is not None]:
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла). '
                          f'Стол номер {table.number} свободен"')
                    table.guest = None
                if not self.queue.empty():
                    if table.guest is None:
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()
        print('Все поели, всем пока')


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
