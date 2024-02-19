#!/usr/bin/python3

class Employee:

    Raise = 1.2

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.email = f"{self.fname}{self.lname}@gmail.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    def raise_pay(self):
        self.pay = self.pay * self.Raise
        return self.pay


    def __str__(self):
        return f"Employee{self.fname, self.lname, self.email, self.pay}"

class IT(Employee):
    # i want the raise for employees in IT to be 50%
    Raise = 1.5
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.language = prog_lang

    def __str__(self):
        return "{}({}, {}, {}, {}, {})".format(__class__.__name__, self.fname, self.lname, self.email, self.pay, self.language)

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printer(self):
        names = [emp.fullname() for emp in self.employees]
        print('; '.join(names))
        
    def __str__(self):
        return "{}({}, {}, {}, {})".format(__class__.__name__, self.fname, self.lname, self.pay, self.employees)
if __name__ == "__main__":
    x = Employee("John", "Doe", 5000)
    y = Employee("Rosa", "Jose", 10000)
    # print(x, y)
    # print(x.raise_pay())
    # print(x.fullname())
    # print(help(IT))
    dev1 = IT("Timothy", "Smith", 20000, 'Python')
    dev2 = IT("Alicia", "Makena", 30000, 'Java')
    print(dev1)
    print(dev2)
    # print(dev1.pay)
    # dev1.raise_pay()
    # print(dev1.pay)
    # print(dev2.pay)
    # dev2.raise_pay()
    # print(dev2.pay)

    mgr_1 = Manager('Sue', 'Morton', 90000, [dev1, x])
    # print(mgr_1)
    mgr_1.add_emp(y)
    mgr_1.printer()
    mgr_1.remove_emp(y)
    mgr_1.printer()
    print(isinstance(mgr_1, Manager))
    print(isinstance(mgr_1, Employee))
    print(type(mgr_1) == Manager)
    print(type(mgr_1) == Employee)
    print(issubclass(IT, Employee))
    print(issubclass(Manager, Employee))
    print(issubclass(IT, Manager))
