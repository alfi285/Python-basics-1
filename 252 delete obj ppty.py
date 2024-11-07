#Delete object property

#You can delete properties on objects by using del keyword
#Delete the age property from the p1 object

class Person:
    def __init__(init,name,age):
        init.name = name
        init.age= age

    def disp(display):
        print(f"Name:{display.name}\nAge:{display.age}")

p1 = Person("Zaara",6)
del p1.age
p1.age #It gives error because there is age attribute or property