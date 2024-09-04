"""
Декораторы

Цель задания:
Освоить механизмы создания декораторов Python
Практически применить знания, создав функцию декоратор и обернув ею другую функцию
"""


def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n < 2:
            return f'Составное'
        if n == 2:
            return f'Простое'
        if n % 2 == 0:
            return f'Составное'

        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return f'Составное'
            else:
                return f'Простое'

        return n
    return wrapper


@is_prime
def sum_three(*args):
    sum_ = sum(args)
    print(sum_)
    return sum_


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)
    result = sum_three(0)
    print(result)
    result = sum_three(2)
    print(result)
    result = sum_three(44)
    print(result)
