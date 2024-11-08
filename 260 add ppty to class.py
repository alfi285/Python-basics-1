#Add position property to employee class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Employee(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

        self.position = "Software Engineer"


x = Employee("Alfiya", "A")

print(x.position)