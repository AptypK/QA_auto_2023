# Course: QA Automation
# Week: 4
# Theme: Structured data types
# Modul 8. Structured data types
# Cotrol task: 8.2
# Dev: Artur Kychenko
# Date: 08.04.2023

number = int(input("Введіть число "))
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rez = False
# your code goes here
for i in range(len(a)):
    if number == a[i]:
        rez = True
        break

if rez:
    print("Введене число - існує")
else:
    print("Введене число - не існує")
