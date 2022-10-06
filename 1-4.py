n = int(input("Введите число:\n"))
m = 0
while n > 0:
    s = n % 10
    if s > m:
        m = s
    n = n // 10

print(m)
