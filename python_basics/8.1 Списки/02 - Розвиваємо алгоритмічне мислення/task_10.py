# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task 10
# Перевірити чи введене число є паліндромом
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Dev: Artur Kychenko
# Date: 07.04.2023

mas = []
f_div = 10
mas_reverse = []

check = False

number = int(input("Введіть число:"))
n = len(str(number))

if n > 1:
    for i in range(n):
        mas.append(int((number - ((number // f_div) * f_div))))
        number = number // f_div
#        print(mas[i], end=" ")
else:
    mas.append(number)
    check = True

mas_reverse = list(mas)
mas.reverse()

for i in range(n):
    if mas[i] == mas_reverse[i]:
        check = True
    else:
        check = False
        break

if check:
    print("\n Palindrome")
else:
    print("\n Not a palindrome")
