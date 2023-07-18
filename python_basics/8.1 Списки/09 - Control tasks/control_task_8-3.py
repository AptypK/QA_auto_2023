# Course: QA Automation
# Week: 4
# Theme: Structured data types
# Modul 8. Structured data types
# Cotrol task: 8.3
# Dev: Artur Kychenko
# Date: 08.04.2023

value = input("Введіть елемент ")
digits_tuple = (1, 2, 3)

# your code goes here
value2 = list()

value2.append(value)
digits_tuple_sum = tuple(value2) + digits_tuple

print(digits_tuple_sum)
