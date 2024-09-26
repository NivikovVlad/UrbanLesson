nato_code = {
    'A': 'Álpha',
    'B': 'Brávo',
    'C': 'Chárlie',
    'D': 'Délta',
    'E': 'Écho',
    'F': 'Fóxtrot',
    'G': 'Gólf',
    'H': 'Hotél',
    'I': 'Índia',
    'J': 'Júliett',
    'K': 'Kílo',
    'L': 'Líma',
    'M': 'Míke',
    'N': 'Novémber',
    'O': 'Óscar',
    'P': 'Papá',
    'Q': 'Quebéc',
    'R': 'Rómeo',
    'S': 'Siérra',
    'T': 'Tángo',
    'U': 'Úniform',
    'V': 'Víctor',
    'W': 'Whísky',
    'X': 'X́ray',
    'Y': 'Yánkee',
    'Z': 'Zúlu'
}
reg = [' ', ',', '.', '!', ':', ';', '-', '_']


def nato_decoder(text):
    if not text:
        return ''
    else:
        result = str(nato_code[text[0]]) + ' ' + str(nato_decoder(text[1:]))
        return result


if __name__ == '__main__':
    # text = 'Hello hh'
    text = input('Текст для шифра: ')
    for elem in text:
        if elem in reg:
            text = text.replace(elem, '')
    text = text.upper()
    print(nato_decoder(text))
