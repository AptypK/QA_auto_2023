# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task 4
# Створити список , який складатиметься з 6 значень дійсного типу.
# Організувати введення цього списку з клавіатури. Знайти максимальний елемент списку
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Dev: Artur Kychenko
# Date: 06.04.2023

mas = []
n = 6

for i in range(n):
    mas.append(float(input("Введіть значення:")))


# Початок - Функція пошуку максимального значення
def max_number(mas_f):
    if type(mas_f) == list:
        max = mas_f[0]
        for i in range(1, len(mas_f)):
            if mas_f[i] > max:
                max = mas_f[i]
    return max


# Кінець - Функція пошуку максимального значення
print("MAX значення:", max_number(mas))
