class New_Employee:
    salary_inc = 2
    no_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        New_Employee.no_of_employee +=1

    def salary_change(self):
        self.salary = self.salary_inc * self.salary


    @classmethod
    def update_salary_inc(cls, amount):
        cls.salary_inc = amount

    @classmethod
    def input_string(cls,emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def is_open(day):
        if day == "sunday":
            return "open"
        else:
            return "close"

    def __add__(self, other):  # magic method,, dunder method
        return self.salary + other.salary

    def __repr__(self):
        return 'New_Employee({}, {}, {})'.format(self.fname, self.lname, self.salary)

    def __str__(self):
        return f'First name is {self.fname}'


harshi = New_Employee("harshi","shiroya",30000)
print(harshi.salary)
print(New_Employee.is_open("monday"))


harshita = New_Employee("harshita","patel",60000)
print(harshita.lname)

print(harshi + harshita)

print(repr(harshi))
print(str(harshi))

print(harshi)