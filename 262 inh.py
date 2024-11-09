#1- Create a Person class with firstname and lastname properties.

# Add an _init_ method to initialize these properties.
# Add a printname method to print the full name.

#2- Create a Student class that inherits from the Person class.
# Add a property called graduationyear to the Student class,
# with a default value of 2025.
# Modify the Student class so that you can pass
# a specific graduation year when creating an object.

#3- Write code to:

# Create an object of the Student class,
# using the name "Anna Smith" and a graduation year of 2023.
# Print the graduation year.

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        return self.fname,self.lname

class Student(Person):
    def __init__(self,fname,lname,year=2025):
        super().__init__(fname,lname)
        self.year = year

    def printdetails(self):
        print(f"{self.fname} {self.lname}-Graduation year:{self.year}")

s1 = Student("Anna","Smith",2023)
s1.printdetails()

