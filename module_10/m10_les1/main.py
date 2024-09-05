"""
Создание потоков
Цель: понять как работают потоки на практике, решив задачу
"""
import time
from threading import Thread
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'w+', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')


if __name__ == "__main__":
    # Без потоков
    time_start = datetime.now()

    wite_words(10, 'example1.txt')
    wite_words(30, 'example2.txt')
    wite_words(200, 'example3.txt')
    wite_words(100, 'example4.txt')

    time_end = datetime.now()
    print(f'Время работы без потоков: {time_end - time_start}')

    # С потоками
    time_start = datetime.now()

    thr1 = Thread(target=wite_words, args=(10, 'example5.txt'))
    thr2 = Thread(target=wite_words, args=(30, 'example6.txt'))
    thr3 = Thread(target=wite_words, args=(200, 'example7.txt'))
    thr4 = Thread(target=wite_words, args=(100, 'example8.txt'))
    threads = [thr1, thr2, thr3, thr4]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    time_end = datetime.now()
    print(f'Время работы c потоками: {time_end - time_start}')

