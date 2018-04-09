class Employee:
    raise_amt = 1.04
    employee_count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.employee_count += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp1 = Employee('brill', 'wang', 100000)
emp2 = Employee('test', 'test', 100000)

emp1.raise_amt = 1.1
emp1.apply_raise()
emp2.apply_raise()

print emp1.pay
print emp2.pay
print Employee.employee_count
