# Course: QA Automation
# Week: 5
# Theme: OOP. Main principles


# Modul 10. OOP. Main principles
# Dev: Artur Kychenko
# Date: 24.05.2023

class ShopWorker:
    _count_workers = 0

    def __init__(self, name1="", age1=0):
        self.name = name1
        self.__age = age1
        self.settings_id

    def settings_id(self):
        ShopWorker._count_workers += 1
        self.id = ShopWorker._count_workers

    def add_year(self):
        self.__age += 1

    def __str__(self):
        str_out = "Працівник " + str(self.id) + ": " + self.name + " " + str(self.__age)
        str_out += " всіх працівників " + str(ShopWorker._count_workers)
        return str_out

    @staticmethod
    def info():
        print("В магазині працює:", ShopWorker._count_workers, "працівників")

    @classmethod
    def naming_shop(cls, name):
        cls.name_shop = name
        return cls.name_shop


ShopWorker.info()
print(ShopWorker._count_workers)

worker_one = ShopWorker("Іван", 25)
print(worker_one)
worker_one.add_year(3)
print(worker_one)


worker_two = ShopWorker("Петро", 32)
print(worker_two)

worker_two.add_year(2)
print(worker_two)

print("Назва магазину: ", worker_one.naming_shop("Fara"))
print("Назва магазину: ", ShopWorker.name_shop)
print("Назва магазину: ", ShopWorker.naming_shop("Para"))
