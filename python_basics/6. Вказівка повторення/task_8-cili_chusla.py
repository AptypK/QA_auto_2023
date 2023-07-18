# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Задача 8
# Програма - Вивід цілих чисел та к-ті символів '#'

n = int(input(print("Введіть число n:")))
s = "#"
count = n

for count in range(n, 0, -1):
    print(count, end=" ")
    count1 = 0
    while count1 < count:
        print(s, end="")
        count1 += 1
    print("\n")
    count -= 1
