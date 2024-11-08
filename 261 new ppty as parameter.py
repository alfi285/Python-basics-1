#Add a year parameter,
# and pass the correct year when creating objects ?

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)

        self.graduationyear = year


x = Student("Alfiya", "A",2015)

print(x.graduationyear)