# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Задача 6
# Програма - Підрахунок к-ті вантажу, що надходить на склад ємністю 100т

count = 0
weight = int(input(print("Введіть вагу машини:")))
real_weight = weight


while real_weight <= 100:
    count += 1
    weight = int(input(print("Введіть вагу машини:")))
    real_weight += weight

print("Кількість машин", count)
