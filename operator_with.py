

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:

            with open(file_name, encoding="utf-8") as file:
                text = file.read().lower().translate(str.maketrans("", "", ".,!"))
                all_words[file_name] = text.split()

        return  all_words

    def find(self, word):
        find_word = {}

        for name, words in self.get_all_words().items():

            if word.lower() in words:
                find_word[name] = words.index(word.lower()) + 1

        return find_word

    def count(self, word):
        count_word = {}

        for name, words in self.get_all_words().items():

            if words.count(word.lower()) > 0:
                count_word[name] = words.count(word.lower())

        return count_word

with open("test_file.txt", "w", encoding="utf-8") as file:
    file.write("It's a text for task Найти везде,\n"
               "Используйте его для самопроверки.\n"
               "Успехов в решении задачи!\n"
               "text text text\n")

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего