class Salary:
    def __init__(self, pay):
        self._pay = pay

    def get_total(self):
        return (self._pay * 12) / 4.95


class Employee:
    def __init__(self, pay, bonus):
        self._pay = pay
        self._bonus = bonus

    def annual_salary(self):
        return "Total salary is " + str(self._pay.get_total() + self._bonus)


x = Salary(123)
y = Salary(150)
e = Employee(x, 1000)
print(e.annual_salary())
