"""
Вывод на консоль:
((1, 0), 'Text for tell.')
((2, 16), 'Используйте кодировку utf-8.')
((3, 66), 'Because there are 2 languages!')
((4, 98), 'Спасибо!')
"""


def custom_write(file_name, strings):
    strings_positions = {}
    open(file_name, 'a').close()
    with open(file_name, 'w', encoding='utf-8') as f:
        for i, line in enumerate(strings):
            byte_ = f.tell()
            f.write(line + "\n")
            strings_positions[(i + 1, byte_)] = line
    return strings_positions


if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
