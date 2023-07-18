print("Введіть вік Sasha: ")
age_Sasha = int(input())
print("Введіть вік Tanya: ")
age_Tanya = int(input())

if age_Sasha > age_Tanya:
    rez = "Sasha is older"
else:
    if age_Sasha < age_Tanya:
        rez = "Tanya is older"
    else:
        rez = "Sasha and Tanya are the same age"
print(rez)