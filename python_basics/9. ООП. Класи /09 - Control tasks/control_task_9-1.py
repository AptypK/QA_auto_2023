# Course: QA Automation
# Week: 5
# Theme: OOP. Classes
# Modul 9. OOP. Classes
# Cotrol task: 9.1
# Dev: Artur Kychenko
# Date: 22.05.2023
windows_count = int(input("Введіть кількість вікон "))
flors_count = int(input("Введіть кількість поверхів "))


class Building:
    # your code goes here
    windows_count = 0
    flors_count = 0

    def __init__(self, windows_count1=0, flors_count1=0):
        Building.windows_count = windows_count1
        Building.flors_count = flors_count1

    def __str__(self):
        str_out = str(Building.windows_count * Building.flors_count)
        return str_out


print("Загальна кількість вікон {}".format(Building(windows_count, flors_count)))
