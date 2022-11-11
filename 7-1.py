# 1

class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        s=''
        for i in self.param:
            s += str(i) + '\n'
        return s

    def __add__(self, other):
        if len(self.param) != len(other.param):
            return 'Размер матриц должен быть одинаков'
        try:
            n = []
            for i in range(0, len(self.param)):
                m = []
                for j in range(0, len(self.param[i])):
                    m.append(self.param[i][j] + other.param[i][j])
                n.append(m)
            return Matrix(n)
        except:
            return 'Ошибка сложения матриц. Проверьте размерность матриц!'

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
a = Matrix(m1)
b = Matrix(m2)
print(a)

print(a + b)