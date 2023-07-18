# Course: QA Automation
# Week: 4
# Theme: Structured data types
# Modul 8. Structured data types
# Cotrol task: 8.7
# Dev: Artur Kychenko
# Date: 08.04.2023

# your code goes here
dict_num = {}

n = int(input("Введіть значення ключа:"))

for i in range(n + 1):
    dict_num[i] = i * i

print(dict_num)
