"""
Списковые, словарные сборки
Цель: закрепить знания о списочных и словарных сборках, решив несколько небольших задач
"""


if __name__ == '__main__':
    first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
    second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
    first_result = [len(word) for word in first_strings if len(word) > 5]
    second_result = [(word_1, word_2)
                     for word_1 in first_strings
                     for word_2 in second_strings
                     if len(word_1) == len(word_2)]
    third_result = {word: len(word) for word in (first_strings + second_strings) if not len(word) % 2}

    print(first_result)
    print(second_result)
    print(third_result)


"""
Вывод на консоль:
[10, 8, 8]
[('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
{'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
"""