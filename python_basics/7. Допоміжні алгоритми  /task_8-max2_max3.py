# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Модуль 7
# Задача 8
# Використовуючи функцію max2(a,b), яка визначає максимальне з двох заданих значень,
# написати функцію max3(a,b,c)..
# Dev: Artur Kychenko
# Date: 27.04.2023


def max2(a, b):
    if a > b:
        max = a
    else:
        max = b
    return max


def max3(a, b, c):
    max = max2(max2(a, b), c)
    return max


a = int(input("Введіть a:"))
b = int(input("Введіть b:"))
c = int(input("Введіть c:"))
d = int(input("Введіть d:"))
e = int(input("Введіть e:"))
f = int(input("Введіть f:"))

print(max3(a, b, c) + max3(d, e, f))
