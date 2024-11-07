#MOdify object properties

#set age 6 to 7

class Person:
    def __init__(init,name,age):
        init.name = name
        init.age= age

    def disp(display):
        print(f"Name:{display.name}\nAge:{display.age}")

p1 = Person("Zaara",6)
p1.age = 7
p1.disp()