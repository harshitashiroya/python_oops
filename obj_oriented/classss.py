class Employee:
    salary_increment = 2.5  # class variable
    no_of_employee = 0

    def __init__(self, fname, lname, salary):  # constructor
        self.fname = fname  # self.fname ->left side, class variable
        self.lname = lname  # fname, lname ->right side, instance variable
        self.salary = salary
        Employee.no_of_employee += 1

    def salary_inc(self):  # function - take instance as an argument
        self.salary = int(self.salary * self.salary_increment)

    @classmethod
    def change_salary_increment(cls, amount):  # change the class variable value
        cls.salary_increment = amount  # replace salary_increment with amount

    @classmethod # work as an alternative constructor
    def from_str(cls,emp_string): # emp_string - take a string as an argument
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary) # cls() = Employee class

    @staticmethod
    def open(day):
        if day == "Sunday":
            return "close"
        else:
            return "Open"


""" 
class method->special method of class take class as an argument
when want to direct work with or change the class variable and don't need to use instance variable 

use 
@staticmethod --- decorator
static function (independent function)- when we neither use instance variable nor class variable 
not take self argument or class as an argument
"""

print(Employee.no_of_employee)
harshi = Employee("harshi", "shiroya", 40000)  # class object/instance
print(harshi.lname, harshi.fname, harshi.salary)
print(Employee.no_of_employee)

print(harshi.salary)
harshi.salary_inc()
print(harshi.salary)

print(Employee.__dict__)
print(harshi.__dict__)

print(harshi.salary)
Employee.change_salary_increment(4)  # 4 = amount ,,,access through class
harshi.salary_inc()
print(harshi.salary)


harshita = Employee.from_str("Harshita-patel-56000") # alternative constructor
print(harshita.fname, harshita.lname, harshita.salary)


print(Employee.open("Sunday")) # static method
print(Employee.open("monday"))