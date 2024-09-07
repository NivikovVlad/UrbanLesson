"""
Блокировки и обработка ошибок
Цель: освоить блокировки потоков, используя объекты класса Lock и его методы
"""
from random import randint
from threading import Lock, Thread
from time import sleep


class Bank:
    TRANSACTION = 100
    # withdraw_list = []
    # deposit_list = []

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        self.lock.acquire()
        for _ in range(self.TRANSACTION):
            deposit = randint(50, 500)
            self.balance += deposit
            # self.deposit_list.append('1')
            print(f"Пополнение: {deposit}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        self.lock.acquire()
        for _ in range(self.TRANSACTION):
            withdraw = randint(50, 500)
            print(f'Запрос на {withdraw}')
            if withdraw <= self.balance:
                self.balance -= withdraw
                # self.withdraw_list.append('1')
                print(f"Снятие: {withdraw}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                # self.withdraw_list.append('1')
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
    # print(f'deposit_list {len(Bank.deposit_list)}')
    # print(f'withdraw_list {len(Bank.withdraw_list)}')
