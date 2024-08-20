from pprint import pprint


class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        """
        Читает файлы. Удаляет пунктуацию
        :return: словарь - Название файла: список слов
        """
        all_words = {}
        dell_symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            with open(file, encoding='utf-8') as f:
                file_read = f.read().lower()
                for symbol in dell_symbols:
                    file_read = file_read.replace(symbol, '')
                all_words[file] = file_read.split()
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        find_words = {}
        for key, value in all_words.items():
            for i, iter_word in enumerate(value):
                if word.lower() == iter_word:
                    find_words[key] = i + 1
                    break
        return find_words

    def count(self, word):
        all_words = self.get_all_words()
        count_words = {}
        for key, value in all_words.items():
            i = 0
            for iter_word in value:
                if word.lower() == iter_word:
                    i += 1
            count_words[key] = i
        return count_words


if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt', 'test2_file.txt')
    pprint(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
