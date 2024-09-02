"""
Создание функций на лету
Цель: освоить на практике замыкание, объекты-функторы и lambda-функции
"""


from random import choice


def comparison_of_symbols():
    """
    Lambda-функция
    Результатом должен быть список совпадения букв в той же позиции:
    [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
    """

    first = 'Мама мыла раму'
    second = 'Рамена мало было'

    result = list(map(lambda x, y: x == y, first, second))

    return result


def get_advanced_writer(file_name):
    """
    Замыкание
    """

    def write_everything(*data_set):
        try:
            with open(file_name, 'w', encoding='utf8') as f:
                for data in data_set:
                    f.write(str(data) + '\n')
        except Exception as exc:
            print('Упс!\n' + str(exc))
        else:
            print(f'Файл {file_name} успешно создан\n'
                  f'Данные добавлены')
    return write_everything


class MysticBall:
    """
    Метод __call__
    """

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        rand_choice = choice(self.words)
        return rand_choice


if __name__ == '__main__':
    # Lambda - функция
    print(comparison_of_symbols())

    # Замыкание
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    # Метод __call__
    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())
