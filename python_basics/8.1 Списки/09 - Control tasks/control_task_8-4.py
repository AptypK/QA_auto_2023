# Course: QA Automation
# Week: 4
# Theme: Structured data types
# Modul 8. Structured data types
# Cotrol task: 8.4
# Dev: Artur Kychenko
# Date: 08.04.2023

value1 = input("Введіть перший елемент ")
value2 = input("Введіть другий елемент ")
value3 = input("Введіть третій елемент ")
value4 = input("Введіть четвертий елемент ")
value5 = input("Введіть п'ятий елемент ")

# your code goes here
numbers1 = (value1, value2, value3, value4, value5)
numbers2 = numbers1[(len(numbers1) - 2) :]

print(numbers2)
