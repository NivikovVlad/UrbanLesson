def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    print(f' Корень: {root_word} \n Список слов: {other_words}')
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(f'Однокоренные: {result1}')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(f'Однокоренные: {result2}')
