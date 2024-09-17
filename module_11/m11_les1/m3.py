"""
Библиотека matplotlib помогает визуализировать вычисления
Построение всех возможных графиков и их комбинаций
"""


import matplotlib.pyplot as plt


def run():

    x = [1, 2, 3, 4, 5]
    y = [25, 32, 34, 20, 25]
    plt.plot(x, y)
    plt.xlabel('Ось х')  # Подпись для оси х
    plt.ylabel('Ось y')  # Подпись для оси y
    plt.title('Первый график')  # Название
    plt.show()

    vals = [24, 17, 53, 21, 35]
    labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]

    plt.pie(vals, labels=labels)
    plt.title("Распределение марок автомобилей на дороге")
    plt.show()
