a = float(input("Введите число км в 1-й день:"))
b = float(input("Введите число км в X день:"))
n = 0
while a < b:
    a *= 1.1
    n += 1
print(n + 1)
