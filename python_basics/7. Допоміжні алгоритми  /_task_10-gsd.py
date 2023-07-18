# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Модуль 7
# Задача 10
# Написати функцію обчислення НСД (найбільший спільний дільник). Скористайтеся алгоритмом Евкліда
# Dev: Artur Kychenko
# Date: 27.04.2023


def gsd(num1, num2):
    if num2 == 0:
        return num1
    else:
        result = gsd(num2, num1 % num2)


a = int(input("Введіть a:"))
b = int(input("Введіть b:"))

result = gsd(a, b)
print(result)
