print("Введіть число num1: ")
num1 = int(input())
print("Введіть число num2: ")
num2 = int(input())

sum = num1 + num2
product = num1 * num2

if  sum < product:
    rez = product
else:
    if product < sum:
        rez = sum
    else:
  #      if sum == product:
        rez = num1-num2
print(rez)
