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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod # an alternative constructor
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, int(pay))

    @staticmethod # doesn't automatically take in self, or cls cuz it doesn't need it
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('brill', 'wang', 100000)
emp2 = Employee('test', 'test', 100000)

Employee.set_raise_amt(1.07)
print emp1.raise_amt
print emp2.raise_amt

emp3 = Employee.from_string("john-doe-50000")
print emp3.__dict__

import datetime
date = datetime.date(2018, 1, 10)
print Employee.is_workday(date)

#tutorial from https://www.youtube.com/watch?v=rq8cL2XMM5M
