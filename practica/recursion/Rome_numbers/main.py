"""
M = 1000
D = 500
C = 100
L = 50
X = 10
V = 5
I = 1
"""

rome_code = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def rome_decoder(rome_number):
    if not rome_number:
        return 0
    elif len(rome_number) == 1:
        return rome_code[rome_number]
    else:
        pos_1, pos_2 = rome_code[rome_number[0]], rome_code[rome_number[1]]
        if pos_1 > pos_2:
            decimal_number = pos_1 + rome_decoder(rome_number[1:])
            return decimal_number
        elif pos_1 < pos_2:
            decimal_number = pos_2 - pos_1 + rome_decoder(rome_number[2:])
            return decimal_number
        else:
            decimal_number = pos_1 + rome_decoder(rome_number[1:])
            return decimal_number


if __name__ == '__main__':
    rome_number = input('Введите число в формате <MDCLXVI> ')
    # 99
    # rome_number = 'XCIX'
    rome_number = rome_number.upper()

    print(rome_decoder(rome_number))
