# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task 8
# З клавіатури вводять число. Знайти суму цифр числа (див. задачу 9 алгоритми з циклами)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Dev: Artur Kychenko
# Date: 06.04.2023

mas = []
sum = 0
f_div = 10

number = int(input("Введіть число:"))
n = len(str(number))

if n > 1:
    for i in range(n):
        mas.append(int((number - ((number // f_div) * f_div))))
        number = number // f_div
        sum += mas[i]
else:
    sum += number

print(sum)
