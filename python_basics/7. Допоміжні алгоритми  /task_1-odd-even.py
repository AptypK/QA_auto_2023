# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Модуль 7
# Задача 1
# Програма - Напишіть функцію, яка приймає ціле число і друкує
# інформацію про парність чи непарність числа.
# Dev: Artur Kychenko
# Date: 27.04.2023


def parity_check(number):
    if number % 2 == 0:
        print("The number is odd")
    else:
        print("The number is even")
    return number


n = int(input("Введіть число n:"))
parity_check(n)
