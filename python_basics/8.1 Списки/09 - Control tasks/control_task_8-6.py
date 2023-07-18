# Course: QA Automation
# Week: 4
# Theme: Structured data types
# Modul 8. Structured data types
# Cotrol task: 8.6
# Dev: Artur Kychenko
# Date: 08.04.2023

str_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

# your code goes here
str_del = input("Вкажіть елемент для видалення:")
if str_del in str_set:
    str_set.difference_update(str_del)

print(str_set)
