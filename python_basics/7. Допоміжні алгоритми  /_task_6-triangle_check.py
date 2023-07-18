# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Модуль 7
# Задача 6
# Напишіть функцію, яка перевіряє, чи існує трикутник із введеними сторонами a, b, c.
# Dev: Artur Kychenko
# Date: 27.04.2023


def triangle_check(side1, side2, side3):
    if side1 <= side2 + side3:
        rez = False
    else:
        rez = True
    return rez


a = int(input("Введіть a:"))
b = int(input("Введіть b:"))
c = int(input("Введіть c:"))

rez1 = triangle_check(a, b, c)
rez2 = triangle_check(b, a, c)
rez3 = triangle_check(c, b, a)

if rez1 and rez2 and rez3:
    print("True")
else:
    print("False")
