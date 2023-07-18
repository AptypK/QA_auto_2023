# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Задача 7
# Програма - Вивід парних чисел з 0 до твого віку

age = int(input(print("Введіть Ваш вік:")))

if age % 2 == 0:
    start = 0
else:
    start = 1
i = start
while i <= age:
    print(i)
    i += 2
