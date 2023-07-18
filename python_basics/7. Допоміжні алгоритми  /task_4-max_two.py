# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Модуль 7
# Задача 4
# Напишіть функцію max_two, яка визначає більше з двох чисел a, b.
# Використовуючи цю функцію, знайдіть найбільше з чотирьох чисел.
# Dev: Artur Kychenko
# Date: 27.04.2023


def max_two(a, b):
    if a > b:
        max = a
    else:
        max = b
    return max


number1 = int(input("Введіть число №1:"))
number2 = int(input("Введіть число №2:"))
number3 = int(input("Введіть число №3:"))
number4 = int(input("Введіть число №4:"))

more_than_two1 = max_two(number1, number2)
more_than_two2 = max_two(number3, number4)
more_than_four = max_two(more_than_two1, more_than_two2)

print(more_than_four)
