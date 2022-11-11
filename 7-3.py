# 3

class Cell:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

    def __add__(self, other):
        return Cell(round(self.n + other.n, 0))

    def __sub__(self, other):
        if self.n > other.n:
            return Cell(round(self.n - other.n, 0))
        else:
            return 'значение первой клетки должно быть больше чем у второй!'

    def __mul__(self, other):
        return Cell(round(self.n * other.n, 0))

    def __truediv__(self, other):
        if self.n > other.n:
            return Cell(round(self.n / other.n, 0))
        else:
            return 'значение первой клетки должно быть больше чем у второй!'

    def make_order(self, m):
        if m > self.n:
            return 'слишком большое количество рядов!'
        s = list("*" * self.n)
        for i in range(1, self.n // m + 1):
            s.insert(i * m + i-1,'\n')
        return ''.join(s)

a = Cell(15)
b = Cell(3)

c =  a + b
print(c)

c =  a - b
print(c)

c =  a * b
print(c)

c =  a / b
print(c)

print(a.make_order(3))