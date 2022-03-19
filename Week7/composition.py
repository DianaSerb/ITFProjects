class Salary:
    def __init__(self, pay):
        self._pay = pay

    def get_total(self):
        return (self._pay * 12) / 4.95


class Employee:
    def __init__(self, pay, bonus):
        self._bonus = bonus
        self.object_salary = Salary(pay)

    def annual_salary(self):
        return "Total salary: " + str(self.object_salary.get_total() + self._bonus)


employee = Employee(1000, 100)
print(employee.annual_salary())

object_salary = Salary(100)
print(object_salary.get_total())
