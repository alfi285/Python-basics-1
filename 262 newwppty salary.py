# Add a salary parameter,
# and pass the correct salary when creating objects.
# Use the Employee class to create an object with the specified salary,
# and then print the salary property:

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        return self.fname,self.lname

class Employee(Person):
    def __init__(self,fname,lname,salary):
        super().__init__(fname,lname)

        self.salary = salary

e1 = Employee("Alfiya","A",50000)
print(e1.salary)
