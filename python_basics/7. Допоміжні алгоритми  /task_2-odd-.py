# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Модуль 7
# Задача 2
# Напишіть функцію яка перевірятиме чи введений рік високосний.
# Dev: Artur Kychenko
# Date: 27.04.2023


def year_check(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print(True)
    else:
        print(False)
    return year


n = int(input("Введіть число n:"))
year_check(n)
