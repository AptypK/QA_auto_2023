# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# Задача: Зі списку температури повітря за тиждень, знайти: макс. значенняб к-ть днів з t > 0 та сер. t
# Dev: Artur Kychenko
# Date: 06.04.2023


# Ф-ція пошуку максимального значення у списку
def max_list(mas):
    max = mas[0]
    for i in range(1, len(mas)):
        if mas[i] > max:
            max = mas[i]
    return max


# Ф-ція обчислення к-ті значень більше 0 у списку
def positive_count(mas):
    number = 0
    for i in range(len(mas)):
        if mas[i] > 0:
            number += 1
    return number


def average_temperature(mas):
    s = 0
    for i in mas:
        s += i
    return s / len(mas)


temperature = [3, 5, -1, -3, -2, 1, 3]
print("Максимальна температура:", max_list(temperature))
print("К-ть днів з t>0:", positive_count(temperature))
print("Cередня температура:", round(average_temperature(temperature), 2))
