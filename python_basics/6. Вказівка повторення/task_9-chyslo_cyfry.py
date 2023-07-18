# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Задача 9
# Програма - З клавіатури вводять число. Вивести всі його цифри

n = int(input(print("Введіть число n:")))
div = 1
temp = n

while temp > 10:
    temp = temp // 10
    div *= 10

while n > 0:
    print(n // div)
    n = n % div
    div = div // 10
