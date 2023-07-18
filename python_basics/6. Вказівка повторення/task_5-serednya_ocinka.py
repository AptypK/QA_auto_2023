# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Задача 5
# Програма - Визначення середньої оцінки учна

n = int(input(print("Введіть к-ть предметів n:")))
avg = 0
i = 1
mark = 0

while i <= n:
    mark = int(input(print("Введіть", str(i) + "-у оцінку:")))
    i += 1
    avg += mark
avg /= n
print("Середня оцінка:", avg)
