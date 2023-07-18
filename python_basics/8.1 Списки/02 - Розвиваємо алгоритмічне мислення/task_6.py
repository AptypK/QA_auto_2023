# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task 6
# Створити список, який складатиметься з 8 значень дійсного типу.
# Організувати введення цього списку з клавіатури.
# Поміняти місцями максимальний та мінімальний елементи списку.
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Dev: Artur Kychenko
# Date: 06.04.2023

mas = []
n = 9
count = 0


for i in range(n):
    mas.append(float(input("Введіть значення:")))


# Початок - Функція пошуку max значення
def max_number(mas_f):
    if type(mas_f) == list:
        max_f = mas_f[0]
        for i in range(1, len(mas_f)):
            if mas_f[i] > max_f:
                max_f = mas_f[i]
    return max_f


# Кінець - Функція пошуку max значення


# Початок - Функція пошуку min значення
def min_number(mas_f):
    if type(mas_f) == list:
        min_f = mas_f[0]
        for i in range(1, len(mas_f)):
            if mas_f[i] < min_f:
                min_f = mas_f[i]
    return min_f


# Кінець - Функція пошуку min значення


max = max_number(mas)
min = min_number(mas)


for i in range(n):
    if mas[i] == max:
        pos_max = i
    if mas[i] == min:
        pos_min = i
    print(mas[i], " ", end="")
print("\n")

mas[pos_max] = min
mas[pos_min] = max

for i in range(n):
    print(mas[i], " ", end="")
print("\n")
