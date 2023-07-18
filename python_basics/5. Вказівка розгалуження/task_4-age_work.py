print("Вводимо стаж робітника: ")
experience = int(input())
print("Вводимо вік робітника: ")
age = int(input())

if experience >= 5 and age <= 40:
    rez = "Candidate is suitable"
else:
    rez = "Candidacy is not suitable"
print(rez)