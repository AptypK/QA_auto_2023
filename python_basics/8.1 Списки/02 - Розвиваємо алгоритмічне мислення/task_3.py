# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task 3
# Створити список , який складатиметься з 9 значень цілого типу.
# Організувати введення цього списку з клавіатури.
# Знайти кількість від’ємних елементів списку
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Dev: Artur Kychenko
# Date: 06.04.2023

mas = []
count = 0
n = 9
for i in range(n):
    mas.append(int(input("Введіть значення:")))


for i in range(n):
    if mas[i] < 0:
        count += 1
if count > 0:
    print("Кількість від’ємних елементів списку:", count)
else:
    print("Кількість від’ємних елементів списку:", count)
