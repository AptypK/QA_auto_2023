# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Модуль 7
# Задача 9
# Визначте, яку суму отримає вкладник через m років, якщо відсоткова ставка складає p% в рік.
# Дані вводяться в порядку n, p, m як у вхідних даних.
# Dev: Artur Kychenko
# Date: 27.04.2023


def deposit(dep, rate, year):
    suma = dep + dep * rate / 100 * year
    return suma


n = int(input("Введіть суму:"))
p = int(input("Введіть відсоткову ставку %:"))
m = int(input("Введіть термін:"))

result = deposit(n, p, m)
print(result)
