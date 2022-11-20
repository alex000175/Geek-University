class Complex:
    def __init__(self, str):
        try:
            self.param = complex(str)
        except:
            print('Введите комплесное число без пробелов!')

    def __add__(self, other):
        try:
            return(self.param + other.param)
        except:
            return 'Ошибка сложения комплексных чисел!'

    def __mul__(self, other):
        try:
            return(self.param * other.param)
        except:
            return 'Ошибка умножения комплексных чисел!'


a = Complex('3+10j')
b = Complex('30-3j')

print(a + b)
print(a * b)
