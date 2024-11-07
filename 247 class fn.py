#Object Methods
#Objects can also contain methods.
# Methods in objects are functions that belong to the object.

#create a method in the Person class?
#Insert a function that prints a greeting, and execute it on the p1 object ?

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Hello my name is " + self.name)

p1 = person("Alfi",30)

p1.display()