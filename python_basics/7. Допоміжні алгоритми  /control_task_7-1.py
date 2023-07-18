# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)


# Модуль 7
# Завдання 7.1
# Реалізувати функцію, яка переводить введені користувачем милі в кілометри.
# Dev: Artur Kychenko
# Date: 27.04.2023
def convert_miles_to_km(miles):
    km = miles * 1.6
    return round(km, 2)


miles = float(input("Введіть милі:"))
print(convert_miles_to_km(miles))
