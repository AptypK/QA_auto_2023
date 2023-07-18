# Course: QA Automation
# Week: 5
# Theme: OOP. Classes
# Modul 9. OOP. Classes
# Cotrol task: 9.4
# Dev: Artur Kychenko
# Date: 24.05.2023
input_sentence = input("Введіть речення: ")
sentence_to_compare = input("Введіть речення для порівняння: ")
new_word = input("Введіть нове слово, яке потрібно додати в кінець речення: ")
input_word_to_remove = input("Введіть слово яке потрібно вилучити: ")


class Sentence:
    sentence = str()

    # your code goes here
    def __init__(self, sentence1):
        Sentence.sentence = sentence1

    # Змінити регістр на всі маленькі літери значення атрибута об'єкту sentence
    def to_lower(self):
        Sentence.sentence = Sentence.sentence.lower()

    # Видалити введене слово в атрибуті об'єкта sentence і зберегти змінений стан цього атрибута
    def remove_word(self, word_to_remove):
        Sentence.sentence = Sentence.sentence.replace(word_to_remove, "")

    # Додати введений текст в кінець речення в атрибуті об'єкта sentence і зберегти змінений стан цього атрибута
    def add_word(self, word_to_add):
        Sentence.sentence += word_to_add

    # Порівняти речення з введеним користувачем
    def is_similar(self, sentence_to_compare=str):
        rez = bool
        if Sentence.sentence.lower() == sentence_to_compare.lower():
            rez = True
        else:
            rez = False
        return rez


my_sentence = Sentence(input_sentence)
print(my_sentence.is_similar(sentence_to_compare))

my_sentence.add_word(new_word)
my_sentence.to_lower()
print(my_sentence.sentence)


my_sentence.remove_word(input_word_to_remove)
print(my_sentence.sentence)
