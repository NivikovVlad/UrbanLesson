"""
Генераторы
Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python
"""


def all_variants(text):
    len_ = len(text)
    for i in range(len_):
        for j in range(i, len_):
            yield text[j - i: j + 1]


if __name__ == '__main__':
    a = all_variants("abc")
    for k in a:
        print(k)
