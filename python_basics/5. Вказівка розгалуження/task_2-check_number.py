print("Введіть число: ")
number = int(input())

if number > 0:
    rez = "Number is positive"
if number < 0:
    rez = "Number is negative"
if number == 0:
    rez = "Number is zero"

print(rez)
