print("Введіть значення a: ")
a = int(input())
print("Введіть значення b: ")
b = int(input())
print("Введіть значення c: ")
c = int(input())

count = 0

if a == b:
    count += 1
    if a == c:
        count += 1
else:
    if a == c:
        count += 1
    else:
        if b == c:
            count += 1
print(count)
