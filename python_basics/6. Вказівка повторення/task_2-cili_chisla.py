# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Задача 2
# Програма - Цілі числа

a = int(input(print("Введіть число а:")))
b = int(input(print("Введіть число b:")))
c = int(input(print("Введіть число c:")))

while a <= b:
    if a % c == 0:
        print(a)
    a += 1
