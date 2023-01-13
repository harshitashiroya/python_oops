class New_Employee:  # parent class
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


class position(New_Employee):  # child class
    def __init__(self, fname, lname, salary, position, experience):
        super().__init__(fname, lname, salary)
        self.position = position
        self.experience = experience

    def salary_change(self):  # over-ride the class method
        self.salary = self.salary_inc * (self.salary + 0.5)
        return self.salary


harshi = position("harshi","shiroya",30000,"programmer","3 years")
print(harshi.experience)
print(position.is_open("monday"))  # derive all methods from parent class

print(harshi.salary)
harshi.salary_change()
print(harshi.salary)