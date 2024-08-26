"""
001 Домашнее задание по теме "Try и Except".
"""


def add_everything_up(a, b):
    try:
        result = a + b
        return result

    except TypeError as exp:
        result = (f'обошли ошибку {exp}'
                  f'\n{str(a) + str(b)}')
        return result


if __name__ == "__main__":
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))

'''
123.456строка
яблоко4215
130.456
'''
