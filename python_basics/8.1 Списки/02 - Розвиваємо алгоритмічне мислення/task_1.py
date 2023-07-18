# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task 1
# Створити список, який містить 10 значень цілого типу. Організувати введення цього списку
# з клавіатури. Вивести отриманий список на екран. Знайти суму всіх елементів списку.
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Dev: Artur Kychenko
# Date: 06.04.2023

mas = []
sum = 0
for i in range(10):
    mas.append(int(input("Введіть значення:")))

print("Result down")

for i in range(10):
    sum += mas[i]
    print(mas[i], " ", end="")

print("\n", "Сума всіх елементів:", sum)
