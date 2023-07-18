# Course: QA Automation
# Week: 5
# Theme: OOP. Classes
# Modul 9. OOP. Classes
# Cotrol task: 9.2
# Dev: Artur Kychenko
# Date: 22.05.2023
car_1 = input("Введіть марку автомобіля 1 ")
car_2 = input("Введіть марку автомобіля 2 ")
car_3 = input("Введіть марку автомобіля 3 ")

str_out = [""]


class Cars:
    list_of_cars = []

    # your code goes here
    def __init__(self, list_of_cars1=[]):
        pass


Cars.list_of_cars.append(car_1)
Cars.list_of_cars.append(car_2)
Cars.list_of_cars.append(car_3)

"-".join(str_out)

print(
    "Список авто: {} та {} та {}".format(
        Cars.list_of_cars[0], Cars.list_of_cars[1], Cars.list_of_cars[2]
    )
)
