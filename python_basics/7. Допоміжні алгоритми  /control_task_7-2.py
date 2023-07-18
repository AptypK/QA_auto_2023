# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)


# Модуль 7
# Завдання 7.2
# Реалізувати функцію, яка визначає чи число парне чи непарне.
# Dev: Artur Kychenko
# Date: 27.04.2023
def is_even_or_odd(n):
    if n % 2 == 0:
        return "число " + str(n) + " парне"
    else:
        return "число " + str(n) + " непарне"


number = int(input("Введіть число"))
print(is_even_or_odd(number))
