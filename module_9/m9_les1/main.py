"""
Введение в функциональное программирование
Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова
"""


def apply_all_func(int_list: (int, float), *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


if __name__ == "__main__":
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

'''
Вывод на консоль:
{'max': 20, 'min': 6} 
{'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
'''