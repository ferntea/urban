# module_7_c Оператор "with".

'''
Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:

    'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

Алгоритм получения словаря такого вида в методе get_all_words:

    Создайте пустой словарь all_words.
    Переберите названия файлов и открывайте каждый из них, используя оператор with.
    Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
    Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
    Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.


find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

for name, words in get_all_words().items():
  # Логика методов find или count
'''

class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)
        self.all_words = {}

    def get_all_words(self):
        punctuation_table = str.maketrans('', '', ',.=!-?;:')
        for file_name in self.file_names:
            words_list = []
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.lower()
                    line = line.translate(punctuation_table)
                    words = line.split()
                    words_list.extend(words)
            self.all_words[file_name] = words_list
        return self.all_words

    def find(self, word):       # finds first position according to the task
        word_lower = word.lower()
        for name, words in self.get_all_words().items():
            for idx, w in enumerate(words):
                if w.lower() == word_lower:
                    return {name: idx + 1}  # Add 1 to the index to show the actual position
        return {}

    def count(self, word):
        result = {}
        word_lower = word.lower()
        for name, words in self.get_all_words().items():
            result[name] = sum(w.lower() == word_lower for w in words)
        return result


finder = WordsFinder('module_7_3_file1.txt', 'module_7_3_file2.txt', 'module_7_3_file3.txt')
print(finder.get_all_words())
print(finder.find('word1'))
print(finder.count('word1'))

finder2 = WordsFinder('module_7_3_test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
