# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Модуль 7
# Задача 3
# Дано чотири числа x1, y1, x2, y2. Написати функцію dist(x1, y1, x2, y2),
# яка обчислює відстань між двома точками (x1, y1) та (x2, y2).
# Dev: Artur Kychenko
# Date: 27.04.2023


def dist(x1, y1, x2, y2):
    import math

    distance_between_points = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    return distance_between_points


coord_x1 = int(input("Введіть координатиn X1:"))
coord_y1 = int(input("Введіть координатиn Y1:"))
coord_x2 = int(input("Введіть координатиn X2:"))
coord_y2 = int(input("Введіть координатиn Y2:"))

print("Відстань між точками:", dist(coord_x1, coord_y1, coord_x2, coord_y2))
