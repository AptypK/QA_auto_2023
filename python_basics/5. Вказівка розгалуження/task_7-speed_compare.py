print("Введіть швидкість в кілометрах за годину: ")
speed1 = int(input())
print("Швидкість в метрах за секунду: ")
speed2 = int(input())

speed1 = speed1 * 1000 /3600

if speed1 > speed2:
    rez = "First speed is higher"
else:
    if speed1 < speed2:
        rez = "Second speed is higher"
    else:
        rez = "Speeds are the same"
print(rez)
