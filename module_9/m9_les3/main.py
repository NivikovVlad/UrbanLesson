"""
Генераторные сборки
Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов
"""


if __name__ == '__main__':
    first = ['Strings', 'Student', 'Computers']
    second = ['Строка', 'Урбан', 'Компьютер']

    first_result = (len(word_1) - len(word_2) for word_1, word_2 in zip(first, second) if len(word_1) != len(word_2))
    second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))
    # print(first_result)
    print(list(first_result))
    # print(second_result)
    print(list(second_result))


"""
Вывод в консоль:
[1, 2]
[False, False, True]
"""