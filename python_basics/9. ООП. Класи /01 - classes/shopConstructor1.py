# Course: QA Automation
# Week: 5
# Theme: OOP. Classes


# Modul 9. OOP. Classes
# Задача:
# Dev: Artur Kychenko
# Date: 22.05.2023
class ShopWorker:
    count_workers = 0

    def __init__(self, name1, age1):
        self.name = name1
        self.age = age1
        ShopWorker.count_workers += 1


print("всіх працівників ", ShopWorker.count_workers)

worker_one = ShopWorker("Іван", 25)

print(
    "Працівник 1: ",
    worker_one.name,
    " ",
    worker_one.age,
    " всіх працівників ",
    worker_one.count_workers,
)

worker_two = ShopWorker("Петро", 32)


print(
    "Працівник 2: ",
    worker_two.name,
    " ",
    worker_two.age,
    " всіх працівників ",
    worker_two.count_workers,
)
print("всіх працівників ", ShopWorker.count_workers)
