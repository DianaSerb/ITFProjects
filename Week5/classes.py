class Calculator:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def sum(self):
        return self._a + self._b

    def dif(self):
        return self._a - self._b

    def inmultire(self,c):
        return self._a * self._b *c

    @staticmethod
    def impartire(a, b):
        return a / b


my_calculator = Calculator(3, 4)

print(my_calculator.sum())
print(my_calculator.dif())
print(my_calculator.impartire(10, 5))
print(my_calculator.inmultire(5))
