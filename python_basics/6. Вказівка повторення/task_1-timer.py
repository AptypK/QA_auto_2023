# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Задача 1
# Програма - Timer
import time

n = int(input(print("введіть початкове значення таймеру:")))
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print("Start!")
