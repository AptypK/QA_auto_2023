# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task 5
# Створити список , який складатиметься з 12 значень дійсного типу.
# Організувати введення цього списку з клавіатури.
# Знайдіть кількість елементів списку (включаючи максимальний), які відмінні
# від найбільшого елемента не більше ніж на 30%.
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Dev: Artur Kychenko
# Date: 06.04.2023

mas = []
n = 12
count = 0


for i in range(n):
    mas.append(float(input("Введіть значення:")))


# Початок - Функція пошуку максимального значення
def max_number(mas_f):
    if type(mas_f) == list:
        max_f = mas_f[0]
        for i in range(1, len(mas_f)):
            if mas_f[i] > max_f:
                max_f = mas_f[i]
    return max_f


# Кінець - Функція пошуку максимального значення

max = max_number(mas)

for i in range(n):
    if mas[i] >= (max - (max * 30 / 100)):
        count += 1

# print("MAX значення:", max)
print("К-ть :", count)
