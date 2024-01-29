#!/usr/bin/python3

class Employee:
    number_of_employees = 0
    raise_amt = 1.04

    def __init__(self, first, last, age, pay, location="Nairobi"):
        self.first = first
        self.last = last
        self.email = '{}{}@gmail.com'.format(self.first, self.last)
        self.age = age
        self.pay = pay
        self.location = location

        Employee.number_of_employees += 1
    

    def fullname(self):
        return self.first + ' ' + self.last

    def raisepay(self):
        self.pay = (int(self.pay) * int(self.raise_amt))

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, age, pay, location = emp_str.split('-')
        return cls(first, last, age, pay, location)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


    def __str__(self):
        return self.first + ', ' + self.last + "\n" + str(self.age) + "\n" + str(self.pay) + '\n' + self.location

    """You can also use class methods as alternative constructors.
    Class methods can be used to provide multiple ways of
    creating class objects."""



if __name__ == "__main__":
    from datetime import date
    day = date.today()
    print(day)
    print(Employee.is_work_day(day))
    # use class method set_raise_amount to change raise_amt
    Employee.set_raise_amt(2.0)
    emp3 = 'John-Doe-50-90000-London'
    emp3 = Employee.from_string(emp3)
    emp2 = Employee("Jake", "Tendai", 7, 10000)
    print(emp3.email)
    print(emp3)
    emp1 = Employee('Alicia', 'Makena', 30, 30000)
    print(emp1)
    print(emp1.number_of_employees)
    print(emp1.fullname())
    #print(emp1.raisepay())
    print(Employee.raise_amt)
    print(emp1.raise_amt)
    print(emp2.raise_amt)
    #print(emp3)
    
