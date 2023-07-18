# Course: QA Automation
# Week: 4
# Theme: Structured data types
# Modul 8. Structured data types
# Cotrol task: 8.10
# Dev: Artur Kychenko
# Date: 08.04.2023


last_name = input("Введіть прізвище ")
name = input("Введіть ім'я ")
second_name = input("Введіть по батькові ")

# your code goes here
if len(last_name) == 0 or len(name) == 0 or len(second_name) == 0:
    print("Не введений ключовий параметр")
else:
    print(f"{last_name} {name[0]}.{second_name[0]}.")
