# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Модуль 7
# Задача 5
# Дано два циліндра задані радіусами основи та висотами.
# Визначити, який з циліндрів має більший об’єм.
# Dev: Artur Kychenko
# Date: 27.04.2023


def cylinder_volume(radius, height):
    import math

    volume = math.pi * radius**2 * height
    return volume


r1 = int(input("Введіть число r1:"))
h1 = int(input("Введіть число h1:"))
r2 = int(input("Введіть число r2:"))
h2 = int(input("Введіть число h2:"))

v1 = cylinder_volume(r1, h1)
v2 = cylinder_volume(r2, h2)

if v1 > v2:
    print("The first cylinder is larger")
elif v2 > v1:
    print("The second cylinder is larger")
else:
    print("The cylinders are of equal size")
