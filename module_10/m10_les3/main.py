"""
Блокировки и обработка ошибок
Цель: освоить блокировки потоков, используя объекты класса Lock и его методы
"""
from random import randint
from threading import Lock, Thread
from time import sleep


class Bank:
    TRANSACTION = 100

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(self.TRANSACTION):
            deposit = randint(50, 500)
            self.balance += deposit
            print(f'Пополнение: {deposit}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(self.TRANSACTION):
            withdraw = randint(50, 500)
            print(f'Запрос на {withdraw}')
            if withdraw <= self.balance:
                self.balance -= withdraw
                print(f'Снятие: {withdraw}. Баланс: {self.balance}')
                sleep(0.001)
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


if __name__ == '__main__':
    bk = Bank()

    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')

