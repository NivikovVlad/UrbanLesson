"""
Многопроцессорное программирование
Цель: понять разницу между линейным и многопроцессорным подходом, выполнив операции обоими способами
"""
from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf8') as f:
        for line in f.readlines():
            if line is not None:
                all_data.append(f'{line}\n')


def main(n, p):
    """
    Запускает код 'n' раз в 'p' процессах
    :param n: количество запусков
    :param p: количество процессов
    """
    for _ in range(0, n):
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        with Pool(p) as pool:
            pool.map(read_info, filenames)


if __name__ == "__main__":
    start = datetime.now()
    main(3, 1)
    end = datetime.now()
    print(end - start)

    """
    0:00:44.987368 для 'n' = 5, 'p' = 1
    0:00:18.625874 для 'n' = 5, 'p' = 3
    0:00:17.952446 для 'n' = 5, 'p' = 5
    """
