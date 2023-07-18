day = int(input(print("Введіть номер дня тижня (1-7): ")))
time = int(input(print("Введіть тривалість розмови (хв): ")))
price = 2.30

if day == 6 or day == 7:
    price *= 0.8

cost = price * time

print(cost)
