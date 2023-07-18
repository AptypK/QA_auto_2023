# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Задача 10
# Програма - Перевірити, чи введене число просте.
import math

n = int(input(print("Введіть число n:")))
flag = False
div = 2

while div <= math.sqrt(n) and not (flag):
    if n % div == 0:
        flag = True
    div += 1
if flag:
    print("Not a prime number")
else:
    print("Prime number")
