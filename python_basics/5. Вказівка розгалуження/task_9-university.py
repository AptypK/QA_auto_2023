print("Ввести значення оцінки: ")
mark = int(input())

if mark >= 90:
    rez = "A"
else:
    if mark >= 80:
        rez = "B"
    else:
        if mark >= 70:
            rez = "C"
        else:
            if mark >= 60:
                rez = "D"
            else:
                rez = "F"
print(rez)
