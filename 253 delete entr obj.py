#Delete object
#You can completely delete object by using del keyword

#Delete the p1 object

class Person:
    def __init__(init,name,age):
        init.name = name
        init.age= age

    def disp(display):
        print(f"Name:{display.name}\nAge:{display.age}")

p1 = Person("Zaara",6)

del p1
print(p1) #it gives error because there is no object here