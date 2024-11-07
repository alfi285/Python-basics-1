#Python Inheritance

#Inheritance allows us to define a class that inherits all the methods
# and properties from another class.

#Parent class is the class being inherited from, also called base class.

#Child class is the class that inherits from another class,
# also called derived class.

#Create a Parent Class named Person

#Create a class named Person,
# with name and age properties, and a disp method:

class Person:
    def __init__(init,name,age):
        init.name = name
        init.age= age

    def disp(display):
        print(f"Name:{display.name}\nAge:{display.age}")


#Create a Child Class

#To create a class that inherits the functionality from another class,
# send the parent class as a parameter when creating the child class:


#Create a class named Student,
# which will inherit the properties and methods from the Person class:
class Student(Person):
    pass

#Note: Use the pass keyword when you do not want to add any other properties
# or methods to the class.

#Now the Student class has the same properties and methods as the Person class.

#Use the Student class to create an object,
# and then execute the disp method:
s1 = Student("Fadil",10)
s1.disp()