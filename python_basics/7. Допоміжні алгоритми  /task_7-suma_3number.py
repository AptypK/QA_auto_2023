# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Модуль 7
# Задача 7
# Напишіть функцію для визначення суми трьох цілих чисел.
# Якщо будь-які два значення однакові, необхідно вивести нуль.
# Dev: Artur Kychenko
# Date: 27.04.2023


def suma(num1, num2, num3):
    if num1 == num2:
        sum = 0
    elif num1 == num3:
        sum = 0
    elif num2 == num3:
        sum = 0
    else:
        sum = num1 + num2 + num3
    return sum


a = int(input("Введіть a:"))
b = int(input("Введіть b:"))
c = int(input("Введіть c:"))

result = suma(a, b, c)
print(result)
