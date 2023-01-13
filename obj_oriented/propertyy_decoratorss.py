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

    @property # take email as attribute not function , property decorator
    def email(self):
        if self.fname == None :
            return "email not set"
        else:
            return self.fname + '.' +self.lname + "@gmail.com"

    @email.setter
    def email(self,new_email):
        name_list = new_email.split("@")[0].split(".")
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname =  None
        self.lname = None

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

if __name__ == '__main__':
    harshi = New_Employee("harshi","shiroya",90000)
    harshita = New_Employee("harshita","patel",70000)
    print(harshi.email)
    print(harshita.email)
    print("\n")
    harshi.lname = "shiroyaaaa"
    print(harshi.email)

    harshi.email = "shiroya.harshi@gmail.com"
    print(harshi.email)

    del harshi.email
    print(harshi.email)




