# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)


# Модуль 7
# Завдання 7.3
# Реалізувати функцію, яка виводить на екран значення від 0 до заданого числа включно з кроком 2.
# Dev: Artur Kychenko
# Date: 27.04.2023
def print_numbers(n):
    for i in range(0, n + 1, 2):
        print(i)


number = int(input("Введіть число"))
print_numbers(number)
