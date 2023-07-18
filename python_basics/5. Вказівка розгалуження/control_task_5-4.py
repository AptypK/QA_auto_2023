t = int(input())
if t <= 0:
    rez = "Лід"
else:
    if t >0 and t < 100:
        rez = "Вода"
    else:
        if t >= 100:
            rez = "Пара"
print(rez)