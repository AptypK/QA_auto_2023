import math

price = 6500

rate = float(input("Введіть курс євро до гривні: "))
rate = math.fabs(rate)
donate = int(input("Введіть сума в гривнях, яку зібрали волонтери: "))
donate = math.fabs(donate)


print(int(donate // (price*rate)))