# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task 9
# Напишіть програму, яка формує список з 10 цілих чисел - членів арифметичної прогресії
# (користувач задає значення першого члена і різницю арифметичної прогресії).
# Знайдіть суму десяти членів цієї арифметичної прогресії.
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Dev: Artur Kychenko
# Date: 07.04.2023

mas = []
n = 10

first_elem = int(input("Введіть перший член фриф. прог.:"))
step = int(input("Введіть різницю фриф. прог.:"))
sum = 0

for i in range(n):
    mas.append(first_elem)
    first_elem += step
    sum += mas[i]
#    print(mas[i], end=" ")
print("Cумв = ", sum)
