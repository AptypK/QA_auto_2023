# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task 2
# Створити список , який складатиметься з 7 значень дійсного типу.
# Організувати введення цього списку з клавіатури. Знайти добуток додатних елементів списку.
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Dev: Artur Kychenko
# Date: 06.04.2023

mas = []
result = 1
flag = False
for i in range(7):
    mas.append(float(input("Введіть значення:")))

for i in range(7):
    if mas[i] > 0:
        result *= mas[i]
        flag = True

if flag:
    print("Добуток додатних елементів списку.", result)
else:
    print("Додатні числа відсутні.")
