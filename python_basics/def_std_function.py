# Початок - Функція пошуку max значення
def max_number(mas_f):
    if type(mas_f) == list:
        max_f = mas_f[0]
        for i in range(1, len(mas_f)):
            if mas_f[i] > max_f:
                max_f = mas_f[i]
    return max_f


# Кінець - Функція пошуку max значення


# Початок - Функція пошуку min значення
def min_number(mas_f):
    if type(mas_f) == list:
        min_f = mas_f[0]
        for i in range(1, len(mas_f)):
            if mas_f[i] < min_f:
                min_f = mas_f[i]
    return min_f


# Кінець - Функція пошуку min значення

i_massiv = [1, 5, 7, 0, 10, 111, -6]
print("Max =", min_number(i_massiv))
