print("Введіть температуру: ")
temp = int(input())

if temp <= 0:
    rez = "A cold, isn’t it?"
else:
    if temp < 10:
        rez = "Cool"
    else:
        rez = "Nice weather we’re having"
print(rez)
